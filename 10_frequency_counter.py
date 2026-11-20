# Frequency counter using dictionaries
text = input("Enter a sentence: ")
frequency = {}

for word in text.lower().split():
    word = word.strip(".,!?;:")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")
