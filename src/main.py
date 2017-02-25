"""
Pyweek 23 entry
Theme: The lesser of two evils

Game Idea
    Space game with shooting
    each play level you have to choose between two options 
    neither option is good

"""
import pygame
import math
try:
    from . import printdialog
except:
    import printdialog

datapath = 'data/'
screen_size = (1028, 768)

def collision(sprite1, sprite2):
    # check collision between sprites
    hitradius1 = (sprite1.width + sprite1.height)/2
    hitradius2 = (sprite2.width + sprite2.height)/2
    hitradius = (hitradius1 + hitradius2) * .6

    loc1 = (sprite1.x + sprite1.width/2, sprite1.y + sprite1.height/2)
    loc2 = (sprite2.x + sprite2.width/2, sprite2.y + sprite2.height/2)
    if math.sqrt((loc1[0] - loc2[0]) * (loc1[0] - loc2[0]) + (loc1[1] - loc2[1]) * (loc1[1] - loc2[1]))  < hitradius:
        return True
    else:
        return False

def hit_wall():
    # check for collision with wall
    pass

def play_intro():
    # background music
    pygame.mixer.music.load(datapath + '0788.ogg')
    pygame.mixer.music.play(10)

def draw_console(screen):
    # load the image
    console_image = datapath + 'control_console_large.png'
    console = pygame.image.load(console_image)
    consolerect = console.get_rect()  
    consolerect = consolerect.move([0,0])
    screen.blit(console, consolerect) 

def draw_broken_console(screen):
    # load the image
    broken_console_image = datapath + 'broken_console.png'
    broken_console = pygame.image.load(broken_console_image)
    broken_consolerect = broken_console.get_rect()  
    broken_consolerect = broken_consolerect.move([0,0])
    screen.blit(broken_console, broken_consolerect) 

def draw_bang(screen):
    # load the image
    bang_image = datapath + 'bang.png'
    bang = pygame.image.load(bang_image)
    bangrect = bang.get_rect()  
    bangrect = bangrect.move([0,0])
    screen.blit(bang, bangrect) 

def slow(x):
    # if x is a speed reduce speed
    x1 = math.fabs(x)
    if x1 > 0.1:
        signofx = x/x1
        x1 -= 0.1
        return signofx * x1
    else:
        return 0

