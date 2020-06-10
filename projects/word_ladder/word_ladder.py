import string
from util import Queue

word_set = set()

with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip() # no new line
        word_set.add(line.lower())

letters = list(string.ascii_lowercase)

def get_neighbors(word):
    neighbors = []

    word_letters = list(word)

    # for each letter in the word
    for i in range(len(word_letters)):
        # replace with all English letters
        for letter in letters:
            separated = list(word_letters)
            separated[i] = letter

            together = "".join(separated)

            # see if we form a word
            if together != word and together in word_set:
                neighbors.append(together)

    return neighbors

def get_word_ladder(initial, result):
    visited = set()

    q = Queue()

    q.enqueue([initial])

    while q.size() > 0:
        path = q.dequeue()
        cur_word = path[-1] # get last word from path list
        if cur_word not in visited:
            visited.add(cur_word)
            if cur_word == result:
                return path
            else:
                for neighbor in get_neighbors(cur_word):
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)


print(get_word_ladder('cat', 'dog'))