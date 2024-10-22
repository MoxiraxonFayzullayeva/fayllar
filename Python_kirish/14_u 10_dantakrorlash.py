# _______________________if elif else___________________________________
# _________________________and or_______________________________________
# lst = [1, 5, 'soz', [5, 8], 6, 'matn', [0]]
# for i in lst:
#     if type(i) != list:
#         if isinstance(i, int):
#             print(i, end=" ")
#         else:
#             print(i.upper(), end=" ")
#     else:
#         for j in i:
#             if type(j) != list:
#                 if isinstance(j, int):
#                     print(j, end=" ")
#                 else:
#                     print(i.upper(), end=" ")

# bilet ={
#     'bola': 0,
#     'yosh': 25_000,
#     'orta': 65_0000
# }
# narx = 0
# odam = 1
# kun = input('Kun kiriting: ').lower()
# for i in range(int(input('Nechta bilet olmoqchisiz: '))):
#     yosh = int(input(f'{odam}- odamning yoshingizni kiriting: '))
#     odam += 1
#     if yosh <= 7 or yosh >= 65:
#         narx += bilet['bola']
#     elif kun == 'juma' and (yosh >=8 and yosh <= 18):
#         narx += bilet['yosh']
#     else:
#         narx += bilet['orta']
# print(f'UMUMIY BILET NARXI: {narx} so\'m')

# ____________________________________UYGA VAZIFA_______________________

# dct ={
#     'ism': 'abdulloh',
#     'familiya': 'nosirov',
#     'yil': 2005,
#     'skils': ['python', 'c', 'java', 'postgresql']
# }
# # Abdulloh: PYTHON, C, JAVA, POSTGRESQL.
# for i in dct.values():
#     if i == 'abdulloh':
#         print(f'{i.title()}', end=": " )
# for i in dct['skils']:
#     if i == dct['skils'][-1]:
#         print(f'{i.upper()}', end=".")
#     else:
#         print(f'{i.upper()}', end=", ")















