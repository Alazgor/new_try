def filter_strings_starting_with_vowel(strings):
    return [s for s in strings if s[0].lower() in 'aeiou']

# Test
input_strings = ["Apple", "Banana", "Orange", "Grapes", "Kiwi", "Pear", "Pineapple"]
result = filter_strings_starting_with_vowel(input_strings)
print(result)
