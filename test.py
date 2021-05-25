s = """(defrule read_input
        ?a <- ({})
        =>
        (printout t "Insert sentence: " crlf)
        (assert (text S (explode$ (readline))))

        (retract ?a))""".format("ceva")

if __name__ == '__main__':
    print(s)
