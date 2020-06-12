"""
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""

# Find the smallest value in each sub-array

# add the smallest to a new array

# add the elements of the smaller array together


start = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
smallest = []

total = 0

for each in start:
    littlest = None
    for num in each:
        if littlest is None:
            littlest = num
        elif littlest > num:
            littlest = num
        else:
            pass
    smallest.append(littlest)

for numeral in smallest:
    total += numeral

print(total)
            
arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
total = 0
for i in arr:
   total += min(i)
print(total)