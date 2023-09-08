import nltk

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Tokenize the text
def tokenize(text):
  tokens = nltk.word_tokenize(text)
  return tokens

# Tag the tokens with part-of-speech tags
def pos_tag(tokens):
  pos_tags = nltk.pos_tag(tokens)
  return pos_tags

# Identify passive voice by looking for past participles that are not followed by an auxiliary verb
def find_passive_voice(pos_tags):
  passive_voice = False
  for i, (word, pos) in enumerate(pos_tags):
    if pos == 'VBN':
      if i == 0 or pos_tags[i-1][1] not in ['VBD', 'VBG', 'VBP', 'VBZ']:
        passive_voice = True
  return passive_voice

# Function to analyze a text input and determine if it is in the passive voice
def analyze_text(text):
    tokens = tokenize(text)
    pos_tags = pos_tag(tokens)
    passive_voice = find_passive_voice(pos_tags)
    return passive_voice

# Test the model on a sample sentence
if __name__ == "__main__":
    sentence = "The ball was thrown by the boy."
    print(f"Passive voice: {analyze_text(sentence)}")

