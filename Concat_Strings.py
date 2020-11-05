'''
Funcion que concatena multiples strings
-> Hola Amigos mios
-> Hola-amigos-mios
'''

def strings(*args) :
    accumulator = ''
    for string in args:
        accumulator += string+'-'
    
    return accumulator.rstrip('-')


