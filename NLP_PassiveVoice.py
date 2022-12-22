import nltk

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
      if i+1 >= len(pos_tags) or pos_tags[i+1][1] not in ['MD', 'BE']:
        passive_voice = True
  return passive_voice

# Test the model on a sample sentence
sentence = "The ball was thrown by the boy."
tokens = tokenize(sentence)
pos_tags = pos_tag(tokens)
passive_voice = find_passive_voice(pos_tags)
print(f"Passive voice: {passive_voice}")
