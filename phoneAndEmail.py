import re, pyperclip

# Creat a regex for phone number
phoneRegex = re.compile(r'''(
# 413-233-0000, 555-4444, (432) 444-0000, 555-0000 et 12345, x12345

(\d{3}|\(\d{3}\))?       # area code (optional)
(\s|-)                        # first seperator
(\d{3})                    # first 3 digits
-                             # seperator
(\d{4})                     # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?              # extension (optional)

)''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d(2,5)))?.com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone for this text
extractPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractEmail)
pyperclip.copy(results)
