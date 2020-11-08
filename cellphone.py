'''
Verificar que una cadena cumpla con unicamente numeros , que comiencen con 1,8 o 9 y que sean 8 digitos
'''

import re

request = r'^([189])(\d{7})([A-Za-z]{0})'

pattern = re.compile(request)

prueba = '123456789'

if pattern.search(prueba) is not None and len(prueba) == 8 :
    print('Valid')
else :
    print('Invalid')
