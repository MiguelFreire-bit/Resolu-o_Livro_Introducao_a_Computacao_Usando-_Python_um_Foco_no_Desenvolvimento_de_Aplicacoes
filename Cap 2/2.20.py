import math

a = (16, 75)
b = (20, 0)
c = (24, 45)
d = (24, 80)
radianos = []
altura = []
i=0

for x,y in a,b,c,d:
    radianos.append(y/180)
    altura.append(round((x * math.sin(radianos[i])),2))
    i = i+1

print(altura)



