import Monster
import Bodypart
import GameData
import FileReader
import MonsterBuilder
import os

class UserInterface:
    def __init__(self):
        self.current_monster = Monster.Monster()
        self.hierarchy_dict = GameData.GameData().monster_hierarchy
        self.curr_selected_part = self.current_monster.torso
        self.counter = {}
        self.index_mapping = {}
        self.index = 1

    def builder(self):
        while True:
            os.system("clear")
            self.resetVars()
            self.graphCurrentMonsterFrom(self.current_monster.torso)
            user_input = self.getUserInput("\n\n[1] Add part\n[2] Select other part\n[3] Delete part\n[4] Save monster\n[5] Exit\n")
            if user_input == 1:
                self.printAddInterface()
            if user_input == 2:
                self.switchCurrentPart()
            if user_input == 4:
                exit()

    def resetVars(self):
        self.counter = {}
        self.index_mapping = {}
        self.index = 1

    def switchCurrentPart(self):
        self.printAllOptions(self.curr_selected_part, 0) #0 stands for parts actually in bodypart
        user_input = self.getUserInput("To what do you want to switch?\n")
        self.curr_selected_part = self.index_mapping[user_input]


    def getUserInput(self, query):
        while True:
            user_input = input(query)
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please input a number")
            else:
                return int(user_input)
    
    def printAddInterface(self):
        self.printAllOptions(self.curr_selected_part, 1) #1 stands for all possibilities
        user_input = self.getUserInput("What do you want to add?\n")
        self.addXtoY(Bodypart.Bodypart(self.index_mapping[user_input]), self.curr_selected_part)

    def printAllOptions(self, part, mode):
        if mode == 1:
            if self.hierarchy_dict[part.part_type] != []:
                for possibility in self.hierarchy_dict[part.part_type]:
                    print("{}".format(self.index), possibility.title())
                    self.index_mapping[self.index] = possibility
                    self.index += 1
            else: #end_point e.g. spike, eye
                print("END_POINT")
        elif mode == 0:
            if part.contains != []:
                for possibility in part.contains:
                    print("{}".format(self.index), possibility.part_type.title())
                    self.index_mapping[self.index] = possibility
                    self.index += 1
            else: #end_point e.g. spike, eye
                print("END_POINT")

    def addXtoY(self, part, receiver):
        receiver.contains.append(part)

    def graphCurrentMonsterFrom(self, current,  layer =  0):
        layer += 1
        if current.part_type == "TORSO" and current.part_type == self.curr_selected_part.part_type:
            print("*Torso*")
        for part in current.contains:
            if layer in self.counter.keys():
                self.counter[layer] += 1
            else:
                self.counter[layer] = 1
            if current.part_type == self.curr_selected_part.part_type and layer != 1:
                print(('\n' if layer == 1 else ''), ' ' * layer, layer, '.', self.counter[layer], " *", ((part.part_type.title()) if (part.part_type[-1:] == 'T') else (part.part_type[:-1].title())), "* ", sep='')
            else:
                print(('\n' if layer == 1 else ''), ' ' * layer, layer, '.', self.counter[layer], ' ', ((part.part_type.title()) if (part.part_type[-1:] == 'T') else (part.part_type[:-1].title())), sep='')

            if part.contains != []:
                self.graphCurrentMonsterFrom(part, layer)
