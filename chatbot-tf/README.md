# Chatbot Using TensorFlow

This is a Python-based chatbot powered by a neural network built using TensorFlow. The chatbot is designed to recognize user inputs and respond accordingly based on predefined intents.

## Features

- **Natural Language Processing (NLP)**: Uses tokenization and lemmatization to process and understand user input.
- **Machine Learning Model**: Utilizes a TensorFlow neural network for classifying intents and predicting responses.
- **Customizable Intents**: Define your own intents and responses in the `intents.json` file to suit different chatbot applications.

## Project Structure

```bash
├── chatbot_model.h5        # Trained neural network model
├── classes.pkl             # Serialized class labels
├── words.pkl               # Serialized word list used for training
├── intents.json            # File defining the intents, patterns, and responses
├── train_chatbot.py        # Script to train the chatbot model
├── chatbot.py              # Main script to run the chatbot
├── README.md               # Project documentation (this file)
└── requirements.txt        # List of dependencies
```

## Requirements

- Python 3.x
- TensorFlow
- Numpy
- NLTK
- Keras

Install dependencies using:

```bash
pip install -r requirements.txt
```

## How It Works

1. **Preprocessing**: 
   - The chatbot processes the input by tokenizing and lemmatizing the user's sentence using NLTK.
   - It then creates a "bag of words" representation of the sentence based on the trained vocabulary.

2. **Intent Classification**:
   - The preprocessed sentence is passed to the trained neural network, which predicts the most likely intent.

3. **Response Generation**:
   - Based on the predicted intent, the chatbot selects a random response from the predefined set of responses for that intent in `intents.json`.

## Training the Model

To train the chatbot's neural network model, run:

```bash
python train_chatbot.py
```

This script will read the intents from `intents.json`, process the patterns, and train a model to classify intents.

## Running the Chatbot

Once the model is trained, you can run the chatbot using:

```bash
python chatbot.py
```

The chatbot will prompt you for input and respond based on the predictions.

## Customizing the Chatbot

### Updating Intents

You can modify or create new intents by editing the `intents.json` file. The file is structured as follows:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hello",
        "How are you?"
      ],
      "responses": [
        "Hello!",
        "Hi there!",
        "Greetings!"
      ]
    },
    ...
  ]
}
```

- **Tag**: A unique identifier for the intent.
- **Patterns**: Sample user inputs that correspond to the intent.
- **Responses**: Possible responses the chatbot can give for that intent.

After updating `intents.json`, you need to retrain the model by running `train_chatbot.py` again.

## Example Conversation

```bash
User: Hi
Chatbot: Hello!
User: Can you help me?
Chatbot: Sure, what do you need help with?
User: Goodbye
Chatbot: Bye! Take care!
```

## Dependencies

The project requires the following libraries:

- TensorFlow
- Keras
- Numpy
- NLTK
- Pickle

All dependencies can be installed via `requirements.txt`.

```bash
pip install -r requirements.txt
```

## License

This project is open-source and only for personal use and education purpose.
