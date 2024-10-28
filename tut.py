game  = [[1, 0, 1],
         [0, 2, 0],
         [2, 2, 0]]

def win(current_game):
    for row in current_game:
        print(row)
        
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Congrats jackass")

win(game)
