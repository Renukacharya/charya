#! /usr/bin/python3
import random 
count=0
r=0
while count<=100:
	roll=input("press r to roll the dice")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random num is",r)
		print("you are on count",count)
	elif count=="8":
		  count=37
		print("you climb the ladder",count)
	if count=="13":
		count=34
		print("you climb the ladder",count)
	elif count=="25":
		  count=4
		print("snake ate you down",count)
	if count=="11":
		count=2
		print("snake ate you down",count)
	elif count=="25":
		count=4
		print("snake ate you down",count)
	if count=="38":
		count=9
		print("snakea ate you down",count)
	elif count=="40":
		count=68
		print("you climb the ladder",count)
	if count=="65":
		count=46
		print("snake ate you down",count)
	elif count==""	 
				
				
