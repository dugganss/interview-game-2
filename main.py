import pygame
from settings import *
import random
from classes import *


# INITIATES PYGAME
pygame.init()

# SURFACE CREATION
size = (WINDOW_W, WINDOW_H)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)


# CLOCK
clock = pygame.time.Clock()


# ~~~~~~GAME PROCEDURE~~~~~~#

def game():

    # ~ VARIABLES ~ #

    # BOOLEAN #
    Up = False
    Down = False
    Left = False
    Right = False

    jumping = False

    isMoving = False

    isBird = False
    isCloud = False
    notFalling = True
    fallColour = False
    swung = False
    swinging = False

    # INTEGERS #

    vely = 11

    # ~ SPRITE GROUPS ~ #

    blocks = pygame.sprite.Group()
    backs = pygame.sprite.Group()
    players = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    rings = pygame.sprite.Group()
    birds = pygame.sprite.Group()
    grasses = pygame.sprite.Group()
    pebbles = pygame.sprite.Group()
    flowers = pygame.sprite.Group()
    layergrass = pygame.sprite.Group()
    layerflower = pygame.sprite.Group()
    layerenemy = pygame.sprite.Group()
    swords = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # ~ MAP LAYOUT ~ #

    # ~ Based on the value given in the layout 2D array, an instance of a class will be made and placed
    #   on screen relative to the position of the item in the 2d array.
    # ~ All instances will have an offset to them on their x and y axis so that they are laid out in a way that connects
    #   the isometrically drawn sprites to each other
    # ~ Certain things such as the block will have things placed over the top of it for graphical detail,
    #   these details are given in the GroundDetails class. Certain methods of this class alter the image so that it
    #   appears as a different thing.

    for col in range(27):
        for row in range(29):
            if layout[row][col] == 1:
                block = Block()
                block.rect.x = 300 + (col * 32 - row * 32) + 10
                block.rect.y = (col * 10 + row * 10) + 10
                blocks.add(block)
                for x in range(6):
                    grass = GroundDetails()
                    grass.GrassImageSelect()
                    grass.rect.x = block.rect.x +random.randrange(0,50)
                    grass.rect.y = block.rect.y +random.randrange(-8,2)
                    grasses.add(grass)
                for x in range(random.randrange(2,5)):
                    pebble = GroundDetails()
                    pebble.PebbleImageSelect()
                    pebble.rect.x = block.rect.x +random.randrange(5,50)
                    pebble.rect.y = block.rect.y +random.randrange(6,13)
                    pebbles.add(pebble)
                for x in range(random.randrange(1,2)):
                    flower = GroundDetails()
                    flower.FlowerImageSelect()
                    flower.rect.x = block.rect.x + random.randrange(6, 40)
                    flower.rect.y = block.rect.y + random.randrange(-8, 3)
                    flowers.add(flower)
            if layout[row][col] == 4:
                platform = Platform()
                platform.rect.x = 300 + (col * 32 - row * 32) + 10
                platform.rect.y = (col * 10 + row * 10) + 10
                blocks.add(platform)
                platforms.add(platform)
                for x in range(random.randrange(3,6)):
                    pebble = GroundDetails()
                    pebble.PebbleImageSelect()
                    pebble.rect.x = platform.rect.x +random.randrange(5,50)
                    pebble.rect.y = platform.rect.y +random.randrange(6,13)
                    pebbles.add(pebble)
            if layout[row][col] == 3:
                player = Player()
                player.rect.x = 300 + (col * 32 - row * 32)+random.randrange(20,30)
                player.rect.y = (col * 10 + row * 10)-random.randrange(20,30)
                players.add(player)
                block = Block()
                block.rect.x = 300 + (col * 32 - row * 32) + 10
                block.rect.y = (col * 10 + row * 10) + 10
                blocks.add(block)
                for x in range(10):
                    grass = GroundDetails()
                    grass.GrassImageSelect()
                    grass.rect.x = block.rect.x +random.randrange(5,50)
                    grass.rect.y = block.rect.y +random.randrange(-2,6)
                    grasses.add(grass)
                for x in range(random.randrange(2,5)):
                    pebble = GroundDetails()
                    pebble.PebbleImageSelect()
                    pebble.rect.x = block.rect.x +random.randrange(0,50)
                    pebble.rect.y = block.rect.y +random.randrange(6,13)
                    pebbles.add(pebble)
            if layout[row][col] == 5:
                enemy = Enemy()
                enemy.rect.x = 300 + (col * 32 - row * 32)+random.randrange(20,30)
                enemy.rect.y = (col * 10 + row * 10)-random.randrange(20,30)
                enemies.add(enemy)
                block = Block()
                block.rect.x = 300 + (col * 32 - row * 32) + 10
                block.rect.y = (col * 10 + row * 10) + 10
                blocks.add(block)
                for x in range(10):
                    grass = GroundDetails()
                    grass.GrassImageSelect()
                    grass.rect.x = block.rect.x + random.randrange(5, 50)
                    grass.rect.y = block.rect.y + random.randrange(-2, 6)
                    grasses.add(grass)
                for x in range(random.randrange(2, 5)):
                    pebble = GroundDetails()
                    pebble.PebbleImageSelect()
                    pebble.rect.x = block.rect.x + random.randrange(0, 50)
                    pebble.rect.y = block.rect.y + random.randrange(6, 13)
                    pebbles.add(pebble)

    # ~ CONTAINING GRASS PLACEMENT ~ #

    # ~ Although not entirely necessary and can have a downside to performance, this code checks every blade of grass
    #   and ensures that it is not on top of the platforms or suspended in the sky, based on the colours that it is
    #   touching

    for x in range(len(grasses)):
        colours = screen.get_at((grasses.sprites()[x].rect.x + 3, grasses.sprites()[x].rect.y + 12))
        if colours == (161, 150, 31):
            grasses.sprites()[x].kill()
            break
        elif colours == (175, 163, 33):
            grasses.sprites()[x].kill()
            break
        elif colours == (161, 150, 31):
            grasses.sprites()[x].kill()
            break

    # ~ This variable keeps track of how many enemies are alive

    enemyCount = len(enemies)

    # ~ CREATING INSTANCES OF CLASSES THAT ARE NOT DEFINED IN layout ~ #

    # ~ Seeing as the sword follows the player I just need to give it the same coordinates as the player with some
    #   offset so that it appears as though the player is holding it

    sword = Sword()
    swords.add(sword)
    sword.rect.x = player.rect.x + 6
    sword.rect.y = player.rect.x + 6

    # ~ I have created 2 instances of the Background class so that it can continuously move in the background.

    background2 = Background()
    background2.rect.x = 800
    background2.rect.y = 0
    backs.add(background2)

    background1 = Background()
    background1.rect.x = 0
    background1.rect.y = 0

    backs.add(background1)

    # ~ The ring is what follows at the legs of the player so that it is clear where the player's feet are among the
    #   flowers

    ring = Ring()
    rings.add(ring)

    # ~~~~ GAME LOOP ~~~~ #

    run = True
    while run:
        # ~ PYGAME EVENT LOOP ~ #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # ~ Checks the if the event type is a keypress and if so it detects whether the Up, Down, Left or Right
            #   key has been pressed
            # ~ I have decided to do this as an event because other wise the movement can be controlled simultaneously
            #   by pressing down multiple keys at a time
            # ~ Due to the offset of the movement due to the isometric plane, this causes the player to move off course
            #   and can combine velocities to make it move faster in particular directions
            # ~ Having it so that it only takes one directional input at a time combats this issue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Up = True
                    Down = False
                    Left = False
                    Right = False
                elif event.key == pygame.K_DOWN:
                    Down = True
                    Up = False
                    Left = False
                    Right = False
                elif event.key == pygame.K_LEFT:
                    Left = True
                    Up = False
                    Down = False
                    Right = False
                    direction = 1
                elif event.key == pygame.K_RIGHT:
                    Right = True
                    Up = False
                    Down = False
                    Left = False
                    direction = 2
                # ~ If the event key is Space and the player isnt falling (because in that case, the space bar resets
                #   the player from falling) then the boolean jumping variable becomes true
                if event.key == pygame.K_SPACE and notFalling:
                    jumping = True

        # ~JUMPING~ #

        # ~ As explained above, if the jumping variable is true then the vely variable will have 1 constantly taken off
        #   of it so that the player moves up and then when vely is 0 it starts moving back down again.
        # ~ When vely is -10 jumping becomes false as vely is reset to 11
        # ~ The code below that ensures that the player can still move in the air while the player is jumoping

        if jumping:
            vely-= 1
            player.rect.y-=vely
            if vely < -9:
                jumping = False
                vely = 11
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and Right:
                isMoving = player.moving()
                player.moveRight(3)
            if keys[pygame.K_LEFT] and Left:
                isMoving = player.moving()
                player.moveLeft(3)
            if keys[pygame.K_DOWN] and Down:
                isMoving = player.moving()
                player.moveDown(3)
            if keys[pygame.K_UP] and Up:
                isMoving = player.moving()
                player.moveUp(3)

        # ~ THE RING ~ #

        # ~ This code ensures that the ring is constantly at the feet of the player

        ring.rect.x = player.rect.x+5
        ring.rect.y = player.rect.y+43

        # ~ THE BACKGROUND ~ #

        # ~ This constantly moves the background images to the left and once they move off screen, they loop becak to
        #   where they started. This gives the effect that their is a constantly moving, never ending background

        background1.update()
        background2.update()
        if background1.rect.x == -800:
            background1.rect.x = 800
        if background2.rect.x == -800:
            background2.rect.x = 800

        isMoving = False

        # ~ CHECKING IF THE PLAYER SHOULD FALL ~ #

        # ~ If the coordinate of the players feet is the same as the colour of the background, the side of the blocks
        #   or the side of the platform then the player will fall
        # ~ This is ignored when the player is jumping so that if the player touches any of this colours mid air,
        #   it wont just fall

        if notFalling and jumping == False:
            colour = screen.get_at((player.rect.x+20, player.rect.y + 50))
            if colour == (61, 28, 0):
                fallColour = True
                notFalling = False
            if colour == (31, 14, 0):
                fallColour = True
                notFalling = False
            if colour == (179,254,240):
                fallColour = True
                notFalling = False
            if colour == (138,138,138):
                fallColour = True
                notFalling = False
            if colour == (77,77,77):
                fallColour = True
                notFalling = False

        # ~ DECIDING WHETHER THE PLAYER SHOULD FALL, CONTINUED... PLUS DETECTING FOR THE ABILITY TO MOVE ~ #

        # ~ Due to the fact that detecting the colour at the player's feet isn't always 100% reliable, I have added
        #   a check for whether the player is still colliding with any of the blocks, if not it will fall.
        # ~ If the player is colliding with any of the blocks then a movement input will be able to be taken.
        # ~ It checks whether the key has been pressed and if the variable for the direction is True so that it only
        #   takes one input at a time and will then allow the player to move.
        # ~ It will also perform the walking animation for the sword when the player is walking

        if notFalling and jumping == False:
            Block_Collide = pygame.sprite.groupcollide(players, blocks, False, False)
            if Block_Collide and fallColour == False:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT] and Right:
                    isMoving = player.moving()
                    sword.walking()
                    player.moveRight(3)
                if keys[pygame.K_LEFT] and Left:
                    isMoving = player.moving()
                    sword.walking()
                    player.moveLeft(3)
                if keys[pygame.K_DOWN] and Down:
                    isMoving = player.moving()
                    sword.walking()
                    player.moveDown(3)
                if keys[pygame.K_UP] and Up:
                    isMoving = player.moving()
                    sword.walking()
                    player.moveUp(3)
            else:
                notFalling = False
                fallColour = False

        # ~ FALL CHECK ~ #

        # ~ If the fall variable is true and the player is not jumping then the player will fall

        if notFalling == False and jumping == False:
            player.fall()

        # ~ IDLE CHECK ~ #

        # ~ If the player is not moving then it will reset the state of the player and the sword to the original
        #   images so that it is not just frozen at the point that the walking animation finished

        if isMoving == False:
            player.idle()
            sword.reset()

        # ~ FALLING RESET CHECK ~ #

        # ~ If the player is falling and not jumpinmg then it will check for a keyboard input for the space bar.
        # ~ When pressed, the current instance of the player class will be killed and a new one will be created at the
        #   original starting position
        # ~ It will also check if there are any enemies left and if not it will respawn all the enemies along side the
        #   player

        if notFalling == False and jumping == False:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                player.kill()
                notFalling = True
                for col in range(27):
                    for row in range(29):
                        if layout[row][col] == 3:
                            player = Player()
                            player.rect.x = 300 + (col * 32 - row * 32)+random.randrange(20,30)
                            player.rect.y = (col * 10 + row * 10)-random.randrange(20,30)
                            players.add(player)
                        if enemyCount <= 0:
                            if layout[row][col] == 5:
                                enemy = Enemy()
                                enemy.rect.x = 300 + (col * 32 - row * 32)+random.randrange(20,30)
                                enemy.rect.y = (col * 10 + row * 10)-random.randrange(20,30)
                                enemies.add(enemy)
                enemyCount = len(enemies)

        # ~ RANDOM DECORATION ~ #

        # ~ For a 1 in 750 chance every cycle there is a chance that an instance of a cloud will appear and move across
        #   the screen. (there are three different clouds which is also randomly selected)
        randomCloud = random.randint(1, 750)
        if randomCloud == 500:
            cloud = Clouds()
            cloud.selection()
            clouds.add(cloud)
            cloud.rect.x = 800
            cloud.rect.y = random.randint(50, 400)
            isCloud = True

        # ~ For a 1 in 650 chance every cycle, there is a chance that a bird appears and moves across the screen
        #   at a random diagonal velocity

        randomBird = random.randint(1, 650)
        if randomBird == 325:
            bird = Bird()
            birds.add(bird)
            bird.rect.x = 800
            bird.rect.y = random.randint(50,400)
            isBird = True

        # ~ RANDOM DECORATION UPDATES ~ #

        # ~ If a cloud exists then the cloud will move across the screen. If it reaches the end of the screen, it
        #   will be killed

        if isCloud:
            for x in range(len(clouds)):
                clouds.sprites()[x].update()
                if clouds.sprites()[x].rect.x <= -600:
                    clouds.sprites()[x].kill()
                    break

        # ~ If a bird exists then the bird will move across the screen. If it reaches the end of the screen, it
        #   will be killed

        if isBird:
            for x in range(len(birds)):
                birds.sprites()[x].update()
                if birds.sprites()[x].rect.x <= -50:
                    birds.sprites()[x].kill()
                    break

        # ~ SWORD ~ #

        # ~ The sword sprite always follows the player's y positon and constantly checks which way the sword is facing
        #   along the x axis
        # ~ This is checked with the directionCheck() procedure.

        sword.rect.y = player.rect.y + 1

        sword.directionCheck()

        # ~ If right control is pressed then swinging is true

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RCTRL]:
            swinging = True

        # ~ If swinging is true then it checks for a collision with an enemy.
        # ~ If it collides with an enemy while swinging then the healthDecrease method is called on the affected enemy

        if swinging:
            collide_enemy = pygame.sprite.groupcollide(enemies, swords, False, False)
            if collide_enemy:
                hitenemy = list(collide_enemy.keys())[0]
                hitenemy.healthDecrease()
            swung = sword.swing()
            if swung == True:
                swinging = False

        # ~ This checks whether the player is facing right or up and depending on what way, the sword will be
        #   flipped in that direction.

        if Right or Up:
            sword.rect.x = player.rect.x + 5
            sword.Right()

        # ~ This checks whether the player is facing left or down and depending on what way, the sword will be
        #   flipped in that direction.

        if Left or Down:
            sword.rect.x = player.rect.x - 25
            sword.Left()

        # ~ CONSISTENT LAYERING OF SPRITES ~ #

        # ~ The code below constantly checks every grass instance and every flower instance to see fi they are within
        #   an area around the player's feet.
        # ~ If they are within that area then they will be added to the layergrass or layerflower sprite group
        # ~ Otherwise if they are in the group but are not within the area then they will be removed from the
        #   layergrass or layerflower sprite group
        # ~ If they are in either of those groups then they will appear over the player so that it looks like the player
        #   is standing within the grass and flowers. Otherwise they will be drawn behind the player

        for x in range(len(grasses)):
            if grasses.sprites()[x].rect.y > player.rect.y +25 and grasses.sprites()[x].rect.y < player.rect.y + 50 and grasses.sprites()[x].rect.x < player.rect.x +30 and grasses.sprites()[x].rect.x > player.rect.x +10:
                layergrass.add(grasses.sprites()[x])
            elif grasses.sprites()[x] in(layergrass):
                layergrass.remove(grasses.sprites()[x])

        for x in range(len(flowers)):
            if flowers.sprites()[x].rect.y > player.rect.y + 25 and flowers.sprites()[x].rect.y < player.rect.y + 50 and flowers.sprites()[x].rect.x < player.rect.x +30 and flowers.sprites()[x].rect.x > player.rect.x +10:
                layerflower.add(flowers.sprites()[x])
            elif flowers.sprites()[x] in (layerflower):
                layerflower.remove(flowers.sprites()[x])

        # ~ This code checks for the same thing as the flowers and grass however the box is a slightly different size
        #   due to the large size of the enemy sprites
        # ~ This code also checks whether the health has been depleted and if so that sprite will be killed

        for x in range(len(enemies)):

            if enemies.sprites()[x].rect.y+20 > player.rect.y + 25:
                layerenemy.add(enemies.sprites()[x])
            elif enemies.sprites()[x] in (layerenemy):
                layerenemy.remove(enemies.sprites()[x])
            if enemies.sprites()[x].getHealth() == 0:
                enemies.sprites()[x].kill()
                enemyCount-=1
                break

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # ~ THIS CODE IS CURRENTLY IN DEVELOPMENT AND IS NOT FUNCTIONING CORRECTLY AS OF RIGHT NOW
        # ~ YOU CAN CONTINUE READING WORKING CODE BELOW THIS BLOCK

        # It will be to allow for enemies to move around the map without falling off the edges.

            #collide_enemy = pygame.sprite.groupcollide(enemies, platforms, False, False)
            #if collide_enemy:
            #    enemies.sprites()[x].movementCounter()
            #    currentCounter = enemies.sprites()[x].getcounter()
            #    if currentCounter < 30:
            #        directionchoice = enemies.sprites()[x].getdirectionChoice()
            #        if directionchoice == 1:
            #            enemies.sprites()[x].moveUp()
            #        elif directionchoice == 2:
            #            enemies.sprites()[x].moveDown()
            #        elif directionchoice == 3:
            #            enemies.sprites()[x].moveLeft()
            #        elif directionchoice == 4:
            #            enemies.sprites()[x].moveRight()
            #    colour = screen.get_at((enemies.sprites()[x].rect.x + 20, enemies.sprites()[x].rect.y + 50))
            #    if colour == (61, 28, 0):
            #        if directionchoice == 1:
                        #choicesss = [2, 3]
                        #enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveDown()
            #        elif directionchoice == 2:
                        #choicesss = [1, 4]
                        #enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveUp()
            #        elif directionchoice == 3:
                        #choicesss = [2, 4]
                        #enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveRight()
            #        elif directionchoice == 4:
                        #choicesss = [1, 4]
                        #enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveLeft()
                        # enemies.sprites()[x].counterReset()
            #    if colour == (31, 14, 0):
            #        if directionchoice == 1:
                        # choicesss = [2, 3]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveDown()
            #        elif directionchoice == 2:
                        # choicesss = [1, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveUp()
            #        elif directionchoice == 3:
                        # choicesss = [2, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveRight()
            #        elif directionchoice == 4:
                        # choicesss = [1, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveLeft()
                        # enemies.sprites()[x].counterReset()
            #    if colour == (179, 254, 240):
            #        if directionchoice == 1:
                        #choicesss = [2, 3]
                        #enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveDown()
            #        elif directionchoice == 2:
                        #choicesss = [1, 4]
                        #enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveUp()
            #        elif directionchoice == 3:
                        #choicesss = [2, 4]
                        #enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveRight()
            #        elif directionchoice == 4:
                        #choicesss = [1, 4]
                        #enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveLeft()
                        # enemies.sprites()[x].counterReset()
            #    if colour == (255,255,255):
            #        if directionchoice == 1:
                        # choicesss = [2, 3]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveDown()
            #        elif directionchoice == 2:
                        # choicesss = [1, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveUp()
            #        elif directionchoice == 3:
                        # choicesss = [2, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveRight()
            #        elif directionchoice == 4:
                        # choicesss = [1, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveLeft()
            #            # enemies.sprites()[x].counterReset()
            #    if colour == (138, 138, 138):
            #        if directionchoice == 1:
                        # choicesss = [2, 3]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveDown()
            #        elif directionchoice == 2:
                        # choicesss = [1, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveUp()
            #        elif directionchoice == 3:
                        # choicesss = [2, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveRight()
            #        elif directionchoice == 4:
                        # choicesss = [1, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveLeft()
                        # enemies.sprites()[x].counterReset()
                # enemies.sprites()[x].counterReset()
            #    if colour == (77, 77, 77):
            #        if directionchoice == 1:
                        # choicesss = [2, 3]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveDown()
            #        elif directionchoice == 2:
                        # choicesss = [1, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveUp()
            #        elif directionchoice == 3:
                        # choicesss = [2, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveRight()
            #        elif directionchoice == 4:
                        # choicesss = [1, 4]
                        # enemies.sprites()[x].setdirectionChoice(random.choice(choicesss))
            #            enemies.sprites()[x].moveLeft()
                        # enemies.sprites()[x].counterReset()
                # enemies.sprites()[x].counterReset()
            #    if currentCounter > 30:
            #        enemies.sprites()[x].counterReset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # ~ DRAWING ~ #

        backs.draw(screen)

        # ~ If the player isn't falling, the player is layered on top of everything

        if notFalling:
            blocks.draw(screen)
            pebbles.draw(screen)
            grasses.draw(screen)
            flowers.draw(screen)
            enemies.draw(screen)
            rings.draw(screen)

            swords.draw(screen)
            players.draw(screen)

        # ~ If the player is falling it is layered behind everything

        else:
            rings.draw(screen)
            swords.draw(screen)
            players.draw(screen)
            blocks.draw(screen)
            pebbles.draw(screen)
            grasses.draw(screen)
            flowers.draw(screen)
            enemies.draw(screen)

        # ~ These are where the flowers, grass and enemies are drawn if they are at the feet of the player

        layergrass.draw(screen)
        layerflower.draw(screen)
        layerenemy.draw(screen)

        birds.draw(screen)
        clouds.draw(screen)

        # ~ MOUSE ~ #

        # ~ This gets the mouses position, removes it and adds a custom cursor in place of it.

        mousepos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        newcursor = pygame.image.load('isocursor.png')
        newcursor = pygame.transform.scale(newcursor,(15,15))
        newcursor = pygame.transform.rotate(newcursor, -10)
        screen.blit(newcursor,mousepos)


        pygame.display.update()

        clock.tick(60)


game()
