 🤖 1-Year AI Engineering Roadmap | نقشه راه ۱ ساله مهندسی هوش مصنوعی

> **Tailored for:** Self-directed learner | Python + Kaggle foundation | Goal: Build large-scale AI systems
> **مناسب برای:** یادگیرنده خودآموز | پایه Python + Kaggle | هدف: ساخت سیستم‌های هوش مصنوعی بزرگ

---

## 🗺️ Overview of the 5 Phases | نگاه کلی به ۵ فاز

| Phase | Weeks | Focus EN | Focus FA |
|-------|-------|----------|----------|
| 1 | 1–8 | Foundation Reinforcement | تقویت پایه |
| 2 | 9–18 | Core Machine Learning | یادگیری ماشین اصلی |
| 3 | 19–30 | Deep Learning | یادگیری عمیق |
| 4 | 31–42 | AI Engineering & MLOps | مهندسی هوش مصنوعی |
| 5 | 43–52 | Portfolio, Projects & Career | پورتفولیو و مسیر شغلی |

---

# PHASE 1 — Foundation Reinforcement
# فاز ۱ — تقویت پایه‌ها
### Weeks 1–8 | هفته‌های ۱ تا ۸

> You already have Python basics and Kaggle experience. This phase fills the math and code gaps that every AI engineer needs.
> تو قبلاً پایتون یاد گرفتی و در Kaggle کار کردی. این فاز شکاف‌های ریاضی و کد را پر می‌کند که هر مهندس هوش مصنوعی نیاز دارد.

---

### ✅ Week 1 | هفته ۱
**English:** Advanced Python — Object-Oriented Programming (OOP)
- Re-read your own OOP code. Write 3 classes from scratch (e.g., a `BankAccount`, a `Student`, a `MLModel` placeholder)
- Practice: inheritance, `__init__`, `__str__`, `@property`
- Tool: Cursor IDE + push to GitHub every day
- **Deliverable:** A Python file with 3 clean, documented classes

**فارسی/دری:** پایتون پیشرفته — برنامه‌نویسی شیءگرا (OOP)
- کدهای OOP قدیمی خودت را دوباره بخوان. ۳ کلاس از صفر بنویس (مثلاً `BankAccount`، `Student`، `MLModel`)
- تمرین: وراثت، `__init__`، `__str__`، `@property`
- ابزار: Cursor + هر روز push به GitHub
- **تحویلی:** یک فایل پایتون با ۳ کلاس تمیز و مستندشده

---

### ✅ Week 2 | هفته ۲
**English:** Advanced Python — Decorators, Generators, Comprehensions
- Learn `@staticmethod`, `@classmethod`, custom decorators
- Write a generator that yields Fibonacci numbers
- Use list/dict/set comprehensions instead of loops
- **Deliverable:** 10 Python mini-exercises combining all three concepts

**فارسی/دری:** پایتون پیشرفته — دکوراتورها، جنریتورها، comprehension‌ها
- یاد بگیر `@staticmethod`، `@classmethod`، دکوراتور سفارشی
- یک جنریتور بنویس که اعداد فیبوناچی تولید کند
- از list/dict/set comprehension به‌جای حلقه استفاده کن
- **تحویلی:** ۱۰ تمرین کوچک پایتون که هر سه مفهوم را ترکیب کند

---

### ✅ Week 3 | هفته ۳
**English:** NumPy Deep Dive
- Arrays, shapes, broadcasting, slicing, vectorized operations
- Practice: matrix multiplication by hand → then with `np.dot()`
- Resource: NumPy official quickstart (100 NumPy exercises on GitHub)
- **Deliverable:** Solve 30 NumPy exercises from the "100 NumPy Exercises" list

**فارسی/دری:** NumPy عمیق
- آرایه‌ها، شکل‌ها، broadcasting، slicing، عملیات برداری
- تمرین: ضرب ماتریس با دست → بعد با `np.dot()`
- **تحویلی:** ۳۰ تمرین NumPy از لیست "100 NumPy Exercises" حل کن

---

### ✅ Week 4 | هفته ۴
**English:** Pandas Deep Dive
- DataFrames, Series, `groupby`, `merge`, `pivot_table`, handling missing values
- Load a real CSV (e.g., Netflix dataset from Kaggle), explore it fully
- **Deliverable:** A Kaggle notebook with full EDA (Exploratory Data Analysis) on any public dataset

**فارسی/دری:** Pandas عمیق
- DataFrames، Series، `groupby`، `merge`، `pivot_table`، مدیریت مقادیر گمشده
- یک CSV واقعی لود کن (مثلاً dataset نتفلیکس از Kaggle)، کاملاً بررسی کن
- **تحویلی:** یک Kaggle notebook با تحلیل اکتشافی کامل (EDA) روی یک dataset عمومی

---

### ✅ Week 5 | هفته ۵
**English:** Statistics for ML
- Mean, median, variance, standard deviation, distributions (normal, Poisson)
- Correlation vs causation
- Hypothesis testing basics (p-value, t-test)
- Resource: StatQuest YouTube channel (Josh Starmer) — watch 5 videos
- **Deliverable:** Written notes + code examples for each concept in a Jupyter notebook

**فارسی/دری:** آمار برای یادگیری ماشین
- میانگین، میانه، واریانس، انحراف معیار، توزیع‌ها (نرمال، پواسون)
- همبستگی در مقابل علیّت
- اصول آزمون فرضیه (p-value، t-test)
- منبع: کانال YouTube StatQuest — ۵ ویدیو تماشا کن
- **تحویلی:** یادداشت‌های نوشته‌شده + مثال‌های کد برای هر مفهوم در Jupyter notebook

---

### ✅ Week 6 | هفته ۶
**English:** Linear Algebra for ML
- Vectors, matrices, dot product, matrix multiplication, transpose, inverse
- Understand why these matter: neural networks ARE matrix multiplications
- Watch 3Blue1Brown "Essence of Linear Algebra" (YouTube) — all episodes
- **Deliverable:** Implement matrix operations from scratch in NumPy + explain each in comments