def main():

    # setup timing
    clock = pygame.time.Clock()
    FRAMES_PER_SECOND = 30
    deltat = clock.tick(FRAMES_PER_SECOND)

    black = (0,0,0)
    white = (255, 255, 255)
    grey = (200, 200, 200)

    # a surface
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill(grey)

    # intro screen
    play_intro()

    running = True
    part1 = True
    part2 = False
    part20 = False
    part99 = False
    printpage = [True, False, False, False, False, False, False,
                False, False, False, False, False, False]
    printpagenum = 0
    # default to orpington numbers
    speedchange = 5
    anglechange = 2.0
    shields = 40
    weapons = 40
    player_file = 'b201.png'
    missile_file = 'missile_big.png'
    enemy_file = 'enemyship1.png'
    live_missile = False
    live_enemy = False
    enable_enemy = False
    enemyspeed = 10
    enemycount = 30
    x = 0
    y = 0
    mx = 0
    my = 0
    ex = 0
    ey = 0
    # intro screen
    while running and part1:
        # timing
        clock.tick(FRAMES_PER_SECOND)
        # get keyboard events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                # if event.type == pygame.KEYDOWN and event.key == pygame.K_A:
                if event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    player_file = 'b201.png'
                    # using default speed and angle
                    printpagenum = 9
                    part1 = False
                    part2 = True
                elif event.key == pygame.K_b and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    player_file = 'a202.png'
                    missile_file = 'missile_small.png'
                    speedchange = 3
                    anglechange = 5.0
                    shields = 20
                    weapons = 15
                    printpagenum = 9
                    part1 = False
                    part2 = True

                # when ESC is pressed end game
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif event.type == pygame.QUIT:
                    running = False
                if printpagenum == 9:
                    # final dialog before game play
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        part1 = False
                        part2 = True
                elif printpagenum == 7:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        printpagenum += 2
                elif printpagenum == 6:
                    # pick a ship
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                        player_file = 'b201.png'
                        # using default speed and angle                    
                        printpagenum += 1
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                        player_file = 'a202.png'
                        missile_file = 'missile_small.png'
                        speedchange = 3
                        anglechange = 5.0
                        shields = 20
                        weapons = 15
                        printpagenum += 2
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    printpagenum += 1
                
        # print dialog
        draw_console(screen)
        printdialog.opening(printpagenum)
        pygame.display.flip()

    # a ship has been chosen, the play begins
    pygame.key.set_repeat(200, 100)
    screen.fill(grey)

    # get a player ship
    player = pygame.image.load(datapath+player_file)
    playerrect = player.get_rect()
    playerrect.x = 100
    playerrect.y = 100
    playerdegrees = 0.0
    playerradians = playerdegrees * 3.141592654 / 180

    # get a missile
    missile = pygame.image.load(datapath+missile_file)
    missilerect = missile.get_rect()

    # get an enemy
    enemy = pygame.image.load(datapath+enemy_file)
    enemyrect = enemy.get_rect()


    while running and part2:
        # timing
        clock.tick(FRAMES_PER_SECOND)
        screen.fill(grey)

        # get keyboard events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                enable_enemy = True
                # when ESC is pressed end game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    # rear thrust go forward 
                    # calculate the player motion
                    x += speedchange * math.sin(-playerradians)
                    y += -speedchange * math.cos(-playerradians)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    # reverse thrust
                    x += -speedchange * math.sin(-playerradians)
                    y += speedchange * math.cos(-playerradians)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    playerdegrees -= anglechange 
                    playerradians = playerdegrees * 3.141592654 / 180
                    player = pygame.image.load(datapath+player_file)
                    player = pygame.transform.rotate(player, playerdegrees)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    playerdegrees += anglechange
                    playerradians = playerdegrees * 3.141592654 / 180
                    player = pygame.image.load(datapath+player_file)
                    player = pygame.transform.rotate(player, playerdegrees)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LESS:
                    # right thrust move left
                    x += -speedchange * math.cos(-playerradians)
                    y += -speedchange * math.sin(-playerradians)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_COMMA:
                    # right thrust move left
                    x += -speedchange * math.cos(-playerradians)
                    y += -speedchange * math.sin(-playerradians)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_GREATER:
                    # left thrust move right
                    x += speedchange * math.cos(-playerradians)
                    y += speedchange * math.sin(-playerradians)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_PERIOD:
                    # left thrust move right
                    x += speedchange * math.cos(-playerradians)
                    y += speedchange * math.sin(-playerradians)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # fire
                    if weapons > 0:
                        weapons -= 1
                        live_missile = True
                        # start the missile in the center of the ship
                        missilerect.x = playerrect.x + (playerrect.width - missilerect.width)/2.0
                        missilerect.y = playerrect.y + (playerrect.height - missilerect.height)/2.0
                        # launch missile in the direction the ship is pointed
                        mx = 4 * speedchange * math.sin(-playerradians)
                        my = 4 * -speedchange * math.cos(-playerradians)
        else:
            if playerrect.x > 0 and playerrect.x < screen_size[0] - playerrect.width:
                x = slow(x)
            else:
                x = 0
                if playerrect.x <= 0:
                    playerrect.x += 1
                elif playerrect.x >= screen_size[0] - playerrect.width:
                    playerrect.x -= 1
            if playerrect.y > 0 and playerrect.y < screen_size[1] - playerrect.height:
                y = slow(y)
            else:
                y = 0
                if playerrect.y <= 0:
                    playerrect.y += 1
                elif playerrect.y >= screen_size[1] - playerrect.height:
                    playerrect.y -= 1
        
        # move and fire enemy
        if enable_enemy and not live_enemy:
            # launch a new enemy
            live_enemy = True
            # enemy ship enters near the corner farthest from the player
            enemy = pygame.image.load(datapath+enemy_file)
            if playerrect.x < screen_size[0]/2:
                enemyrect.x = screen_size[0] - enemyrect.width
                enemy = pygame.transform.rotate(enemy, 90)
                ex = -enemyspeed
                ey = 0
            else:
                enemyrect.x = 1
                enemy = pygame.transform.rotate(enemy, -90)
                ex = enemyspeed
                ey = 0
            if playerrect.y < screen_size[1]/2:
                enemyrect.y = screen_size[1] - (enemyrect.width + 1)
            else:
                enemyrect.y = 1
            # it moves horizontally initially 
            enemyrect = enemyrect.move([ex,ey])

        # until its x position crosses the players x 
        # then it turns and continues toward the player
        if enable_enemy and live_enemy:
            if math.fabs((playerrect.x + playerrect.width/2) - (enemyrect.x + enemyrect.width/2)) < 10:
                enemy = pygame.image.load(datapath+enemy_file)
                if (playerrect.y + playerrect.height/2) > (enemyrect.y + enemyrect.height/2):
                    # turn down
                    enemy = pygame.transform.rotate(enemy, 180)
                    ex = 0
                    ey = enemyspeed

                else:
                    # turn up
                    enemy = pygame.transform.rotate(enemy, 0)
                    ex = 0
                    ey = -enemyspeed
            enemyrect = enemyrect.move([ex, ey])        
            screen.blit(enemy, enemyrect)
            # when the enemy runs off the screen, launch a new one
            if enemyrect.x > screen_size[0] + enemyrect.width or \
                enemyrect.x < -enemyrect.width or \
                enemyrect.y > screen_size[1] + enemyrect.height or \
                enemyrect.y < -enemyrect.height:
                live_enemy = False

            # if it hits, the whole thing blows up
            if collision(enemyrect, playerrect):
                live_enemy = False
                draw_bang(screen)
                pygame.display.flip()
                pygame.time.delay(200)
                # if final hit go to end screen
                if shields < 1:
                    part2 = False
                    part99 = True
                shields -= 10

            # see if the missile hit the enemy
            if collision(enemyrect, missilerect):
                live_enemy = False
                live_missile = False
                draw_bang(screen)
                pygame.display.flip()
                pygame.time.delay(200)
                # if final hit go to end screen
                if enemycount < 1:
                    part2 = False
                    part20 = True
                enemycount -= 10
                enemyspeed += 5

        # check for round completed
        # show progress
        printdialog.scoreboard(shields, weapons, enemycount)

        print ('playerradians', playerradians, x, y, math.sin(-playerradians), math.cos(-playerradians))
                
        # move sprites
        playerrect = playerrect.move([x,y])
        if live_missile:
            missilerect = missilerect.move([mx, my])
            screen.blit(missile, missilerect)
            if missilerect.x < -missilerect.width or \
                missilerect.x > screen_size[0] or \
                missilerect.y < - missilerect.height or \
                missilerect.y > screen_size[1]:
                live_missile = False

        # check for wall
        # if ship hits wall stop its movement in that direction
        playerrect.x = max(playerrect.x, 0)
        playerrect.x = min(playerrect.x, screen_size[0] - playerrect.width)
        playerrect.y = max(playerrect.y, 0)
        playerrect.y = min(playerrect.y, screen_size[1] - playerrect.height)

        screen.blit(player, playerrect)
        pygame.display.flip()

    while running and part20:
        # won
        draw_console(screen)
        printdialog.opening(20)
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            # when ESC is pressed end game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

    while running and part99:
        # lost
        draw_broken_console(screen)
        printdialog.opening(19)
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            # when ESC is pressed end game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

    pygame.quit()

if __name__ == "__main__":
    # this path is for local testing
    datapath = '../data/'
    main()
