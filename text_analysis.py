import string
from collections import Counter

def process_file(filename):
    """Function to read the file and process the text"""
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    word_count = Counter(words)

    return word_count

def display_most_frequent(word_count):
    """Function to display the 10 most frequent words"""
    most_common_words = word_count.most_common(10)

    print("The 10 most frequent words are:")
    for word, frequency in most_common_words:
        print(f"{word}: {frequency}")