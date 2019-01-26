#spam= 0
#while spam<5:
  #  print('Hello World!!.')
#    spam = spam+ 1
#    if spam == 3:
#        continue
#    print('spam is '+str(spam))

#name =''
#while True:
#    print('Please type your name.')
#    name = input()
#    if name=='your name':
#        break
#print('Thank You')

#print('My name is')
#for i in range(2, 51, 5):
#    if i%6 == 4:
#        continue
#    print('My name is five times '+ str(i))

#Sum = 0
#for i in range(101):
#   Sum = Sum + i
#print('The Sum of first 100 whole numbers is ' + str(Sum))

#import sys
#print('Hello')
#sys.exit()
#print('Good Bye')


#def hello(name):
#    print('Hello ' + name)
#    print('Hello there.')
#hello('Ram')
#hello('Shyam')

#def plusOne(number):
#    return number +1
#newNumber = plusOne(5)
#print(newNumber)

#print('Hello ', end='')
#print('World')

#try and except statements
#def div42by(divideBy):
#    try:
#        return 42/ divideBy
#    except: #ZeroDivisionError
#        print('Error: You tried to divide by zero.')
#print(div42by(2))
#print(div42by(6))
#print(div42by(0))
#print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('You have lots of cats')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number')

