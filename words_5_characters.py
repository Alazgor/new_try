text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

# Split the text into words and count the words with more than 5 characters
words_more_than_5_chars = [word for word in text.split() if len(word) > 5]

# Print the result
print("Number of words with more than 5 characters:", len(words_more_than_5_chars))
