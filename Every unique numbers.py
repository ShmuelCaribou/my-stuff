# List = int(input("Write a list of numbers. Write some numbers multiple times and other numbers only once."))
# Number = 1,2,3,4,5,6,7,8,9,10
# if Number in List(2):
#     print(Number)

val = []
for i in range(10):
    val[i] = int(input("Please enter a number: "))
    
def challenge2(list):
    unique_vals = []
    for i in list:
        if list.count(i) == 1:
            unique_vals.append(i)
    print(unique_vals)

challenge2(val)
