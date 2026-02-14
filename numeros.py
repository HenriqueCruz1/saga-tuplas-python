from operator import index
from symtable import Class

print(20*'-','Numeros escritos por extenso',20*'-')

numeros = (
    'Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete',
    'Oito','Nove','Dez','Onze','Doze','Treze','Quatorze',
    'Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte'
)


def numero_por_extenso(numero:int) -> Result:
    if 0 <= numero <=20:
        return Result(value=numeros[numero])
    else:
        return Result(error= 'Numero fora do intervalo')

class Result:
    def __init__(self, value = None, error = None):
        self.value= value
        self.error= error

    def is_ok(self):
            return self.error is None

numero = (int(input('Digite um valor de 0 a 20 ..')))

resultado = numero_por_extenso(numero)

if resultado.is_ok():
    print(resultado.value)
else:
    print(resultado.error)








