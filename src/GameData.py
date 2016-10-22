class GameData:
    monster_properties = dict()
    monster_hierarchy = dict()

    def __init__(self):
        properties_file = open("MonsterProperties.txt", 'r')

        for s in properties_file.readlines():
            if s != "\n":
                temp_key = s.split(':')[0].strip(' ').upper()

                try:
                    temp_value = s.split(':')[1].strip(' ').strip('\n')
                except:
                    print("INVALID VALUE IN MONSTER PROPERTIES")
                    return

                self.monster_properties[temp_key] = temp_value
