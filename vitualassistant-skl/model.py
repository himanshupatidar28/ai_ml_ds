import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import random

# Load the data
with open('intents.json', 'r') as f:
    data = json.load(f)

# Extract patterns and their corresponding tags
texts = []
tags = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        texts.append(pattern)
        tags.append(intent['tag'])

# Encode labels to numerical values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(tags)

# Define the pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train the model
model.fit(texts, y)

# Define the predict function
def predict(text):
    predicted_label = model.predict([text])
    tag = label_encoder.inverse_transform(predicted_label)[0]
    for intent in data['intents']:
        if intent['tag'] == tag:
            predictions= intent['responses']
            i =random.randint(0,len(predictions)-1)
            return predictions[i]

# while(True):
#     new_text = input("enter: ")
#     predictions = predict(new_text)
#     print(predictions)  # Output could be one of the responses from the "greeting" tag
