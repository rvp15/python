
# snake_casing => all lower char
# first_name ='vedha'

# naming multiple variables:
# a,b = 10,20
# print(a,b)
# your_name = input('please enter your name')
# print(your_name)

# Data type:
# string, int ,float

# a =input('enter a')
# b=input('enter b')
# print(int(a)+int(b))

# divide and round it use(//) ex: 13 // 2 = 6
# exponents  2**3 (its 2 power 3)
# modulo 4%2 => gives remainder

# string formatting= f used to use python expression inside string
# total =120
# print(f'${total}')

# if,else:
# weather = 'rain'
# if weather == 'rain':
#   print('umberlla')
# else:
#   print('glasses')

# and or operator
# score =int(80)
# if(score >=75 and score <= 100):
#   print('Pass')
             # or
# if 60 <= score <=100 // pythonic wau of writting

# function:
# calling fun with arguments -> default argumentin argument)

# def fun_name(name, greet='hello'):
#   print(f'{greet} {name}')

# fun_name(name ='vedha') // named argument (assigning name)
# fun_name('vedha','hello' )// positional argument


# example 1:
# def sum(a: int,b: int)->int: //TYPE HINTING like typescript
#   return a+b

# print(sum(4,5))

# Exampl2 2://you can use str,nonefor easier reability // Type Hinting

# def weather(its: str)->None: //str->expects string & None-> doesnt return anything
#   if its == 'cold':
#     print('wear jacket')
#   elif its == 'hot':
#     print('wear sunscreen')
#   else:
#     print('wear casual')

# weather('hot')

# import exercises.bigger_guy

############### lambda ################ anonymous function: (implicit return)
# fun should be assigned to a variable (like fun expression and arrow fun)

# sum = lambda a,b: a+b //arguments: expression(implicit return)
# print(sum(3,6))

# greet = lambda greet,name: f'{greet}{name}'
# print(greet('hello ','vedha'))

###################### assert for testing ############################
# used to write test cases:
#  when code run if the result is not as expected it throws the below error:

 # assert sum(1,2) == 3, 'the sum has to return 3 but it provides diff value for check for error'

###################### LIST (ARRAYS) ###################################33
#methods list.append() vs functions print()
# indexing: 0,1,2....(from left to right)
# from right to left : -1,-2,-3......

fruits = ['apple','pear','banana','peach']

#1. adding at end :append()
fruits.append('orange')

# 2.slicing: first index inclusive, 2nd index exclusive
# print(fruits[0:4])

# Length:
# print(len(fruits))

# String slicing:
# print('vedhapriya'[0:3])
# string reverse:
# print('vedha'[::-1])

# REVERSE:
# [firstindex:lastbeforeindex:step(skipping)]

#  important to reverse dont specify start and end ,just empty and -1
# print(fruits[::-1])


