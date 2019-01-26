#def isPhoneNumber(text):
#    if len(text) != 12:
#        return False
#    for i in range(0,3):
#        if not text[i].isdecimal():
#            return False
#    if text[3] != '-':
#        return False
#    for i in range(4,7):
#        if not text[i].isdecimal():
#            return False
#    if text[7] != '-':
#        return False
#    for i in range(8,12):
#        if not text[i].isdecimal():
#            return False
#    return True

import re 

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me at 454-234-5555 tomorrow, or at 232-344-5543 my office line.'))


#foundNumber = False
#for i in range(len(message)):
#    chunk = message[i:i+12]
#    if isPhoneNumber(chunk):
#        print('Phone number found: '+chunk)
#        foundNumber = True
#if not foundNumber:
#    print('Could not find any phone number')
#print(isPhoneNumber('343-555-6774'))
