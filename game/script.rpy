define st = Character("Skibidi Toilet", color = "cbc3b2")

play music "audio/skibidisong.mp3"

image stim = Movie(play="images/stimstation.webm", loop = True)

# The game starts here.

label start:

    scene bg bathroom

    "The player stumbles into a dimly lit bathroom at 3AM. The flickering lights barely illuminate a strange figure—a Skibidi Toilet. Its porcelain gleams in the eerie light, and its head bobs rhythmically, softly humming the Skibidi Dob Dob tune."

    show skibidi happy with moveinbottom

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        st "Yo, blud! Erm, what the sigma are you doing here at 3AM? You looking for the backrooms, or you just vibin' with the goofy ahh aura in this place? Either way, I need your help, pookie wookie bear."

        "Help? With what? This is literally hitting the griddy for Ukraine levels of weird.":
            jump choice1_help
        
        "Nah blud, you lowkey capping. Go rizz another gyatt before I call Baby Gronk.":
            jump choice2_nohelp

    return

label choice1_help:
    scene bg bathroom

    show skibidi happy

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        st "That's the rizz I'm looking for, fr! You see, these CameraHeads have been edging me for days, and they've got my Grimace Shake stash. Without it, I'm just another mouth breather in the toilet gang. I need you to sneak into their lair and grab my shakes. Lock in, blud. You in?"

        "Let's lock in and grab those shakes *2 second pause and smirk* together.":
            st "Let me be clear with you, my little gyatt, ever since I first jelqed with you, I felt like you Fanum Taxed my heart. Every time I'm with you, I feel my Skibidi best. I feel like +100 aura, and you make me want to bring the boom like AJ and Big Justice."
            jump choice3_helplove
        
        "I'll help, but I'm only doing this for the Sigma Patrick Bateman Ohio grindset.":
            st "I knew you were an alpha! Once I get my Grimace Shakes back, Lets eat some MrBeast Burger while we watch the Talk Tuah Podcast."
            jump choice4_helpfriend

        "This is so sus. Are you even real, or are you Tyler Durden?":
            st "Erm, yeah, no. You've got less aura than a NPC in Ohio. Back to the Gulag for you, lil bro."
            jump choice2_nohelp
    
    return

label choice2_nohelp:
    scene bg bathroom

    show skibidi sad

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    st "Ermm, what the Sigma? I thought you were alpha enough to help a beta in need. Turns out, you're just another bop."

    "You abandoned Skibidi Toilet. Social credit -1000000 (beta endong)"

    return

label choice3_helplove:
    scene bg bathroom

    show skibidi love

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        st "*Opens RizzApp* So, my little Skibidi, I've been thinkmaxxing, and I think I need to keep it a buck fiddy with you. You've got the fattest gyatt I've ever seen. It makes me want to kill myself. So how about you and me mew together from now on."

        "Skibidi, you're great, I'd love to edgemaxx with you for the rest of my Chungus life.":
            jump choice5_date
        
        "Skibidi, you're great, but I'd rather keep it a buck fiddy":
            show skibidi happy
            st "Damn, I went to Friendzone town and everybody knew you."
            jump choice4_helpfriend
        
    return

label choice4_helpfriend:
    scene bg bathroom

    show skibidi happy

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        st "Alright blud, let's lock in. Our vibes are strong, like Lunchly and Still Prime (those who know 💀💀💀). How about we go to the backrooms and use our Balkan rage and noradrenaline on the NPCs like Skibidi broskis."

        "We got us being friends before GTA 6 💀":
            st "When I'm in a friendship competition and my opponent is us. I went to Friendship town and everybody knew us."
            "You befriended Skibidi Toilet. Social credit +20000 (neutral endong)"
        
        "I'm sorry Skibidi, but I think we should edge our separate ways.":
            st "Wow… really? You're breaking our edge streak, just like that? Fine, you were always just a bop anyway. *griddys away*"
            "You rejected Skibidi Toilet. Social credit -9999999 (kys endong)"
    
    return

