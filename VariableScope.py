name = 'PLACEHOLDER'

def capitalize_name():
    name = input('What is your name? ')
    first_letter = name[0]
    after_first = name[1:]
    name = first_letter.upper() + after_first.lower()

capitalize_name()
print('Hi there', name)