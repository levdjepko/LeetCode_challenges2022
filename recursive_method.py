

def go_right(coordinate_x):
    if coordinate_x == 10:
        return
    else:
        coordinate_x += 1
        print(coordinate_x)
        go_right(coordinate_x)
x = 1
go_right(x)
