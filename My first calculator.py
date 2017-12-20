Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> while True:
	print("Options:")
	print("Enter 'add' to add two numbers")
	print("Enter 'subtract' to subtract two numbers")
	print("Enter 'multiply' to multiply two numbers")
	print("Enter 'divide' to divide two numbers")
	print("Enter 'quit' to quit the program")
	user_input = input(": ")
	if user_input == "quit":
		break
	elif user_input == "add":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number: "))
		result = str(num1+num2)
		print("The answer is " + result)
	elif user_input == "subtract":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number: "))
		result = str(num1-num2)
		print("The answer is " + result)
	elif user_input == "multiply":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number: "))
		resut = str(num1*num2)
		print("The answe is " + result)
	elif user_input == "divide":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter another number: "))
		result = str(num1/num2)
		print("The answer is "+ result)
	else:
		print("Unknown input")



	
