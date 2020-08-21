from CURSO_PYTHON_DIO.aula6_3 import Televisao
from CURSO_PYTHON_DIO.aula6_2 import Calculadora
from CURSO_PYTHON_DIO.aula7_2_contador_letras import contador_letras

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora()
    print(calculadora.soma(5,10))

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print(f'A lista {lista}, tem {total_letras} letras em cada palavra respectivamente')

