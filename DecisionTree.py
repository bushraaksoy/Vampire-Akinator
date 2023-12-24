import numpy as np
from constants import questions
from utils import colored, Color

class DecisionTree:
    class Node():
        def __init__(self, feature=None, character=None, left=None, right=None):
            self.right = right
            self.left = left
            self.feature = feature
            self.character = character

    def __init__(self):
        self.root = None

    # TODO add a condition for when we dont have any more features to split with, we will return the closest one
    def build_tree(self, data, target):
        # stopping condition - All leaf nodes
        if len(np.unique(target)) == 1:
            return self.Node(feature=None, character=np.unique(target)[0])
    
        best_feature = self.find_best_split(data, target) 

         # Split the data based on the best feature
        right_data, left_data = self.split(data, best_feature)

        right_target = target[data[best_feature] == 1]
        left_target = target[data[best_feature] == 0]

        # Recursively building the tree
        right_child = self.build_tree(right_data, right_target)
        left_child = self.build_tree(left_data, left_target)

        return self.Node(feature=best_feature, character=None, left=left_child, right=right_child)



    def split(self, data, feature):
        # returns two subsets of the dataset - (left and right for one and zero)
        right = data[data[feature] == 1]
        left = data[data[feature] == 0]
        return(right, left)
    
    def gini_index(self, labels):
        # to decide which feature to split on at each node
        # returns numerical value of the gini impurity

        # Count the occurrences of each label
        counts = dict()
        for label in labels:
            if label not in counts:
                counts[label] = 0
            counts[label] += 1

        # Calculate the impurity
        impurity = 1
        for label in counts:
            prob_of_label = counts[label] / float(len(labels))
            impurity -= prob_of_label**2
        return impurity
    
    def find_best_split(self, data, target):
        best_gini = 1  # Initialize the best Gini Index to 1
        best_feature = None  # Initialize the best feature to None
        
        for feature in data.columns:
            # Split the data based on current feature and value
            left_child = target[data[feature] == 0]
            right_child = target[data[feature] == 1]

            # Calculate Gini Index for each child
            left_gini = self.gini_index(left_child)
            right_gini = self.gini_index(right_child)

            # Calculate average Gini Index
            gini = (len(left_child) * left_gini + len(right_child) * right_gini) / len(target)

            # If this is the best split so far, update the best Gini Index and best feature
            if gini < best_gini:
                best_gini = gini
                best_feature = feature

        return best_feature


    def fit(self, X, y):
        self.root = self.build_tree(X, y)

    def predict(self, X):
        node = self.root
        while node.left or node.right:
            feature_value = X[node.feature].values[0]  # Extract the value from the Pandas Series
            if feature_value == 0:
                node = node.left
            else:
                node = node.right
        return node.character
    
    def play(self):
        node = self.root
        while node.left or node.right:
            value = 1 if input(colored(questions[node.feature], Color.CYAN)).lower() == 'y' else 0
            feature_value = value  
            if feature_value == 0:
                node = node.left
            else:
                node = node.right
        return node.character
