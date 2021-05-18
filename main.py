import re
import nltk


grammar = {
    "key": "value",
    "s": ["np", "vp"],
    "np": ["det", "n", "np", "rel"],
    "vp": ["tv", "v", "np"],
    "rel": ["rpn", "vp"]
}


def read_data(path):
    sentences = [[]*100]
    with open(path) as file:
        data = file.read()
    res = re.split('[.?!;]', data)
    for sentence in res:
        # aici exista niste probleme, string - list
        if "," in sentence:
            aux = sentence.split(",")
            aux_sentence = ""
            for word in aux:
                aux_sentence += word
            sentence = aux_sentence
        if '\n' in sentence:
            sentence = sentence[1:]
        if sentence != '':
            sentences.append(sentence)
    return sentences


def tokenize_sentences(sentences):
    tokenized = []
    for line in sentences[:-1]:
        tokens = nltk.word_tokenize(line.lstrip())
        tagged = nltk.pos_tag(tokens)
        buffer = []
        for index in range(len(tagged)):
            buffer.append(tagged[index][1])
        tokenized.append(buffer)
    return tokenized


def verifying_rules(tokenized):
    for line in range(len(tokenized)):
        for col in range(len(tokenized[line])-1):
            actual_location = tokenized[line][col].lower()
            future_location = tokenized[line][col+1].lower()
            if actual_location not in grammar.keys():
                grammar[actual_location] = future_location
                print(actual_location, " ", future_location)
            else:
                if future_location not in grammar[actual_location]:
                    grammar[actual_location].append(future_location)
                    print(actual_location, " ", future_location)
    print("success")
    print(grammar)


if __name__ == '__main__':
    sentences = []
    sentences = read_data("./input.txt")
    sentences_tokenized = tokenize_sentences(sentences[1:])
    print(sentences_tokenized)
    verifying_rules(sentences_tokenized)
