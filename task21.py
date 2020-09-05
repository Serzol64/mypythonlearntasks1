import collections

text = 'Безумно жаль, что это все когда-нибудь закончится.'
words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

print(most_common, longest)