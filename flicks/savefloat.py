x = []
file_in = open('tess.txt', 'r')


y = file_in.read().split(',')
w = ''.join(y)
r = w.replace('\n\x0c', '')
q = float(r)
z = x.append(q)
print(x)
