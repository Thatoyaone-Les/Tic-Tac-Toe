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
def checkInput(p:str, aM:list)->int:
    if p in map(str, aM):
        return int(p)
    else:
        return 10
