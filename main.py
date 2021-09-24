import msvcrt

import game

world = game.World(20, 100, True)
player = game.Player(20, 'BeBr0', 14, 13, world)
gameOver = False

while not gameOver:
    if player.isDead:
        gameOver = True

    char = ord(msvcrt.getch())
    # Движение игрока
    if char == 100:
        player.move_player('r')
    elif char == 97:
        player.move_player('l')
    elif char == 119 or char == 32:
        player.move_player('u')

    # Разрушение блоков
    elif char == 80:
        player.break_block('d')
    elif char == 77:
        player.break_block('r')
    elif char == 75:
        player.break_block('l')
    elif char == 72:
        player.break_block('u')

    # Выбор блока
    elif char == 49:
        if len(player.inventory) > 0:
            player.chosenItem = list(player.inventory.keys())[0]
            world.update_console()
    elif char == 50:
        if len(player.inventory) > 1:
            player.chosenItem = list(player.inventory.keys())[1]
            world.update_console()
    elif char == 51:
        if len(player.inventory) > 2:
            player.chosenItem = list(player.inventory.keys())[2]
            world.update_console()
    elif char == 52:
        if len(player.inventory) > 3:
            player.chosenItem = list(player.inventory.keys())[3]
            world.update_console()
    elif char == 53:
        if len(player.inventory) > 0:
            player.chosenItem = list(player.inventory.keys())[4]
            world.update_console()
    elif char == 54:
        if len(player.inventory) > 0:
            player.chosenItem = list(player.inventory.keys())[5]
            world.update_console()

    # Установка блоков
    elif char == 65:
        player.place_block('l')
    elif char == 68:
        player.place_block('r')
    elif char == 87:
        player.place_block('u')
    elif char == 83:
        player.place_block('d')

    world.physics()

print('Press any button to exit')
msvcrt.getch()
