import time
import random
running = 1
golden_room = [random.randint (1,3)]
gold_bars = 0
print ('==========================:WELCOME TO MAGICAL CASTLE:===========================')
START = input ('Press ANY key to play')
while running == 1:
    print ('You are in a dark room,in a mysterious castle...')
    print ('In front of you are 3 doors.You must chooose one...')
    user_reply = int(input('Choose a room...'))
    if user_reply == golden_room:
        print ('YOU ARE RICH!!!!!')
        gold_bars = gold_bars+ 1
        print ('Gold Bars:',gold_bars)
    else:
        print ('You were eaten by a troll.')
        print ('The troll said you were VERY tasty,')
        print ('Gold Bars:',gold_bars)
        running = 0
time.sleep (10)
