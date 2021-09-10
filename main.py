import random









def new_layout():
    row4 = ["X","X","X","X","X"]
    row3 = ["X","X","X","X","X"]
    row2 = ["X","X","X","X","X"]
    row1 = ["X","X","X","X","X"]
    row0 = ["X","X","X","X","X"]



    base_layout = [row0,row1,row2,row3,row4]
    display_base = []
    bomb_count = 0
    current_bombs = []

    while bomb_count <= 3:
        row_bomb = random.randint(0,4)
        column_bomb = random.randint(0,4)
        base_layout[row_bomb][column_bomb] = "O"
        bomb_count += 1
        bomb_placement = [column_bomb,row_bomb]
        current_bombs.append(bomb_placement)


    for i in base_layout[::-1]:
        print(i)
    print(current_bombs)









new_layout()
