
r = []

def mod(x, m , n):
  return x % m == n

for j in range(100000):
  for i in range(10):
    if mod(j, 10 - i, 9 - i):
      if i == 0:
        if j not in r:
          r.append(j)
    else:
      if j in r:
        # Remove the element from the list with value of j
        r.pop(r.index(j))
print(r)