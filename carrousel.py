persons_ages = []
pers_age = 0
i = 0

while i<3:
    pers_age = int(input("Algo :"))
    persons_ages.append(pers_age)
    i+=1
 
#tu código va aquí
def Validahion_Age(Ages) :
    for age in Ages :
       if age < 16:
          return 'Too young!'
    return 'Get ready!'

validation = Validahion_Age(persons_ages)

print(validation)
