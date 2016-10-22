import Monster
import Bodypart
import GameData

class MonsterBuilder:
    template = None
    attach_hierarchy = {}

    def __init__(self, attributes):
        self.template = attributes
        self.attach_hierarchy = GameData.GameData().loadHierarchy("MonsterHierarchy.txt")

    def buildMonster(self):
        proto_monster = Monster.Monster()
        for entry in self.template:
            if entry in self.attach_hierarchy.keys():
                for i in range(self.template[entry]):
                    print("Entry: ", entry)
                    proto_monster.torso.contains[entry + str(i)] = Bodypart.Bodypart(entry)
           # elif entry in self.attach_hierarchy["ARMS"]:
           #     proto_monster.torso["ARMS"][entry] = self.template[entry]
        return proto_monster
