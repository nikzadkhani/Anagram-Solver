import csv

MAX_CHARACTERS = 6
MIN_CHARACTERS = 3

FILENAME = 'words_small.txt'

def is_valid_word(characters, word) -> bool:
    character_list = list(characters)
    for c in word:
        if c in character_list:
            character_list.remove(c)
        else:
            return False
    return True

def get_valid_words(characters):
    assert(MIN_CHARACTERS <= len(characters) <= MAX_CHARACTERS)

    valid_words = []
    with open(FILENAME, mode='r') as f:
        r = csv.reader(f)
        for line in f:
            word = line.rstrip("\n")
            if is_valid_word(characters, word):
                valid_words.append(word)

    return valid_words

def main():
    characters = input("Enter the characters:\n")
    valid_words = get_valid_words(characters)
    sorted_words = sorted(valid_words, key=len)

    current_length = 2
    for word in sorted_words:
        if len(word) > current_length:
            current_length += 1
            print('\nWord Length of {}'.format(current_length))
        print(word)


if __name__ == '__main__':
    main()
