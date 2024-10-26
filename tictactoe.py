game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try: 
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Make sure you put row/column as 0,1 or 2 ?",e)
    except Exception as e:
        print("You did something very wrong, SKILL ISSUE !",e)

game_map = game_board(game, just_display=True)
game_map = game_board(game_board, player=1, row=2, column=1)
