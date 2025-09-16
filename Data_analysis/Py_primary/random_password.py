import random
import string

def get_user_length():
    length = int(input("Enter password length: "))
    return length

def generate_mandatory_chars():
    mandatory = [
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    return mandatory

def generate_remaining_chars(length, mandatory_chars):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_chars) for _ in range(length - len(mandatory_chars))]
    return remaining

def shuffle_and_combine(mandatory_chars, remaining_chars):
    password_list = mandatory_chars + remaining_chars
    random.shuffle(password_list)
    return ''.join(password_list)