**فارسی/دری:** جبر خطی برای یادگیری ماشین
- بردارها، ماتریس‌ها، حاصل‌ضرب داخلی، ضرب ماتریس، ترانسپوز، معکوس
- درک کن چرا اهمیت دارند: شبکه‌های عصبی در واقع ضرب ماتریس‌ها هستند
- ویدیوهای "Essence of Linear Algebra" از 3Blue1Brown را ببین
- **تحویلی:** عملیات ماتریس را از صفر در NumPy پیاده‌سازی کن + هر مورد را در کامنت توضیح بده

---

### ✅ Week 7 | هفته ۷
**English:** Probability & Calculus for ML
- Probability: Bayes' theorem, conditional probability, distributions
- Calculus: what is a derivative, gradient, chain rule (conceptually — not formulas by heart)
- Why this matters: training ML models = finding minimum with gradients
- **Deliverable:** Write a Jupyter notebook explaining Bayes' theorem with a real-world example

**فارسی/دری:** احتمال و حساب دیفرانسیل برای یادگیری ماشین
- احتمال: قضیه بیز، احتمال شرطی، توزیع‌ها
- حساب: مشتق چیست، گرادیان، قانون زنجیره (مفهومی — نه از بر)
- چرا مهم است: آموزش مدل‌های ML = پیدا کردن حداقل با گرادیان‌ها
- **تحویلی:** یک Jupyter notebook بنویس که قضیه بیز را با مثال واقعی توضیح دهد

---

### ✅ Week 8 | هفته ۸
**English:** Data Visualization + Mini-Project
- Matplotlib, Seaborn: histograms, scatter plots, heatmaps, box plots
- Build a full EDA project on a dataset of your choice (sports, finance, health, etc.)
- Push to GitHub with a README
- **Deliverable:** GitHub repository with complete EDA project — your first public portfolio piece

**فارسی/دری:** تجسم داده + پروژه کوچک
- Matplotlib، Seaborn: هیستوگرام، نمودار پراکندگی، heatmap، box plot
- یک پروژه EDA کامل روی dataset دلخواه بساز (ورزش، مالی، سلامت و غیره)
- به GitHub push کن با یک README
- **تحویلی:** مخزن GitHub با پروژه EDA کامل — اولین قطعه پورتفولیو عمومی تو

---
---

# PHASE 2 — Core Machine Learning
# فاز ۲ — یادگیری ماشین اصلی
### Weeks 9–18 | هفته‌های ۹ تا ۱۸

> This is the engine room. Every algorithm here is something you'll use professionally.
> این اتاق موتور است. هر الگوریتم اینجا چیزی است که حرفه‌ای از آن استفاده خواهی کرد.

---

### ✅ Week 9 | هفته ۹
**English:** Scikit-learn Framework + ML Pipeline
- `train_test_split`, `StandardScaler`, `Pipeline`, `fit()`, `predict()`
- Understand: features (X) vs labels (y), overfitting vs underfitting
- **Deliverable:** Build a pipeline that preprocesses + trains on any tabular dataset

**فارسی/دری:** چارچوب Scikit-learn + Pipeline یادگیری ماشین
- `train_test_split`، `StandardScaler`، `Pipeline`، `fit()`، `predict()`
- درک: ویژگی‌ها (X) در مقابل برچسب‌ها (y)، overfitting در مقابل underfitting
- **تحویلی:** یک Pipeline بساز که روی هر dataset جدولی پیش‌پردازش + آموزش می‌دهد

---

### ✅ Week 10 | هفته ۱۰
**English:** Linear & Logistic Regression
- Theory: cost function, gradient descent (understand visually)
- Code: implement from scratch in NumPy, then use Scikit-learn
- **Deliverable:** Predict house prices (Linear) AND predict survived/died (Logistic) — compare scratch vs library

**فارسی/دری:** رگرسیون خطی و لجستیک
- تئوری: تابع هزینه، gradient descent (درک بصری)
- کد: از صفر در NumPy پیاده کن، بعد از Scikit-learn استفاده کن
- **تحویلی:** قیمت خانه پیش‌بینی کن (خطی) و زنده/مرده پیش‌بینی کن (لجستیک) — صفر را با کتابخانه مقایسه کن

---

### ✅ Week 11 | هفته ۱۱
**English:** Decision Trees & Random Forests
- How trees split data, Gini impurity, max depth
- Why Random Forests beat single trees (ensemble concept)
- Visualize a trained tree with `export_graphviz`
- **Deliverable:** Classification project comparing single tree vs Random Forest accuracy

**فارسی/دری:** درخت تصمیم و جنگل تصادفی
- چطور درخت‌ها داده را تقسیم می‌کنند، ناخالصی Gini، حداکثر عمق
- چرا Random Forest از درخت تکی بهتر است (مفهوم ensemble)
- یک درخت آموزش‌دیده را با `export_graphviz` تجسم کن
- **تحویلی:** پروژه طبقه‌بندی که دقت درخت تکی را با Random Forest مقایسه کند

---

### ✅ Week 12 | هفته ۱۲
**English:** SVM & KNN
- SVM: hyperplane, margin, kernel trick (intuitively)
- KNN: how it votes, the k parameter, distance metrics
- **Deliverable:** Image classification mini-project (digits dataset) using both SVM and KNN

**فارسی/دری:** SVM و KNN
- SVM: ابرصفحه، حاشیه، ترفند هسته (به صورت شهودی)
- KNN: چطور رای می‌دهد، پارامتر k، معیارهای فاصله
- **تحویلی:** پروژه کوچک طبقه‌بندی تصویر (dataset ارقام) با SVM و KNN

---

