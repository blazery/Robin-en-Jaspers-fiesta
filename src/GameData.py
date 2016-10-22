class GameData:
    monster_properties = dict()
    monster_hierarchy = dict()

    def __init__(self):
        # loads the monster properties
        self.monster_properties = self.dataReader("MonsterProperties.txt")
        # loads the monster hierarchy
        self.monster_hierarchy = self.dataReader("MonsterHierarchy.txt")

    def dataReader(self, path):
        properties_file = open(path, 'r')
        temp_dict = dict()

        for s in properties_file.readlines():
            if s != "\n":
                temp_key = s.split(':')[0].strip(' ').upper()

                try:
                    temp_value = s.split(':')[1].strip(' ').strip('\n')
                except:
                    print("NO VALUE IN " + str(temp_key))
                    return

                temp_dict[temp_key]= temp_value
        return temp_dict