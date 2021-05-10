import nltk

# (deffacts facts (waiting_input) (answer)
# (rule G1 S La A)
# (rule G2  A librarie B)
# (rule G3 B am C)
# (rule G4  C cumparat D)
# (rule G5 D o E)
# (rule G6  E carte EPS)
# (rule G7 S Am G)
# (rule G8  G citit H)
# (rule G9 H o E)
# (rule G10  H la I)
# (rule G11 I librarie EPS)
# (rule G12  G cumparat J)
# (rule G13 J si K)
# (rule G14  K am C)
# (rule G15 C citit H)
# )

if __name__ == '__main__':
    # download required nltk packages
    # required for tokenization
    nltk.download('punkt')
    # required for parts of speech tagging
    nltk.download('averaged_perceptron_tagger')

    # input text
    sentence = """Today morning, Arthur felt very good."""

    # tokene into words
    tokens = nltk.word_tokenize(sentence)

    # parts of speech tagging
    tagged = nltk.pos_tag(tokens)

    buffer = []
    for index in range(len(tagged)):
        buffer.append(tagged[index][1])

    # print tagged tokens
    print(buffer)
