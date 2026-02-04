n1 = int(input('qual é a Altura da parede? '))
n2 = int(input('qual é a Largura da parede? '))
area = n1 * n2
tinta = area / 2
print ('Altura: {}'.format(n1))
print('Largura: {}'.format(n2))
print('Área: {}m²'.format(area))
print('Para pintar essa parede serão necessários {} litros de tinta.'.format(tinta))