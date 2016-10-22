import Bodypart
import os
import GameData

class UserInterface:
    def __init__(self):
        self.current_monster = Bodypart.Bodypart("TORSO")
        self.hierarchy_dict = GameData.GameData().monster_hierarchy

    def builder(self):
        print("\n\nThis you can add: \n")
        self.index = 1
        self.mappe = {}
        for i in self.hierarchy_dict.values():
            for j in i:
                self.mappe[j] = {j : self.index}
                self.index += 1
        while True:
            print(self.current_monster.part_type)
            for bodypart in self.current_monster.contains:
                print("  {}".format(bodypart.part_type))
                for bodypartspart in bodypart.contains:
                    print("  {}".format(bodypartspart.part_type))

            self.printAllOptions()
            self.add(input("What do you want to add?:\n"))
            os.system("clear")

    def printAllOptions(self):
        for possibility in self.hierarchy_dict[self.current_monster.part_type]:
            print("{:3}: {}".format(self.mappe[possibility][possibility], possibility), sep='\t', end=' ')
            for x in self.current_monster.contains:
                for second_layer in self.hierarchy_dict[possibility]:
                    if possibility in x.part_type:
                        print("{:3}: {}".format(self.index, second_layer), sep='\t', end=' ')
            print('\n')
        print('\n')

    def add(self, index):
        index = int(index)
        if index == 1:
            self.current_monster.contains.append(Bodypart.Bodypart("ARMS"))
        elif index == 2:
            self.current_monster.contains.append(Bodypart.Bodypart("LEGS"))
        elif index == 3:
            self.current_monster.contains.append(Bodypart.Bodypart("NECKS"))
        elif index == 4:
            self.current_monster.contains.append(Bodypart.Bodypart("TAILS"))
        elif index == 5:
            self.current_monster.contains.append(Bodypart.Bodypart("WINGS"))
        elif index == 6:
            self.current_monster.contains.append(Bodypart.Bodypart("TENTACLES"))
