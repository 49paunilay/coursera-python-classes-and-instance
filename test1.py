python = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
for element in python:
    element[0],element[1]=element[1],element[0]

print(python)
numlist=[]
for i in python:
    numlist.append(i[0])

print(numlist)
smallest=sorted(numlist)[4]
print(smallest)
