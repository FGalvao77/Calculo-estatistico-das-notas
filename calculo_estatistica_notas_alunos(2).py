# -*- coding: utf-8 -*-
"""calculo_estatistica_notas_alunos(2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p13Xv1ISKbH2UwfTU8i1F4v2KZ-L_s2T

### **Resumo estatístico - notas | alunos**
---

Sabe-se que as notas dos alunos de uma Escola estão no intervalo de 0 a 10 e a Escola tem como objetivo realizar uma análise estatística sobre essas notas.

Faça um Programa utilizando a linguagem Python que solicite ao usuário de cada aluno uma única nota (são 20 alunos) e as armazene em uma lista.
Calcule e mostre:

- a. A média aritmética das notas;
- b. A variância das notas;
- c. O desvio padrão.
"""

app_form = dict()
size = len(app_form)

for i in range(1, 21):
    if len(app_form) > 20:
        break

    app_form[i + size] = [input('nome: ').title(), input('nota: ')]
    command = input('continuar?["S/N"]: ').upper()

    if command in 'N':
        break

import numpy as np 

nomes = [str(i[0]) for i in app_form.values()]
notas = [float(i[1]) for i in app_form.values()]
media = round(np.mean(notas), 2)
desv_pad = round(np.std(notas), 2)
var = round(np.var(notas), 2)

print(
    '\nESTATÍSTICAS [notas | alunos]\n'
    '===============================',
    f'Alunos: {nomes}',
    f'Notas: {notas}',
    f'Média: {media}',
    f'Variância: {var}',
    f'Desvio-padrão: {desv_pad}',
    sep='\n'
)





