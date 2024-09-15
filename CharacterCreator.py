def print_head(hair,eye):
    print(12*hair)
    print(hair+'|'+8*' '+ '|'+hair)
    print(hair+'|'+2*' '+eye+2*' '+eye+2*' '+ '|'+hair)
    print(' '+'|'+3*' '+'/'+"\\"+3*' '+ '|')
    print(' '+'|'+8*' '+ '|')
    print(' '+'\\'+2*' '+"'__'"+2*' ' +'/')
    print(3*' '+6*'_')

def print_body(height,arm):
    print(5*' '+'XX')
    print('#'+4*arm+'XX'+4*arm+'#')
    for i in range(height):
        print(4*' '+4*'X')

def reverse_shoe(shoe_string):
    reverse=shoe_string[::-1]
    return reverse

def print_legs(height,shoe):
    shoe_string=shoe
    shoe_string_reverse=reverse_shoe(shoe_string)
    print(4*' '+'====')
    for i in range(height):
        print('   '+'||'+2*' '+'||')
    print(' '+shoe_string+'  '+shoe_string_reverse)

def main():
    hair='M'
    eye='0'
    height=3
    arm='-'
    shoe='WXYZ'
    print_head(hair,eye)
    print_body(height,arm)
    print_legs(height,shoe)

main()