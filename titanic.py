"""
Hello from LivePreso :) This is the file you should be editing. Good luck!
"""

path = "./titanic.csv"

import pandas as pd


def number_of_passengers():
    df = pd.read_csv(path)
    return df["PassengerId"].count()


def total_fare_paid():
    df = pd.read_csv(path)
    return df["Fare"].sum()


def median_fare():
    df = pd.read_csv(path)
    return df["Fare"].median()


def cherbourg_survival_rate():
    # I assume "Embarked" column "C" is Cherbourg
    df = pd.read_csv(path)

    cherbourg = df[df["Embarked"] == "C"]

    passenger_count = cherbourg["PassengerId"].count()
    survived_count = cherbourg[cherbourg["Survived"] == 1]["PassengerId"].count()

    return round(survived_count / passenger_count, 6)


def surviviest_passenger_class():
    df = pd.read_csv(path)
    df = df[df["Survived"] == 1].groupby(["Pclass"])["Pclass"].count()
    return list(df.to_dict().keys())
