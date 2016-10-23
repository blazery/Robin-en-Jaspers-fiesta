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
        return proto_monster


    def monsterToFile(self, par_monster, file_name):
        text_file = self.recursiveMonsterToFile(par_monster.torso)
        name = file_name.split('.')[0].strip(' ')

        file =open((name + ".mst"), 'w')
        for x in text_file:
            file.writelines(x + "\n")
        file.close()

        for x in text_file:
            print(x)


    def recursiveMonsterToFile(self, par_part, depth_counter = -1):
        text_file = []
        counter = depth_counter + 1
        start_part = par_part

        for temp_part in start_part.contains:
            line = ('   '*counter) + start_part.part_type + '>' + temp_part.part_type
            text_file.append(line)

            text_file += self.recursiveMonsterToFile(temp_part, counter)

        return text_file

    def loadMonsterFile(self, par_path):
        path = par_path.split('.')[0].strip(' ')
        try:
            file = open((path+".mst"), 'r')
        except:
            print("FILE READING ERROR")
            print("MONSTER COULD NOT BE FOUND")
            return

        text = []

        for x in file.readlines():
            temp_text = x.strip(' ').strip("\n")
            text.append(temp_text)

        monster = Monster.Monster()
        try:
            monster.torso = self.recursiveMonsterLoad(monster.torso, text)
        except:
            print("Corrupt file")
        if monster.torso is not None:
            return monster
        else:
            return None

    def recursiveMonsterLoad(self, par_part, text, par_counter = 0):
        monster_part = par_part
        temp = text
        counter = par_counter


        while counter < len(temp):
            items = temp[counter].split('>')
            if items[0]in self.attach_hierarchy.keys(): #skip to next line if incorrect may cause V
                if par_part.part_type == items[0]: # skips back to torso if bodytype lower in hierarchy than parent in text
                    if items[1] in self.attach_hierarchy[items[0]]: # skips to next line if incorrect may cause ^
                        temp_bodyPart = Bodypart.Bodypart(items[1])
                        par_part.contains.append(temp_bodyPart)
                        counter = self.recursiveMonsterLoad(temp_bodyPart, temp, (counter+1))
                        print(counter)

                        if counter is None or type(counter) == type(par_part):
                            return monster_part
                    else:
                        #redesign this else to prevent errors in corrupt files
                        counter += 1
                else:
                    if par_part.part_type != "TORSO":
                        return counter
                    else:
                        counter += 1
            else:
                counter += 1
        print("FILE CORRUPT LOL DIDNT READ")
        return None