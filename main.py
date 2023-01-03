def select_op(choice):
	if choice == '+':
		res = float(num1) + float(num2)
	elif choice == '-':
		res = float(num1) - float(num2)
	elif choice == '*':
		res = float(num1) * float(num2)
	elif choice == '/':
		res = float(num1) / float(num2)
	elif choice == '^':
		res = float(pow(float(num1), float(num2)))
	elif choice == '%':
		res = float(num1) % float(num2)

	return res


def history():
	if calHistory == []:
		print("No past calculations to show")

	else:
		for i in range(len(calHistory)):
			print(calHistory[i])



choice = ''
num1 = 0
num2 = 0
res = 0
calHistory = []
while choice != '#':
	print("Select operation.")
	print("1.Add      : + ")
	print("2.Subtract : - ")
	print("3.Multiply : * ")
	print("4.Divide   : / ")
	print("5.Power    : ^ ")
	print("6.Remainder: % ")
	print("7.Terminate: # ")
	print("8.Reset    : $ ")
	print("8.History  : ? ")

	# take input from the user
	choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
	print(choice)

	if (choice == '#'):
		#program ends here
		print("Done. Terminating")
		exit()

	try:
		if (choice == '$'):
			calHistory = []
			continue
		if (choice == '?'):
			history()
			continue

		num1 = input("Enter first number: ")
		print(num1)
		num2 = input("Enter second number: ")
		print(num2)

		finalRes = select_op(choice)
		print(f'{float(num1)} {choice} {float(num2)} = {float(finalRes)}')
		newNum1 = float(num1); newNum2 = float(num2);
		calHistory.append(str(newNum1) + " " + choice + " " + str(newNum2) + " = " + str(finalRes))

	except ValueError:
		if num1.isdigit() == False:
			print(num1)
			if num1 == '#':
				#program ends here
				print("Done. Terminating")
				exit()

		elif num2.isdigit() == False:
			print(num2)
			if num2 == '#':
				#program ends here
				print("Done. Terminating")
				exit()

		continue

	except ZeroDivisionError:
		print("float division by zero")
		print(f"{float(num1)} / {float(num2)} = None")
		newNum1 = float(num1); newNum2 = float(num2);
		calHistory.append(str(newNum1) + " / " + str(newNum2) + " = None")
