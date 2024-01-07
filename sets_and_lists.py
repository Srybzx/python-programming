# 1.0 code
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
lenght_list = len(it_companies)
print(lenght_list)

# 2.0 code 
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add("Twitter")
print(it_companies)

# 3.0 code
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
x = {"apple", "banana", "cherry"}
x.update(it_companies)
print(x)

# 4.0 code
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.pop()
print(it_companies)

# 6.0 code
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print(A)

# 7.0 code
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
result = A.intersection(B)
print(result)

# 8.0 code
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
result2 = A.union(B)
print(result2)

# 9.0 code
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
result3 = B.difference(A)
print(result3)

# 10.0
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.clear()
B.clear()
print(A)
print(B)
