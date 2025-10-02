#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
import re

def is_sentence(text):
    # Make sure input is actually text and not empty
    if not isinstance(text, str) or not text.strip():
        return False

    # First character should be a capital letter
    if not text[0].isupper():
        return False

    # Must finish with punctuation like . ? or !
    if not re.search(r'[.!?]$', text):
        return False

    # Needs to have at least one word (not just spaces)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

# Keep asking until the input fits the rules above
while (is_sentence(user_sentence) == False):
    print("That doesn’t count as a proper sentence.")
    user_sentence = input("Enter a sentence: ")

# Break the sentence into words and clean punctuation
words = user_sentence.split()
clean_words = [re.sub(r'[^\w]', '', word).lower() for word in words]

word_list = []
freq_list = []

# Go through each word and count how many times it shows up
for word in words:
    if word in word_list:
        index = word_list.index(word)
        freq_list[index] += 1
    else:
        word_list.append(word)
        freq_list.append(1)

# Print the word frequency results
for i in range(len(word_list)):
    print(f"{word_list[i]}: {freq_list[i]}")
print()
