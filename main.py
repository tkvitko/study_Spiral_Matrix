def go_right(start_pos, value, list):
    # Функция заполнения данных "направо"
    x, y = start_pos[0], start_pos[1]  # координаты стартовой точки

    while y < len(list):  # пока не достигли края
        if list[x][y] == 0:  # если точка еще не заполнена
            list[x][y] = value  # заполняем
        else:
            break  # если заполнена, конец направления
        y += 1
        value += 1

    next_pos = [x + 1, y - 1]  # возвращаем следующую позицию следующей функции
    return next_pos, value


def go_down(start_pos, value, list):
    # Функция заполнения данных "вниз"
    x, y = start_pos[0], start_pos[1]

    while x < len(list):
        if list[x][y] == 0:
            list[x][y] = value
        else:
            break
        x += 1
        value += 1

    next_pos = [x - 1, y - 1]
    return next_pos, value


def go_left(start_pos, value, list):
    # Функция заполнения данных "налево"
    x, y = start_pos[0], start_pos[1]

    while y >= 0:

        if list[x][y] == 0:
            list[x][y] = value
        else:
            break
        y -= 1
        value += 1

    next_pos = [x - 1, y + 1]
    return next_pos, value


def go_up(start_pos, value, list):
    # Функция заполнения данных "вверх"
    x, y = start_pos[0], start_pos[1]

    while x > 0:

        if list[x][y] == 0:
            list[x][y] = value
        else:
            break
        x -= 1
        value += 1

    next_pos = [x + 1, y + 1]
    return next_pos, value


def change_direction(direction):
    # Функция вернет следующее направление для текущего (отработавшего) направления

    order = [go_right, go_down, go_left, go_up]

    next_pos = order.index(direction) + 1

    try:
        next_direction = order[next_pos]
    except IndexError:
        next_direction = order[0]
    return next_direction


if __name__ == '__main__':

    size = int(input('Введите размер матрицы: '))

    matrix = [[0 for i in range(size)] for i in range(size)]

    # Стартовые данные
    direction = go_right
    pos = [0, 0]
    value = 1
    step = 0

    while step < size * 2:  # Для заполнения матрицы достаточно 2n шагов
        new_pos, new_value = direction(pos, value, matrix)
        direction = change_direction(direction)
        pos = new_pos
        value = new_value
        step += 1

    for line in matrix:
        print(line)
