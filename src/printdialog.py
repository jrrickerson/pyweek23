try:
    from . import ptext
except:
    import ptext

def opening(pagenum=0):
    tx = 150
    ty = 150
    dty = 20

    texttodraw = ["""
    Press Enter to Reply or Continue

    Press ESC to Quit Game.""", 
    """
    Marans:
    Commander Silkie!
    Attention!
    This is Adjunct Fleet Administrator Marans. The enemy 
    Aseel has invaded the Cochin system. You are our only
    fighter in the area. We need you to take one of the 
    two ships stationed on Cochin 1 and engage the enemy.""",
    """
    Silkie:
    Marans, Sir, This is Commander Silkie.
    What can you tell me about the two fighters?
    """,
    """
    Marans:
    The first ship, the Orpington, is heavily
    armed, but it is built for interstellar flight
    and not very manuverable.
    The other ship is smaller and will be a more 
    difficult target. It's name is the Fayoumi.""",
    """
    Silkie:
    Neither one sounds like a good choice to me.""",
    """
    Marans:
    That's true, but you don't have much time. 
    Your best chance is to reduce the Aseel fleet before 
    they enter the asteroid belt. Now pick one 
    and get going.""",
    """
    To pick the Orpington, Press A.
    To pick the Fayoumi, Press B.
    """,
    """
    Silkie:
    Right, Adjunct Fleet Administrator. 

    I'll take the Orpington. It has been through a lot 
    of battles and always come through.""",
    """
    Silkie:
    Right, Adjunct Fleet Administrator. 

    I'll take the Fayoumi and hope I can catch the 
    Aseel by surprise.""",
    """
    Use the arrow keys to navigate.
    The Fayoumi has side thrusters operated
    with keys < > or , .
    Press the space bar to fire. 
    Press Return to begin play.

    Next time, to skip the dialog, press 
    Shift A or Shift B at the beginning.

    Good Luck Silkie.
    """,
    """
    10
    """,
    """
    11
    """,
    """
    12
    """,
    """
    13
    """,
    """
    14
    """,
    """
    15
    """,
    """
    16
    """,
    """
    17
    """,
    """
    18
    """,
    """
    Marans:
    Bad luck Silkie, your ship has taken too much
    damage. You will have to sit the rest of the
    battle out. 
    
    But thanks for fighting so hard.
    You have given our fleet on Welsummer a chance
    to mobilize. There is still hope.

    Press ESC key to exit.
    """,
    """
    Marans:
    Way to go Silkieo!

    You really handled those Aseel. Your job here 
    is done. The fleet from Welsummer will mop up
    any stray enemy ships still out there.

    You can get the rest you deserve. Just press 
    the ESC key to sign off.
    """]

    for index, line in enumerate(texttodraw[pagenum].split('\n')):
        ptext.draw(line, (tx, ty + index * dty), color = 'black')

def scoreboard(shields=0, weapons=0, enemycount=0):
    tx = 10
    ty = 768 - 30
    line = 'Shields: ' + str(shields) + ' Weapons: ' + str(weapons) + ' Enemies: ' + str(enemycount)
    ptext.draw(line, (tx, ty), color = 'black')

if __name__ == "__main__":
    # this path is for local testing
    import ptext
    import main
    main.main()