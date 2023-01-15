# The purpose of this project is to practice string concatenation in Python using 3 different approaches

# take user input
food = input("Food: ")
name = input("Name: ")
adj = input("Adjective: ")
animal = input("Animal: ")
verb1 = input("Past tense verb: ")
verb2 = input("Past tense verb: ")
verb3 = input("Past tense verb: ")
noun = input("Noun: ")

# using regular concatenation
reg_madlib = "It was " + food + " day at school, and " + name + " was super " + adj + " for lunch. But when she went outside to eat, a "\
     + animal + " stole her " + food + "! " + name + " chased the " + animal + " all over school. She " + verb1 + ", " + verb2\
     + ", and " +  verb3 + " through the playground. Then she tripped on her " + noun + " and the " + animal + " escaped! Luckily, " + name\
     + "’s friends were willing to share their " + food + " with her."

# using fstring
fstring_madlib = f"It was {food} day at school, and {name} was super {adj} for lunch. But when she went outside to eat, a "\
     f"{animal} stole her {food}! {name} chased the {animal} all over school. She {verb1}, {verb2}, "\
     f"and {verb3} through the playground. Then she tripped on her {noun} and the {animal} escaped! Luckily, {name}"\
     f"’s friends were willing to share their {food} with her."

# using .format()
format_madlib = "It was {} day at school, and {} was super {} for lunch. But when she went outside to eat, a "\
     "{} stole her {}! {} chased the {} all over school. She {}, {}, "\
     "and {} through the playground. Then she tripped on her {} and the {} escaped! Luckily, {}"\
     "’s friends were willing to share their {} with her.".format(food, name, adj, animal, food, name, animal, verb1, verb2, verb3, noun, animal, name, food)

# print results
print("Madlib using regular concatenation: " + reg_madlib)
print()
print("Madlib using fstring: " + fstring_madlib)
print()
print("Madlib using .format(): " + format_madlib)