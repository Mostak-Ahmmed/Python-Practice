# basic printing
print("Hello World!")
print('Hello World!')

first_name = 'DM'
last_name = 'Lab'

full_name = first_name + " " + last_name
print(full_name)

# type casting
x = str(5)
print(type(x))

# input - all inputs in python are stored as string
n = int(input("Enter a value: "))
n = int(input("Enter a value: "))
print(type(n))
print("n =",n)

# operators
x = 3
y = 2
print(x*y)
print(2**3) # exponentiation
print(x%y) # modulus
print(x/y) # float division/ divsion
print(x//y) # int division/ floor division

# comparison operator => boolean
x = 10
y = 5

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

# logical operator
x = 10
y = 5
print(x==10 and y==5)
print(x==10 or y==5)
print(not x)


# Lab TASK # 01

# Write a Python program that accepts,
# two integers (n, m) and computes the value of n^2 + 2nm + m^2, 
# and computes (n+m)^2, 
# now use comparison operator to evaluate whether they are equal
# and print the value of the comaprison.

# List
thislist = ["A", "B", "C"]
print(thislist)
# Set (Unique), List (Multiple)
thislist = ["A","B","A"]
print(thislist)

# length
print(len(thislist))

# Access Item in List
thislist = ["A", "B", "C"]
print(thislist[0])
print(thislist[-1])
print(thislist[2])

thisString = "ABCDEF"
print(thisString[2])
print(thisString[2:5]) # first:last-1
print(thisString[2:]) # first:len(list)-1
print(thisString[:5]) # 0:last-1

# Change Item in a List
thisList = ["A", "B", "C"]
thisList[1] = "D"
print(thisList)
thisList[0:2] = ["D", "E"]
print(thisList)

# Add Item (Append)
thisList = ["A", "B", "C"]
thisList.append("D")
thisList.append(2)
print(thisList)

# Add Item at a Specific Index ()
thisList = ["A", "B", "C"]
thisList.append("D")
thisList.insert(0,"D")
thisList.insert(-1,"D")
print(thisList)

# Adv.
thisList = ["A", "B", "C"]*2
print(thisList)
thisList1 = ["A", "B", "C"]
thisList2 = ["D", "E", "F"]
thisList = thisList1 + thisList2
print(thisList)
thisList1.extend(thisList2)
print(thisList1)

# Remove
thisList = ["A", "B", "C"]
thisList.pop()
thisList.pop(1)
print(thisList)
thisList.remove("C")
print(thisList)

thisList = ["A","B","C"]
del thisList[1]
print(thisList)

# Remove
thisList = ["A", "B", "C"]
thisList.remove("C")
print(thisList)

# type
thisList = ["A", "B", "C"]
print(type(thisList))


# Advance
nums = input()
print(nums)
print(type(nums))
nums = nums.split(",")
print(nums)
ans = []
for i in nums:
    ans.append(int(i))
print(ans)
print(type(ans[2]))

nums = [int(i) for i in input().split(",")]
print(nums)
print(type(nums))


# Lab TASK # 02

# Write a Python program which accepts a sequence of 
# comma-separated numbers from user and generate
# a list with those numbers.

# if-else
a = 1
b = 2

if a>b:
    print("A is Greater")
else:
    print("B is Greater")



# if-elif-else
labNo = 1
if labNo==1:
    print("No Report :)")
elif labNo==3:
    print("No Report :)") 
else:
    print("Report :(")

# bit short

# real life
labNo = 1
if labNo ==1 or labNo==3:
    print("No Report :)")
else:
    print("Report :(")

# sorted
nums = [1,2,5,6,4]
nums = sorted(nums)
print(nums)
maxNum = max(nums)
print(maxNum)

## Report TASK: 3.5.7

# List
# Index (positive):    0   1   2   3   4   5   6   7  
# Index (negative):   -8  -7  -6  -5  -4  -3  -2  -1
