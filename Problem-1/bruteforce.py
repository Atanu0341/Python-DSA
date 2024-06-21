
def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0

    # print('cards:' , cards)
    # print('query:' , query)

    
    # Set up a loop for repetition
    while True:
        # print('position' , position)
        
        # Check if element at the current position matche the query
        if cards[position] == query:
            
            # Answer found! Return and exit..
            return position
        
        # Increment the position
        position += 1
        
        # Check if we have reached the end of the array
        if position == len(cards):
            
            # Number not found, return -1
            return -1

# Testing our function
        
cards = [7,6,5,4,3,2,1]
query = 5

print("The card is located in position",locate_card(cards,query))