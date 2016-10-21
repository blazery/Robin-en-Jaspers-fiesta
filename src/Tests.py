import MonsterBuilder

test_template = {"ARMS" : 2, "LEGS" : 2, "HEADS" : 3, "NECKS" : 3, "HANDS" : 2}
builder = MonsterBuilder.MonsterBuilder(test_template)
print(builder.buildMonster().torso)
print(builder.attach_hierarchy)
