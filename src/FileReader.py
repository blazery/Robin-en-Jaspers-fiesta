from PropertyList import PropertyList

class FileReader:

    last_read_file = None
    properties = PropertyList()


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

            if ':' in s:
                temp_value = s.split(':')[1].strip(' ').strip('\n')

            if temp_key in self.properties.properties:
                properties_dictionary[temp_key] = temp_value

        self.last_read_file = properties_dictionary
        return  properties_dictionary

test = FileReader()
print(test.readFile("emptyfile.txt"))