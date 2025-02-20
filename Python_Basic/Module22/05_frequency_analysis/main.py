import string
from collections import Counter

with open('text.txt', 'r') as f:
    text = f.read()


letters = [char.lower() for char in text if char.isalpha()]


letter_counts = Counter(letters)


total_letters = sum(letter_counts.values())


letter_percentages = {}
for letter in string.ascii_lowercase:
    if letter_counts[letter] > 0:
        letter_percentages[letter] = round((letter_counts[letter] / total_letters * 100) / 100, 3)


sorted_letter_percentages = sorted(letter_percentages.items(), key=lambda x: (-x[1], x[0]))


with open('analysis.txt', 'w') as f:
    for letter, percentage in sorted_letter_percentages:
        f.write(f"{letter}: {percentage}\n")
