import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text = """In this project, we are building a text summarizer using machine learning. The project uses natural language processing to teach computers to understand human text. 
This could help to discover relevant information and to consume relevant information faster. The program takes in a text and returns a summary of the text, which is useful for busy individuals who do not have the time to read lengthy articles and reports. 
Text Summarization can be performed in two ways: Extraction-based and Abstraction-based. 
The project uses the Python library called Spacy for natural language processing, and the first step is to install Spacy on the machine. We also set up a Python virtual environment to keep the project dependencies separate 
from the global Python dependencies. We use Flask for the frontend and it provides us with a seamless and user- friendly interface."""

stopwords = list(STOP_WORDS)
# print(stopwords)
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
# print(doc)
tokens = [token.text for token in doc]
# print(tokens)
word_frequency = {}
for word in doc : 
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_frequency.keys():
            word_frequency[word.text]=1
        else:
            word_frequency[word.text]+=1
# print(word_frequency)
max_freq = max(word_frequency.values())
# print(max_freq)
for word in word_frequency.keys():
    word_frequency[word] = word_frequency[word]/max_freq   
# print(word_frequency)
    
sent_tokens = [sent for sent in doc.sents]
# print(sent_tokens)

sent_scores={}
for sent in sent_tokens: 
    for word in sent:
        if word.text in word_frequency.keys():
            if sent not in sent_scores.keys():
                sent_scores[sent] = word_frequency[word.text]
            else:
                sent_scores[sent] += word_frequency[word.text]
print(sent_scores)