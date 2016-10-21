
class FileReader:

        def __init__(self):

            print()

        def readFile(self, path):

            file_object = open("suckadick.txt", 'r')
            text = file_object.readlines()
            print(text)








test = FileReader()
test.readFile("test")