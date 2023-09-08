## NLP Passive Voice Detector

Welcome to the NLP Passive Voice Detector! This project leverages Natural Language Processing (NLP) techniques to identify sentences written in passive voice. The underlying method hinges on identifying past participles not followed by auxiliary verbs, a common indicator of passive voice.

### How it Works

Here’s an overview of how the NLP model functions:

1. **Text Tokenization**:
   - The first step involves breaking down the input text into individual words or tokens using NLP tokenization techniques.
   
2. **Part-of-Speech Tagging**:
   - Once we have the tokens, the next step is to assign each word a part-of-speech (POS) tag utilizing the `pos_tag` function from the nltk library. This function helps in identifying the grammatical role of each word in the text.

3. **Passive Voice Identification**:
   - With the POS tags at hand, the model searches for past participles not succeeded by an auxiliary verb, which is a prevalent indicator of passive voice in a sentence.

### Getting Started

To get started with the project, you'll need to have Python and the NLTK library installed. Here are the installation instructions:

```bash
pip install nltk
```

Next, clone this repository to your local machine to access the script and start working with the passive voice detector.

### Usage

To use the passive voice detector, simply input the text you wish to analyze into the script. The script will then output whether the text is in passive voice or not based on the criteria mentioned in the “How it Works” section.

### Contributions

Feel free to fork this project and make contributions. We welcome contributions that improve the accuracy and efficiency of the passive voice detector.

