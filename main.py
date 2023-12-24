import pandas as pd
from DecisionTree import DecisionTree
from utils import colored, Color, typewriter
from constants import title, welcome, welcome_msg


def start(clf):
    print(colored(welcome, Color.MAGENTA))
    print(colored(title, Color.RED))
    typewriter(welcome_msg, Color.MAGENTA)

    play = True
    while play:
        print("\n")
        prediction = clf.play()
        print("\nYour character is : "+ prediction + "\n")

        play = True if input(colored("PLAY AGAIN? (y/n) ", Color.YELLOW)).lower() == 'y' else False


df = pd.read_csv("vamp_characters.csv")
df.drop(columns=["actorName", "id"], inplace=True)

x = df.drop("name", axis=1)
y= df["name"]

clf = DecisionTree()
clf.fit(x, y)

start(clf)