label choice5_date:
    scene bg park
    
    $ renpy.movie_cutscene("images/skibidifall.webm")

    show skibidi sad

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        st "Whoa, pookie! Not Sigma… I got too lost in the sauce… My lid's all crooked now. You see that? What an L move!"

        "Wow. That was -100 aura. You really are a beta.":
            show skibidi angry
            st "Yo, what the flip? You're actually acting so beta rn. I'm invitingn't you from my goon sesh."
            "You laughed at Skibidi Toilet's misfortune. Social credit -50000 (bad endong)"
        
        "Don't worry about it my little pogchamp. You're just a chill guy who lowkey doesn't give a fuck, and lowkey trips a lot.":
            show skibidi happy
            st "Lil bro glazing me. Lowkey gonna make me cream. Oil up pookie lets get freaky."
            jump choice6_rizz
    
    return

label choice6_rizz:
    scene bg park

    show skibidi love

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        st "You know, maybe you're not so bad after all… Thanks for that. You're a real one g."

        "Bro's not beating the sweetie pie allegations":
            menu:
                st "Oi oi oi, how about we continue datemaxxing at the Diddy Party?"

                "That would be absolutely poggers, but I can't. I'm allergic to baby oil, and my cousin Quandale Dingle got my whole family banned from there. Don't ask about it.":
                    st "Blud's definitely from Ohio 💀"
                
                "Aww hell nah. Diddy's such a yapper. He's from Yapghanistan and only speaks Yapanese. Lil bro only drinks yapaccinos.":
                    st "Blud's definitely from Ohio 💀"
        
        "Chat am I the rizzler? Chat am I getting rizzy?":
            menu:
                st "Oi oi oi, how about we continue datemaxxing at the Diddy Party?"

                "That would be absolutely poggers, but I can't. I'm allergic to baby oil, and my cousin Quandale Dingle got my whole family banned from there. Don't ask about it.":
                    st "Blud's definitely from Ohio 💀"
                
                "Aww hell nah. Diddy's such a yapper. He's from Yapghanistan and only speaks Yapanese. Lil bro only drinks yapaccinos.":
                    st "Blud's definitely from Ohio 💀"
    
    menu:
        "How about we go grab some Lunchly and Prime?":
            st "Sounds bussin'. I like my cheese drippy bruh."
            jump choice7_date
        
        "Let's go back to my goon cave and edge to Caseoh, you down?":
            st "I thought you'd never ask. Chat clip this."
            jump choice7_date
    
    return

label choice7_date:
    scene bg goon cave

    show skibidi love

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        "Pookie, you're more perfect for me than a low taper fade is for Ninja. Would you like to merge our edging streaks?":
            st "A level 100 gyatt like you? Rizzing up lil ol' me? I'm honored."
            jump choice8_date2
        
        "No cap, the first time your German stare met my lightskin stare, I knew we were destined to be. Like mold and Lunchly cheese.":
            st "Lets lock in together and lovemaxx. Maybe even relationshipmaxx?"
            jump choice8_date2
        
        "Chat I don't think this is working out. Chat am I cooked?":
            show skibidi sad
            st "What an L beta move. I should've known from the start that you were a sus NPC from Ohio."
            "You broke Skibidi Toilet's heart. Social credit -1000 (sad endong)"

    return

label choice8_date2:
    scene bg goon cave

    show skibidi love

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        st "You're such a Sigma male. Like you mog everyone fr fr. How about we have a... freak off?"

        "I knew bringing baby oil everywhere would eventually pay off. Time to pay the Fanum tax lil bro":
            "You got freaky. Social credit +696969 (freaky endong)"

        "Freaky ahh Skibidi. Bro's not beating the freaky allegations.":
            "No pressure if you don't wanna oil up and get freaky just yet."
            jump choice9_nofreak

    return

label choice9_nofreak:
    scene bg goon cave

    show skibidi love

    show stim behind st:
        xalign 0.1
        yalign 0.1
        zoom 0.25

    menu:
        st "How does a second date sound?"

        "Bro's the ultimate rizz king. Chat I just got rizzed up. Lets see each other again at the Tiktok Rizz Party.":
            "You began dating Skibidi Toilet. Social credit +infinite (serious romance endong)"
        
        "Bro really think he Carti 💀":
            show skibidi sad
            "You rejected Skibidi Toilet. Social credit -infinite (wasteful endong)"

    return