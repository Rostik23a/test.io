
n=input('n=')

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (n,) for t in l])