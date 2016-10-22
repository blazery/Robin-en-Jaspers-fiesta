import Monster
import Bodypart

class MonsterBuilder:
    template = None
    attach_hierarchy = {}

    def __init__(self, attributes):
        self.template = attributes
        self.attach_hierarchy["ARMS"] = ["SPIKES", "HANDS"]
        self.attach_hierarchy["LEGS"] = ["SPIKES", "FEET"]
        self.attach_hierarchy["TAILS"] = ["SPIKES"]
        self.attach_hierarchy["WINGS"] = ["SPIKES"]
        self.attach_hierarchy["NECKS"] = {"HEADS" : ["HORNS", "EARS", "NOSES", "EYES","GILLS", {"MOUTHS" : "TEETH"}]}


    def buildMonster(self):
        proto_monster = Monster.Monster()
        for entry in self.template:
            if entry in self.attach_hierarchy.keys():
                print(entry)
                proto_monster.torso[entry] =  {"AMOUNT" : self.template[entry]}
            elif entry in self.attach_hierarchy["ARMS"]:
                proto_monster.torso["ARMS"][entry] = self.template[entry]
        return proto_monster
