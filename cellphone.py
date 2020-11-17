'''
Verificar que una cadena cumpla con unicamente numeros , que comiencen con 1,8 o 9 y que sean 8 digitos
'''

import re

request = r'^([189])(\d{7})([A-Za-z]{0})'

pattern = re.compile(request)

test = '123456789'
test2 = '000000031'
test3 =  '12345678'

if pattern.search(test) is not None and len(test) == 8 :
    print('Valid')
else :
    print('Invalid')
if pattern.search(test2) is not None and len(test2) == 8 :
    print('Valid')
else :
    print('Invalid')
if pattern.search(test3) is not None and len(test3) == 8 :
    print('Valid')
else :
    print('Invalid')
