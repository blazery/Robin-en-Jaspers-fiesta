import MonsterBuilder
import FileReader
import MonsterCreationView

reader = FileReader.FileReader()
test_template = reader.readFile("TestTemplate.txt")
builder = MonsterBuilder.MonsterBuilder(test_template)
view = MonsterCreationView.MonsterCreationView()

print("test")
monster = builder.buildMonster()
view.Go(monster)







print("Template as read from file: ", test_template, '\n')
builder = MonsterBuilder.MonsterBuilder(test_template)
monster = builder.buildMonster()
print("count: ", monster.countBodyPart(monster.torso, "TENTACLES"))
print(type(monster.torso))
for part in monster.torso.contains:
    print("Parts: ", part.part_type)
    for partspart in part.contains:
        print("Partsparts: ", partspart.part_type)
        for xd in partspart.contains:
            print("sadsadasdas: ", xd.part_type)

builder.monsterToFile(monster, "firstMonsterSave")
monster = builder.loadMonsterFile("firstMonsterSave")
print(monster.torso.part_type)
for part in monster.torso.contains:
    print("Parts: ", part.part_type)
    for partspart in part.contains:
        print("Partsparts: ", partspart.part_type)
        for xd in partspart.contains:
            print("sadsadasdas: ", xd.part_type)


print("\nSlots for body parts: ", builder.slots)


