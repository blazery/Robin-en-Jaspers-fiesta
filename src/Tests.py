import MonsterBuilder
import FileReader

test_template = {"ARMS" : 2, "LEGS" : 2, "HEADS" : 3, "NECKS" : 3, "HANDS" : 2}
builder = MonsterBuilder.MonsterBuilder(test_template)
for part in builder.buildMonster().torso.contains:
    print("Directly from template ", test_template, ": ", part) 
reader = FileReader.FileReader()
test_template = reader.readFile("TestTemplate.txt")
print("Template as read from file: ", test_template)
builder = MonsterBuilder.MonsterBuilder(test_template)
for part in builder.buildMonster().torso.contains:
    print("Directly from template ", test_template, ": ", part) 
