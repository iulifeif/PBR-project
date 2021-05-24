import nltk
import clips


def read_sentence():
    while True:
        sentence = input("Sentence:")
        if sentence[-1] not in ['.', '?', '!', ';']:
            print("You didn't finished the sentence properly.")
        else:
            cnt = 0
            for i in sentence:
                if i in ['.', '?', '!', ';']:
                    cnt = cnt + 1
            if cnt == 1:
                return sentence
            else:
                print("Read only one sentence at a time.")


def words_tagging(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged


def get_rules():
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


def clips_fragment(rules, architecture):
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

    print(sentence)

    fact_string = f'(sentence {sentence})'
    fact = env.assert_string(fact_string)
    template = fact.template

    assert template.implied == True

    x = env.run()
    return x


def get_result(sentence, architecture, correctitude):
    print("The sentence:", end=" ")
    print(sentence)
    print()
    print("With the next morphology sintax:")
    print(architecture)
    print()
    print("Seems to be:", end=" ")
    if correctitude == 1:
        print("WRONG")
        print()
        final = input("Is our answer correct? (y = yes , n = no) --> ")
        if final == 'n':
            print()
            print("Thank you for your feedback.")
            print("Next time we will know the correct answer for this type of sentence.")
            rule = ''
            for morph in architecture:
                rule = rule + morph + ' '
            rule = rule[:-1]
            file = open("rules", "a")
            file.write(rule)
            file.write('\n')
    else:
        print("CORRECT")


sentence = read_sentence()
architecture = []
for i in words_tagging(sentence):
    architecture.append(i[1])
correctitude = clips_fragment(get_rules(), architecture)
print()
print()
print()
print()
print()
get_result(sentence, architecture, correctitude)
