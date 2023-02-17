import itertools

a = [[1,2,3],[3,4,5],[6,7,8]]
b = [[-4,5,-6],[7,-8,5],[9,8,-1]]
c = [1,2,3,4,5,6]
i = 0
for n1, n2 in itertools.combinations(c, 2):
    x = -(n1 + n2)
    print(x)



