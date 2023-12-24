import pandas as pd
from constants import questions

# THIS IS THE VERSION OF THIS GAME WITHOUT THE USE OF MACHINE LEARNING

df = pd.read_csv("vamp_characters.csv")
df.drop(columns=["actorName", "id"], inplace=True)

# checking for duplicates in the dataset
def checkDuplicates(data):
    df2 = data.copy()
    df2.drop(columns=["name"], inplace=True)
    print(data[df2.duplicated()])


def find_not(condition):
    return df[df[condition] == 0]


def find(condition):
    return df[df[condition] == 1]


def ask():
    global df
    for question in questions:
        if valid_question(question, df):
            ans = input(questions[question])
            df = find(question) if ans.lower() == "y" else find_not(question)
            if len(df) <= 1:
                break
        else:
            continue
    if len(df) > 1:
        print("We could not find your character, but the closest match is: ")
    return df


def valid_question(feature, data):
    # returns true if remaining database has a 1 in feature column of next question
    return True if data[feature].isin([1]).any() else False


def play():
    answer = ask()["name"].values[0]
    print("Your character is:", answer)

play()
