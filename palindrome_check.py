#Hope you find it useful ^^
#iJ


string = input("Enter possible palindrome: ").lower().strip()

#Palindrome check
if string == string[::-1]:
	print("Palindrome")
else:
	print("not Palindrome")