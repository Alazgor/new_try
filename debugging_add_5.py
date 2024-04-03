# This code attempts to concatenate a list of words into a sentence

def create_sentence(words):
    return ' '.join(words)

word_list = ["The", "quick", "brown", "fox"]
result = create_sentence(word_list)
print(result)
