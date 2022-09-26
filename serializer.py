import pickle

words_file = "./anglish_words.txt"
serial_file = "./anglish_words.pickle"

words = []

with open(words_file, "r") as f:
    for line in f:
        words.append(line.strip().lower())

pickle.dump(words, open(serial_file, "wb"))