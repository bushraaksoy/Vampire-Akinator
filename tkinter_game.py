import tkinter as tk
import pandas as pd
from DecisionTree import DecisionTree
from constants import questions

def yes_button_clicked():
    question_label.config(text="You clicked 'Yes'")

def no_button_clicked():
    question_label.config(text="You clicked 'No'")

root = tk.Tk()
root.title("AKINATOR")
root.geometry("600x400")  # Setting window size to 600x400

# Configure the background color and font
root.configure(bg='black')
root.option_add('*Font', 'Consolas 12')  # Monospace font (Consolas)

# Title label in the center
title_label = tk.Label(root, text="AKINATOR", font=("Consolas", 34, "bold"), bg='black', fg='white' )
title_label.pack(pady=50)  # Add padding on top

# Question label at the center
question_label = tk.Label(root, text="Is the character supernatural?", font=("Consolas", 18), bg='black', fg='white')
question_label.pack()

# Frame to hold buttons
button_frame = tk.Frame(root, bg='black')
button_frame.pack(pady=20)  # Add padding between question and buttons

# Yes button
yes_button = tk.Button(button_frame, text="Yes", width=10, command=yes_button_clicked)
yes_button.pack(side=tk.LEFT, padx=20)  # Add padding on the left

# No button
no_button = tk.Button(button_frame, text="No", width=10, command=no_button_clicked)
no_button.pack(side=tk.LEFT, padx=20)  # Add padding on the right

root.mainloop()



# df = pd.read_csv("vamp_characters.csv")
# df.drop(columns=["actorName", "id"], inplace=True)

# x = df.drop("name", axis=1)
# y= df["name"]


# clf = DecisionTree()
# clf.fit(x, y)

# xtest = df[df["name"] == "Katherine Pierce"]
# xtest = xtest.drop(columns=["name"])

# play = True
# while play:
#     prediction = clf.play()
#     print("Your predicted character is: ", prediction, "\n")

#     play = True if input("Play again? (y/n) ").lower() == 'y' else False