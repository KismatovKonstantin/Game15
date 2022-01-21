from tkinter import *
import sys

problems = [
    [
        "По кругу стоит 6 аборигенов. Каждый из них\n говорит “Мой сосед справа — лжец”.\n Сколько среди них лжецов?",
        "Художник Худобеднов за месяц работы написал\n 42 картины. На 17 из них есть лес,\n на 29 река, а на 13 - и то,\n и другое. На остальных картинах\n - не пойми что. Сколько картин\n изображают не пойми что?"
    ],
    [
        "Нескольким третьеклассниками раздали\n 50 яблок так, чтобы каждый получил\n хотя бы по одному яблоку и ни у каких двух\n не было поровну яблок. Какое наибольшее\n количество третьеклассников могли\n получить яблоки?",
        "От прямоугольника отрезали квадрат\n (прямым разрезом от края до края)\n и его площадь уменьшилась в 2 раза.\n Найдите площадь исходного прямоугольника,\n если его периметр был равен 60 м."
    ],
    [
        "Художник Худобеднов за месяц работы написал\n 42 картины. На 17 из них есть лес,\n на 29 река, а на 13 - и то, и другое. На остальных\n картинах - не пойми что. Сколько картин\n изображают не пойми что? ",
        "Сколько получится, если сложить наименьшее\n двузначное, наименьшее трехзначное\n и наименьшее четырехзначное число?"
    ],
    [
        "У Пети 3 разных футболок и 6 разных шорт.\n Каждый день он одевает одну футболку\n и одни шорты так, чтобы не ходить\n в одной одежде два раза. Сколько дней\n он может это делать?",
        "В ящике лежит 10 красных, 8 синих, 8 зеленых\n и 4 желтых шарика. Сколько надо\n вынуть шариков, чтобы среди них\n наверняка нашелся шарик каждого цвета?"
    ],
    [
        "Лиса Алиса и кот Базилио пришли в харчевню\n Трех пескарей, заказали обед и дали\n хозяину 10 золотых. Тот в качестве\n сдачи вернул им столько денег,\n сколько стоил обед. Лиса заметила,\n что хозяин дал им на 2 золотых\n меньше, чем нужно. Сколько денег\n он должен был вернуть им на самом деле?",
        "Студент за пять лет учебы сдал 31 экзамен.\n В каждом следующем году он сдавал\n больше экзаменов, чем в предыдущем,\n а на пятом курсе – втрое больше,\n чем на первом. Сколько экзаменов он\n сдал на четвертом курсе?"
    ],
    [
        "От прямоугольника отрезали квадрат\n (прямым разрезом от края до края)\n и его площадь уменьшилась в 2 раза.\n Найдите площадь исходного прямоугольника,\n если его периметр был равен 60 м.",
        "Деревянный куб, ребро которого равно\n 6 см, покрасили снаружи и разрезали\n на кубики, ребро каждого из которых\n равно 1 см. Сколько маленьких кубиков\n имеют по две закрашенные грани?"
    ],
    [
        "Выписав 6 четных чисел, идущих подряд,\n Вася обнаружил, что самое большое\n из них вдвое больше самого\n маленького. Чему равно самое\n маленькое число?",
        "На распродаже марок любая почтовая марка\n стоила 10 рублей. При этом к каждым\n десяти купленным маркам одна\n давалась бесплатно, а за каждую сотню\n оплаченных марок еще дарили 5 марок.\n Заплатив все свои деньги за марки\n в этом магазине, Андрей получил\n 200 марок. Сколько у него\n было денег?"
    ],
    [
        "Кенгуру купил конфеты трех видов:\n большие, маленькие и средние.\n Каждая большая конфета стоит 4 монеты,\n средняя — 2 монеты и маленькая — 1 монету.\n За 10 конфет Кенгуру заплатил 16 монет.\n Сколько больших конфет он купил,\n если каждого сорта он купил хотя бы по 1?",
        "Четырехзначное число начинается\n с цифры 5. Эту цифру переставили\n в конец числа. Полученное число\n оказалось на 747 меньше исходного.\n Какова сумма цифр этого числа?"
    ],
    ["7*5", "aaa"],
    ["6*6", "aaa"],
    ["6*5", "aaa"],
    ["6*4", "aaa"],
    ["5*5", "aaa"],
    ["5*4", "aaa"],
    ["5*3", "aaa"],
    ["4*4", "aaa"]
]
answers = [
    ["3", "9"],
    ["10", "200"],
    ["9", "1110"],
    ["18", "27"],
    ["6", "8"],
    ["200", "48"],
    ["10", "1780"],
    ["1", "18"],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""]
]