### ✅ Week 13 | هفته ۱۳
**English:** Gradient Boosting — XGBoost & LightGBM
- These are the top competition winners for tabular data
- Understand boosting: weak learners → strong model
- Install XGBoost, LightGBM; tune basic hyperparameters
- **Deliverable:** Return to Titanic dataset — beat your old score using XGBoost

**فارسی/دری:** Gradient Boosting — XGBoost و LightGBM
- اینها برندگان برتر مسابقات برای داده‌های جدولی هستند
- boosting را درک کن: یادگیرنده‌های ضعیف → مدل قوی
- XGBoost، LightGBM نصب کن؛ hyperparameter‌های اصلی را تنظیم کن
- **تحویلی:** به dataset Titanic برگرد — امتیاز قدیمی‌ات را با XGBoost بهبود بده

---

### ✅ Week 14 | هفته ۱۴
**English:** Unsupervised Learning — K-Means & PCA
- K-Means clustering: elbow method, silhouette score
- PCA: reduce 100 features to 2 for visualization
- **Deliverable:** Customer segmentation project using K-Means + visualize with PCA

**فارسی/دری:** یادگیری بدون نظارت — K-Means و PCA
- خوشه‌بندی K-Means: روش آرنج، امتیاز silhouette
- PCA: کاهش ۱۰۰ ویژگی به ۲ برای تجسم
- **تحویلی:** پروژه بخش‌بندی مشتری با K-Means + تجسم با PCA

---

### ✅ Week 15 | هفته ۱۵
**English:** Feature Engineering — The Secret Weapon
- Creating new features, handling categorical variables (one-hot, label encoding)
- Dealing with outliers, skewed distributions, feature scaling
- Feature selection: correlation matrix, importance scores
- **Deliverable:** Take any old project, apply advanced feature engineering, and measure accuracy improvement

**فارسی/دری:** مهندسی ویژگی — سلاح مخفی
- ایجاد ویژگی‌های جدید، مدیریت متغیرهای دسته‌بندی (one-hot، label encoding)
- برخورد با outlier‌ها، توزیع‌های کج، مقیاس‌بندی ویژگی
- انتخاب ویژگی: ماتریس همبستگی، امتیازهای اهمیت
- **تحویلی:** یک پروژه قدیمی بگیر، مهندسی ویژگی پیشرفته اعمال کن، بهبود دقت را اندازه بگیر

---

### ✅ Week 16 | هفته ۱۶
**English:** Model Evaluation & Hyperparameter Tuning
- Metrics: accuracy, precision, recall, F1, ROC-AUC, RMSE
- Cross-validation (k-fold), GridSearchCV, RandomizedSearchCV
- Understand the bias-variance tradeoff deeply
- **Deliverable:** A notebook that properly evaluates 3 different models on the same dataset with all metrics

**فارسی/دری:** ارزیابی مدل و تنظیم Hyperparameter
- معیارها: دقت، precision، recall، F1، ROC-AUC، RMSE
- اعتبارسنجی متقاطع (k-fold)، GridSearchCV، RandomizedSearchCV
- تعادل bias-variance را عمیقاً درک کن
- **تحویلی:** یک notebook که ۳ مدل مختلف را روی یک dataset با تمام معیارها ارزیابی کند

---

### ✅ Week 17 | هفته ۱۷
**English:** Kaggle Competition Week
- Join an active Kaggle tabular competition (or use a recent one)
- Make at least 5 submissions with different approaches
- Study top public notebooks to learn new tricks
- **Deliverable:** A competition submission + a write-up of what you learned

**فارسی/دری:** هفته مسابقه Kaggle
- به یک مسابقه Kaggle جدولی فعال بپیوند (یا از یکی اخیر استفاده کن)
- حداقل ۵ ارسال با رویکردهای مختلف داشته باش
- notebook‌های عمومی برتر را مطالعه کن تا ترفندهای جدید یاد بگیری
- **تحویلی:** یک ارسال مسابقه + یادداشتی از آنچه یاد گرفتی

---

### ✅ Week 18 | هفته ۱۸
**English:** End-to-End ML Project
- Choose a real problem (salary prediction, churn prediction, etc.)
- Full pipeline: data → EDA → feature engineering → modeling → evaluation
- Deploy as a simple FastAPI endpoint (preview of Phase 4)
- **Deliverable:** GitHub repo with complete project, README, and working API endpoint

**فارسی/دری:** پروژه ML کامل از ابتدا تا انتها
- یک مشکل واقعی انتخاب کن (پیش‌بینی حقوق، پیش‌بینی churn و غیره)
- Pipeline کامل: داده → EDA → مهندسی ویژگی → مدل‌سازی → ارزیابی
- به عنوان یک endpoint ساده FastAPI deploy کن (پیش‌نمایش فاز ۴)
- **تحویلی:** مخزن GitHub با پروژه کامل، README، و endpoint API کارکننده

---
---

# PHASE 3 — Deep Learning
# فاز ۳ — یادگیری عمیق
### Weeks 19–30 | هفته‌های ۱۹ تا ۳۰

> This is where AI becomes *magical*. Neural networks, vision, language — all of it starts here.
> اینجاست که هوش مصنوعی *جادویی* می‌شود. شبکه‌های عصبی، بینایی، زبان — همه اینجا شروع می‌شود.

---

### ✅ Week 19 | هفته ۱۹
**English:** Neural Network Theory
- Perceptron → Multi-Layer Perceptron (MLP)
- Activation functions: ReLU, sigmoid, softmax — why each one?
- Forward pass, loss function, backpropagation (conceptually)
- Watch 3Blue1Brown "Neural Networks" series on YouTube (4 videos)
- **Deliverable:** Hand-drawn (or digital) diagram of a neural network with labels for every component

