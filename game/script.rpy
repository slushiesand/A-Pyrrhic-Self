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

    $ mina_friendship = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    my "hi"
    mi "hi"
    ty "hi"
    al "hi"
    ya "hi"
    ur "hi"
    kt "hi"
    sp "hi"



label day_2_start:
    scene black

    "I'm not always the only one featured in my nightmares."

    show cg nightmare2 one
    with fade

    "Newsperson" "... The search for the five missing persons is still ongoing after one month."
    "Newsperson" "These five individuals were reported to have all disappeared around 5 PM on January 14..."

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

    "Of course, I knew where all five of them went. They were the first, but they were certainly not the last."

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