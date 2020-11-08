from functools import reduce #importa reduce 

# variables
word = '{4+4 -[6*10] + 10 - (100-5)}'
PAIRS = '()[]{}'
filtered_word = ''

# se encarga de dejar unicamente los caracteres
for letter in word :
    if letter in PAIRS :
        filtered_word += letter

# verifica si se encuentra el par en 
def Index_Pattern(index,word,pair) :
    if index == -1 :
        return word.find(pair)
    else :
        return index

# quita el ultimo par encontrado
def cut(_str,_from,_to) :
    return _str[0:_from] + _str[_to+1:]

# funcion principal que valida si se encuentra
def Validation(_str) :
    if _str == '' :
        return True
    PAIRS = ['()','[]','{}']
    index_pair = reduce(lambda index,pair : Index_Pattern(index,_str,pair) ,PAIRS, -1 )

    if index_pair != -1 :
        cut_word = cut(_str,index_pair,index_pair+1)
        return Validation(cut_word)
    else :
        return False

# caso de prueba
print(Validation(filtered_word))

