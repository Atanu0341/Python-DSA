
# O(N) ---- Worst Case

def locate_card(cards, query):
    position=0

    print('cards:' , cards)
    print('query:' , query)

    while position < len(cards):
        print('position' , position)
        if cards[position]==query:
            return position
        position +=1
    return -1

cards=[9,8,7,6,5]
query=5
print("The card is located in position",locate_card(cards,query))