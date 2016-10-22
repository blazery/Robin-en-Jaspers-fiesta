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

    def countBodyPart(self, part):
        eyes = 0
        start_part = self.torso


        for part in start_part.contains:
            if part.part_type == part:
                eyes += 1

            if not part.contains:
                eyes += self.countBodyPart(part)

        return eyes