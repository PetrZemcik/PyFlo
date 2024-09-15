# Comprehensive solution

phone = input('Enter your phone number: ')

# Check to ensure that what the user gave us is 11 characters
if len(phone) != 12:
    print('Invalid phone number!')
    exit()

# Ensure that the dashes are in the correct locations
if phone[3] != '-' or phone[7] != '-':
    print('Invalid phone number!')
    exit()

# Ensure every other character is a digit
for i in range(0, 12):
    if i != 3 and i != 7 and phone[i].isdigit() == False:
        print('Invalid phone number!')
        exit()

print('Valid phone number!')