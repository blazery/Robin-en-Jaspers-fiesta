import Bodypart
import Attack

class Monster:

    def __init__(self):
        self.torso = Bodypart.Bodypart("TORSO")
        self.basic_attacks = {}


    def calcTotalHP(self):
        hp = 0
        par_part = self.torsos


        for part in par_part.contains:
            hp += part.hit_points

            if part.contains != {}:
                hp += self.calcTotalHP()

        return hp

    def countBodyPart(self, part, search):
        count = 0
        start_part = part


        for temp_part in start_part.contains:
            if temp_part.part_type == search:
                count += 1

            count += self.countBodyPart(temp_part, search)

        return count

    def findBodyPart(self, part, search):
        parts = []
        start_part = part

        for temp_part in start_part.contains:
            if temp_part.part_type == search:
                parts.append(temp_part)


            parts += self.findBodyPart(temp_part, search)

        return parts

    def createBasicAttackList(self):
        temp_array = []
        temp_dic = {}
        for x in self.torso.contains:
            temp_array= []
            for y in x.contains:
                if y.part_type == "HANDS" and x.part_type =="ARMS":
                    dmg = (self.countBodyPart(x, "HANDS") + int(self.countBodyPart(x, "SPIKES") * 1.5)
                           + int(self.countBodyPart(x, "CLAWS") * 1.5) - (self.countBodyPart(x,"FINS" ) * 2)
                           + self.countBodyPart(x, "TENTACLES") - self.countBodyPart(x, "EYES"))

                    canAdd = True
                    for z in temp_array:
                        if z.name == "Punch":
                            canAdd = False
                    if canAdd:
                        temp_array.append(Attack.Attack("Punch",dmg, "PHYSICAL", 75))
                if y.part_type == "SPIKES" and x.part_type=="ARMS":
                    dmg = ((self.countBodyPart(x, "SPIKES")*2) + self.countBodyPart(x, "CLAWS")
                           - self.countBodyPart(x, "EYES") - self.countBodyPart(x, "FINS"))

                    canAdd = True
                    for z in temp_array:
                        if z.name == "Stab":
                            canAdd = False
                    if canAdd:
                        temp_array.append(Attack.Attack("Stab", dmg, "PHYSICAL", 90))
                if y.part_type == "HEADS" and x.part_type =="NECKS":
                    dmg = 5
                    for z in y.contains:
                        if z.part_type == "HORNS":
                            dmg += 1
                        if z.part_type == "GILLS":
                            dmg -= 1
                    temp_array.append(Attack.Attack("Headbutt", dmg, "PHYSICAL", 50))
                if y.part_type == "FEET" and x.part_type == "LEGS":
                    dmg = ((self.countBodyPart(x, "SPIKES")*2) + self.countBodyPart(x, "FEET")
                           - self.countBodyPart(x, "FINS") + int(self.countBodyPart(x, "WINGS")*0.5))

                    canAdd = True
                    for z in temp_array:
                        if z.name == "Kick":
                            canAdd = False
                    if canAdd:
                        temp_array.append(Attack.Attack("Kick", dmg, "PHYSICAL", 50))



            if temp_array:
                temp_dic[x] = temp_array

        for x in temp_dic:
            print(x.part_type)
            for y in temp_dic[x]:
                print(y.name)

        return temp_dic