**فارسی/دری:** تئوری شبکه عصبی
- Perceptron → Multi-Layer Perceptron (MLP)
- توابع فعال‌سازی: ReLU، sigmoid، softmax — چرا هر کدام؟
- پاس رو به جلو، تابع خطا، backpropagation (به صورت مفهومی)
- سری "Neural Networks" از 3Blue1Brown در YouTube تماشا کن (۴ ویدیو)
- **تحویلی:** دیاگرام دست‌نویس (یا دیجیتال) از یک شبکه عصبی با برچسب برای هر جزء

---

### ✅ Week 20 | هفته ۲۰
**English:** Build a Neural Network from Scratch in NumPy
- No frameworks. Just NumPy.
- Implement: forward pass, backpropagation, weight updates
- Train it on XOR or MNIST (simple version)
- **Deliverable:** Working neural network in pure NumPy — this is your proudest code yet

**فارسی/دری:** ساخت شبکه عصبی از صفر با NumPy
- هیچ چارچوبی نه. فقط NumPy.
- پیاده‌سازی: پاس رو به جلو، backpropagation، به‌روزرسانی وزن‌ها
- روی XOR یا MNIST (نسخه ساده) آموزش بده
- **تحویلی:** شبکه عصبی کارکننده در NumPy خالص — این مفیدترین کد تاکنون توست

---

### ✅ Week 21 | هفته ۲۱
**English:** PyTorch Fundamentals
- Tensors, autograd, computational graph
- `torch.nn.Module`, `optimizer`, training loop
- Compare: NumPy array vs PyTorch tensor
- **Deliverable:** Reproduce last week's neural network in PyTorch — same task, fewer lines

**فارسی/دری:** مبانی PyTorch
- Tensor‌ها، autograd، نمودار محاسباتی
- `torch.nn.Module`، `optimizer`، حلقه آموزش
- مقایسه: آرایه NumPy در مقابل tensor PyTorch
- **تحویلی:** شبکه عصبی هفته قبل را در PyTorch دوباره پیاده کن — همان کار، خطوط کمتر

---

### ✅ Week 22 | هفته ۲۲
**English:** PyTorch — Building Real Networks
- `DataLoader`, `Dataset`, batch training, GPU support (`cuda`)
- Dropout, Batch Normalization, learning rate schedulers
- Train on MNIST digit classification
- **Deliverable:** PyTorch MLP that achieves >97% accuracy on MNIST

**فارسی/دری:** PyTorch — ساخت شبکه‌های واقعی
- `DataLoader`، `Dataset`، آموزش دسته‌ای، پشتیبانی GPU (`cuda`)
- Dropout، Batch Normalization، برنامه‌ریزهای learning rate
- روی طبقه‌بندی ارقام MNIST آموزش بده
- **تحویلی:** MLP در PyTorch که دقت بالای ۹۷٪ در MNIST به دست آورد

---

### ✅ Week 23 | هفته ۲۳
**English:** Convolutional Neural Networks (CNNs) — Theory
- Convolution operation, filters, feature maps
- Pooling layers, stride, padding
- Famous architectures: LeNet, AlexNet, VGG (understand, not memorize)
- **Deliverable:** Illustrated notes explaining how a CNN processes an image step by step

**فارسی/دری:** شبکه‌های عصبی کانولوشنی (CNN) — تئوری
- عملیات کانولوشن، فیلترها، نقشه‌های ویژگی
- لایه‌های Pooling، stride، padding
- معماری‌های معروف: LeNet، AlexNet، VGG (درک کن، حفظ نکن)
- **تحویلی:** یادداشت‌های مصور که توضیح می‌دهد CNN چگونه یک تصویر را مرحله به مرحله پردازش می‌کند

---

### ✅ Week 24 | هفته ۲۴
**English:** CNN Project — Image Classification
- Use CIFAR-10 or a custom image dataset
- Build, train, and evaluate a CNN in PyTorch
- Apply transfer learning with ResNet or EfficientNet (pretrained)
- **Deliverable:** Image classifier with >85% accuracy + GitHub deployment

**فارسی/دری:** پروژه CNN — طبقه‌بندی تصویر
- از CIFAR-10 یا یک dataset تصویر سفارشی استفاده کن
- یک CNN در PyTorch بساز، آموزش بده، ارزیابی کن
- یادگیری انتقالی با ResNet یا EfficientNet (پیش‌آموزش‌دیده) اعمال کن
- **تحویلی:** طبقه‌بند تصویر با دقت بالای ۸۵٪ + استقرار در GitHub

---

### ✅ Week 25 | هفته ۲۵
**English:** Recurrent Neural Networks (RNNs) & LSTMs
- Why sequences are different: time series, text, audio
- RNN vanishing gradient problem → why LSTMs solve it
- Code: LSTM for time series prediction
- **Deliverable:** Stock price (or weather) forecasting LSTM in PyTorch

**فارسی/دری:** شبکه‌های عصبی بازگشتی (RNN) و LSTM
- چرا دنباله‌ها متفاوتند: سری زمانی، متن، صدا
- مشکل vanishing gradient در RNN → چرا LSTM آن را حل می‌کند
- کد: LSTM برای پیش‌بینی سری زمانی
- **تحویلی:** پیش‌بینی قیمت سهام (یا آب‌وهوا) با LSTM در PyTorch

---

### ✅ Week 26 | هفته ۲۶
**English:** NLP Fundamentals
- Tokenization, stemming, lemmatization
- Bag of Words, TF-IDF
- Word embeddings: Word2Vec, GloVe (what they are, how to use)
- Sentiment analysis project with classic NLP
- **Deliverable:** Sentiment classifier on movie reviews using TF-IDF + Logistic Regression

**فارسی/دری:** مبانی پردازش زبان طبیعی (NLP)
- Tokenization، stemming، lemmatization
- Bag of Words، TF-IDF
- جاسازی کلمه: Word2Vec، GloVe (چیست، چطور استفاده کنیم)
- پروژه تحلیل احساسات با NLP کلاسیک
- **تحویلی:** طبقه‌بند احساسات روی نقدهای فیلم با TF-IDF + رگرسیون لجستیک

