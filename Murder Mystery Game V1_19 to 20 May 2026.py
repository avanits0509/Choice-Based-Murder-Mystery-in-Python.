# Murder Mystery Game V1_19 to 20 May 2026‎

import pygame
import time
import random

pygame.init()

typing_sound = pygame.mixer.Sound("typing.wav")

def type_print(text,speed=0.05):
    for char in text:
        print(char,end ="")
        
        if char != " ":
            typing_sound.play()
        
        time.sleep(speed)
    
    print()


trust_jennifer = 0

def mark():
    trust_mark= 0
    type_print("A guy in his mid-20s is sitting on the other side of the metal chair.\nPosh. Well-dressed and at ease.\nThe picture of innocence.")
    trust_mark = trust_mark+5
    type_print('"Good Evening Detective. Shame you had to miss your day off because of this little-" he says, smiling. "misunderstanding"')

    type_print("You will have no problem answering a few quick questions then. \nWhere were you when the murder took place? \n7pm? today")

    choices = ["Of course not","I have no time for this bullshit"]

    mark_answer = random.choice(choices)

    type_print(mark_answer)

    if mark_answer == "Of course not":
        trust_mark = trust_mark + 10
    
    else:
        trust_mark = trust_mark - 10
    
    if trust_mark > 10:
        type_print('"You seem like a good kid," you say')
    
    else:
        type_print('"You are treading dangerously, son," you say')

type_print("On a dark, rainy night, you enter the interrogation chambers in your formal clothes.")
type_print("Still wrinkled because you didn't know you would have to come in tonight.")  
type_print("... but someone was murdered.")
type_print("Danger lies ahead........")
ask = input("Do you wish to continue?  1]Yes  2]No")

if ask.strip().lower() == "yes":
    type_print("Not the wisest decision... but I respect it")

    type_print("Here are the files, Detective. Choose wisely.")

    mark()

else:
    type_print("GAME OVER...BEFORE IT EVEN BEGAN.")



