import csv

MAX_CHARACTERS = 6
MIN_CHARACTERS = 3

def main():
    with open('words_alpha.txt', mode ='r') as fr:
        with open('words_small.txt', mode = 'w+') as fw:
            r = csv.reader(fr)
            w = csv.writer(fw)

            for line in r:
                first_word = line[0].split()[0]
                if MIN_CHARACTERS <= len(first_word) <= MAX_CHARACTERS:
                    w.writerow([first_word])


if __name__ == '__main__':
    main()