---

### ✅ Week 27 | هفته ۲۷
**English:** Transformers & Attention Mechanism — Theory
- "Attention is All You Need" paper (read the intro + figures, not all math)
- Self-attention, multi-head attention, positional encoding
- The BERT and GPT architecture difference (encoder vs decoder)
- **Deliverable:** A written explanation (in your own words) of how a Transformer works

**فارسی/دری:** Transformer‌ها و مکانیزم توجه — تئوری
- مقاله "Attention is All You Need" (مقدمه + شکل‌ها را بخوان، نه همه ریاضیات)
- self-attention، multi-head attention، positional encoding
- تفاوت معماری BERT و GPT (encoder در مقابل decoder)
- **تحویلی:** یک توضیح نوشته‌شده (به کلمات خودت) از چگونگی کار Transformer

---

### ✅ Week 28 | هفته ۲۸
**English:** Hugging Face — Using Pre-trained Models
- Install Transformers library, load BERT/GPT-2 models
- Text classification, text generation, question answering
- Understand the `pipeline()` API and `AutoModel` classes
- **Deliverable:** 3 NLP mini-apps using Hugging Face pipelines (classifier, generator, Q&A)

**فارسی/دری:** Hugging Face — استفاده از مدل‌های پیش‌آموزش‌دیده
- کتابخانه Transformers را نصب کن، مدل‌های BERT/GPT-2 را لود کن
- طبقه‌بندی متن، تولید متن، پاسخ به سوال
- `pipeline()` API و کلاس‌های `AutoModel` را درک کن
- **تحویلی:** ۳ اپلیکیشن کوچک NLP با Hugging Face pipelines (طبقه‌بند، مولد، Q&A)

---

### ✅ Week 29 | هفته ۲۹
**English:** Fine-tuning a Transformer Model
- What is fine-tuning? Adapting a pre-trained model to your task
- Fine-tune BERT on a custom text classification dataset (small dataset is OK)
- Use the Hugging Face `Trainer` API
- **Deliverable:** A fine-tuned BERT model pushed to Hugging Face Hub (your first public model!)

**فارسی/دری:** Fine-tuning یک مدل Transformer
- Fine-tuning چیست؟ تطبیق یک مدل پیش‌آموزش‌دیده به کار خودت
- BERT را روی یک dataset طبقه‌بندی متن سفارشی fine-tune کن (dataset کوچک هم خوب است)
- از `Trainer` API در Hugging Face استفاده کن
- **تحویلی:** یک مدل BERT fine-tune‌شده که در Hugging Face Hub push شده باشد (اولین مدل عمومی تو!)

---

### ✅ Week 30 | هفته ۳۰
**English:** Deep Learning Capstone Project
- Build a complete end-to-end deep learning project in NLP or Computer Vision
- Ideas: fake news detector, product review analyzer, face emotion classifier
- Full pipeline: data collection → model → evaluation → deployment sketch
- **Deliverable:** GitHub repo with README, demo, and model weights — your strongest portfolio piece so far

**فارسی/دری:** پروژه جامع یادگیری عمیق
- یک پروژه یادگیری عمیق کامل در NLP یا بینایی کامپیوتر بساز
- ایده‌ها: تشخیص اخبار جعلی، تحلیل‌گر نقد محصول، طبقه‌بند احساسات چهره
- Pipeline کامل: جمع‌آوری داده → مدل → ارزیابی → طرح استقرار
- **تحویلی:** مخزن GitHub با README، دمو، و وزن‌های مدل — قوی‌ترین قطعه پورتفولیو تاکنون

---
---

# PHASE 4 — AI Engineering & MLOps
# فاز ۴ — مهندسی هوش مصنوعی و MLOps
### Weeks 31–42 | هفته‌های ۳۱ تا ۴۲

> Building models is only 20% of the job. This phase teaches you how AI engineers actually ship products.
> ساخت مدل فقط ۲۰٪ کار است. این فاز به تو یاد می‌دهد مهندسان هوش مصنوعی واقعاً چطور محصولات را ارائه می‌دهند.

---

### ✅ Week 31 | هفته ۳۱
**English:** APIs with FastAPI
- Build REST APIs in Python with FastAPI
- Create an endpoint: POST a text → get a sentiment prediction
- JSON requests/responses, Pydantic models, async
- **Deliverable:** A FastAPI app that serves your Week 18 ML model

**فارسی/دری:** API‌ها با FastAPI
- REST API در Python با FastAPI بساز
- یک endpoint بساز: POST یک متن → پیش‌بینی احساسات دریافت کن
- درخواست/پاسخ JSON، مدل‌های Pydantic، async
- **تحویلی:** یک اپ FastAPI که مدل ML هفته ۱۸ تو را ارائه دهد

---

### ✅ Week 32 | هفته ۳۲
**English:** Docker — Containerize Your Model
- What is Docker? Why containers matter in production
- Write a `Dockerfile` for your FastAPI app
- `docker build`, `docker run`, understanding layers
- **Deliverable:** Your ML API running inside a Docker container, reproducible on any machine

**فارسی/دری:** Docker — containerize کردن مدل تو
- Docker چیست؟ چرا container‌ها در تولید اهمیت دارند
- یک `Dockerfile` برای اپ FastAPI خودت بنویس
- `docker build`، `docker run`، درک لایه‌ها
- **تحویلی:** API یادگیری ماشین تو که در یک container Docker اجرا می‌شود، قابل بازتولید در هر ماشینی

---

### ✅ Week 33 | هفته ۳۳
**English:** Experiment Tracking with MLflow
- Log experiments: parameters, metrics, artifacts
- Compare runs, visualize training curves
- Register and version your models
- **Deliverable:** 5 ML experiments tracked and compared in MLflow dashboard

