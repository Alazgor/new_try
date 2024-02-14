def can_find(bigrams, words):
    # Check if every bigram can be found in at least one word
    return all(any(bigram in word for word in words) for bigram in bigrams)

# Test cases
print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))  # True
print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))  # False
print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))  # True
print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))  # False
