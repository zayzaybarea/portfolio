from threading import Timer

def banner():
    print('''
Slayer by: day & oyasumi
'''
)

def opening() :
	print('''
you wake up in a coffin. Before you have time to process what’s going on you remember why you’re here: you were crushed by a piano. 
The memory is painful but you wonder why you’re still having thoughts, shouldn’t that have been the end?
*clunk* “Ouch” your head hits the top of the coffin. “Are we even on a paved road” you think. The coffin comes to a stop and you hear voices getting closer. They’re speaking a language you don’t recognize. Light peaks through as the coffin is opened.
The figures jump back as you sit up revealing you are in fact not a corpse. 
You get a better look at them and see they are short stocky men with red hair and beards dressed mostly in animal hides with large silver jewelry pieces on their arms and in their hair. The men look frightened and run from the coffin 
''')


def opt7():
    print('''You awake to the sunlight hitting your face though the boards of the shack. You walk outside and see that even the animals are still asleep. You wash your face with a tub of water sitting outside and relieve yourself to start the day.''')

    choice6 = input('start, lay down')

    if choice6.strip() == 'start'.strip():
        
        print('You pick up a shovel and start setting the first post')
        flag2 = input('Enter root flag from HTB Oopsie: ')
        
        if flag2.strip() == 'placeholderflag' :
            print('''The man seems to be satisfied with the first fence post and leaves you too it''')
            opt7()

        else :
            print('Try again!')
            opt6()

    elif choice6.strip() == 'lay down'.strip():    

        print('Before long the man from yesterday comes over and looks disappointed that you are laying in the hay. You quickly stand up and he gestures to the fence')



    else :
        print('Invalid Input')
        opt6()



def opt6() :
    print('''You're then taken to a large house out back there is a half finished fence and livestock in small stables. A man comes out to greet you and the shaman. They talk shortly and the man returns inside. Two men come out of the doorway. That's when you see the first person who is taller than you, a towering man with one eye and scars covering his arms. The shaman nods his head and starts to leave. I guess this is your new employer. He takes the sword from your waist and swings it almost too easily. He sends you on your way with the first man and he leads you to where the fence ends and gestures towards it. It looks simple enough just posts in the ground connected by a few pieces of lumber nailed in.''')

    choice6 = input('start')

    if choice6.strip() == 'start'.strip():
        
        print('You pick up a shovel and start setting the first post')
        flag2 = input('Enter root flag from HTB Oopsie: ')
        
        
        if flag2.strip() == 'placeholderflag' :
            print('''The man seems to be satisfied with the first fence post and leaves you too it''')
            opt7()

        else :
            print('Try again!')
            opt6()
        

        print('You get started with what looks like will be your life for a while')
        flag3 = input('Enter root flag from HTB : ')
        
        
        if flag3.strip() == 'placeholderflag' :
            print('''The man seems to be satisfied with the first fence post and leaves you too it''')
            opt7()

        else :
            print('Try again!')
            opt6()

        print('Two down... many more to go')
        flag4 = input('Enter root flag from HTB : ')
        
        
        if flag4.strip() == 'placeholderflag' :
            print('''That took longer than expected you think. The sun is setting and the man from before comes out and checks your work. Pleased with what he sees he gestures for you to follow him. You reach a shack near the ones holding the animals. He points to a stack of hay with tattered blankets thrown to the side of it. You guess this is your lodging for now, too tired to think about it you curl up and fall asleep ''')
            opt7()

        else :
            print('Try again!')
            opt6()

    else :
        print('Invalid Input')
        opt6()

    




def opt5() :
    

    print('''He talks with a man for a few minutes and eventually takes you into the long building as you enter the building you see a man on a wooden throne surrounded by servants, he rises upon seeing the shaman and presumably makes a joke which he proceeds to laugh at. The shaman seems less amused, he responds and they enter a more serious conversation. You still can't understand a word but eventually they come to an agreement and the king orders two of the servants to do something you wait for a few minutes and they return with a bloodied man who is screaming and trying to swing his restrained arms. The shaman draws your sword, cuts your bindings, and hands you the sword. The other man is given a sword by one of the servants. It quickly becomes apparent. This is a deathmatch. Before you even have a chance to process what's going on the man charges''')
    
    choice5 = input('fight, skip')

    if choice5.strip() == 'fight'.strip():
        flag1 = input('Enter root flag from HTB: ')
        time = 1800
        t = Timer(time,print,['Time expired'])
        t.start()
        
        print('You draw your sword and get ready for a fight')
        if flag1.strip() == 'placeholderflag' :
            print('''The whole room is goes silent and all you can hear is your heartbeat and the last choke of the man who's now been run through by your blade. The shaman looks surprised and the man on the throne looks pleased''')

        else :
            print('You stumble back onto the ground. The man comes to deliver the final blow but is stopped by the shamans staff. The man is restrained again and taken out of the hall.')
            opt6()
        t.cancel()
    

    elif choice5.strip() == 'skip':
        print('You stumble back onto the ground. The man comes to deliver the final blow but is stopped by the shamans staff. The man is restrained again and taken out of the hall.')
        opt6
    else :
        print('Invalid Input')
        opt5()


