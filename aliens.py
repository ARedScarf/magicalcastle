import random
hints = ['An american cow', 'It has plenty of buff','A flavour of crisps','American Indians hunted them']
aliens = 2
password = 'BUFFALO'
print ('Quickly! The Aliens are invading!')
print ('Activate the defense systems!')
print ('You do know the password,right?')
print ()
print ('=======================================================')
print ('             WELCOME TO THE DEFENSE SYSTEM')
print ('=======================================================')
print ()
guess = input ('Enter a password, and be quick about it!').upper ()
while guess != password:
    print()
    print('INCORRECT PASSWORD')
    aliens = aliens ** 2
    print ('Hurry! There are,' ,aliens,  'on Earth.Try again')
    if aliens > 740000000:
        break
    HintToGive = hints [random.randint(0,3)]
    print ('Password Hint:',HintToGive)
    guess = input ('Quickly,enter a password!').upper ()
if aliens > 740000000:
    print ('Nooooooooo! They outnumber humanity.All is lost.')
else:
    print ('Victory!!!!!!!!!!')
    
