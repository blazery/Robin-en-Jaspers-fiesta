import Monster

class MonsterBuilder:
    template = None

    def __init__(self, attributes):
        self.template = attributes


    def buildMonster(self):
        proto_monster = Monster.Monster()
        proto_monster.torso.append(self.template)
        return proto_monster
