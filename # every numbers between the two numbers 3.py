# every numbers between the two numbers
def list_numbers_between(start, end):
    if start > end:
        start, end = end, start

    return list(range(start + 1, end))

start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

numbers_between = list_numbers_between(start_num, end_num)
print("Numbers between", start_num, "and", end_num, "are:", numbers_between)