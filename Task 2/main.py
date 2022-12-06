# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
from statistics import mean, median
users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
def getUserAverageAge(users):
  a_key = "age"
  list_of_values = [a_dict[a_key] for a_dict in users]
  return mean(list_of_values)

print(getUserAverageAge(users))

# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

def getUsersNames(users):
  a_key = "name"
  list_of_values = [a_dict[a_key] for a_dict in users]
  return sorted(list_of_values)

print(getUsersNames(users)) 

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka