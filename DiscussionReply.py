def words_to_numbers(text):
    words_to_digits = {
        "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12
    }
    return [words_to_digits[word] for word in text.split() if word in words_to_digits]

# Example usage
text = "one two eleven"
print(words_to_numbers(text))  # Output: [1, 2, 11]
