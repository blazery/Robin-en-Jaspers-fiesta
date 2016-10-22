import Monster
import Bodypart
import GameData

class MonsterBuilder:
    template = None
    attach_hierarchy = {}
    slots = {}

    def __init__(self, attributes):
        self.template = attributes
        self.attach_hierarchy = GameData.GameData().monster_hierarchy
    
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

    def buildMonster(self):
        proto_monster = Monster.Monster()
        for entry in self.template:
            if entry in self.attach_hierarchy["TORSO"]:
                for i in range(self.template[entry]):
                    proto_monster.torso.contains[entry + str(i)] = Bodypart.Bodypart(entry)
            for torso_part in self.attach_hierarchy["TORSO"]:
                for i in range(self.template[entry]):
                    if entry in self.attach_hierarchy[torso_part] and torso_part in self.template.keys():
                        proto_monster.torso.contains
        return proto_monster
