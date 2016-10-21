import MonsterBuilder

test_template = {"ARMS" : 2, "LEGS" : 2}
builder = MonsterBuilder.MonsterBuilder(test_template)
print(builder.buildMonster().torso)
