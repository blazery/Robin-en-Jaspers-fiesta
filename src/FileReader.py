import GameData

class FileReader:

    last_read_file = None
    properties = GameData.GameData().monster_properties


    def readFile(self, path):
        try:
            file = open(path, 'r')
        except:
            print("LOADING FILE ERROR")
            print("File could not be found")

            if self.last_read_file is not None:
                print("returning last successfull monster")
                return self.last_read_file

            return False

        properties_dictionary = dict()
        string_list = file.readlines()

        for s in string_list:
            temp_key = s.split(':')[0].strip(' ').upper()
            temp_value = None

            if ':' in s :
                temp_value = s.split(':')[1].strip(' ').strip('\n')

            if temp_key in self.properties:
                if self.valueTypeValidate(temp_key, temp_value):
                    temp_value = self.valueConverter(temp_key, temp_value)
                    properties_dictionary[temp_key] = temp_value

        self.last_read_file = properties_dictionary
        return properties_dictionary

    # only validates int, bool, and string
    def valueTypeValidate(self, key, value):
        if self.properties[key] == "int":
            if value.isdigit():
                return True
        elif self.properties[key] == "bool":
            if value.upper() == "TRUE" or value.upper() == "FALSE":
                return True
        elif self.properties[key] == "string":
            if value.isprintable():
                return True

        return False

    def valueConverter(self, key, value):
        if self.properties[key] == "int":
            if value.isdigit():
                return int(value)
        elif self.properties[key] == "bool":
            if value.upper() == "TRUE" or value.upper() == "FALSE":
                return bool(value)
        elif self.properties[key] == "string":
            if value.isalpha():
                return value

        return value