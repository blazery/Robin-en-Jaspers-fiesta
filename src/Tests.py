import MonsterBuilder
import FileReader

reader = FileReader.FileReader()
test_template = reader.readFile("TestTemplate.txt")
builder = MonsterBuilder.MonsterBuilder(test_template)

print("Template as read from file: ", test_template, '\n')
monster = builder.buildMonster()
for part in monster.torso.contains:
    print("Parts: ", part.part_type)
    for partspart in part.contains:
        print("Partsparts: ", partspart.part_type)


print("\nSlots for body parts: ", builder.slots)

builder = MonsterBuilder.MonsterBuilder(reader.readFile("TestTemplate2.txt"))
monster2 = builder.buildMonster()

print("\n")
for part in monster2.torso.contains:
    print("Parts: ", part.part_type)
    for partspart in part.contains:
        print("Partsparts: ", partspart.part_type)
