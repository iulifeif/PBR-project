import nltk


def read_data(path):
    # functie de parsare, ce primeste path catre un fisier,
    # extrage propozitiile, si va scrie intr-un alt fisier,
    # analiza acelor propozitii(engleza)
    with open(path, 'r') as file:
        data = file.read()
        data = ''.join(data.splitlines())
        data = re.split('[.?!]', data)
    with open('output.txt', 'w') as file:
        for line in data[:-1]:
            tokens = nltk.word_tokenize(line.lstrip())
            tagged = nltk.pos_tag(tokens)
            buffer = []
            for index in range(len(tagged)):
                buffer.append(tagged[index][1])
            current = ''
            for i in buffer:
                if i not in ',:;)(':
                    file.write(str(i) + ' ')
            file.write('\n')
