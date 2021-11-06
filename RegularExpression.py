import re
def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumRegex.search(text)
    return mo
      

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: "+chunk)
print('Done')

   