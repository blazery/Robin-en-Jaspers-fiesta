import Bodypart

class Monster:
    torso = Bodypart.Bodypart("TORSO")

    def calcTotalHP(self, par_hp = torso.hit_points, par_part = torso):
        hp = par_hp

        for part in par_part.contains:
            hp += part.hit_points

            if part.contains != {}:
                hp += self.calcTotalHP(hp, part)

        return hp

    def countEyes(self, par_part = torso):
        eyes = 0

        for part in par_part.contains:
            if part.part_type == "EYES":
                eyes += 1

            if part.contains != {}:
                eyes += self.countEyes(part)

        return eyes