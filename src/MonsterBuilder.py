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
        self.placed = {}

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
                if hierarchy_part in self.slots.keys(): #this would mean its not connected to torso
                    if  hierarchy_part in self.attach_hierarchy["TORSO"]:

                        amount = math.ceil(self.template[hierarchy_part] / (self.slots[hierarchy_part] + 1))
                        for i in range(amount):
                            if self.placed[hierarchy_part] < self.template[hierarchy_part]:
                                body_part.contains.append(Bodypart.Bodypart(hierarchy_part))
                                self.placed[hierarchy_part] += 1
                    else:
                        amount =math.ceil( self.template[hierarchy_part] / self.slots[hierarchy_part])
                        for i in range(amount):
                            if self.placed[hierarchy_part] < self.template[hierarchy_part]:
                                body_part.contains.append(Bodypart.Bodypart(hierarchy_part))
                                self.placed[hierarchy_part] += 1

                else:
                    for i in range(self.template[hierarchy_part]):
                        if self.placed[hierarchy_part] < self.template[hierarchy_part]:
                            body_part.contains.append(Bodypart.Bodypart(hierarchy_part))
                            self.placed[hierarchy_part] += 1

        for temp_part in body_part.contains:
            self.recursiveBuild(temp_part)

    def buildMonster(self):
        proto_monster = Monster.Monster()
        self.calcSpaceForBP()

        for x in self.template.keys():
            self.placed[x] = 0

        self.recursiveBuild(proto_monster.torso)




        #for body_part in self.template:
            #if not body_part in self.slots.keys():
                ##if not self.template[body_part] == 0:
                    #for i in range(self.template[body_part]):
                        #proto_monster.torso.contains[body_part[:-1].lower() + str(i + 1)] = Bodypart.Bodypart(body_part)

        #for entry in self.template:
            #if entry in self.attach_hierarchy["TORSO"]:
                #for i in range(self.template[entry]):
                    #proto_monster.torso.contains[entry + str(i)] = Bodypart.Bodypart(entry)
            #for torso_part in self.attach_hierarchy["TORSO"]:
                #for i in range(self.template[entry]):
                    #if entry in self.attach_hierarchy[torso_part] and torso_part in self.template.keys():
                        #proto_monster.torso.contains
        return proto_monster


