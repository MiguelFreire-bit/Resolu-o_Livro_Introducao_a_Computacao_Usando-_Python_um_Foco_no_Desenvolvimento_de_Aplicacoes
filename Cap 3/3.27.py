while True:
    n = input("digite n: ")
    if n.isdigit() and int(n) >= 0:
        n = int(n)
        break

for i in range(n):
    if n%(i+1) == 0:
        print(i+1)
if n == 0:
    print(n)