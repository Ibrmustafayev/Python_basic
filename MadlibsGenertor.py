with open("story.txt", "r") as f:
    story = f.read()

phrase_start = "["
phrase_end = "]"
words = set()
index = -1

for idx, character in enumerate(story):
    if character == phrase_start:
        index = idx
    if character == phrase_end and index != -1:
        word = story[index: idx+1]
        words.add(word)
        index = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print("\n" + story)