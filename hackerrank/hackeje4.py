##https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
'''
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
'''

x = int(2)
y = int(2)
z = int(1)
n = int(3)

#sintaxis newlist = [expression for item in iterable if condition == True]
new_list = [[i,j,k] for i in range(x + 1) for j in range(y + 1 ) for k in range(z + 1) if((i + j + k ) != n ) ] 
print(new_list)

#below is the same excersice but with for loop

output = []
for i in range(x + 1):
    for j in range(y + 1 ):
        for k in range(z + 1):
            if((i + j + k) == n):
                continue
            else:
                output.append([i,j,k])
print("mismo ejercicio pero con for loops nested", output) 