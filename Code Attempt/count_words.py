from collections import Counter
import re

def read_text():
    return input("Enter text: ")


def split_words(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().split()


def count_words(words):
    return Counter(words)


def sort_words(word_count):
    return word_count.most_common()

def print_word_count(sorted_list):
    for word, count in sorted_list:
        print(f"{word}: {count}")


def main():
    text = read_text()
    words = split_words(text)
    word_count = count_words(words)
    sorted_list = sort_words(word_count)
    print_word_count(sorted_list)

if __name__ == "__main__":
    main()
