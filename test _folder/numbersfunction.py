num=90
def check_number(num):
    if num > 0:
        return "Positive"
    else:
        return "Non-positive"

result1 = check_number(5)
print(f"5 is {result1}")

result2 = check_number(-2)
print(f"-2 is {result2}")

result3 = check_number(0)
print(f"0 is {result3}")
