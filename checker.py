import pickle
import spacy
import string

nlp = spacy.load("en_core_web_trf") #...web_sm if you got that package
lemmatizer = nlp.get_pipe("lemmatizer")

serial_file = "./anglish_words.pickle"
words = pickle.load(open(serial_file, "rb"))

extra_ignored_characters = ["—"]

while True:
    sentence = input(">> ").lower().strip()
    
    doc = nlp(sentence)
    # print([token.lemma_ for token in doc])
    tokens = []
    for token in doc:
        token_lemma = str(token.lemma_)
        if token_lemma not in string.punctuation and \
            not token_lemma.isdigit() and \
            token_lemma not in extra_ignored_characters:
            tokens.append(token.lemma_.lower())
    
    non_anglish_words = []
    
    for token in tokens:
        if token not in words:
            non_anglish_words.append(token)
    
    non_anglish_words = list(set(non_anglish_words))
    
    print(f"\nThe following words are not found in the Anglish Wordbook and Germanic Thesaurus:\n")
    list_of_words = ""
    for word in non_anglish_words:
        # print(word)
        list_of_words += f"{word}, "
    print(list_of_words)