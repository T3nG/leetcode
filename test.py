from itertools import permutations
ls = [10, 0, -9, -9, -1, 1, -3, -6, -9, -4]
x = permutations(ls, 3)
temp = [tuple(sorted(sub)) for sub in x]
# removing duplicates
print(temp)
res = set(temp)
r = []
for i in res:
    if sum(i) == 0:
        r.append(list(i))

print(r)
