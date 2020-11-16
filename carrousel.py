persons_ages = []
person_age = 0
i = 0

while i<3:
    person_age = int(input("Algo :"))
    persons_ages.append(person_age)
    i+=1

#tu código va aquí
def Validation_Ages(Ages) :
    for age in Ages :
       if age < 16:
          return 'Too young!'
    return 'Get ready!'

validation = Validation_Ages(persons_ages)

print(validation)
