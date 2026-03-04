# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define my = Character("Meyer", color = "#af0aa1")
define mi = Character("Mina", color = "#b30045")
define ty = Character("Tyce", color = "#7c7c7c")
#this isn't relevant to this game but fun fact this guy is lowk death, horseman of the apocalypse. he chillin though the apoc is not here (yet)
define al = Character("Altair", color = "#b60000")
#these characters have official colors change these later VV
define ya = Character("Yamini", color = "#b700ff")
define ur = Character("Urmi", color = "#008CFF")
define kt = Character("Kathryn", color = "#f30071")
define sp = Character("Spata", color = "#ff5100")
                      
image black = "#000"


# The game starts here.

label start:

    $ happiness = 0

    scene cg nightmare1 one
    with fade
    """
    Nightmares.

    It's always nightmares.

    It's always him, in the middle of the void.

    A teenage boy. Or, maybe a tween.
    """

    show cg nightmare1 two
    with dissolve
    """
    It doesn't matter, really.

    What matters is what he's done.

    It's always him.
    """
    show cg nightmare1 three
    #laugh sound
    "It's always—{nw=1}"

    show cg meyerBed
    #ambient music?
    "— Me."
    my "Haah. Not again..."
    "Cold sweat clings to my skin like fleas."

    scene bg bedroom
    with hpunch
    "Time to get up, lonesome body."
    show meyer default neu
    with dissolve
    """
    I often have nightmares in my sleep. Definintely more than the average adult, but maybe not in the city where I live.
    
    Lots of bad things happened here, and still do.
    
    I try to make the world a better place, along with my friends. People have to look out for each other, you know?
    """
    show meyer cheek happy
    "We've all dedicated our lives to humanity, in a way. Some of my friends are going to college to become teachers. Others are starting a non-profit just for peace. It's amazing how far we've come as people!"
    show meyer hand sad
    "Of course, I shouldn't be included in that gallantry."
    
    scene cg calendar1
    with fade
    """
    February 14th is my birthday, better known as the Day of Love.
    
    I've always found it ironic, considering everything that has happened. {color=#7c7c7c}(Considering everything I've done.){/color}{nw=1}
    
    ... {w=1}This year should have been given to the dead. But nevertheless, I survive.

    But at least I get to see all of my friends happy.

    I like seeing people live brighter lives. It makes me forget about my own, just a bit.
    """
    show cg calendar2
    with zoomin
    "Ah, that's right! I was going to visit my father today!"
    "I shouldn't just stand around, then. He'll scold me if I'm late to visit because I got stuck in my own head again..."

    show bg bathroomCurtain
    with fade

    "... But there are nightmares everywhere."
    "Especially in my shaded, rusty mirror."
    show bg bathroomCurtainOpen
    show mina mirror shade
    #sound effect, music 
    mi "It's been a while, Meyer."
    "One and the same."
    mi "Well, technically, your dreams are a figment of your imagination. {color=#b30045}I'm{/color} as real as you."
    "They can hear your thoughts, know your deepest secrets. {b}{color=#af0aa1}They are you.{/color}{/b}"
    show mina mirror tilt
    mi "... {w=1}So, are you going to talk to me directly, or what?"

    scene bg bathroom
    show meyer hand sad at right
    show mina default neu at left
    with dissolve

    my "I'm ignoring you for a {b}{color=#af0aa1}reason.{/color}{/b}"
    show mina default surprise
    mi "What~? Shouldn't you just leave the curtain closed, then?"
    mi "Unless we were playing hide-and-seek? Who was 'it'? You or I?"
    show meyer hand bother
    my "I'm not playing games with you. Your idea of 'fun' is nothing to be proud of."
    show mina up shade
    mi "Hm... I guess 'it' {i}would{/i} be you. You were the one that found me, after all."
    show meyer hand sad
    my "..."
    "He's right. The villain of the game... it was always me."
    show meyer default neu
    my "... {w=1}I don't have time to think about that. Please, just show me my own appearance."
    show mina up stare 
    mi "Fine... I guess you win."

    scene cg meyerMirror
    with dissolve
    """
    He disappears to show my physical face. At least he respects me enough to do that.
    
    Truthfully, I've always had eyebags. I was a high-achiever in school, so I spent a lot of nights studying until my dad yelled at me to go to sleep.
    
    It was fun, in a way! Stressing my hair our trying to make a better future for myself.\n{color=#7c7c7c}(But it was useless.){/color}
    
    Although, my eyebags have gotten darker lately, along with the rest of my mind.
    """
    #sound effect
    "Unfortunately, I don't have much in the way of makeup, so I opt to splash my face with cold water instead and hope it somehow clears up."
    "Still, my own face feels ugly to look at. I'd almost rather look at my actual Reflection."

    scene bg bathroom
    show mina point at left
    show meyer default neu at right
    mi "Only almost?"
    my "That wasn't an invitation for you to show up again."
    show mina default neu
    mi "Well, you seemed done, so I invited myself back!"
    show meyer hand sad
    my "I'd rather you never come back, frankly."
    mi "Haha, then I wouldn't be doing my job!"

    scene bg bathroomCurtainOpen
    show mina mirror tilt
    mi "... {w=1}Meyer, you'll have to forgive {s}yourself{/s} me one day, you know?"
    mi "Or one day, the pressure will get to you.\n{color=#7c7c7c}(Again.){/color}"
    my "..."
    show bg bathroomCurtain
    hide mina
    #sfx
    "A dismissal of myself. He is no longer welcome to speak."
    "But I know what he'd say to me:"
    show black
    "... I just want to play like we used to."
    "Before everything."
    # day 1 start end