**فارسی/دری:** ردیابی آزمایش با MLflow
- آزمایش‌ها را ثبت کن: پارامترها، معیارها، artifact‌ها
- اجراها را مقایسه کن، منحنی‌های آموزش را تجسم کن
- مدل‌هایت را ثبت و نسخه‌بندی کن
- **تحویلی:** ۵ آزمایش ML که در داشبورد MLflow ردیابی و مقایسه شده باشند

---

### ✅ Week 34 | هفته ۳۴
**English:** LLMs — How They Work & Prompt Engineering
- Architecture of GPT models (decoder-only transformers)
- Tokens, context window, temperature, top-p sampling
- Prompt engineering: zero-shot, few-shot, chain-of-thought
- Use the Anthropic or OpenAI API with Python
- **Deliverable:** A Python script that uses an LLM API to solve 5 different tasks via smart prompting

**فارسی/دری:** LLM‌ها — چطور کار می‌کنند و مهندسی Prompt
- معماری مدل‌های GPT (transformer‌های decoder-only)
- توکن‌ها، پنجره context، temperature، نمونه‌برداری top-p
- مهندسی prompt: zero-shot، few-shot، chain-of-thought
- از Anthropic یا OpenAI API با Python استفاده کن
- **تحویلی:** یک اسکریپت Python که از LLM API برای حل ۵ کار مختلف از طریق prompting هوشمند استفاده کند

---

### ✅ Week 35 | هفته ۳۵
**English:** RAG — Retrieval Augmented Generation
- What is RAG? Why LLMs hallucinate and how RAG fixes it
- Embeddings, vector similarity, semantic search
- Build a simple Q&A system over your own documents
- **Deliverable:** A RAG system that can answer questions about any PDF you give it

**فارسی/دری:** RAG — تولید تقویت‌شده با بازیابی
- RAG چیست؟ چرا LLM‌ها توهم می‌زنند و RAG چطور آن را رفع می‌کند
- Embedding‌ها، شباهت برداری، جستجوی معنایی
- یک سیستم Q&A ساده روی اسناد خودت بساز
- **تحویلی:** یک سیستم RAG که می‌تواند به سوالات درباره هر PDF که به آن می‌دهی پاسخ دهد

---

### ✅ Week 36 | هفته ۳۶
**English:** LangChain / LangGraph Basics
- Chains, agents, tools, memory
- Build a multi-step AI agent that uses external tools
- Connect to a search engine, calculator, or your own API
- **Deliverable:** An AI agent that can search the web and answer questions with sources

**فارسی/دری:** مبانی LangChain / LangGraph
- Chain‌ها، agent‌ها، ابزارها، حافظه
- یک agent هوش مصنوعی چند مرحله‌ای بساز که از ابزارهای خارجی استفاده کند
- به یک موتور جستجو، ماشین‌حساب، یا API خودت متصل شو
- **تحویلی:** یک AI agent که می‌تواند در وب جستجو کند و با منابع پاسخ دهد

---

### ✅ Week 37 | هفته ۳۷
**English:** Vector Databases
- What is a vector database? How embeddings are stored and searched
- Use ChromaDB (local) or Pinecone (cloud)
- Build a semantic search system
- **Deliverable:** A semantic document search engine using ChromaDB + Sentence Transformers

**فارسی/دری:** پایگاه‌های داده برداری
- پایگاه داده برداری چیست؟ Embedding‌ها چطور ذخیره و جستجو می‌شوند
- از ChromaDB (محلی) یا Pinecone (ابری) استفاده کن
- یک سیستم جستجوی معنایی بساز
- **تحویلی:** یک موتور جستجوی اسناد معنایی با ChromaDB + Sentence Transformers

---

### ✅ Week 38 | هفته ۳۸
**English:** Cloud Basics for AI Engineers (AWS Free Tier)
- S3 for data storage, EC2 for compute, SageMaker basics
- Deploy your Docker container to the cloud
- IAM permissions, environment variables, secrets management
- **Deliverable:** Your ML model API live on AWS EC2 with a public URL

**فارسی/دری:** مبانی ابر برای مهندسان هوش مصنوعی (AWS Free Tier)
- S3 برای ذخیره‌سازی داده، EC2 برای محاسبه، مبانی SageMaker
- container Docker خودت را به ابر مستقر کن
- مجوزهای IAM، متغیرهای محیطی، مدیریت secrets
- **تحویلی:** API مدل یادگیری ماشین تو که روی AWS EC2 با یک URL عمومی در اجرا باشد

---

### ✅ Week 39 | هفته ۳۹
**English:** CI/CD for ML with GitHub Actions
- What is CI/CD? Automated testing, building, deploying
- Write a GitHub Actions workflow that tests your code and redeploys on push
- Linting (flake8), unit tests (pytest) for ML code
- **Deliverable:** A GitHub repo where every push auto-tests and auto-deploys your model

**فارسی/دری:** CI/CD برای یادگیری ماشین با GitHub Actions
- CI/CD چیست؟ آزمایش، ساخت، استقرار خودکار
- یک workflow GitHub Actions بنویس که کدت را آزمایش کند و روی push مجدداً مستقر کند
- لینتینگ (flake8)، تست واحد (pytest) برای کد یادگیری ماشین
- **تحویلی:** یک مخزن GitHub که در هر push به طور خودکار مدل تو را آزمایش و مستقر کند

---

### ✅ Week 40 | هفته ۴۰
**English:** Model Monitoring in Production
- Data drift, concept drift — what goes wrong after deployment
- Monitoring tools: Evidently AI, Grafana (basics)
- Set up alerts for degraded model performance
- **Deliverable:** A monitoring dashboard for one of your deployed models

