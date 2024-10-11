# """
# #This is a comment
# hwvws
# swbshwbvs
# """

# print("Hello World")

# if 5 > 2:
#     print("Five is greater than two!")
#     print("Five is greater than two!")


# x=5
# y="Cherav"
# print(x)
# print(y)


# x = 4       # x is of type int
# print(x)
# x = "Sally" # x is now of type str
# print(x)
# print(type(x))


# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)



# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)



# x = "Python is awesome"
# print(x)


# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)


# x = "awesome"
# print("Python is " + x)
# def myfunc():
# #   global x
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()
# print("Python is " + x)
# myfunc()



# import random
# print(random.randrange(1, 10))


# print(2+3)

# print(2<3)


# Python program showing a use of
# global in nested function

def add():
	x = 15
	def change():
		global x
		x = 20
		print("Before making changing: ", x)
	
	print("Making change")
	change()
	print("After making change: ", x)

add()
# print("value of x", x)
