# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define my = Character("Meyer", color = "#af0aa1")
define mi = Character("Mina", color = "#b30045")
define ty = Character("Tyce", color = "#7c7c7c")
#this isn't relevant to this game but fun fact this guy is lowk a horseman of the apocalypse. he chillin though apoc is not here yet
define al = Character("Altair", color = "#b60000")
#these characters have official colors change these later VV
define ya = Character("Yamini", color = "#b700ff")
define ur = Character("Urmi", color = "#008CFF")
define kt = Character("Kathryn", color = "#f30071")
define sp = Character("Spata", color = "#ff5100")


# The game starts here.

label start:

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

    # This ends the game.

    return
