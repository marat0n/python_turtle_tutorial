# Подключаем модуль turtle
import turtle


# Приводим черепашку в начальное положение
turtle.reset()
# Поднимаем черепаху - перестаём рисовать
turtle.up()

# Выводим надпись IThub
turtle.left(180)
turtle.forward(50)
turtle.write('IThub', font=('TT firs neue', 40, 'bold'))

# Занимаем стартовую позицию для первого квадрата
turtle.forward(30)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
# Рисуем первый квадрат
turtle.down()
turtle.begin_fill()
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.end_fill()
# Занимаем стартовую позицию для белой дыры в квадрате и меняем цвет
turtle.up()
turtle.color('white')
turtle.left(180)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
# Рисуем белую дыру в квадрате
turtle.down()
turtle.begin_fill()
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.end_fill()

# Занимаем стартовую позицию для второго квадрата
turtle.up()
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(210)
turtle.left(90)
# Рисуем второй квадрат и меняем цвет на чёрный
turtle.color('black')
turtle.down()
turtle.begin_fill()
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.end_fill()
# Занимаем стартовую позицию для белой дыры в квадрате
turtle.up()
turtle.left(180)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
# Рисуем белую дыру в квадрате
turtle.color('white')
turtle.down()
turtle.begin_fill()
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.end_fill()
# Занимаем стартовую позицию для ещё одного чёрного квадрата внутри
turtle.up()
turtle.left(180)
turtle.forward(8)
turtle.right(90)
turtle.forward(8)
# Рисуем ещё чёрный квадрат внутри
turtle.color('black')
turtle.down()
turtle.begin_fill()
turtle.forward(13)
turtle.left(90)
turtle.forward(13)
turtle.left(90)
turtle.forward(13)
turtle.left(90)
turtle.forward(13)
turtle.end_fill()

# Занимаем стартовую позицию для третьего квадрата
turtle.up()
turtle.forward(28)
turtle.right(90)
turtle.forward(240)
# Рисуем третий квадрат
turtle.color('black')
turtle.down()
turtle.begin_fill()
turtle.forward(70)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(70)
turtle.end_fill()
# Занимаем позицию для белой дыры
turtle.up()
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
# Рисуем белую дыру для третьего квадрата
turtle.color('white')
turtle.down()
turtle.begin_fill()
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.end_fill()

# Занимаем стартовую позицию для четвёртого квадрата
turtle.up()
turtle.color('black')
turtle.forward(20)
turtle.left(90)
turtle.forward(170)
# Рисуем четвёртый квадрат
turtle.down()
turtle.begin_fill()
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.end_fill()
# Занимаем стартовую позицию для белой дыры
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
# Рисуем белую дыру для четвёртого квадрата
turtle.color('white')
turtle.down()
turtle.begin_fill()
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.end_fill()

turtle.up()
# Перемещение черепашки в самое начало окна, чтобы не мешала
turtle.goto(0,0)
# Задержать окно на экране
turtle.mainloop()