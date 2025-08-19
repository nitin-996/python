import re

email_list = [
    "alice.smith@example.com",
    "john.doe@example.org",
    "michael.jordan@testmail.com",
    "emma.watson@sample.net",
    "rohit.verma@company.co",
    "linda.jones@demo.io",
    "aarav.shah@mailhub.org",
    "sophia.liu@mockmail.com",
    "david.kim@fakemail.net",
    "fatima.khan@webmail.co"
]

# c = any("alice" in email for email in email_list)
#  we have all() built in function.
# print(c)

for email in email_list:
    print(email)
    if "rohit" in email:
         print(email)
         break


# using regex
for email in email_list:
     if re.search(r'[Ss]ophia', email):
          print(f'match found {email}')


# name group

for email in email_list:
     matched = re.search(r'(?P<username>[\w\.]+)\@(?P<SLD>\w+)', email)
     if matched:
          print(matched.group('username'))
          print(matched.group('SLD'))