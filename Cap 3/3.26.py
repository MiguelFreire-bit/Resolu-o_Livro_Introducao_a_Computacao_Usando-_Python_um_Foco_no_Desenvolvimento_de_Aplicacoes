while True:
    n = input("digite n: ")
    if n.isdigit():
        n = int(n)
        break

for i in range(n):
    print(i**2)

