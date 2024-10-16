
import classes as cl
def gameOn(playAgain = True):
    moves = [x for x in range(1, 10)]
    availMoves = [x for x in range(1, 10)]
    playerX = []
    playerO = []
    winners = [[1,2,3], [1,5,9], [1,4,7], [4,5,6], [7,8,9], [7,5,3], [8,5,2], [9,6,3]]
    blockMoves = [[1,2], [1, 3], [2, 3], [1, 5], [1, 9], [5, 9], [1, 4], [1, 7], [4,7], [4, 5], [4, 6], [5, 6], [7, 8], [7, 9], [8, 9], [7, 5], [7, 3], [5, 3], [8, 5], [8, 2], [5, 2],[9, 6], [9, 3], [6, 3]]
    #getting number of players
    num_players  = input('Play against another player PRESS[2] or against our AI PRESS[1]? : ')
    if num_players == str(1):
        f_p = input("PRESS[1] to go first or PRESS[2] to play after AI: ")
        if f_p == str(1):
            while(len(availMoves)> 0 and playAgain == True):
                cl.gameState(moves)
                pick = input("Player[1] select number: ")
                if len(availMoves) % 2 == 1:
                    cl.gameState(moves)
                    pick = input("Player[1]select number: ")
                    while pick not in availMoves:
                        pick = int(input(f"invalid input Player[1] select number from {availMoves}: "))
                    else:
                        moves[pick-1] = 'X'
                        playerX.append(pick)
                        availMoves.remove(pick)
                    for x in winners:
                        if cl.findall(x, playerX):
                            cl.gameState(moves)
                            print("player[1] wins\n")
                            break
                    else:
                        continue
                    break
        else:
            print("playing AI first")
    else:
        while(len(availMoves)> 0 and playAgain == True):
            if len(availMoves) % 2 == 1:
                cl.gameState(moves)
                pick = input("Player X select number: ")
                pick = cl.checkInput(pick, availMoves)
                while pick not in availMoves:
                    pick = input(f"invalid input Player X select number from {availMoves}: ")
                    pick = cl.checkInput(pick, availMoves)
                    
                else:
                    moves[pick-1] = 'X'
                    playerX.append(pick)
                    availMoves.remove(pick)
                for x in winners:
                    if cl.findall(x, playerX):
                        cl.gameState(moves)
                        print("player X wins\n")
                        break
                else:
                    continue
                break
                        

            else:
                cl.gameState(moves)
                pick = input("Player O select number: ")
                pick = cl.checkInput(pick, availMoves)
                while pick not in availMoves:
                    pick = input(f"invalid input Player O select number from {availMoves}: ")
                    pick = cl.checkInput(pick, availMoves)
                else:
                    moves[pick-1] = 'O'
                    playerO.append(pick)
                    availMoves.remove(pick)
                for x in winners:
                    if cl.findall(x, playerO):
                        cl.gameState(moves)
                        print("player O wins\n")
                        break
                else:
                    continue
                break
            

        else:
            cl.gameState(moves)
            #print(f'player X moves = {playerX}\nplayer O moves = {playerO}')
            print("Its's a tie!!")

if __name__ == '__main__':
    gameOn(True)
    an = input("Do you want to play again [Y] or [N]: ")
    if an.upper() == 'Y' or an.upper() == 'YES':
        gameOn(True)
    else:
        exit()
