"""
Tio Patinhas era um milionário que vivia em sua mansão, e tinha três sobrinhos: Huguinho, Zezinho e Luisinho. 
Ele se confundia facilmente entre os três sobrinhos, pois eram bem parecidos, apesar de terem idades diferentes. 
Um dia, os três fizeram uma aposta com o tio: se ele acertasse quem era o sobrinho do meio, ou seja, nem o mais novo, 
nem o mais velho, eles dariam uma moeda de ouro para ele, e se ele errasse, teria que dar uma moeda de ouro para cada um. Assim, 
o tio pede a tua ajuda para que ele possa ganhar essa aposta.

Entrada
A entrada consiste em vários casos de teste. Cada caso contém três valores inteiros H, Z e L, que representam as idades de Huguinho, Zezinho e Luisinho, respectivamente. 

Saída
Para cada caso de teste imprima o nome do sobrinho do meio, com letras minúsculas.
"""

valor = input().split(" ")

H, Z, L = valor
if(int(Z) > int(H) and int(Z) < int(L)) or (int(Z) > int(L) and int(Z) < int(H)):
    print("zezinho")
if (int(H) > int(Z) and int(H) < int(L)) or (int(H) > int(L) and int(H) < int(Z)):
    print("huguinho")
if (int(L) > int(Z) and int(L) < int(H)) or (int(L) > int(H) and int(L) < int(Z)):
    print("luisinho")