label day_1:
    scene bg house
    with fade
    $ hasViolin = False
    """
    I arrive at my Dad's house.
    
    It's nothing special. Just a single-family home in a copy-paste neighborhood.
    
    But therein lies a very peculiar man.
    """

    show black
    with fade
    #knock

    show cg tyce one
    with fade
    #music
    ty "Come in. I tuned your violin for you."
    my "Ahh, I don't know... you know I quit practicing when I got out of high school."
    ty "Well, you got ears. Last time I checked, you weren't tone deaf."
    menu: 

        "Pick up the violin.":
            $ happiness += 5

            show cg tyce violin
            my "Haha. Fine~."
            #sfx
            ty "There you go, kid. Music's good for the soul."
            my "I'm twenty, Dad."
            ty "Hm. Still ten times younger than me."
            my "Sure-sure, sir."

        "Don't.":

            show cg tyce two
            my "Uh, I haven't cut my fingernails."
            ty "Yeesh. Long fingernails? Forget it, then."
            ty "I'll gift you some nail clippers for your birthday. How about that?"
            my "Haha. Absolutely not!"
    
    #day 1 end

label day_2_start:
    scene black
    #ambient music?

    "I'm not always the only one featured in my nightmares."

    show cg nightmare2 one
    with fade

    "Newsperson" "... The search for the five missing persons is still ongoing after one month of little progress."
    "Newsperson" "These five individuals were all reported to have disappeared around 5 PM on January 14..."

    """

    I remember seeing this broadcast a week after I moved in with Tyce.

    I was sitting on the floor playing with a toy ukelele Tyce got me. 
    
    He wasn't paying attention; Mostly making sure I didn't break the dang thing, haha.

    """

    show cg nightmare2 two

    "Newsperson" "...The final person is a 40 year old woman named XXXX XXXX, approximately average height..."

    "Out of everyone I met, that lady was the one I liked the most."
    "She reminded me of my old friend's parents: Gentle, steadfast, strong. But she was too kind."

    "Newsperson" "If you have any information of their whereabouts, please leave a tip at our local police line..."

    "Of course, I knew where all five of them went."
    "They were the first, but they were certainly not the last."

    #fade

    show cg nightmare2 three
    with fade
    "Principal" """ 
    
    We are here to honor the lives of the five students lost to the hands of the X?!!??!?@@X...

    These bright youths of tomorrow had their light unceremoniously taken away from them in the night, as if their life was worth less than another's...

    """

    """ 

    Yes... that was the kind of thing I thought back then. 

    It was a terrible, terrible notion.

    """

    "Principal" "... We will now proceed to have a moment of silence. Please cease any movement in or out of the building until directed."

    """

    In the end, the one who found me out was Altair, who was on their own kind of redemption journey.

    We'd hadn't known each other personally for very long, but we grew up in the same environment. 
    
    It was strange having someone who knew exactly why I was made the way I was.

    Afterwards, they continued on their journey, and grasped a well-deserved happy ending.
    """
    show cg nightmare2 four
    #ringing sound
    my "And yet... I still find my old habits clinging onto me today--"
    #E
label day_3_start:

    "woah"

    return