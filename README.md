# Vampire Akinator Project🧞

This project is about a character guessing game which uses machine learning algorithms to guess a character from a tv series. 
This game is a mystery game and is targeted for anyone who wants to have some fun with testing to see how well a machine learning algorithm can guess their character.

## Characters:
The game includes 32 characters from The Vampire Diaries series that the akinator will try to guess using a series of yes and no questions.

The characters range between difficult to guess and easy to guess. Difficult to guess characters are the ones which are very similar to other characters in terms of their features, making them hard to predict, while easy to guess are very unique compared to others, making them easier to predict.

## Dataset:
The dataset contains of rows 32 characters and 24 columns with 23 being the characters' features in the form of “isFemale” or “isVampire” and so on, 
with boolean data at the values.

We also utilize a dictionary with key value pairs. The key being the question: “isVampire”, and the value being the corresponding questions: “Is your character a vampire? (y/n)”. This dictionary will be used to determine the question to be asked in relation with the column values present in the dataset.


## Input:
The user will answer the questions given in terms of y or n, indicating yes or no.

## Prediction:
Each response from the user will be used to predict the character better by filtering the database and reducing it down to the features only answered with a yes.

A decision tree will be used to make predictions by splitting the data into subsets based on the values of the features. Each split corresponds to a node in the tree. The feature and value used for the split are chosen to maximize the separation of the classes in the resulting subsets.

When the user answers a question, the decision tree is being traversed effectively. A ‘yes’ answer will take you down the right branch of the tree, while a ‘no’ answer will take you down the left branch. Each question helps to narrow down the possible characters.

The decision tree is trained to ask the most informative questions first. That is, the questions that do the best job of separating the characters into distinct groups. This allows the game to quickly narrow down to the correct character.

## Conclusion:
In conclusion, our application will try to guess a character from “The Vampire Diaries” series based on a series of yes and no questions answered by the user, using a machine learning decision tree model. All the while keeping the experience fun and exciting for the user😄.


# How you can use this project

### Clone the project from your terminal: 
git clone https://github.com/bushraaksoy/VampireAkinator.git

### Install pandas and numpy libraries if you dont already have them intalled:
pip install pandas

pip install numpy

### Play
Run the main file and you are ready to play!
