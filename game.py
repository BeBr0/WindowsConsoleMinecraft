import os
import random
import time
from colorama import Back, Fore


class Player:
    EntityPlayer = None

    def __init__(self, hp, name, posX, posY, world):
        if type(hp) == int and type(name) == str and type(posX) == int and type(posY) == int and \
                isinstance(world, World):
            self.hp = hp
            self.name = name
            self.posX = posX
            self.posY = posY
            self.world = world
            self.isDead = False
            self.inventory = {}
            self.chosenItem = None

            Player.EntityPlayer = self

            world.worldArray[posY][posX] = Back.RED + " "
            world.update_console()

    def move_player(self, direction):
        self.world.worldArray[self.posY][self.posX] = Back.LIGHTBLUE_EX + " "
        if direction == 'r':
            if self.posX + 1 < self.world.width:
                if ' ' in self.world.worldArray[self.posY][self.posX + 1]:
                    self.posX += 1
                elif ' ' in self.world.worldArray[self.posY - 1][self.posX + 1] and self.posY - 1 >= 0:
                    self.posY -= 1
                    self.posX += 1

        elif direction == 'u':
            if ' ' in self.world.worldArray[self.posY - 1][self.posX]:
                if self.posY - 1 >= 0:
                    self.posY -= 1

        elif direction == 'l':
            if ' ' in self.world.worldArray[self.posY][self.posX - 1]:
                if self.posX - 1 >= 0:
                    self.posX -= 1

            elif ' ' in self.world.worldArray[self.posY - 1][self.posX - 1] and self.posY - 1 >= 0:
                self.posY -= 1
                self.posX -= 1

        elif direction == 'd':
            if self.posY + 1 < self.world.height:
                if ' ' in self.world.worldArray[self.posY + 1][self.posX]:
                    self.posY += 1

        self.world.worldArray[self.posY][self.posX] = Back.RED + " "
        self.world.update_console()

    def break_block(self, direction):
        if direction == 'r':
            if ' ' not in self.world.worldArray[self.posY][self.posX + 1]:
                if self.world.worldArray[self.posY][self.posX + 1] in self.inventory.keys():
                    self.inventory[self.world.worldArray[self.posY][self.posX + 1]] += 1
                else:
                    self.inventory[self.world.worldArray[self.posY][self.posX + 1]] = 1
                self.world.worldArray[self.posY][self.posX + 1] = Back.LIGHTBLUE_EX + " "

            elif ' ' not in self.world.worldArray[self.posY][self.posX + 2]:
                if self.world.worldArray[self.posY][self.posX + 2] in self.inventory.keys():
                    self.inventory[self.world.worldArray[self.posY][self.posX + 2]] += 1
                else:
                    self.inventory[self.world.worldArray[self.posY][self.posX + 2]] = 1
                self.world.worldArray[self.posY][self.posX + 2] = Back.LIGHTBLUE_EX + " "

        elif direction == 'l':
            if ' ' not in self.world.worldArray[self.posY][self.posX - 1]:
                if self.world.worldArray[self.posY][self.posX - 1] in self.inventory.keys():
                    self.inventory[self.world.worldArray[self.posY][self.posX - 1]] += 1
                else:
                    self.inventory[self.world.worldArray[self.posY][self.posX - 1]] = 1
                self.world.worldArray[self.posY][self.posX - 1] = Back.LIGHTBLUE_EX + " "

            elif ' ' not in self.world.worldArray[self.posY][self.posX - 2]:
                if self.world.worldArray[self.posY][self.posX - 2] in self.inventory.keys():
                    self.inventory[self.world.worldArray[self.posY][self.posX - 2]] += 1
                else:
                    self.inventory[self.world.worldArray[self.posY][self.posX - 2]] = 1
                self.world.worldArray[self.posY][self.posX - 2] = Back.LIGHTBLUE_EX + " "

        elif direction == 'u':
            if ' ' not in self.world.worldArray[self.posY - 1][self.posX]:
                if self.world.worldArray[self.posY - 1][self.posX] in self.inventory.keys():
                    self.inventory[self.world.worldArray[self.posY - 1][self.posX]] += 1
                else:
                    self.inventory[self.world.worldArray[self.posY - 1][self.posX]] = 1
                self.world.worldArray[self.posY - 1][self.posX] = Back.LIGHTBLUE_EX + " "

            elif ' ' not in self.world.worldArray[self.posY - 2][self.posX]:
                if self.world.worldArray[self.posY - 2][self.posX] in self.inventory.keys():
                    self.inventory[self.world.worldArray[self.posY - 2][self.posX]] += 1
                else:
                    self.inventory[self.world.worldArray[self.posY - 2][self.posX]] = 1
                self.world.worldArray[self.posY - 2][self.posX] = Back.LIGHTBLUE_EX + " "

        elif direction == 'd':
            if self.posY + 1 >= self.world.height:
                return
            if ' ' not in self.world.worldArray[self.posY + 1][self.posX]:
                if self.world.worldArray[self.posY + 1][self.posX] in self.inventory.keys():
                    self.inventory[self.world.worldArray[self.posY + 1][self.posX]] += 1
                else:
                    self.inventory[self.world.worldArray[self.posY + 1][self.posX]] = 1
                self.world.worldArray[self.posY + 1][self.posX] = Back.LIGHTBLUE_EX + " "

            else:
                return

        self.world.update_console()

    def place_block(self, direction):
        if direction == 'l':
            if ' ' in self.world.worldArray[self.posY][self.posX - 1]:
                if self.inventory[self.chosenItem] > 0:
                    self.world.worldArray[self.posY][self.posX - 1] = self.chosenItem
                    self.inventory[self.chosenItem] -= 1
        elif direction == 'u':
            if ' ' in self.world.worldArray[self.posY - 1][self.posX]:
                if self.inventory[self.chosenItem] > 0:
                    self.world.worldArray[self.posY - 1][self.posX] = self.chosenItem
                    self.inventory[self.chosenItem] -= 1
        elif direction == 'r':
            if ' ' in self.world.worldArray[self.posY][self.posX + 1]:
                if self.inventory[self.chosenItem] > 0:
                    self.world.worldArray[self.posY][self.posX + 1] = self.chosenItem
                    self.inventory[self.chosenItem] -= 1
        elif direction == 'd':
            if self.inventory[self.chosenItem] > 0:
                self.move_player('u')
                self.world.worldArray[self.posY + 1][self.posX] = self.chosenItem
                self.inventory[self.chosenItem] -= 1

        self.world.update_console()

    def damage_player(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.death()

    def death(self):
        self.world.worldArray = [
            ['░██████╗░░█████╗░███╗░░░███╗███████╗        ░█████╗░██╗░░░██╗███████╗██████╗░'],
            ['██╔════╝░██╔══██╗████╗░████║██╔════╝        ██╔══██╗██║░░░██║██╔════╝██╔══██╗'],
            ['██║░░██╗░███████║██╔████╔██║█████╗░░        ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝'],
            ['██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░        ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗'],
            ['╚██████╔╝██║░░██║██║░╚═╝░██║███████╗        ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║'],
            ['░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝        ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝']]

        self.world.update_console()
        self.isDead = True


class World:

    def __init__(self, height, width, is_flat):
        if type(height) == int and type(width) == int and type(is_flat) == bool:
            self.height = height
            self.width = width
            self.isFlat = is_flat

            self.worldArray = []

            if is_flat:
                for i in range(height):
                    self.worldArray.append([])
                    for j in range(width):
                        if i < 2 / 3 * self.height:
                            self.worldArray[-1].append(Back.LIGHTBLUE_EX + " ")

                        elif i < 2 / 3 * self.height + 1:
                            self.worldArray[-1].append(Back.GREEN + Fore.GREEN + "D")

                        else:
                            self.worldArray[-1].append(Back.LIGHTBLACK_EX + Fore.LIGHTBLACK_EX + "S")

                number_of_tress = random.randint(0, 10)
                for i in range(number_of_tress):
                    x = random.randint(1, width - 1)
                    self.draw_tree_at_point(int(2/3 * height), x)
                self.update_console()

    def draw_tree_at_point(self, point_y, point_x, height=3):
        for i in range(height):
            if point_y - i >= 0:
                self.worldArray[point_y - i][point_x] = Back.LIGHTYELLOW_EX + Fore.LIGHTYELLOW_EX + "W"
            else:
                break

        if point_y - height >= 0:
            self.worldArray[point_y - height][point_x] = Back.GREEN + Fore.GREEN + "L"
        if point_y - height >= 0 and point_x < self.width:
            self.worldArray[point_y - height][point_x + 1] = Back.GREEN + Fore.GREEN + "L"
        if point_y - height >= 0 and point_x - 1 >= 0:
            self.worldArray[point_y - height][point_x - 1] = Back.GREEN + Fore.GREEN + "L"
        if 0 < point_y - height + 1 < self.height and point_x + 1 < self.width:
            self.worldArray[point_y - height + 1][point_x + 1] = Back.GREEN + Fore.GREEN + "L"
        if point_y - height + 1 >= 0 and point_x - 1 >= 0:
            self.worldArray[point_y - height + 1][point_x - 1] = Back.GREEN + Fore.GREEN + "L"
        if point_y - height + 1 >= 0 and point_x + 2 < self.width:
            self.worldArray[point_y - height + 1][point_x + 2] = Back.GREEN + Fore.GREEN + "L"
        if point_y - height + 1 >= 0 and point_x - 2 >= 0:
            self.worldArray[point_y - height + 1][point_x - 2] = Back.GREEN + Fore.GREEN + "L"

    def physics(self):
        if Player.EntityPlayer.posY + 1 >= self.height:
            return
        if Player.EntityPlayer.isDead:
            return
        ctr = 0
        while ' ' in self.worldArray[Player.EntityPlayer.posY + 1][Player.EntityPlayer.posX]:
            Player.EntityPlayer.move_player('d')
            ctr += 1

            if Player.EntityPlayer.posY + 1 >= self.height:
                return
            if ' ' in self.worldArray[Player.EntityPlayer.posY + 1][Player.EntityPlayer.posX]:
                time.sleep(1 / 20)

        if ctr > 3:
            Player.EntityPlayer.damage_player(ctr - 3)

    def update_console(self):
        os.system('cls')
        for string in self.worldArray:
            for char in string:
                print(char, end="")

            print(Back.RESET)

        if Player.EntityPlayer is not None:
            for item in Player.EntityPlayer.inventory:
                if 'D' in item:
                    if item == Player.EntityPlayer.chosenItem:
                        print('Dirt: ' + str(Player.EntityPlayer.inventory[item]) + ' - CHOSEN')
                    else:
                        print('Dirt: ' + str(Player.EntityPlayer.inventory[item]))

                if 'S' in item:
                    if item == Player.EntityPlayer.chosenItem:
                        print('Stone: ' + str(Player.EntityPlayer.inventory[item]) + ' - CHOSEN')
                    else:
                        print('Stone: ' + str(Player.EntityPlayer.inventory[item]))

                if 'W' in item:
                    if item == Player.EntityPlayer.chosenItem:
                        print('Wood: ' + str(Player.EntityPlayer.inventory[item]) + ' - CHOSEN')
                    else:
                        print('Wood: ' + str(Player.EntityPlayer.inventory[item]))

                if 'L' in item:
                    if item == Player.EntityPlayer.chosenItem:
                        print('Leave: ' + str(Player.EntityPlayer.inventory[item]) + '- CHOSEN')
                    else:
                        print('Leave: ' + str(Player.EntityPlayer.inventory[item]))
