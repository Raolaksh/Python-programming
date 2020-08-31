
def max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))

print("we can also compare strings or bulleans not only numbers")
print("these are comparision operators")
print("! sign means not equal and if we have to tell python that this "
      "is equal to this we have to put double = like this == ")