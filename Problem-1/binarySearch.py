
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        print("lo:", lo, "hi:", hi, "mid:", mid, "mid_number:", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid-1
        elif mid_number > query:
            lo = mid+1

    return -1

cards=[9,8,8,8,7,7,6,5,4,3,2,1]
query=7
print("The card is located in position",locate_card(cards,query))

# repeted numbers will not work