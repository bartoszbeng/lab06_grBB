#!/bin/env usr/bin/python3

import sys

def calculate(num1, operation, num2):
	if operation == "+" :
		return num1 + num2
	elif operation == "-" :
		return num1 - num2
	else:
		return "nieznana operacja"

def main();

	print(sys.argv)

	if len(sys.argv) != 4:
	print("Użycie: calc.py <liczba_1> <operacja> <liczba_2>")
	sys.exit(1)

	num1, operation, num2 = sys.argv[1], sys.argv[2], sys.argv[3]

	try:
		num1 = float(num1)
		num2 = float(num2)
	except ValueError:
		print("Podane liczby są nieprawidłowe")
	sys.exit(1)

	result = open("/tmp/wynik.txt, "w")
	file.write(str(result))
	file.close()

if __name__ == "__main__":
	main()