solved = [
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False
]

BOARD_SIZE = 3
SQUARE_SIZE = 140
EMPTY_SQUARE = BOARD_SIZE ** 2
LVL = 0

root = Tk()
root.title("Игра пятнашки")
c = Canvas(root, width=BOARD_SIZE * SQUARE_SIZE,
           height=BOARD_SIZE * SQUARE_SIZE, bg='#808080')
c.pack()

league = Toplevel()
league.title("Выбери свой класс!")
league.geometry("300x120")
league.after(1, lambda: league.focus_force())
var = IntVar()
Radiobutton(league, text='3 класс', variable=var, value=0).pack()
Radiobutton(league, text='4 класс', variable=var, value=1).pack()
button1 = Button(league, text="Играть!", command=lambda: choose_lvl())
button1.pack()
button2 = Button(league, text="Закрыть", command=lambda: close_game())
button2.pack()

league.protocol("WM_DELETE_WINDOW", lambda: close_game())

lvl = 0


def choose_lvl():
    global lvl
    lvl = var.get()
    root.deiconify()  # Показываем основное окно
    league.destroy()  # Уничтожаем окно выбора сложности


def close_game():
    league.destroy()  # Уничтожаем окно выбора сложности
    root.destroy()  # Уничтожаем основное окно
    sys.exit()  # Выходим из программы


def get_inv_count():
    """ Функция считающая количество перемещений """
    inversions = 0
    inversion_board = board_d[LVL][:]
    inversion_board.remove(EMPTY_SQUARE)
    for i in range(len(inversion_board)):
        first_item = inversion_board[i]
        for j in range(i + 1, len(inversion_board)):
            second_item = inversion_board[j]
            if first_item > second_item:
                inversions += 1
    return inversions


def is_solvable():
    """ Функция определяющая имеет ли головоломка решение """
    num_inversions = get_inv_count()
    if BOARD_SIZE % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0


def get_empty_neighbor(index):
    # получаем индекс пустой клетки в списке
    empty_index = board_d[LVL].index(EMPTY_SQUARE)
    # узнаем расстояние от пустой клетки до клетки по которой кликнули
    abs_value = abs(empty_index - index)
    # Если пустая клетка над или под клектой на которую кликнули
    # возвращаем индекс пустой клетки
    if abs_value == BOARD_SIZE:
        return empty_index
    # Если пустая клетка слева или справа
    elif abs_value == 1:
        # Проверяем, чтобы блоки были в одном ряду
        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    # Рядом с блоком не было пустого поля
    return index


def draw_board():
    # убираем все, что нарисовано на холсте
    c.delete('all')
    # Наша задача сгруппировать пятнашки из списка в квадрат
    # со сторонами BOARD_SIZE x BOARD_SIZE
    # i и j будут координатами для каждой отдельной пятнашки
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # получаем значение, которое мы должны будем нарисовать
            # на квадрате
            index = str(board_d[LVL][BOARD_SIZE * i + j])
            # если это не клетка которую мы хотим оставить пустой
            if index != str(EMPTY_SQUARE):
                # рисуем квадрат по заданным координатам
                c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                                   j * SQUARE_SIZE + SQUARE_SIZE,
                                   i * SQUARE_SIZE + SQUARE_SIZE,
                                   fill='#43ABC9',
                                   outline='#FFFFFF')
                # пишем число в центре квадрата
                c.create_text(j * SQUARE_SIZE + SQUARE_SIZE / 2,
                              i * SQUARE_SIZE + SQUARE_SIZE / 2,
                              text=index,
                              font="Arial {} italic".format(int(SQUARE_SIZE / 4)),
                              fill='#FFFFFF')


