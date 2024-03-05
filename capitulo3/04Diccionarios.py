rae = {}
rae['pizza'] = 'la comida mas deliciosa del mundo'
rae['pasta'] = 'la comida mas deliciosa de Italia'
print(rae)
a = rae.get('pizza', None)
print(a)
print(rae.keys())
print(rae.values())

for key in rae.keys():
    print(key)

for key in rae.values():
    print(key)    

for key in rae.items():
    print(key)