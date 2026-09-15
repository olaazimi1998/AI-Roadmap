import pandas as pd


def extract():
    data = pd.read_csv(r"C:\Users\olaaz\Documents\AI Roadmap\week12-etl\data\employees.csv")
    return data


def transform(data):
    data["name"] = data["name"].str.strip()

    data["department"] = data["department"].str.strip()

    data["salary"] = data["salary"].astype(int)

    return data


def load(data):
    data.to_csv(r"C:\Users\olaaz\Documents\AI Roadmap\week12-etl\data\clean_employees.csv",
                 index=False)


raw_data = extract()
clean_data = transform(raw_data)
load(clean_data)