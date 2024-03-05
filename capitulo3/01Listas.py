import copy
countries = ['Mexico', 'Venezuela', 'España']
ages = [12,18,24,34,50]
weigths = [12,18,24,34,50]

print(id(countries))
print(id(ages))
print(id(weigths))

receta = ['Ensalada', '2', 'lechugas', '5', 'jitomates']

countries[0] = 'Guatemala'


global_countries = countries 
print(global_countries )

global_countries = None
global_countries = copy.copy(countries)
countries[1] = 'Honduras'
print(countries)
print(global_countries )

for country in countries:
    print(country)