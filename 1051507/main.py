from selenium import webdriver
import time
from config import *

#check if n is prime number
def isPrime(n):
	count = 0
	if n == 2:
		return True
	if n%2 == 0 or n <=1:
		return False
	for i in range(2,n-1):
		#print(i)
		if n % i ==0:
			count+=1
	if count == 0:
		return True
	else:
		return False

def numOrChar(string):
	numbers = []
	letters = []
	for ch in string:
		if str(ch).isdigit():
			numbers.append(ch)
		else:
			letters.append(ch)
	return numbers,letters
	
	
def calPrime(number_list):
	prime_numbers = []
	composite_numbers = []
	for num in number_list:
		if isPrime(int(num)):
			prime_numbers.append(int(num))
		else:
			composite_numbers.append(int(num))
	
	composite_numbers = [i for i in composite_numbers if i !=1 ]
	composite_numbers = [i for i in composite_numbers if i !=0 ]
	
	return sum(prime_numbers) * sum(composite_numbers)
	
def shift_ascii(char_list):
	char_list = char_list[:25]
	result = ''
	for char in char_list:
		x = ord(char)
		result += chr(x+1)
	return result


driver = webdriver.Firefox()
driver.get('https://www.hackthissite.org/')
time.sleep(2)

search_input = driver.find_element_by_name("username")
search_input.send_keys(info['user'])
time.sleep(2)

search_input = driver.find_element_by_name("password")
search_input.send_keys(info['pwd'])
time.sleep(2)

start_search_btn = driver.find_element_by_name("btn_submit")
start_search_btn.click()
time.sleep(2)

driver.get('https://www.hackthissite.org/missions/prog/12/')

allHtml = driver.page_source


startPos = str(allHtml).find("String:")
endPos = str(allHtml).find("<form")

targetStr = allHtml[startPos+38:endPos-17]

print('str ' + str(targetStr))

numList, charList = numOrChar(targetStr)

numberProduct = calPrime(numList)

shiftedString = shift_ascii(charList)

ans = shiftedString + str(numberProduct)



print(ans)

ansInput = driver.find_element_by_name("solution")
ansInput.send_keys(str(ans))


submitBtn = driver.find_element_by_name("submitbutton")
submitBtn.click()


#time.sleep(60)

#driver.close()
