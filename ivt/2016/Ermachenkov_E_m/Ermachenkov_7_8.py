# Задача 7. Вариант 8.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.
# Ermachenkov E. M.
# 28.03.2017
print('Программа случайным образом загадыает название одного из семи холмов\n,на которых по легенде была построенная Москва \nЧем меньше попыток вы используете, тем больше балло заработаете.')
import random
list = ('Боровицкий холм', 'Псковская горка', 'Таганский холм', 'Ивановская горка', 'Красный холм', 'Старо-Ваганьковский холм', 'Чертольский холм')
name2 = random.choice(list)
a = 70
name = input('\nВведите назание одного из холмов Москвы - \n\nБоровицкий холм, Псковская горка,\nТаганский холм, Ивановская горка, Красный холм,\nСтаро-Ваганьковский холм, Чертольский холм\n\n')
while name != name2: 
	print('\nВы не угадали\nПопробуйте еще раз\n')
	name = input('Введите назание одного из холмов Москвы - \n\n')
	x = a - 10
	a = x
print('\nВы угадали, программа загадала - ', name2, '\nВам начислено ', a, ' баллов')

input('\nВведите Enter для выхода')