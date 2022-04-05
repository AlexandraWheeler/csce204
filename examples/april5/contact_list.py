from person import Person
'''''''''
friend = Person("Sanda", "White", "8034824934")
friend.display()
friend2 = Person("Bobby", "White", "8034345932")
friend2.display()
'''
people = {
    Person("Sanda", "White", "8034824934"),
    Person("Bobby", "White", "8034345932")
}

for person in people:
    person.display()