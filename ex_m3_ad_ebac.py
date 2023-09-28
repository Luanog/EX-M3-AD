# -*- coding: utf-8 -*-
"""EX - M3 - AD -EBAC

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSQBLw8C4rkF3py0saG-FJ2ZCIEB_JwN

EX
"""

propaganda_online = [
  {'tempo_gasto_site': 68.95, 'idade': 35, 'renda_area': 61833.90, 'tempo_gasto_internet': 256.09, 'cidade': 'Wrightburgh', 'pais': 'Tunisia', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 80.23, 'idade': 31, 'renda_area': 68441.85, 'tempo_gasto_internet': 193.77, 'cidade': 'West Jodi', 'pais': 'Nauru', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 69.47, 'idade': 26, 'renda_area': 59785.94, 'tempo_gasto_internet': 236.50, 'cidade': 'Davidton', 'pais': 'San Marino', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 68.37, 'idade': 35, 'renda_area': 73889.99, 'tempo_gasto_internet': 225.58, 'cidade': 'South Manuel', 'pais': 'Iceland', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 88.91, 'idade': 33, 'renda_area': 53852.85, 'tempo_gasto_internet': 208.36, 'cidade': 'Brandonstad', 'pais': 'Myanmar', 'clicou_no_ad': 0},
  {'tempo_gasto_site': None, 'idade': 48, 'renda_area': 24593.33, 'tempo_gasto_internet': 131.76, 'cidade': 'Port Jefferybury', 'pais': 'Australia', 'clicou_no_ad': 1},
  {'tempo_gasto_site': 74.53, 'idade': 30, 'renda_area': 68862.00, 'tempo_gasto_internet': 221.51, 'cidade': 'West Colin', 'pais': 'Grenada'},
  {'tempo_gasto_site': 69.88, 'idade': 20, 'renda_area': 55642.32, 'tempo_gasto_internet': 183.82, 'cidade': 'Ramirezton', 'pais': 'Ghana', 'clicou_no_ad': 0}
]
tempo_gasto_site_idade = []

print('EX 1 Parte1')

for registro in propaganda_online:
    if 'tempo_gasto_site' in registro and 'idade' in registro:
        tempo_gasto_site = registro['tempo_gasto_site']
        idade = registro['idade']
        tempo_gasto_site_idade.append({'tempo_gasto_site': tempo_gasto_site, 'idade': idade})

for info in tempo_gasto_site_idade:
    print(info)

print('\n EX 1 Parte2')

for dado_de_usuario in propaganda_online:
    tempo_gasto_site = dado_de_usuario.get('tempo_gasto_site')

    if tempo_gasto_site is not None:
        print(tempo_gasto_site)

print('\n EX 1 Parte3')

for dado_de_usuario in propaganda_online:
    idade = dado_de_usuario.get('idade')
    print(idade)


print('\n EX 2')


for dado_de_usuario in propaganda_online:
    tempo_gasto_internet = dado_de_usuario.get('tempo_gasto_internet', 0)

    if tempo_gasto_internet > 100:
        cidade = dado_de_usuario.get('cidade')
        print(cidade)

print('\n EX 3')
for dado_de_usuario in propaganda_online:
    try:
        tempo_gasto_site = dado_de_usuario['tempo_gasto_site']

        if tempo_gasto_site > 70:
            cidade = dado_de_usuario.get('cidade')
            print(cidade)

    except KeyError:
        continue

    except TypeError:
        continue
