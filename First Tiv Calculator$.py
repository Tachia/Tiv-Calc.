from math import *

def add(a,b,c):
	   result = (a*b)+(c*a)
	   print("(a*b)+(c*a) =", result)

def sub(a,b):
	   result = (a+b)-b
	   print("(a+b)-b =", result)

def mul(a,b):
	   result = (a+b)*a
	   print("(a*b)*a =", result)

def div(a,b):
	   result = (a+c)/(c-a)
	   print("(a+c)/(c-a) =", result)

	  
a = int(input("Nyôr iyenge i hii hii:"))
b = int(input("Nyôr iyenge i sha u har:"))
c = int(input("Nyôr iyenge i sha utar:"))
op = input("Nger operator:")
if op == "+":
	add(a,b,c)
elif op == "-":
	sub(a,b)
elif op == "*":
	mul(a,b)
elif op == "/":
	div(a,c)
else:
	print("Orvesen kwagh la ngu shami ga, nenge dedoo yô")