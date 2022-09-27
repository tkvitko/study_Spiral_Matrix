def go_right(start_pos, value, list):
    """
    Fill values "to the right"
    """
    x, y = start_pos[0], start_pos[1]  # coordinates of start position

    while y < len(list):  # while the edge have not been reached
        if list[x][y] == 0:  # if this position has not been filled
            list[x][y] = value  # filling
        else:
            break  # if already filled
        y += 1
        value += 1

    next_pos = [x + 1, y - 1]  # returns next position to the next function
    return next_pos, value


def go_down(start_pos, value, list):
    """
    Fill values "to the down"
    """
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
    """
    Fill values "to the left"
    """
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
    """
    Fill values "to the up"
    """
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
    """
    Function returns "next" direction to the current (already filled) direction
    """

    order = [go_right, go_down, go_left, go_up]

    next_pos = order.index(direction) + 1

    try:
        next_direction = order[next_pos]
    except IndexError:
        next_direction = order[0]
    return next_direction


if __name__ == '__main__':

    size = int(input('Enter the size of the matrix: '))

    matrix = [[0 for i in range(size)] for i in range(size)]

    # Initial data
    direction = go_right
    pos = [0, 0]
    value = 1
    step = 0

    while step < size * 2:  # 2n steps are enough to fill in the matrix
        new_pos, new_value = direction(pos, value, matrix)
        direction = change_direction(direction)
        pos = new_pos
        value = new_value
        step += 1

    for line in matrix:
        print(line)
