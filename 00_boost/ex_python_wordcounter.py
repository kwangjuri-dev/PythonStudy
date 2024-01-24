counts = dict()

line = """
the clown ran after the car and the car ran into the tent
and the tent fell down on the clown and the car 
"""
words = line.split()

for word in words:
    counts[word] = counts.get(word, 0) + 1

print('Counts', counts)
