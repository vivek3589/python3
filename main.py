
 #1 
'''name=input("whats your name? ")
print('Hi ' + name)'''

'''name=input('whats your name? ')
colour=input('whats your colur? ')
print(name + ' likes '  + colour + ' colour ' )'''

'''birth_year=input('Birth year= ')
age=2022 - int(birth_year)
print(age)'''

'''main_price=1000000
has_good_credit=True
if has_good_credit:
    down_payment=0.1 * main_price
else:
    down_payment=0.2 * main_price
print(f"down payment: $ {down_payment}")'''

'''temperature=33
if temperature>30:
    print('its a hot day')
else:
    print('its not a hot day')'''
    
'''name='vi'

if len(name)< 3:
    print('name must be at least 3 charcater')
elif len(name)>50:
    print('name can be a max of 50 characters')
else:
    print('name looks good')'''
    
# wap to convet killograms to pound and vice varsa.
'''weight=int(input('weight='))
unit=input('(l)bs or (k)g: ')
if unit.lower()=='l':
    convert=weight*0.45
    print(f'you are {convert} kilos')
else:
    convert=weight / 0.45
    print(f'you are {convert} pounds')
     '''
# wap to create a guessing number game if you guess right numner than it should print you win other wise you failed.
secret_number=10
guess_count=0
guess_limit=3

while guess_count<guess_limit:
    guess=int(input('Guess= '))
    guess_count += 1
    if guess == secret_number:
        print('You Won !')
        break
else:
    print('Sorry, You Filed!')
print('Sorry, You Filed!')
print('you, You Filed!')
print('you, You passed!')
print('you are good')
