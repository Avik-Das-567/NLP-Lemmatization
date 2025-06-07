import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

text = "The children were running faster than their friends."

words = word_tokenize(text)
lemmatized = [lemmatizer.lemmatize(w) for w in words]

st.write("Lemmatized:", lemmatized)