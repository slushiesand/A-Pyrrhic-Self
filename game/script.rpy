

define my = Character("Meyer", color = "#af0aa1")
define mi = Character("Mina", color = "#b30045")
define ty = Character("Tyce", color = "#7c7c7c")
define al = Character("Altair", color = "#b60000")
define ya = Character("Yamini", color = "#5a23a2")
define ur = Character("Urmi", color = "#1e58c0")
define kt = Character("Kathryn", color = "#00b391")
define sp = Character("Spata", color = "#c54c30")
define fu = Character("Fuca", color = "#fff")
                      
image black = "#000"
define  audio.clownsMarch = "audio/music/0277_道化のマーチ.mp3"

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
    with dissolve
    play sound "<from 3.3>sfx/jessey_drake_synth_space_weird_horror_waterphone_sting_accent_snth_jd.mp3" fadein .5 fadeout .3
    "It's always—{nw=1.5}"

    show cg meyerbed
    #ambient music?
    stop sound
    play sound "sfx/zapsplat_foley_clothing_jacket_hi_vis_single_shake_003_111604.mp3"
    #play sound "<from 6>sfx/jessey_drake_synth_space_weird_horror_waterphone_sting_accent_snth_jd.mp3"
    "— Me."
    my "Haah. Not again..."
    "Cold sweat clings to my skin like fleas."

    scene bg bedroom
    with hpunch
    play sound "sfx/zapsplat_household_bedsheet_movement_single_64354.mp3"
    "Time to get up, lonesome body."
    play sound "sfx/zapsplat_foley_clothing_jacket_hi_vis_single_shake_003_111604.mp3"
    show meyer default neu
    with fade
    """
    I often have nightmares in my sleep. Definintely more than the average adult, but maybe not in the city where I live.
    
    Lots of bad things happened here, and still do.
    
    I try to make the world a better place, along with my friends. People have to look out for each other, you know?
    """
    show meyer cheek happy
    "We've all dedicated our lives to humanity, in a way. Some of my friends are going to college to become teachers. Others vow to protect peace directly."
    show meyer hand sad
    "Of course, I shouldn't be included in that gallantry."
    
    scene cg calendar one
    with fade
    """
    February 14th is my birthday, better known as the Day of Love.
    
    I've always found it ironic, considering everything that has happened. {color=#7c7c7c}(Considering everything I've done.){/color}{nw=1}
    
    ... {w=1}This year should have been given to the dead. But nevertheless, I survive.

    But at least I get to see all of my friends happy.

    I like seeing people live brighter lives. It makes me forget about my own, just a bit.
    """
    show cg calendar two
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
    play music clownsMarch fadeout 1.0 fadein 1.0
    mi "It's been a while, Meyer."
    "One and the same."
    mi "Well, technically, your dreams are a figment of your imagination. {color=#b30045}I'm{/color} as real as you."
    "They can hear your thoughts, know your deepest secrets. {color=#af0aa1}They are you.{/color}"
    show mina mirror tilt
    mi "... {w=1}So, are you going to talk to me directly, or what?"

    scene bg bathroom
    show meyer hand sad at right
    show mina default neu at left
    with dissolve

    my "I'm ignoring you for a {color=#af0aa1}reason.{/color}"
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
    show mina up smug 
    mi "Fine... I guess you win."

    scene cg meyerMirror
    with dissolve
    """
    He disappears to show my physical face. At least he respects me enough to do that.

    I stare at my disheveled appearance in the mirror.
    
    Truthfully, I've always had eyebags. I was a high-achiever in school, so I spent a lot of nights studying until my dad yelled at me to go to sleep.
    
    It was fun, in a way! Stressing my hair our trying to make a better future for myself.\n{color=#7c7c7c}(But it was useless, as you can see.){/color}
    
    """
    #sound effect
    "{w=1}Unfortunately, I don't have much in the way of makeup, so I opt to splash my face with cold water instead and hope it somehow clears up."
    "Still, my own face feels ugly to look at. I'd almost rather look at my actual Reflection."

    scene bg bathroom
    show mina point at left
    show meyer default neu at right
    with vpunch
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
    stop music fadeout 1.0
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

    scene cg tyce one
    with fade
    #music
    ty "Come in. I tuned your violin for you."
    my "Ahh, I don't know... you know I quit practicing when I got out of high school."
    ty "Well, you got ears. Last time I checked, you weren't tone deaf."
    menu: 

        "Pick up the violin.":
            $ happiness += 5

            show cg tyce violin
            with dissolve
            my "Haha. Fine~."
            #sfx
            ty "There you go, kid. Music's good for the heart."
            my "I'm twenty, Dad."
            ty "Hm. Still ten times younger than me."
            my "I think it's a {i}bit{/i} more than that, sir."

        "Don't.":

            show cg tyce two
            with dissolve
            my "Uh, I haven't cut my fingernails."
            ty "Yeesh. Long fingernails? Forget it, then."
            ty "I'll gift you some nail clippers for your birthday. How about that?"
            my "Haha. Absolutely not!"

    show black:
        alpha .5
    with dissolve

    """

    Tyce isn't my biological dad, actually.

    He adopted me when I was twelve, a little after my first incident.

    He lived around the area, didn't have family of his own, and had experience with fostering troublesome children like me. So, it was a natural fit!

    Though, I still caused lots of trouble.

    He's a bit odd himself. A traditional, introverted old man is actually a retired rocker-photographer! It makes for quite the interesting character.

    He's not a perfect man, but compared to my other choice for a father, he's leagues better.{w=1} He's my dad!

    """

    scene bg living
    show meyer default smile at right
    show tyce default smile at left
    with dissolve

    ty "How's the new place?"
    show meyer cheek happy
    my "It's nice! I don't have to drive to work anymore, and the grocery store isn't too far, either."
    my "It's noisy and crowded all day, but that's what the city is like, hehe."
    show tyce default new
    ty "..."
    show meyer default neu
    my "But... I don't know."
    my "It still feels lonely."
    show meyer hand sad 
    my """
    
    There's no one to talk to in my house other than myself.
    
    It feels like I'm trapped inside my own bubble, I guess.

    Is that what living alone feels like? {w=1}\n... Maybe I should get a fishtank, just to fill the space a little.
    
    """
    show tyce default closed
    ty "You never liked being alone, did you?"
    ty "... A pet would be good, yes."
    show tyce hand smile
    ty "Perhaps Altair could move in with you if they finally decide to get out of my hair."
    show meyer default neu
    my "You think they'd want to?"
    show tyce hand wink
    ty "Of course. You {i}are{/i} friends, are you not?"

    
    #---------------------------------------- day 1 end -----------------------------------------------------

