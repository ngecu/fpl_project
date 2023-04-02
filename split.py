import json
numbers = []
anothe =[]
with open('players_0.json') as json_file:
    data = json.load(json_file)
    
    for x in data:
        names = (data[x].split(' '))[0]
        numbers.append(names)
        # print(data[x])


res = [*set(numbers)]

with open('players_0.json') as json_file:
    data = json.load(json_file)
    
    
    for x in data:
        name = (data[x].split(' '))[0]
        for n in res:
            if n==name:
                anothe.append(data[x])


resa = [*set(anothe)]
print(len(resa))
print(len(anothe))

for p in resa:
    if "De Bruyne" in p:
        p.split(' ')[0] = "DeBruyne"
        xyz = p.split(' ')[3]
        p = f"DeBruyne - {xyz}"
    
    percentage = (int(p.split(' ')[2])/10)
    name = p.split(' ')[0]
    # print(percentage)
    print(f"{name} - {percentage} %")