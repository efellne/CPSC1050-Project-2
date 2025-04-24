"""
Author:         Eli Fellner
Date:           4/24/2025
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    25

Program to run an rpg
"""
import time

# Class for all of the map functions
class Map():
    def __init__(self):
        self.map = [[],[],[],[],[],[],[],[],[]]
    
    # creates a new map
    def createMap(self):
        self.map[0] = [['/','-','-','-','-','-','-','-','\\'],
                       ['|',' ',' ','|','W','|',' ',' ','|'],
                       ['|',' ',' ','|',' ','|',' ',' ','|'],
                       ['|',' ',' ','|',' ','|',' ',' ','|'],
                       ['|','-','-','-','E','-','-','-','|'],
                       ['|',' ',' ','|',' ','|',' ',' ','|'],
                       ['|',' ',' ','|',' ','|',' ',' ','|'],
                       ['|',' ',' ','|',' ','|',' ',' ','|'],
                       ['\\','-','-','-','T','-','-','-','/']]
        self.map[1] = [['/','-','-','-','-','-','-','-','\\'],
                       ['|',' ',' ',' ',' ','|',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ','|',' ',' ','T'],
                       ['|',' ',' ','-','-','-','-','-','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['\\','-','-','-','T','-','-','-','/']]
        self.map[2] = [['/','-','-','-','-','-','-','-','\\'],
                       ['|',' ',' ',' ',' ',' ',' ','I','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['T',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['\\','-','-','-','T','-','-','-','/']]
        self.map[3] = [['/','-','-','-','T','-','-','-','\\'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','T'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['\\','-','-','-','T','-','-','-','/']]
        self.map[4] = [['/','-','-','-','T','-','-','-','\\'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ','-',' ','E',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['T',' ',' ',' ',' ',' ','-',' ','T'],
                       ['|',' ',' ','E',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['\\','-','-','-','T','-','-','-','/']]
        self.map[5] = [['/','-','-','-','T','-','-','-','\\'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['T',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['\\','-','-','-','T','-','-','-','/']]
        self.map[6] = [['/','-','-','-','T','-','-','-','\\'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|','-','-','-','-','-','-',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ','-','-','-','-','-','-','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|','-','-','-','-','-','-',' ','|'],
                       ['|','I',' ',' ',' ',' ',' ',' ','|'],
                       ['\\','-','-','-','-','-','-','-','/']]
        self.map[7] = [['/','-','-','-','T','-','-','-','\\'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|','-','-','-','I','-','-','-','|'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ','P',' ',' ',' ','|'],
                       ['\\','-','-','-','-','-','-','-','/']]
        self.map[8] = [['/','-','-','-','T','-','-','-','\\'],
                       ['|',' ',' ',' ',' ',' ',' ',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ','-','|'],
                       ['|',' ',' ',' ',' ',' ','|',' ','|'],
                       ['|',' ','-','-','-',' ','|',' ','|'],
                       ['|',' ',' ',' ',' ',' ','|',' ','|'],
                       ['|',' ',' ',' ',' ',' ','|',' ','|'],
                       ['|',' ',' ',' ',' ',' ',' ','I','|'],
                       ['\\','-','-','-','-','-','-','-','/']]

    # prints out the map with a space between each cell
    def printMap(self,currentRoom):
        for i in range(9):
            for j in range(9):
                print(self.map[currentRoom][i][j], end=' ')
            print()
    
    # makes sure that a move is allowed
    def validateMove(self, player, movement):
        newPosition = [player.position[0] + movement[0],player.position[1] + movement[1],player.position[2] + movement[2]]
        if self.map[newPosition[0]][newPosition[1]][newPosition[2]] == ' ':
            self.map[player.position[0]][player.position[1]][player.position[2]] = ' '
            player.changePosition(newPosition)
            self.map[newPosition[0]][newPosition[1]][newPosition[2]] = 'P'
        elif self.map[newPosition[0]][newPosition[1]][newPosition[2]] == 'T':
            self.map[player.position[0]][player.position[1]][player.position[2]] = ' '
            if movement[1] == 1:
                newPosition = [player.position[0]+3, 1, 4]
                player.changePosition(newPosition)
            elif movement[1] == -1:
                newPosition = [player.position[0]-3, 7, 4]
                player.changePosition(newPosition)
            elif movement[2] == 1:
                newPosition = [player.position[0]+1, 4, 1]
                player.changePosition(newPosition)
            elif movement[2] == -1:
                newPosition = [player.position[0]-1, 4, 7]
                player.changePosition(newPosition)
            self.map[newPosition[0]][newPosition[1]][newPosition[2]] = 'P'
        else:
            print('Invalid movement')
        return 0
    
    # returns what is in a tile
    def checkTile(self, position, direction):
        return self.map[position[0]+direction[0]][position[1]+direction[1]][position[2]+direction[2]]

    #changes what is in a tile
    def changeTile(self, tile, change):
        self.map[tile[0]][tile[1]][tile[2]] = change
    
# all purpose class for stats and other stuff
class Entity():
    def __init__(self, position, health, strength, name, inventory):
        self.position = position
        self.health = health
        self.strength = strength
        self.name = name
        self.inventory = inventory

    def attack(self):
        print(f'{self.name} attacks for {self.strength} damage')
        return self.strength
    
    def damage(self, damage):
        self.health -= damage
    
    # adds an item to the inventory and adjusts stats
    def addToInventory(self, item):
        self.inventory.append(item)
        self.health += item.health
        self.strength += item.strength
        print(item)
    
    # makes sure dropped items have the right position
    def dropItem(self):
        self.inventory[0].changePosition(self.position)
    
    def changePosition(self, newPosition):
        self.position = newPosition
    
    def __str__(self):
        return self.name

# class for items, uses mostly the entity class stuff but without an inventory
class Item(Entity):
    def __init__(self, position, health, strength, name):
        self.position = position
        self.health = health
        self.strength = strength
        self.name = name
    
    # new string method
    def __str__(self):
        return f'{self.name}\nStrength + {self.strength}\nHealth + {self.health}'

# does all of the end of turn attacks
def endOfTurn(position, monsters, player):
    for i in monsters:
        if [i.position[0],i.position[1]+1,i.position[2]] == position or [i.position[0],i.position[1]-1,i.position[2]] == position or [i.position[0],i.position[1],i.position[2]+1] == position or [i.position[0],i.position[1],i.position[2]-1] == position:
            player.damage(i.attack())

# almost all of the inputs go through this except fo quit
def inputValidation(map, player, c, monsters, items):

    # checks if you want help first and then checks the number of inputs
    if c[0] == 'help':
        print('You can input: help, move, attack, inspect, pickup or quit.\n Format is: action direction repetitions.\n Repetitions defaults to 1 if it is not included.\n Quit and help do not need direction')
    elif len(c) < 2:
        print('please input at least two words')
    else:

        # assigns c1, c2 and c3 to the input stuff
        c1 = c[0]
        try:
            if c[1] == 'up':
                c2 = [0,-1,0]
            elif c[1] == 'down':
                c2 = [0,1,0]
            elif c[1] == 'left':
                c2 = [0,0,-1]
            elif c[1] == 'right':
                c2 = [0,0,1]
            else:
                raise ValueError('Invalid direction')
        except ValueError as e:
            print(f'{e}, defaulting to down')
            c2 = [0,1,0]
        heading = [player.position[0] + c2[0],player.position[1] + c2[1],player.position[2] + c2[2]]
        if len(c) == 2:
            c3 = 1
        else:
            try:
                if int(c[2]) < 1:
                    raise TypeError()
                c3 = int(c[2])
            except:
                print(f'{c[2]} is not a valid number, setting to default')
                c3 = 1

        # loop for actions
        for i in range(c3):

            # checks which action you want to do and performs it
            if c1 == 'move':
                map.validateMove(player, c2)
            elif c1 == 'attack':
                if map.checkTile(player.position, c2) == 'E':
                    for i in monsters:
                        if i.position == heading:
                            i.damage(player.attack())
                            if i.health <= 0:
                                map.changeTile(i.position, 'I')
                                i.dropItem()
                                items.append(i.inventory[0])
                                player.health += 3
                                monsters.remove(i)
                                print(f'You have killed {i}')
                            break
            elif c1 == 'inspect':
                if map.checkTile(player.position, c2) == 'E':
                    for i in monsters:
                        if i.position == heading:
                            print(i)
                            break
                elif map.checkTile(player.position, c2) == 'I':
                    for i in items:
                        if i.position == heading:
                            print(i)
                            break
                elif map.checkTile(player.position, c2) == ' ':
                    print('There is nothing there')
                else:
                    print('This is a wall')
            elif c1 == 'pickup':
                if map.checkTile(player.position, c2) == 'I':
                    for i in items:
                        if i.position == heading:
                            player.addToInventory(i)
                            map.changeTile(heading, ' ')
                            items.remove(i)
                            break
                else:
                    print('There is nothing to pick up')
            
            # prints the map of your room now updated for your actions
            map.printMap(player.position[0])
            print(f'Health: {player.health}, Strength: {player.strength}')
            endOfTurn(player.position, monsters, player)

            # time between actions for you to see what happened
            time.sleep(0.5)

# a class made to easily copy paste enemies
class Enemy(Entity):
    def __init__(self, health, strength, name, inventory):
        self.health = health
        self.strength = strength
        self.name = name
        self.inventory = inventory
    
    def createEnemy(self, position, map):
        map.changeTile(position, 'E')
        return Entity(position, self.health, self.strength, self.name, self.inventory)

# main
def main():

    # map creation and prints title
    map = Map()
    map.createMap()
    map.printMap(7)
    print('THE QUEST FOR WATERMELON')

    # monster base creation
    slime = Enemy(3, 1, 'Slime', [Item([0,0,0],3,0,'Slime Jelly')])
    goblin = Enemy(6,1, 'Goblin', [Item([0,0,0],0,1, 'Stick Sharpener')])
    wolf = Enemy(10,2, 'Wolf', [Item([0,0,0],1,1, 'Wolf Fang')])

    # all of the monsters in the game
    monsters = [Entity([0,4,4], 50, 4, 'Big boss dude', [Item([0,4,4], 0, 0, 'Prize')]), slime.createEnemy([4,2,4], map), slime.createEnemy([4,5,3], map), slime.createEnemy([5,2,2], map), slime.createEnemy([5,2,3], map), slime.createEnemy([5,2,4], map), slime.createEnemy([5,2,6], map), slime.createEnemy([5,4,4], map), slime.createEnemy([5,5,5], map), slime.createEnemy([5,7,5], map), 
                goblin.createEnemy([8,7,6], map), goblin.createEnemy([8,3,7], map), goblin.createEnemy([8,5,4], map), goblin.createEnemy([8,3,4], map), goblin.createEnemy([1,7,7], map), goblin.createEnemy([1,6,7], map), goblin.createEnemy([1,3,2], map), goblin.createEnemy([1,3,6], map),
                wolf.createEnemy([6,7,2], map), wolf.createEnemy([6,7,4], map), wolf.createEnemy([6,7,6], map), wolf.createEnemy([6,5,2], map), wolf.createEnemy([6,5,4], map), wolf.createEnemy([6,5,6], map), wolf.createEnemy([6,3,2], map), wolf.createEnemy([6,3,4], map), wolf.createEnemy([6,3,6], map), wolf.createEnemy([2,1,5], map), wolf.createEnemy([2,1,6], map), wolf.createEnemy([2,2,7], map), wolf.createEnemy([2,3,7], map), wolf.createEnemy([2,4,4], map)]
    
    # all of the items that start on the ground. Stuff is added when an enemy dies
    items = [Item([7,5,4], 0, 2, 'Big Stick'), Item([8,7,7], 15, 1, 'Really Good Shield'), Item([6,7,1], 0, 20, 'A BIG sword'), Item([2,1,7], 30, 0, 'Bucket of health')]
    
    # dictionary for final action count
    actions = {'help': 0, 'move': 0, 'attack': 0, 'inspect': 0, 'pickup': 0, 'unknown': 0}
    total = 0
    win = False

    # makes the player
    player = Entity([7,7,4],10,0,'Player',[])
    print('Make sure to read the README file first, it gives instructions on how to play the game')
    choice = input().strip().lower().split(' ')

    # gameplay loop
    while not choice[0] == 'quit':

        # validates inputs
        inputValidation(map, player, choice, monsters, items)

        # counts each action
        if choice[0] in actions:
            actions[choice[0]] += 1
        else:
            actions['unknown'] += 1

        # checks if you have won or died
        if map.checkTile([player.position[0],player.position[1],player.position[2]], [0,-1,0]) == 'W':
            win = True
            break
        if player.health <= 0:
            break
        choice = input().strip().lower().split(' ')
    
    # congratulates you for winning and writes the data to a txt file
    if win:
        print('Congratulations, you retrieved the watermelon. The number of each of your inputs has been put into a txt file')
        with open('results.txt', 'w') as f:
            for key, value in actions.items:
                f.write(f'{key}: {value}\n')
                total += value
            f.write(f'Total: {total}')
    elif player.health <= 0:
        print('You have died')

if __name__ == "__main__":
    main()