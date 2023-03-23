s = 'abcdefghijklmnopqrstuvwxyz'
s1 = "'{a}','{c}','{z}','{y}' e '{q}'".format(a=s[0], c=s[2], z=s[-1], y=s[-2], q=s[16])
print(s1)