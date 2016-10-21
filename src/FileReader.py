import PropertyList

class FileReader:

    last_read_file = None
    properties = PropertyList.PropertyList()


    def readFile(self, path):
        try:
            file = open(path, 'r')
        except:
            print("LOADING FILE ERROR")
            print("File could not be found")
            return False

        properties_dictionary = dict()
        string_list = file.readlines()

        for s in string_list:
            temp_key = s.split(':')[0].strip(' ').upper()
            temp_value = None

            if ':' in s :
                temp_value = s.split(':')[1].strip(' ').strip('\n')

            if temp_key in self.properties.properties:
                if self.valueTypeValidate(temp_key, temp_value):
                    properties_dictionary[temp_key] = temp_value
                    
        self.last_read_file = properties_dictionary
        return properties_dictionary



    def valueTypeValidate(self, key, value):
        if self.properties.properties[key] == "int":
            if value.isdigit():
                return True
        elif self.properties.properties[key] == "bool":
            if value.upper() == "TRUE" or value.upper() == "FALSE":
                return True
        elif self.properties.properties[key] == "string":
            if value.isalpha():
                return True
        else:
            return False