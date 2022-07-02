chodniki = []
def uloz(lst,k,chod):
    x = len(chod)
    available_moves = []
    if x == k:
        if chod not in chodniki:
            chodniki.append(chod)
            return
    if x == 0:
        if lst[0] > 0:
            chod = [1]
            lst[0] -= 1
            uloz(lst, k, chod)
    else:
        for i in range(len(lst)):
            if (x+1)%(i +1) == 0 and lst[i] > 0:
                available_moves.append(i+1)
        for choice in available_moves:
            lol = lst[:choice-1]+[lst[choice -1] -1]+lst[choice:]
            chodn = chod + [choice]
            uloz(lol, k, chodn)
        return

uloz([8, 4, 2, 2, 1, 1, 1, 1], 8, [])
#ostateczną listę kombinacji zawarłem w liście chodniki, aby uzyskac wynik należy wydrukować długość tej listy.
print(len(chodniki))
