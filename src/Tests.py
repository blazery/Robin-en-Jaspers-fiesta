import MonsterBuilder
import FileReader

reader = FileReader.FileReader()
test_template = reader.readFile("TestTemplate.txt")
builder = MonsterBuilder.MonsterBuilder(test_template)

print("Template as read from file: ", test_template, '\n')
builder = MonsterBuilder.MonsterBuilder(test_template)
for part in builder.buildMonster().torso.contains:
    print("From template file: ", test_template, ": ", part)

builder.calcSpaceForBP()
print("\nSlots for body parts: ", builder.slots)
