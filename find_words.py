text = 'In this lecture we will review some additional functionalities of python built-in data structures.'

# Split the text into words and count the words containing the letter 'e'
words_with_e = [word for word in text.split() if word.count('e') > 0]

# Print the result
print("Number of words with the letter 'e':", len(words_with_e))
