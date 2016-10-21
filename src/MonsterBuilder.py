import Monster

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
                proto_monster.torso.append[entry] =  self.template[entry]
            elif entry in self.attach_hierarchy["ARMS"]:
                proto_monster.torso["ARMS"].append({entry : self.template[entry]})
        return proto_monster
