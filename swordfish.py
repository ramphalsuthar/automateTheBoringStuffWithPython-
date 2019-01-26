#while True:
#    print ('Who are you?')
 #   name = input()
  #  if name!= 'Joe':
   #     continue
    #print ('Hello Joe, What is the password? (Is it a FISH)')
    #password = input()
    #if password == 'swordfish':
    #    break
#print ('Access Granted')

name = ''
while not name:
    print ('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough rooms for all your guests.')
print ('Done')
