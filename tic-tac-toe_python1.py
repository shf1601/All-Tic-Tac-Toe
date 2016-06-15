"""
 Created by Samuel Fleischer on 6/10/16
 Tic Tac Toe game
"""

board = [" A B C",
         "1 | | ",
         " _|_|_",
         "2 | | ",
         " _|_|_",
         "3 | | ",
        ]

game_dict = { "A1": "", "A2" : "", "A3": "",
              "B1": "", "B2" : "", "B3": "",
              "C1": "", "C2" : "", "C3": "" }
             
win_combos = (("A1", "A2", "A3"),
               ("B1", "B2", "B3"),
               ("C1", "C2", "C3"),
               ("A1", "B1", "C1"),
               ("A2", "B2", "C2"),
               ("A3", "B3", "C3"),
               ("A1", "B2", "C3"),
               ("A3", "B2", "C1"))      
                          
X_TURN = 0
O_TURN = 1

        
def draw_board():
    for thing in board:
        print thing

def getLocation(turn):
    location = ""
    if turn == X_TURN:
        location = str(raw_input("Place X: ")).upper()
    elif turn == O_TURN:
        location = str(raw_input("Place O: ")).upper()
    
    print ""  
    return location

def makeList(string):
    lst = list()
    for letter in string:
        lst.append(letter)
    return lst

def placeStringInLocation(string, location):
    str_index = {"A": 1, "B" : 3, "C" : 5}.get(location[0])
    board_index = {"1" : 1, "2" : 3, "3" : 5}.get(location[1])
    board_string_list = makeList(board[board_index])
    board_string_list[str_index] = string
    board[board_index] = "".join(board_string_list)
    
def checkForWin():
    for combo in win_combos:
        string = game_dict[combo[0]]
        if string == "":
            continue
        for position in combo:
            if string != game_dict[position]:
                break
                
        else:
            return string + "'s wins!"
        
    for value in game_dict.values():
        if value == "":
            break
    else:
        return "Tie game"
                
    return None
            
       
def main():
    
    turn = X_TURN    
    done = False
    
    draw_board()
    
    #the loop for the game
    while not done:
              
        valid = False
        empty = False
        #keep looping until the user puts in valid input
        while not valid and not empty:
            try:
                location = getLocation(turn)
                value = game_dict[location]
            except KeyError:
                print "Invalid location. Another one."
                continue
            else :
                valid = True
                empty = value == ""
                if not empty:
                    print "Space not empty. Another one."
        
        #Place the X or O in the game dictionary and board
        if turn == X_TURN:
            game_dict[location] = "X"
            placeStringInLocation("X", location)
        elif turn == O_TURN:
            game_dict[location] = "O" 
            placeStringInLocation("O", location)
            
        draw_board()
        
        #Check to see if someone won. If somebody won, end game and display winner. If no one wins, switch turns
        if checkForWin():
            done = True
            print checkForWin()
        elif turn == X_TURN :
            turn = O_TURN
        elif turn == O_TURN :
            turn = X_TURN
               
            
main()
