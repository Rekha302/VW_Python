people = {'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

print("Number of students:", len(people))

people['Lisa'] = 'Green'

people.pop('Jenny')

for name in sorted(people):
    print(name, ":", people[name])

