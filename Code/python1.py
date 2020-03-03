	#!/usr/bin/env python3.8
	
def one(input1, input2):
	if len(input1) > len(input2):
		return input1
	if len(input2) > len(input1):
		return input2
	if len(input1) == len(input2):  
		return input1 + " " + input2

	

def two(input):
	x=input.lower()
	y = x.split("bert")
	for i in range (len(y)):
		if x.count("bert") == 2:
			 return y[i+1]
		else:
			return ""

def three(arg1):
	if arg1%3 == 0 and arg1%5 == 0:
		return "fizzbuzz"
	if arg1 % 3 ==0:
		return "fizz"
	if arg1%5 ==0:
		return "buzz"
	else:
		return "null"


# def four(arg1):
#  	x = arg1.split(" ")
#     add = []
#     sum = 0
#     for i in x :
#         for j in range (len(i)):
#             sum = sum + (int(i[j]))
#         add.append(sum)
#     sum = 0
#     sum = max(add)
#     return sum



def five(input):
    x = input.split(",")
    y = []
    index_name = 0
    index_bool = 2
    for i in range(int((len(x)/4))):
        if x[index_bool] == "False" and x[index_name] not in y:
            y.append(x[index_name])
        index_name +=4
        index_bool +=4
    return y


def six(input):
	
	for i in range(len(input)):

		if input[i] == "e" and input[i+1] == "i" and input[i-1] == "c":
			return True
		if i == 0:
			continue
		if input[i] == "i" and input[i+1] == "e" and input[i-1] != "c" :
			return True
		
	return False




def seven(input):
	vowels = ["a","e","i","o","u"]
	count = 0
	x = input.lower()
	for i in range (len(x)):
		for j in vowels:
			if x[i] == j:
				count +=1
	return count


def seven(input):
    return 0

	

def eight(input):
	return 1

	
def nine(inputString, char):
	return -1


# def ten(string, int, char):
  
# 	str= string.lower()
#     n = int - 1
#     result = str.find(char)
#     if int > len(str):
# 	    return False
#     if (str[n] == char): 
#         return True
#     else:
#         return False