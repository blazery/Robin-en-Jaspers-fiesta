class PropertyList:
    properties = list()

    def __init__(self):
        properties_file = open("MonsterProperties.txt", 'r')

        for s in properties_file.readlines():
            if s != "\n":
                self.properties.append(s.strip(' ').rstrip('\n').upper())



PropertyList()
