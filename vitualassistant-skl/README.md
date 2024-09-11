
# Voice-Controlled Chatbot with Speech Recognition

This project demonstrates a voice-controlled chatbot that listens to user input, recognizes the speech, and responds using a text-based intent classification model. The chatbot uses Google Speech Recognition to convert voice to text and SAPI's text-to-speech functionality to provide responses.

## Features
- **Speech Recognition**: Uses `speech_recognition` library to convert voice input into text.
- **Text-to-Speech**: Uses Microsoft's SAPI (Speech Application Programming Interface) for voice output.
- **Intent Classification**: Uses a machine learning model to predict the intent of the user's text input based on predefined patterns and tags.
- **Custom Responses**: Each intent has a set of possible responses that the model can randomly select from.

## How it Works
1. **Listening for Voice Input**: The program listens to the microphone for speech input.
2. **Speech Recognition**: Converts the speech into text using Google's Speech Recognition API.
3. **Intent Classification**: A trained logistic regression model predicts the user's intent based on the input text.
4. **Response Generation**: The chatbot replies with a suitable response from the predefined intent dataset.
5. **Text-to-Speech Output**: The response is read out loud using SAPI's text-to-speech feature.

## Setup and Installation

### Prerequisites
- Python 3.x
- Required Python libraries:
    - `win32com.client` (for SAPI)
    - `speech_recognition`
    - `scikit-learn`
    - `numpy`
    - `random`

### Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Install the required libraries:
    ```bash
    pip install pywin32 speechrecognition scikit-learn numpy
    ```

3. Ensure you have a working microphone and that Python's `speech_recognition` package can access it.

4. Download the necessary dependencies for `speech_recognition`:
    ```bash
    pip install pyaudio
    ```

5. Make sure your SAPI (Speech API) is properly set up on your Windows machine.

### Usage
1. Run the main script:
    ```bash
    python main.py
    ```

2. The program will start listening for voice input. When a command or query is detected, the chatbot will attempt to classify the intent and provide a spoken response.

3. To exit the program, say "exit" or "bye."

## Customization

### Modifying Intents
The chatbot's responses are based on a JSON file (`intents.json`) containing predefined patterns and responses. You can modify the existing intents or add new ones to customize the bot's behavior.

Example structure for `intents.json`:
```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hello", "Hi", "Hey"],
      "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    {
      "tag": "goodbye",
      "patterns": ["Bye", "Goodbye", "See you later"],
      "responses": ["Goodbye!", "See you later!", "Take care!"]
    }
  ]
}
```

### Training the Model
The project uses a simple logistic regression model with a `TfidfVectorizer` to classify intents. The model is retrained every time you run the script. You can further enhance it by:
- Adding more intents and patterns.
- Using different machine learning models or pipelines.
- Implementing more advanced natural language processing (NLP) techniques.

## Contributing
Feel free to submit issues or pull requests if you would like to contribute to the project!

## License
This project is open-source and educational purpose 