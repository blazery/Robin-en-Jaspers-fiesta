
class MonsterCreationView():

    def __init__(self):
        self.viewLoop = True
        self.monsterList = None
        self.selected = 0


    def Go(self, monster):
        while self.viewLoop:

            self.ShowMonster(monster.torso)
            user_input = input()
            user_input - user_input.split(' ')

            if len(user_input) == 2:
                if user_input[0] == "select" or user_input[0] == "sel":
                    if user_input[1].isDigit():
                        if user_input[1] >= 0 and user_input[1] < len(self.monsterList):
                            self.selected = user_input[1]
                            





    def ShowMonster(self, par_part):
        self.monsterList = self.MonsterToList(par_part)

        x = 0
        while x < len(self.monsterList):
            if x == self.selected:
                print(str(x) + " *" + self.monsterList[x] + "*")
            else:
                print(str(x) + self.monsterList[x])
            x += 1

    def MonsterToList(self, par_part, depth =0):
        monsterPart = par_part
        textList = list()


        textList.append('   '*depth + "<" + par_part.part_type + ">")
        for part in monsterPart.contains:

            if part.contains != {}:
                textList += self.MonsterToList(part, (depth + 1))

        return textList