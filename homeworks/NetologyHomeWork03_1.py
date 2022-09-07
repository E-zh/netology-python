boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
    print("Кому-то не достанется пары!")
couples = zip(sorted(boys), sorted(girls))
print("Идеальные пары: ")
for boy, girl in couples:
    print(f'{boy} и {girl}')