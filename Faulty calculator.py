# Faulty Calculator
print("phela number lekhne ke baad enter dabana mat bholna pher kahi kahoo ki ye clculator to kharab ha \nha manta ho kharab ha par itna bhi nahi")
num1=(float(input("Enter First Number:")))
op=(input("Enter Operator:"))
num2=(float(input("Enter second Number:")))

if num1 == 45 and op == "*" and num2 == 3 or num1 == 3 and op == "*" and num2 == 45:
    print("555")
elif op == "*":
    print(num1 * num2)
elif num1 == 56 and op == "+" and num2 == 9 or num1 == 9 and op == "+" and num2 == 56:
    print("77")
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif num1 == 44 and op == "/" and num2 == 4 or num1 == 4 and op == "/" and num2 == 44:
    print("22")
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