def opt4() :
    choice4 = input('look,run')

    if choice4.strip() == 'look':
        print('')
        opt4()
    elif choice4.strip() == 'run':
        print('You trip and fall again. But this time a sword goes through the roof of your mouth before you can stand up dead')
        print('You died.')
    elif choice4.strip() == 'continue':
        opt5()
    else :
        print('Invalid Input')



def opt3():
    print('''The men bring you to a hut. It doesn't seem like they live here the two from before seem almost scared to get close to it. The older man shoos them away and brings you into a hut. The hut is small and has an.... interesting odor. He pours a liquid from a vase into a large bowl. He drinks it then hands you the bowl. 
''')
    choice3 = input('drink,throw bowl: ')

    if choice3.strip() == 'drink':
        print('''You drink the mysterious liquid and almost immediately feel your senses being heightened and your perception of time start to change. You look over at the man who is in an almost meditative state. He breaks his trance and speaks in your native tongue “who are you” you have more questions than you can ask but you try to answer the man's question “ I'm ()” “where are you from” he asks you tell him the name of your hometown he looks confused, you say America he still looks confused. You ask him where you are “Scandinavia” he says. It all starts to click. You've been isekaid to the Middle Ages and this is a Viking shaman. The revelation that you won't be able to return home hits you and you ponder if you would even want to. You decide to tell the shaman about your situation he listens intently. And when you are finished he only laughs and says “It seems you slipped through the cracks in the afterlife, use this second chance wisely” “Your new name is Ivar” “I will vouch for you to live in the village” “But know you will live as a slave until you can prove your worth” the drink starts to wear off and you can't understand the shaman anymore. Upon noticing this the shaman leads you out of the hut and to the village entrance. ''')
        opt4()
    
    elif choice3.strip() == 'throw bowl'.strip():
        print('The old man laughs, he reveals a hidden dagger and throws it at your neck')
        print('You died.')
        opt3()



def opt2():
    print('''The men come back with a more heavily adorned man wearing pelts with the heads still attached they start having a conversation and finally one of the men tries to ask you something.
''')
    choice2 = input('run,respond,draw sword: ')
    if choice2.strip() == 'respond' :
        print("The men don't seem to understand you they start moving forward")
        opt2()
    elif choice2.strip() == 'run':
        print('You try to run but you trip and one of the men grabs you, ties your hands together, and starts pulliing you down the trail')
        opt3()

    elif choice2.strip() == 'draw sword'.strip():
        flag1 = input('Enter root flag from HTB: ')
        time = 1800
        t = Timer(time,print,['Time expired'])
        t.start()
        
        print('You draw your sword and get ready for a fight')
        if flag1.strip() == 'placeholderflag' :
            print('the end')

        else :
            print('The man quickly wards off your attack and knocks the wind out of you with a punch, he ties your hands together and starts pulliing you down the trail')
            opt3()
        t.cancel()
    else :
        print('Invalid Input')
        opt2()
        




def opt1() :

    choice = input('look,leave: ')

    if choice.strip() == 'leave' :
        print('''You hop onto the ground. You notice a breeze…… you don't have any clothes on. There's a large shirt and pair of baggy pants near the coffin. There's no draw string on the pants and the only thing you could find that looks like a belt is a sword belt. The attached sword is short and slim. But it feels good in your hand and has a great personality.There are also shoes that look like leather Minecraft boots. You take a moment to adjust to your new clothes.
''')
        opt2()

    elif choice.strip() == 'look'       :
    
        print('You seem to be on a beaten trail through a forest. The coffin you are in is on a wooden cart surrounded by gold vases plates and other simple metal items. You look at the coffin you were in and it looks more like a wooden chest than a coffin. Actually everything including the cart looks almost primitive and so does the horse “what is that a wooly horse” you think.')
        opt1()
    else:
        print('Invalid Input')
        opt1()



def easy():
    intro()

def normal():
    intro()
    opt1()

def hard():
    intro()

def intro():
	print(
f'You see yourself again for the first time. You look the same as you always have. A {dif.build} build with {dif.skin} skin and {dif.hair} hair'
)


def dif():

    dif.skin = input('What color is your skin: ')
    dif.hair = input('What color is your hair: ')
    dif.build = input('Difficulty: fat=hard skinny=normal muscular=easy: ')


    if dif.build.strip() == 'fat'  : 

        hard()
    
    elif dif.build.strip() == 'skinny' : 
        normal()

    elif dif.build.strip() == 'muscular' :  
        easy()
        

    else:
        print('Invalid input')
        dif()
















banner()
opening()
dif()
