# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('DataSet/review_dataset.tsv', delimiter='\t', quoting=3)

# Clean the texts
import re

# get one review
review = dataset['Review'][0]

# remove all things except letters
import re
review = re.sub('[^a-zA-Z]', ' ', review)

# set all letters to lowercase
review = review.lower()

# convert the string to a list
review_words = review.split()

# remove non significant words
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

review = [word for word in review_words if not word in set(stopwords.words('english'))]

# stemming => taking the root of the words
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def stemming(word):
    return stemmer.stem(word)

review_after_stemming = [stemming(word) for word in review]

# convert list into string
review = ' '.join(review_after_stemming)

# doing this method to all reviews
corpus = []
for i in range(0,1000):
    review = dataset['Review'][i]
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower()
    review_words = review.split()
    review = [word for word in review_words if not word in set(stopwords.words('english'))]
    stemmer = PorterStemmer()
    review_after_stemming = [stemming(word) for word in review]
    review = ' '.join(review_after_stemming)
    corpus.append(review)
