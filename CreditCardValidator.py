'''

Credit Card Validator developed by Brayan Ayala
This program uses "The Luhn algorithm or Luhn formula" created by  IBM scientist Hans Peter Luhn

'''

###########
# Imports
###########

from colorama import init, Fore, Back, Style
import time

init(convert=True)


###########
# Functions
###########


def getDigitsAndVerify(digits):

	card_numbers = []
	card_dictionary = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15}

	for item in digits:
		trans = int(item)
		card_numbers.append(trans)

	reverse = card_numbers[::-1]

	card_dictionary['zero'] = reverse[-1]
	card_dictionary['one'] = reverse[-2]
	card_dictionary['two'] = reverse[-3]
	card_dictionary['three'] = reverse[-4]
	card_dictionary['four'] = reverse[-5]
	card_dictionary['five'] = reverse[-6]
	card_dictionary['six'] = reverse[-7]
	card_dictionary['seven'] = reverse[-8]
	card_dictionary['eight'] = reverse[-9]
	card_dictionary['nine'] = reverse[-10]
	card_dictionary['ten'] = reverse[-11]
	card_dictionary['eleven'] = reverse[-12]
	card_dictionary['twelve'] = reverse[-13]
	card_dictionary['thirteen'] = reverse[-14]
	card_dictionary['fourteen'] = reverse[-15]
	card_dictionary['fifteen'] = reverse[-16]

	## Once we transform the digits typed in, to integers in a list
	## We can work with them as integers
	## Here is where magic occurs

	first_total = 0
	numcount = 0

	numcount = card_dictionary['zero'] * 2
	first_total += numcount

	if numcount > 10:
		first_total = 0
		conver = str(numcount)
		subtotal = []
		newtotal = 0
		for item in conver:
			trans = int(item)
			subtotal.append(trans)
		for num in subtotal:
			newtotal += num

		numcount = newtotal
		first_total += numcount

	if numcount == 10:
		first_total = 0
		numcount = 1
		first_total += numcount


	second_total = 0
	numcount = 0

	numcount = card_dictionary['two'] * 2
	second_total += numcount

	if numcount > 10:
		second_total = 0
		conver = str(numcount)
		subtotal = []
		newtotal = 0
		for item in conver:
			trans = int(item)
			subtotal.append(trans)
		for num in subtotal:
			newtotal += num

		numcount = newtotal
		second_total += numcount


	if numcount == 10:
		second_total = 0
		numcount = 1
		second_total += numcount


	third_total = 0
	numcount = 0

	numcount = card_dictionary['four'] * 2
	third_total += numcount

	if numcount > 10:
		third_total = 0
		conver = str(numcount)
		subtotal = []
		newtotal = 0
		for item in conver:
			trans = int(item)
			subtotal.append(trans)
		for num in subtotal:
			newtotal += num

		numcount = newtotal
		third_total += numcount

	if numcount == 10:
		third_total = 0
		numcount = 1
		third_total += numcount


	fourth_total = 0
	numcount = 0

	numcount = card_dictionary['six'] * 2
	fourth_total += numcount

	if numcount > 10:
		fourth_total = 0
		conver = str(numcount)
		subtotal = []
		newtotal = 0
		for item in conver:
			trans = int(item)
			subtotal.append(trans)
		for num in subtotal:
			newtotal += num

		numcount = newtotal
		fourth_total += numcount

	if numcount == 10:
		fourth_total = 0
		numcount = 1
		fourth_total += numcount


	fifth_total = 0
	numcount = 0

	numcount = card_dictionary['eight'] * 2
	fifth_total += numcount

	if numcount > 10:
		fifth_total = 0
		conver = str(numcount)
		subtotal = []
		newtotal = 0
		for item in conver:
			trans = int(item)
			subtotal.append(trans)
		for num in subtotal:
			newtotal += num

		numcount = newtotal
		fifth_total += numcount

	if numcount == 10:
		fifth_total = 0
		numcount = 1
		fifth_total += numcount


	sixth_total = 0
	numcount = 0

	numcount = card_dictionary['ten'] * 2
	sixth_total += numcount

	if numcount > 10:
		sixth_total = 0
		conver = str(numcount)
		subtotal = []
		newtotal = 0
		for item in conver:
			trans = int(item)
			subtotal.append(trans)
		for num in subtotal:
			newtotal += num

		numcount = newtotal
		sixth_total += numcount

	if numcount == 10:
		sixth_total = 0
		numcount = 1
		sixth_total += numcount


	seven_total = 0
	numcount = 0

	numcount = card_dictionary['twelve'] * 2
	seven_total += numcount

	if numcount > 10:
		seven_total = 0
		conver = str(numcount)
		subtotal = []
		newtotal = 0
		for item in conver:
			trans = int(item)
			subtotal.append(trans)
		for num in subtotal:
			newtotal += num

		numcount = newtotal
		seven_total += numcount

	if numcount == 10:
		seven_total = 0
		numcount = 1
		seven_total += numcount

	eight_total = 0
	numcount = 0

	numcount = card_dictionary['fourteen'] * 2
	eight_total += numcount

	if numcount > 10:
		eight_total = 0
		conver = str(numcount)
		subtotal = []
		newtotal = 0
		for item in conver:
			trans = int(item)
			subtotal.append(trans)
		for num in subtotal:
			newtotal += num

		numcount = newtotal
		eight_total += numcount

	if numcount == 10:
		eight_total = 0
		numcount = 1
		eight_total += numcount

	globaleven = first_total + second_total + third_total + fourth_total + fifth_total + sixth_total + seven_total + eight_total
	globalodd = card_dictionary['one'] + card_dictionary['three'] + card_dictionary['five'] + card_dictionary['seven'] + card_dictionary['nine'] + card_dictionary['eleven'] + card_dictionary['thirteen'] + card_dictionary['fifteen']
	
	globalsum = globaleven + globalodd

	if globalsum % 10 == 0:
		return True
	else:
		return False



###################
# Complete program runs here
###################

print("")
print(Fore.CYAN + "Welcome to Credit Card Validator!")
print(Style.RESET_ALL)
print("You can enter: " + Fore.GREEN + "Visa, MasterCard, American Express, or Discoverer!")
print(Style.RESET_ALL)


Running = True

while Running:

	print("")
	print("Please type your credit card number below! (Without any space) (16 numbers)")
	print("")

	enterCard = input("Numbers: ")
	print("")

	print(Fore.YELLOW + "Verifying Card...")
	time.sleep(2)
	print(Style.RESET_ALL)

	try:
		if getDigitsAndVerify(enterCard) and len(enterCard) == 16:
			print(Fore.GREEN + "Card Successfully Verified!")
			print(Style.RESET_ALL)

			asking = input("Do you want to verify another card? (Yes or No): ")

			if 'No' in asking or 'no' in asking:
				print("")
				print(Fore.GREEN + "Thank you for using Credit Card Validator!")
				print(Fore.GREEN + "Developed by Brayan Ayala")
				time.sleep(3)
				Running = False
				print("")
				input("Type enter to exit")
			else:
				continue

		else:
			print(Fore.RED + "ERROR: Your card couldn't be verified!")
			print(Fore.RED + "Please check again your card numbers! Type only 16 digits!")
			print(Style.RESET_ALL)
			continue
	except:
		print(Fore.RED + "ERROR: It seems like you typed in less than 16 digits!")
		print(Style.RESET_ALL)
		continue
