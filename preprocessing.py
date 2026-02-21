import re


def preprocess_text(text):
    # convert to lowercase
    text = text.lower()

    # remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # split into words
    words = text.split()

    return words


