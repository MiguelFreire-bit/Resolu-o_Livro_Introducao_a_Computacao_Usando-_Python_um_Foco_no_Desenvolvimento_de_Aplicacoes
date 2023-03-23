s = 'goodbye'

x = []
x.append(s[0] == 'g')
x.append(s[6] == 'g')
x.append((s[0] == 'g' and s[1] == 'a'))
x.append(s[-2] == 'x')

t = int((len(s)-1)/2)
x.append(s[t] == 'd')
x.append(s[0] == s[-1])
z = s[-1]+s[-2]+s[-3]+s[-4]
x.append(z == 'tion')
print(x)
