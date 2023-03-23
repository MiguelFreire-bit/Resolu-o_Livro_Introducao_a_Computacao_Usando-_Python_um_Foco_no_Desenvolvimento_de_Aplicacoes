def pagar (a, b):
    if b <= 40:
        print(round(a * b))
    else:
        print(round((a * 40) + ((b-40) * (a * 1.5))))

pagar(10, 10)
pagar(10, 35)
pagar(10, 45)
