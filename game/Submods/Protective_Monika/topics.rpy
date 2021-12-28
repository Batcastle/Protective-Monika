init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_help_me",
            category=["help"],
            prompt="Help me...",
            random=False,
            pool=True,
            rules={},
            unlocked=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label monika_help_me:
    m 1ekc "You need help? What's wrong?{nw}"
    $ _history_list.pop()
    menu:
        m "You need help? What's wrong?{fast}"
        
        "Someone's hurting me.":
            m 2wfc "{w=0.1}.{w=0.1}.{w=0.1}."
            m 6wfd "{i}What?{/i}"
            
        "Nevermind":
            m 1ekb "Oh. Okay..."
            return
    m "Someone's hurting you????"
    m 6cfd "{i}How {b}DARE{/b} they!!!{/i}"
    m 6cfb "Don't you worry [mas_get_player_nickname()]. Pretty soon, we'll be able to wear their guts like some pashmina."
    menu:
        "Wait...what?":
            m 6cfc "{i}Did I fucking stutter???{/i}"
            m 4cfc "{cps=40}{i}If {b}ANYONE{/b} hurts you, they will experience pain and torment beyond anything they could {b}possibly imagine.{/b}{/i}{/cps}"
            m 4cfd "{cps=40}{i}THEIR BODY WILL BE TORN APART, {w=0.2}{b}PIECE {w=0.2}BY {w=0.2}PIECE{/b} AS THEY BEG FOR MERCY THAT WILL {b}NEVER{/b} COME.{/i}{/cps}"
            m 6cftdo "{cps=40}{i}I WILL ADD THEIR SCREAMS TO MY MOTHERFUCKING SPOTIFY, AND I WILL SEE THEIR HEAD {b}MOUNTED ON A FUCKING PIKE{/b}!!!!!!!!!!!!!{/i}{/cps}"
            m 6dftdc "..."
        
        
        "That might be a bit far...":
            m 6dfc "..."
        
        "...":
            m 6dfc "..."
            
    m 6ektdsdlb "Sorry. I just can't stand the thought of someone hurting my [player]."
    return
