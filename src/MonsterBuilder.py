import math
import Monster
import Bodypart
import GameData

class MonsterBuilder:



    def __init__(self, attributes):
        self.template = attributes
        self.attach_hierarchy = GameData.GameData().monster_hierarchy
        self.slots = {}
        self.proto_monster = None

    def calcSpaceForBP(self):
        for hierarchy_part in self.attach_hierarchy:
            for template_part in self.template.keys():
                if template_part in self.attach_hierarchy[hierarchy_part]:
                    if hierarchy_part != "TORSO":
                        if hierarchy_part in self.template.keys():
                            if template_part in self.slots.keys():
                                self.slots[template_part] += self.template[hierarchy_part]
                            else:
                                self.slots[template_part] = self.template[hierarchy_part]
                        else:
                            if not template_part in self.slots.keys():
                                self.slots[template_part] = 0

    def recursiveBuild(self, body_part):
        for hierarchy_part in self.attach_hierarchy[body_part.part_type]:
            if hierarchy_part in self.template.keys():
                if (not hierarchy_part in self.attach_hierarchy["TORSO"]) and (self.not_in_torso(hierarchy_part)):
                    if hierarchy_part in self.slots.keys(): #this would mean its not connected to torso
                        amount = math.ceil(self.template[hierarchy_part] / self.slots[hierarchy_part])
                        for i in range(amount):
                            body_part.contains.append(Bodypart.Bodypart(hierarchy_part))
                    else:
                        amount = math.ceil( self.template[hierarchy_part] / self.slots[hierarchy_part] + 1)
                        for i in range(amount):
                            body_part.contains.append(Bodypart.Bodypart(hierarchy_part))
                else:
                    for i in range(self.template[hierarchy_part]):
                        body_part.contains.append(Bodypart.Bodypart(hierarchy_part))


        for temp_part in body_part.contains:
            self.recursiveBuild(temp_part)

    def buildMonster(self):
        proto_monster = Monster.Monster()
        self.calcSpaceForBP()
        self.recursiveBuild(proto_monster.torso)
        return proto_monster

    def not_in_torso(self, hier_part):
        print("Keys to look at: ", self.attach_hierarchy.keys())
        print("checking: ", hier_part)
        blacklist = ["TORSO"]
        for keye, value in self.attach_hierarchy.items():
            print("Key skaljd: ", keye)
            if keye != "TORSO":
                if hier_part in self.attach_hierarchy[keye]:
                    print("shit: ", self.attach_hierarchy[keye])
                    return False
                else: 
                    print("shisasast: ", self.attach_hierarchy[keye])
                    return True
            else:
                continue
