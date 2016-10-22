import Bodypart

class Monster:

    def __init__(self):
        self.torso = Bodypart.Bodypart("TORSO")



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