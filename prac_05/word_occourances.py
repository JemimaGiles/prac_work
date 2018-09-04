word_counter = {}

text = input("Text: ")

words = text.split()
for word in words:
    frequency = word_counter.get(word, 0)

words = list(word_counter.keys())
words.sort()

max_length = max((len(words) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_counter[word]))

# why doesnt this work?