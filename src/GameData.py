class GameData:
    monster_properties = dict()
    monster_hierarchy = dict()

    def __init__(self):
        # loads the monster properties
        self.monster_properties = self.loadProperties("MonsterProperties.txt")
        # loads the monster hierarchy
        self.monster_hierarchy = self.loadHierarchy("MonsterHierarchy.txt")

    def loadProperties(self, path):
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

    def loadHierarchy(self, path):
        properties_file = open(path, 'r')
        temp_dict = dict()

        for s in properties_file.readlines():
            if s != "\n":
                temp_key = s.split('>')[0].strip(' ').upper()

                try:
                    temp_value = s.split('>')[1].strip(' ').strip('\n').upper()
                except:
                    print("NO VALUE IN " + str(temp_key))
                    return

                if temp_key in temp_dict:
                    temp_array = temp_dict[temp_key]
                    temp_array.append(temp_value)
                    temp_dict[temp_key] = temp_array
                else:
                    temp_dict[temp_key] = [temp_value]
        return temp_dict