**فارسی/دری:** نظارت بر مدل در محیط تولید
- data drift، concept drift — چه چیزی پس از استقرار خراب می‌شود
- ابزارهای نظارتی: Evidently AI، Grafana (مبانی)
- هشدار برای عملکرد کاهش‌یافته مدل تنظیم کن
- **تحویلی:** یک داشبورد نظارتی برای یکی از مدل‌های مستقرشده تو

---

### ✅ Week 41 | هفته ۴۱
**English:** Data Pipelines with Airflow
- DAGs (Directed Acyclic Graphs) — how scheduled pipelines work
- Build a simple Airflow DAG: fetch data → process → retrain model → save
- **Deliverable:** An automated data pipeline that retrains a model on fresh data weekly

**فارسی/دری:** Pipeline داده با Airflow
- DAGها (گراف‌های بدون دور جهت‌دار) — چطور pipeline‌های زمان‌بندی‌شده کار می‌کنند
- یک DAG ساده Airflow بساز: دریافت داده → پردازش → آموزش مجدد مدل → ذخیره
- **تحویلی:** یک pipeline داده خودکار که هفتگی یک مدل را روی داده‌های تازه مجدداً آموزش می‌دهد

---

### ✅ Week 42 | هفته ۴۲
**English:** MLOps Mini-Project — Full Pipeline
- Combine everything from Phase 4: FastAPI + Docker + MLflow + GitHub Actions + Cloud + Monitoring
- Build one complete production-grade ML system
- **Deliverable:** A production ML system with model serving, experiment tracking, CI/CD, and monitoring

**فارسی/دری:** پروژه کوچک MLOps — Pipeline کامل
- همه چیز از فاز ۴ را ترکیب کن: FastAPI + Docker + MLflow + GitHub Actions + Cloud + نظارت
- یک سیستم ML کامل با درجه تولید بساز
- **تحویلی:** یک سیستم ML تولیدی با ارائه مدل، ردیابی آزمایش، CI/CD، و نظارت

---
---

# PHASE 5 — Portfolio, Projects & Career
# فاز ۵ — پورتفولیو، پروژه‌ها و مسیر شغلی
### Weeks 43–52 | هفته‌های ۴۳ تا ۵۲

> The final phase transforms you from a learner into a candidate. Build what nobody else has built.
> فاز نهایی تو را از یک یادگیرنده به یک نامزد تبدیل می‌کند. چیزی بساز که هیچ‌کس دیگری نساخته است.

---

### ✅ Week 43 | هفته ۴۳
**English:** Capstone Project Planning
- Choose your signature project (see ideas below)
- Define: problem → dataset → architecture → success metric → user
- Write a project plan document (1 page)
- **Ideas:** AI trading signal system, Dari/Persian NLP tool, Dubai real estate predictor, medical diagnosis assistant
- **Deliverable:** Written project spec + GitHub repo initialized

**فارسی/دری:** برنامه‌ریزی پروژه جامع
- پروژه امضایی خودت را انتخاب کن (ایده‌ها را ببین)
- تعریف: مشکل → dataset → معماری → معیار موفقیت → کاربر
- یک سند برنامه پروژه بنویس (۱ صفحه)
- **ایده‌ها:** سیستم سیگنال معاملاتی هوش مصنوعی، ابزار NLP دری/فارسی، پیش‌بینی‌گر املاک دبی، دستیار تشخیص پزشکی
- **تحویلی:** مشخصات پروژه نوشته‌شده + مخزن GitHub راه‌اندازی‌شده

---

### ✅ Weeks 44–47 | هفته‌های ۴۴ تا ۴۷
**English:** Build the Capstone Project (4 Weeks)
- Week 44: Data collection, cleaning, EDA
- Week 45: Modeling and experimentation
- Week 46: Backend API + deployment
- Week 47: Frontend demo (Gradio or Streamlit), documentation
- **Deliverable:** A live, deployed AI application with full documentation

**فارسی/دری:** ساخت پروژه جامع (۴ هفته)
- هفته ۴۴: جمع‌آوری داده، پاکسازی، EDA
- هفته ۴۵: مدل‌سازی و آزمایش
- هفته ۴۶: API پشتیبان + استقرار
- هفته ۴۷: دمو فرانت‌اند (Gradio یا Streamlit)، مستندسازی
- **تحویلی:** یک اپلیکیشن هوش مصنوعی زنده و مستقر با مستندات کامل

---

### ✅ Week 48 | هفته ۴۸
**English:** Open Source Contribution
- Find a Hugging Face, scikit-learn, or LangChain GitHub issue labeled "good first issue"
- Fix it, open a pull request
- Write a blog post about your capstone project (Medium or Substack)
- **Deliverable:** 1 merged PR + 1 published technical blog post

**فارسی/دری:** مشارکت در متن‌باز
- یک مشکل GitHub در Hugging Face، scikit-learn، یا LangChain با برچسب "good first issue" پیدا کن
- آن را رفع کن، یک pull request باز کن
- یک پست وبلاگ درباره پروژه جامع خودت بنویس (Medium یا Substack)
- **تحویلی:** ۱ PR ادغام‌شده + ۱ پست وبلاگ فنی منتشرشده

---

### ✅ Week 49 | هفته ۴۹
**English:** Portfolio Website + GitHub Profile
- Clean GitHub profile: pinned repos, clear READMEs, contribution graph
- Build a simple portfolio site (GitHub Pages or Vercel)
- Link: your best 3 projects + capstone + blog
- **Deliverable:** Public portfolio website live at `yourusername.github.io`

**فارسی/دری:** وب‌سایت پورتفولیو + پروفایل GitHub
- پروفایل GitHub را تمیز کن: مخازن پین‌شده، README‌های واضح، نمودار مشارکت
- یک سایت پورتفولیو ساده بساز (GitHub Pages یا Vercel)
- لینک: ۳ پروژه برتر + پروژه جامع + وبلاگ
- **تحویلی:** وب‌سایت پورتفولیو عمومی در `yourusername.github.io`

---

