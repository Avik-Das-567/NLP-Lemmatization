# Lemmatization in NLP
### App Link
- https://nlp-lemmatization.streamlit.app/
---
### What is Lemmatization?
- **Lemmatization** converts a word to its **root dictionary form (lemma)**.
- Unlike stemming, it returns **real words** using proper **grammar rules**.
- **Example:** “running”, “ran” → “**run**” (valid word).
- **Example Sentence:**

  > "He was running and had run fast."

  After lemmatization:

  > "He be **run** and have **run** fast."

  It corrects based on **tense**, **part of speech**, and **meaning**.
---
### Why Use Lemmatization?
- Produces **real** and **meaningful words**.
- Good for **chatbots**, **text analysis**, and **question answering**.
- It's more accurate than stemming but slightly slower.
---
### Required Python Packages
- **`nltk`**
- **`streamlit`**
---
### Output of the Code

```
Lemmatized: ['The', 'child', 'were', 'running', 'faster', 'than', 'their', 'friend', '.']
```

- "children" → "child", "friends" → "friend"
 
 ---
 ### Some Important Points
- Lemmatization uses **WordNet dictionary**.
- It handles **plural to singular** and **tense conversion**.
- Lemmatization is **smarter** but **slower** than stemming.
---
