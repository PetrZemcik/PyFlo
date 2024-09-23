

def add_word(thesaurus, base_word, similar_word):
    # base_word=input('Enter the base word: ')
    # similar_word=input('Enter the similar word: ')
    if base_word in thesaurus:
        thesaurus[base_word].add(similar_word)
    else:
        thesaurus[base_word] = {similar_word}


def add_line(thes, line):
    sp = line.split(' : ')
    for word in sp[1].split(' '):
        # print(sp[0], word)
        add_word(thes, sp[0], word)

def load_thesaurus(thes):
    f = open('thesaurus.txt', 'r')
    lines = f.readlines()
    for line in lines:
        add_line(thes, line.strip('\n'))
    f.close()

def main():
    thesaurus = {}
    load_thesaurus(thesaurus)
    # From here, use it! It should be populated.
    # ...
    print(thesaurus)
main()

# thesaurus = {}
# load_thesaurus(thesaurus)
# print(thesaurus)