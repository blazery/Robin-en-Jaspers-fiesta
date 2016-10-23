import Monster
import GameData
import FileReader
import MonsterBuilder
import os

class UserInterface:
    counter = {}
    def __init__(self):
        template = FileReader.FileReader().readFile("TestTemplate.txt")
        builder = MonsterBuilder.MonsterBuilder(template)
        self.current_monster = builder.buildMonster()
        self.hierarchy_dict = GameData.GameData().monster_hierarchy

    def builder(self):
        print("Current Monster:\n\nTorso")
        self.graphCurrentMonsterFrom(self.current_monster.torso)

    def printAllOptions(self):
        None

    def add(self, index):
        None

    def graphCurrentMonsterFrom(self, current,  layer =  0):
        layer += 1
        for part in current.contains:
            if layer in self.counter.keys():
                self.counter[layer] += 1
            else:
                self.counter[layer] = 1

            print(('\n' if layer == 1 else ''), ' ' * layer, layer, '.', self.counter[layer], ' ', ((part.part_type.title()) if (part.part_type[-1:] == 'T') else (part.part_type[:-1].title())), sep='')

            if part.contains != []:
                self.graphCurrentMonsterFrom(part, layer)
