import re

import clips
import nltk


def read_from_console():
    '''
    This function reads a single sentence from the keyboard and returns it
    :return:string with the sentence
    '''
    while True:
        input_text = input("Write the text: ")
        if input_text[-1] not in ['.', '?', '!', ';']:
            print("You didn't finished the sentence properly. You must end the sentence with one of these: ?!;.")
        text_splited = re.split('[.?!]', input_text)
        if len(text_splited) > 2:
            print("Read only one sentence at a time.")
        elif len(text_splited) == 2:
            return input_text


def read_from_file():
    '''
    this function reads from input.txt file and returns the text divided into sentences
    :return: list with sentences
    '''
    with open("./input.txt") as file:
        input_text = file.read()
    text_splited = re.split('[.?!;]', input_text)
    return text_splited


def read_rules():
    '''
    This function reads the rules from rules.txt and returns them
    :return: the rules read
    '''
    lines = []
    file = open('rules', 'r')
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line)
    file.close()
    for i, line in enumerate(lines):
        lines[i] = lines[i][:-1]
    return lines


def parser(text):
    '''
    This function takes each sentence separately and parses and checks it
    :param text: the text must be string for 1 sentece(from keyboard) or list for many sentences(from file)
    '''
    rules = read_rules()
    if type(text) == str:
        validate = validate_sentence_by_rules(rules, parse_sentence(text))
    elif type(text) == list:
        for sentence in text:
            validate = validate_sentence_by_rules(rules, parse_sentence(sentence))
    else:
        print("The input is invalid for parsing!")


def parse_sentence(sentence):
    '''
    This function parses with ntlk the sentence received
    :param sentence is a string
    :return: parsed sentence just with symbols
    '''
    buffer = []
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    for elem in tagged:
        buffer.append(elem[1])
    return buffer


def validate_sentence_by_rules(rules, architecture):
    env = clips.Environment()
    for cnt, i in enumerate(rules):
        rule = '''
        (defrule rule%s
            (sentence %s)
            =>
            (printout t "The sentence is correct." crlf))
        ''' % (str(cnt), i)
        env.build(rule)
    rule = '''
    (defrule wrong
        =>
        (printout t "The sentence is wrong." crlf))
    '''
    env.build(rule)

    sentence = ''
    for i in architecture:
        sentence = sentence + i + ' '
    sentence = sentence[:-1]

    # print(sentence)

    fact_string = f'(sentence {sentence})'
    fact = env.assert_string(fact_string)
    template = fact.template

    assert template.implied == True

    validation_result = env.run()
    return validation_result


if __name__ == '__main__':
    print("Hello! Please choose one option.\n"
          "1. Read from console.\n"
          "2. Read from Input file.")

    while True:
        option = input("Type your option: ")
        if option == "1":
            parser(read_from_console())
            break
        elif option == "2":
            parser(read_from_file())
            break
    print("Successfully!")
