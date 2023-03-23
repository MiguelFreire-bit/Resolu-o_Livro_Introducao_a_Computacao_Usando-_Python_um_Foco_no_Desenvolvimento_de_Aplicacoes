def inverte_string (a):
    n = ""
    for i in range(len(a)):
        n = n + a[-i-1]
    print(n)

inverte_string('dna')