### ✅ Week 50 | هفته ۵۰
**English:** Interview Prep — ML Theory
- Study: bias-variance, regularization, gradient descent variants, neural network training tips
- Practice: explain every algorithm you know in 2 minutes (record yourself)
- Read: "Ace the Data Science Interview" book (chapters on ML)
- **Deliverable:** Flashcard deck of 50 ML interview questions + your answers

**فارسی/دری:** آمادگی مصاحبه — تئوری یادگیری ماشین
- مطالعه: bias-variance، regularization، انواع gradient descent، نکات آموزش شبکه عصبی
- تمرین: هر الگوریتمی که می‌دانی را در ۲ دقیقه توضیح بده (خودت را ضبط کن)
- بخوان: کتاب "Ace the Data Science Interview" (فصل‌های یادگیری ماشین)
- **تحویلی:** مجموعه کارت‌های فلش با ۵۰ سوال مصاحبه یادگیری ماشین + پاسخ‌های تو

---

### ✅ Week 51 | هفته ۵۱
**English:** Interview Prep — Coding + System Design
- LeetCode: solve 20 problems (Easy + Medium) in Python
- System design: "Design a recommendation system", "Design a fraud detection pipeline"
- Study: how to estimate scale, discuss tradeoffs, propose architecture
- **Deliverable:** 3 written system design solutions for AI systems

**فارسی/دری:** آمادگی مصاحبه — کدنویسی + طراحی سیستم
- LeetCode: ۲۰ مسئله (ساده + متوسط) در Python حل کن
- طراحی سیستم: "یک سیستم توصیه طراحی کن"، "یک pipeline تشخیص تقلب طراحی کن"
- مطالعه: چطور مقیاس را تخمین بزنی، مبادلات را بحث کنی، معماری پیشنهاد بدهی
- **تحویلی:** ۳ راه‌حل طراحی سیستم نوشته‌شده برای سیستم‌های هوش مصنوعی

---

### ✅ Week 52 | هفته ۵۲
**English:** Launch Week — Apply & Network
- Update LinkedIn: headline "AI Engineer | Python | PyTorch | LLMs"
- Apply to 10 roles: AI Engineer, ML Engineer, Data Scientist (Dubai, Remote)
- Connect with 20 AI professionals on LinkedIn
- Reflect: write what you've built, what you've learned, where you're going next
- **Deliverable:** Active job applications + a personal reflection document

**فارسی/دری:** هفته راه‌اندازی — درخواست و شبکه‌سازی
- LinkedIn را به‌روز کن: عنوان "AI Engineer | Python | PyTorch | LLMs"
- برای ۱۰ موقعیت درخواست بده: مهندس هوش مصنوعی، مهندس یادگیری ماشین، دانشمند داده (دبی، از راه دور)
- با ۲۰ متخصص هوش مصنوعی در LinkedIn ارتباط برقرار کن
- تأمل کن: بنویس چه ساختی، چه یاد گرفتی، بعداً کجا می‌روی
- **تحویلی:** درخواست‌های شغلی فعال + یک سند تأمل شخصی

---
---

## 🔧 Essential Tools Throughout the Year | ابزارهای ضروری در طول سال

| Tool | Purpose EN | Purpose FA |
|------|-----------|-----------|
| **Cursor IDE** | Code editor | ویرایشگر کد |
| **GitHub** | Version control + portfolio | کنترل نسخه + پورتفولیو |
| **Kaggle** | Datasets + competitions | Dataset + مسابقات |
| **Jupyter / Colab** | Notebooks | نوت‌بوک |
| **PyTorch** | Deep learning | یادگیری عمیق |
| **Hugging Face** | Pre-trained models | مدل‌های پیش‌آموزش‌دیده |
| **FastAPI** | Model serving | ارائه مدل |
| **Docker** | Containerization | containerization |
| **MLflow** | Experiment tracking | ردیابی آزمایش |
| **AWS Free Tier** | Cloud deployment | استقرار ابری |

---

## 📚 Core Learning Resources | منابع یادگیری اصلی

| Resource | Phase | Language |
|----------|-------|----------|
| fast.ai — Practical Deep Learning | 3 | English |
| 3Blue1Brown YouTube | 1, 3 | English (visual) |
| StatQuest YouTube | 2 | English (visual) |
| Hugging Face Course (free) | 3, 4 | English |
| Kaggle Learn (free) | 1, 2 | English |
| Full Stack Deep Learning | 4 | English |
| "Hands-On Machine Learning" by Aurélien Géron | 2, 3 | English (book) |

---

## 🏁 Where You'll Be After 1 Year | جایگاه تو بعد از ۱ سال

**English:**
✅ Proficient in Python, NumPy, Pandas, Scikit-learn, PyTorch
✅ Experienced with deep learning (CNNs, LSTMs, Transformers)
✅ Can build and deploy real LLM-powered applications
✅ Understands MLOps: Docker, CI/CD, monitoring, cloud
✅ Has 5+ portfolio projects publicly on GitHub
✅ Ready to apply for AI Engineer / ML Engineer roles

**فارسی/دری:**
✅ مسلط بر Python، NumPy، Pandas، Scikit-learn، PyTorch
✅ دارای تجربه در یادگیری عمیق (CNN‌ها، LSTM‌ها، Transformer‌ها)
✅ می‌توانی اپلیکیشن‌های واقعی با LLM بسازی و مستقر کنی
✅ MLOps را درک می‌کنی: Docker، CI/CD، نظارت، ابر
✅ دارای ۵+ پروژه پورتفولیو عمومی در GitHub
✅ آماده برای درخواست نقش‌های مهندس هوش مصنوعی / مهندس یادگیری ماشین

---

> 💡 **Remember / یادت باشد:**
> The goal is not to finish fast. The goal is to build things that work.
> هدف این نیست که سریع تمام کنی. هدف این است که چیزهایی بسازی که کار می‌کنند.

