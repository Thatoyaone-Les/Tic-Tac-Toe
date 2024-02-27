
def gameState(moves):
    print(f'\n{moves[6]} \t {moves[7]} \t {moves[8]} \n\n{moves[3]} \t {moves[4]} \t {moves[5]} \n\n{moves[0]} \t {moves[1]} \t {moves[2]} \n')

def findall(items: list, list: list)->bool:
    t = []
    for i in items:
        if i in list:
            t.append('true')
            continue
        else:
            t.append('false')

    if 'false' in t:
        return False
    else:
        return True

def blocKMove(pM:list, bM:list, win:list)->None:
    for pos, data  in enumerate(bM):
        if findall(data, pM):
            match pos:
                case 0 | 1 | 2 :
                    delete(win[0], data)
                    ## comp will pick remaining number.
                case _:
                    pass
        else:
            return False
        
def delete(sL:list, bL:list)->None:
    for x in sL:
        bL.remove(x)

def gameOn(playAgain = True):
    moves = [x for x in range(1, 10)]
    availMoves = [x for x in range(1, 10)]
    playerX = []
    playerO = []
    winners = [[1,2,3], [1,5,9], [1,4,7], [4,5,6], [7,8,9], [7,5,3], [8,5,2], [9,6,3]]
    blockMoves = [[1,2], [1, 3], [2, 3], [1, 5], [1, 9], [5, 9], [1, 4], [1, 7], [4,7], [4, 5], [4, 6], [5, 6], [7, 8], [7, 9], [8, 9], [7, 5], [7, 3], [5, 3], [8, 5], [8, 2], [5, 2],[9, 6], [9, 3], [6, 3]]
    while(len(availMoves)> 0 and playAgain == True):
        if len(availMoves) % 2 == 1:
            gameState(moves)
            pick = int(input("Player X select number: "))
            while pick not in availMoves:
                pick = int(input(f"invalid input Player X select number from {availMoves}: "))
            else:
                moves[pick-1] = 'X'
                playerX.append(pick)
                availMoves.remove(pick)
            for x in winners:
                if findall(x, playerX):
                    gameState(moves)
                    print("player X wins\n")
                    break
            else:
                continue
            break
                    

        else:
            gameState(moves)
            pick = int(input("Player O select number: "))
            while pick not in availMoves:
                pick = int(input(f"invalid input Player O select number from {availMoves}: "))
            else:
                moves[pick-1] = 'O'
                playerO.append(pick)
                availMoves.remove(pick)
            for x in winners:
                if findall(x, playerO):
                    gameState(moves)
                    print("player O wins\n")
                    break
            else:
                continue
            break
        

    else:
        gameState(moves)
        #print(f'player X moves = {playerX}\nplayer O moves = {playerO}')
        print("Its's a tie!!")

if __name__ == '__main__':
    gameOn(True)
    an = input("Do you want to play again [Y] or [N]: ")
    if an.upper() == 'Y' or an.upper() == 'YES':
        gameOn(True)
    else:
        exit()