def show_victory_plate():
    # Рисуем черный квадрат по центру поля
    c.create_rectangle(SQUARE_SIZE / 5,
                       SQUARE_SIZE * BOARD_SIZE / 2 - 10 * BOARD_SIZE,
                       BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5,
                       SQUARE_SIZE * BOARD_SIZE / 2 + 10 * BOARD_SIZE,
                       fill='#000000',
                       outline='#FFFFFF')
    # Пишем красным текст Победа
    c.create_text(SQUARE_SIZE * BOARD_SIZE / 2, SQUARE_SIZE * BOARD_SIZE / 1.9,
                  text="ПОБЕДА!", font="Helvetica {} bold".format(int(10 * BOARD_SIZE)), fill='#DC143C')


def show_problem(ind, board_index, empty_index):
    print(ind, board_index, empty_index)

    def check_answer():
        answer = str(ans_entry.get())
        answer = ''.join(answer.split())
        print(answer)
        if answer == answers[ind - 1][lvl]:
            solved[ind - 1] = True
            res = Label(prob, text="Ответ верный!\nМожешь закрыть это окно", font="Arial 12")
            res.grid(row=3, column=0, padx=5, pady=5)
            # Меняем местами пустую клетку и клетку, по которой кликнули
            board_d[LVL][board_index], board_d[LVL][empty_index] = board_d[LVL][empty_index], board_d[LVL][board_index]
            # Перерисовываем игровое поле
            draw_board()
            # Если текущее состояние доски соответствует правильному - рисуем сообщение о победе
            if board_d[LVL] == correct_board:
                # Эту функцию мы добавим позже
                show_victory_plate()
        else:
            res = Label(prob, text="Ответ не верный!\nПопробуй еще раз!", font="Arial 12")
            res.grid(row=3, column=0, padx=5, pady=5)

    prob = Toplevel()
    prob.title("Реши задачу!")

    size = str(SQUARE_SIZE * BOARD_SIZE)
    prob.geometry(size + "x" + size)
    prob.after(1, lambda: prob.focus_force())

    problem = Label(prob, text=problems[ind - 1][lvl], font="Arial 12")
    problem.grid(row=0, column=0, padx=5, pady=5)
    ans_entry = Entry(prob, width=35)
    ans_entry.after(1, lambda: ans_entry.focus_force())
    ans_entry.grid(row=1, column=0, padx=5, pady=5)
    message_button = Button(prob, text="Проверить", command=check_answer)
    message_button.grid(row=2, column=0, padx=5, pady=5)


def click(event):
    # Получаем координаты клика
    x, y = event.x, event.y
    # Конвертируем координаты из пикселей в клеточки
    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE
    # Получаем индекс в списке объекта по которому мы нажали
    board_index = x + (y * BOARD_SIZE)
    # Получаем индекс пустой клетки в списке. Эту функцию мы напишем позже
    empty_index = get_empty_neighbor(board_index)

    if board_index != empty_index:
        if not solved[board_d[LVL][board_index] - 1]:
            show_problem(board_d[LVL][board_index], board_index, empty_index)
        if solved[board_d[LVL][board_index] - 1]:
            # Меняем местами пустую клетку и клетку, по которой кликнули
            board_d[LVL][board_index], board_d[LVL][empty_index] = board_d[LVL][empty_index], board_d[LVL][board_index]
            # Перерисовываем игровое поле
            draw_board()
            # Если текущее состояние доски соответствует правильному - рисуем сообщение о победе
            if board_d[LVL] == correct_board:
                # Эту функцию мы добавим позже
                show_victory_plate()


c.bind('<Button-1>', click)
c.pack()

board = list(range(1, EMPTY_SQUARE + 1))
correct_board = board[:]
board_d = [
            [3, 2, 7, 5, 1, 6, 4, 8, 9],
            [12, 13, 16, 4, 10, 2, 1, 5, 7, 3, 9, 6, 14, 11, 15, 8]
          ]

draw_board()
root.withdraw()  # Скрываем основное окно, пока показываем окно выбора сложности

root.mainloop()