label day_2_start:
    scene black

    "Sometimes, my nightmares are playbacks of memories."
    "A memory of a quiet day with a single trigger, gone south."

    show cg nightmare2 oneA
    with fade
    #tv noise

    "Newsperson" "... The search for the five missing persons is still ongoing after one month of little progress."
    "Newsperson" "These five individuals were all reported to have disappeared around 5 PM on January 14..."

    """

    I remember seeing this broadcast a week after I moved in with Tyce.

    I was sitting on the floor playing with a toy ukelele Tyce got me. 

    """

    ty "See? When you put your fingers on the frets, the sound the strings make changes."

    "He wasn't paying attention to the screen. Mostly making sure I didn't break his physical lecture tool, haha."


    show cg nightmare2 twoA

    "Newsperson" "...The final person is a 40 year old woman named ■■■■■ ■■■■■, approximately average height..."

    my "... I think you'd like her."
    ty "Sorry? Who?"
    my "The lady on the screen! ■■■■■ ■■■■■. She's {i}nice, educated,{/i} and... {w=1} uh..."
    #sfx
    "{i}Missing. Dead. Missing. Dead.{/i}"
    my "I..."
    #sfx
    "{i}{color=#af0aa1}missingdeadmangledmissing{/color}{/i}{nw=1}"

    show cg nightmare2 threeA
    #thump
    ty "{b}Hey. Meyer.{/b} Don't pay attention to the television, alright?"
    ty "She'll be okay. You'll be okay."

    show cg nightmare2 glitch
    #sfx

    al "...{w=1} In what world would you ever think this is okay?!"

    show cg nightmare2 oneB
    "A rainy midnight on a life-changing day."
    al "How is it ever justified to punish petty criminals and cheaters with--{nw=1}"
    play sound "sfx/smartsound_HUMAN_VOCAL_Female_Laugh_05.mp3"
    my "Haha, you're one to talk! Why don't you ask yourself that?"

    show cg nightmare2 twoB
    my "We're cut from the same cloth, you know~? A little different job, maybe, but trapped under the same {color=#af0aa1}dirty puppet strings.{/color}"
    my "It makes me sick, too. {i}Really!{/i} But there's nothing we can do about it."
    my "You must know as well as I do! {color=#af0aa1}We are people who {i}cannot change.{/i}{/color}"

    scene cg meyerbed2
    #ok i know these variable names are inconsistent but IDC i gave up
    stop sound
    play sound "sfx/zapsplat_foley_clothing_jacket_hi_vis_single_shake_003_111604.mp3"
    "..."
    "There's nothing I can do but sigh when I finally wake up."
    
    
label day_3_start:

    "woah"

    if happiness >= 5:
        #make this trigger if you got both endings
        jump secret
    else:
        return

label secret:
    
    scene cg secret1
    with fade
    #night time ambiance
    ty "..."

    show cg secret2
    with vpunch
    fu "Looking for someone?"
    ty "Can't a man admire the heavens in peace? I can see the stars for once."

    show cg secret3
    with dissolve
    fu "Is that so? I personally believe that the sky looks the same as yesterday, and the day before."
    ty "Well, that's your opinion. Perhaps you haven't noticed the stars fading away from your millenia on the moon."
    fu "200 years for a human is also a long time! Though, I suppose it's debatable whether you still qualify as one."


    show cg secret2
    with dissolve
    ty "... What do you want, God of Biotic Beings?"
    fu "I don't mean to offend! Can't a 'person' visit their friends once in a while? I don't talk to you strictly for business, you know?"
    ty "I would not consider you a friend as much as an individual that has stuck around longer than others I have known."
    ty "And nonetheless, it is written on your face. You have dealings with {color=#7c7c7c}Death,{/color} not a former man named {color=#7c7c7c}Tyce{/color}."

    show cg secret3
    with dissolve
    fu "Aagh... Someday, I'll be able to fool you."
    fu "Anyway! I wanted to hear how your children are doing. Your dear Meyer and Altair."
    ty "... My children? They are...{w=1} happy."

    show cg secret2
    with dissolve
    ty "They're well-functioning adults. Altair and Meyer have steady jobs, and Meyer had his birthday recently."
    ty "Of course, these are not indications of happiness. Following the rules makes everyone go insane eventually."

    show cg secret4
    with dissolve
    ty "So I will say this: They are now unburdened by their past.\n... They now forge their own path."
    fu "... It pleases me to hear that."
    ty "I have simply done my duty. Nothing extraordinary."

    show cg secret5
    with dissolve
    fu "Hm... But I think you'll have to watch them a little longer. Say... about 10 more years?"
    ty "Oh? And why is that?"
    fu "... An apocalypse may once again arrive, Death. And these children of yours may be the {i}key to end it.{/i}"

    scene black
    with fade

    return
    
