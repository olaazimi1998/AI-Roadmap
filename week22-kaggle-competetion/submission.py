import re
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import lightgbm as lgb
import xgboost as xgb


base_dir = Path(__file__).resolve().parent
train = pd.read_csv(base_dir / 'data' / 'train.csv')
test = pd.read_csv(base_dir / 'data' / 'test.csv')


def add_features(df):
    df = df.copy()
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    df['CabinKnown'] = df['Cabin'].notna().astype(int)
    df['FareBin'] = pd.qcut(df['Fare'].fillna(df['Fare'].median()), 4, labels=False)
    df['Title'] = df['Name'].apply(
        lambda x: re.search(r',\s*([^\.]+)\.', x).group(1) # type: ignore
        if re.search(r',\s*([^\.]+)\.', x)
        else 'Other'
    )
    df['Deck'] = df['Cabin'].astype(str).str[0].replace({'n': 'Missing', 'N': 'Missing'})
    return df


train_features = add_features(train)
test_features = add_features(test)

X = train_features.drop(columns=['Survived', 'Name', 'Ticket', 'Cabin']).copy()
y = train_features['Survived']
X_test = test_features.drop(columns=['Name', 'Ticket', 'Cabin']).copy()

numeric_features = [
    'Pclass', 'Age', 'SibSp', 'Parch', 'Fare',
    'FamilySize', 'IsAlone', 'CabinKnown', 'FareBin'
]
categorical_features = ['Sex', 'Embarked', 'Title', 'Deck']

preprocessor = ColumnTransformer(
    transformers=[
        (
            'numeric',
            Pipeline([('imputer', SimpleImputer(strategy='median'))]),
            numeric_features,
        ),
        (
            'categorical',
            Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('encoder', OneHotEncoder(handle_unknown='ignore')),
            ]),
            categorical_features,
        ),
    ]
)

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

models = {
    'XGBoost': xgb.XGBClassifier(
        objective='binary:logistic',
        n_estimators=500,
        learning_rate=0.03,
        max_depth=4,
        min_child_weight=1,
        subsample=0.9,
        colsample_bytree=0.8,
        gamma=0.1,
        reg_lambda=1.0,
        random_state=42,
        eval_metric='logloss',
    ),
    'LightGBM': lgb.LGBMClassifier(
        objective='binary',
        n_estimators=500,
        learning_rate=0.03,
        num_leaves=25,
        max_depth=-1,
        subsample=0.9,
        colsample_bytree=0.8,
        reg_lambda=0.5,
        random_state=42,
        verbosity=-1,
    ),
}

best_model_name = None
best_model = None
best_score = -1.0

for name, model in models.items():
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', model),
    ])
    pipeline.fit(X_train, y_train)
    val_preds = pipeline.predict(X_val)
    score = accuracy_score(y_val, val_preds)
    print(f'{name} validation accuracy: {score:.4f}')

    if score > best_score:
        best_model_name = name
        best_model = pipeline
        best_score = score

print(f'Best model selected: {best_model_name} ({best_score:.4f})')

assert best_model is not None
best_model.fit(X, y)
preds = pd.Series(best_model.predict(X_test)).astype(int).to_numpy()

submission = pd.DataFrame({
    'PassengerId': test['PassengerId'],
    'Survived': preds,
})

out_dir = base_dir / 'submissions'
out_dir.mkdir(exist_ok=True)
out_path = out_dir / 'submission_xgb_lightgbm.csv'
submission.to_csv(out_path, index=False)

print(submission.head())
print(f'Created {out_path} with {len(submission)} rows')
