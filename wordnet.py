
import nltk
from nltk.corpus import wordnet


# Get synonyms of a word
def get_synonyms(word):
    synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
    return synonyms

# Get antonyms of a word
def get_antonyms(word):
    antonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return antonyms

# # Example usage
# word = "wood"
# synonyms = get_synonyms(word)
# antonyms = get_antonyms(word)

# print("Synonyms of", word + ":")
# print(synonyms)

# print("Antonyms of", word + ":")
# print(antonyms)
