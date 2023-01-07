#Shernice Oh Yu En(S10204037B)-P09
import random

buildings=['HSE','FAC','SHP','HWY','BCH']
building_count={"HSE":8,"FAC":8,"SHP":8,"HWY":8,"BCH":8}
building_list=[]
building_per_total=8
current_building_list=[]
building1=''
building2=''

#---------------------------------------------------------------------------------------------------------------------------------------------------------
def building():
    for count in range(building_per_total):
        for b in buildings:
            building_list.append(b)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#This function is to Randomize the Buildings
def take_building():
    global building1
    global building2

    #If turn reaches 16, the Game will be over
    if turn==16:
        global game_over
        game_over=True
        return

    current_building_list.clear()

    #Randomize Building 1
    index=random.randint(0,len(building_list)-1)
    building1=building_list[index]
    current_building_list.append(building_list.pop(index))
    building_count[building1]-=1

    #Randomize Building 2 
    index=random.randint(0,len(building_list)-1)
    building2=building_list[index]
    current_building_list.append(building_list.pop(index))
    building_count[building2]-=1

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#1. Display main menu - First Game Menu
#2.5. Exit to Main Menu
def game_menu():
    print("Welcome, mayor of Simp City!")
    print("----------------------------")
    print("1. Start new game")
    print("2. Load saved game\n")
    print("0. Exit")

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#To print the Game Board and, Final Layout once the game is over.
#1.1. Start New Game (Display to start a new game)
#Also displays 3. End of Game
def show_game():    
    print()
    global board,turn
    if turn<=16:
        print("Turn",turn)
    else:
        print("Final layout of Simp City:")
        print("     A     B     C     D")
        print("  +-----+-----+-----+-----+")
        for row in range(1,5):
            print(" {}".format(row),end='')
            for column in range(1,5):
                print("| {:4}".format(board[row][column]),end='')
            print('|')

            print("  +-----+-----+-----+-----+")

        computeScore()

    #To display the Game Board
    print("     A     B     C     D")
    print("  +-----+-----+-----+-----+")
    for row in range(1,5):
        print(" {}".format(row),end='')
        for column in range(1,5):
            print("| {:4}".format(board[row][column]),end='')
        print('|')

        print("  +-----+-----+-----+-----+")

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#To Display the Second Game Menu after Starting the Game
#1.3. Exit Game
def display_game_menu():
    take_building()
    print("1. Build a {}".format(building1))
    print("2. Build a {}".format(building2))
    print("3. See remaining buildings")
    print("4. See current score\n")
    print("5. Save Game")
    print("0. Exit to main menu")

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#1.2. Load Saved Game
def load_game():
    global turn
    file=open("game.txt",'r')
    turn=int(file.readline())
    row=0
    for line in file:
        line=line.strip('\n')                           
        data_list=line.split(',')                       
        for column in range(0,6):
            board[row][column]=data_list[column]
        row+=1
        if row==6:
            break
        
    file.close()
    start_new_game()  
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#2.4. Save Game    
def save_game():
    file=open("game.txt",'w')

    file.write(str(turn) + '\n')
    for row in range(0,6):
        data=""
        for column in range(0,6):
            data=data+board[row][column] + ','
        file.write(data + '\n')

    file.write(str(buildings)+'\n')
    file.write(str(building_count)+'\n')
    file.write(str(building_list)+'\n')
    
    
    file.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#2.Playing the Game
#2.1. Build a Building  
def start_new_game():
    global turn

    quit=False
    while not quit:
        show_game()
        display_game_menu()
        choice=input("Your choice?")

        if choice=='1':
            location=input("Build where?")
            row=int(location[1])
            column=ord(location[0].upper())-ord('A')+1
            
            #Validation for wrong input of location
            if row>4 or row<1 or column>4 or column<1:
                print("Please input the correct Location.")
                continue

            #Validation for when building input is not next to an existing building
            if turn!=1 and board[row][column-1]=="   " and board[row][column+1]=="   " and board[row-1][column]=="   " and board[row+1][column]=="   ":
                print("You must build next to an existing building.")
                continue

            #Validation for when the space is already occupied.
            if board[row][column]!="   ":
                print("This space is occupied.")
                
            else:
                board[row][column]=building1
                turn+=1
                
        elif choice=='2':
            location=input("Build where?")
            row=int(location[1])
            column=ord(location[0].upper())-ord('A')+1

            #Validation for wrong input of location.
            if row>4 or row<1 or column>4 or column<1:
                print("Please input the correct Location.")
                continue

            #Validation for when building input is not next to an existing building.
            if turn!= 1 and board[row][column-1]=="   " and board[row][column+1]=="   " and board[row-1][column]=="   " and board[row+1][column]=="   ":
                print("You must build next to an existing building.")
                continue

            #Validation for when the space is already occupied.
            if board[row][column]!="   ":
                print("This space is occupied.")
                
            else:
                board[row][column]=building2
                turn+=1
                
        elif choice=='3':
            print("\n")
            remaining_building()
        elif choice=='4':
            print("\n")
            computeScore()
        elif choice=='5':
            save_game()
        elif choice=='0':
            quit=True
        else:
            print("Please Choose the Choice Listed Above.")

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#2.2. See Remaining Buildings
def remaining_building():
    print("{:10s}{:5s}{:10s}".format('Building',' ','Remaining'))
    print("{:10s}{:5s}{:10s}".format('--------',' ','---------'))
    for building in building_count:
        print("{:10s}{:5s}{:<10d}".format(building,' ',building_count[building]))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#2.3. See Currrent Score
def computeScore():
    building_score={'HSE':[],'FAC':[],'SHP':[],'HWY':[],'BCH':[]}

    #Score for 4.2. Factory (FAC)
    count=0
    for row in range(1,5):
        for column in range(1,5):
            if board[row][column]=='FAC':
                count+=1
    for i in range(count):
        if count<=4:
            building_score['FAC'].append(count)
        else:
            building_score['FAC'].append(count)
            building_score['FAC'].append(1) 

    #Score for BCH, SHP, HWY, HSE
    for row in range(1,5):
        for column in range(1,5):

            #Score for 4.1. Beach (BCH)
            if board[row][column]=='BCH':
                if column==1 or column==4:
                    building_score['BCH'].append(3)
                else:
                    building_score['BCH'].append(1)

            #Score for 4.4. Shop (SHP)
            elif board[row][column]=='SHP':
                adj_list=[]
                adj_list.append(board[row-1][column])
                if board[row+1][column] not in adj_list:
                    adj_list.append(board[row+1][column])
                if board[row][column-1] not in adj_list:
                    adj_list.append(board[row][column-1])
                if board[row][column+1] not in adj_list:
                    adj_list.append(board[row][column+1])
                if '   ' in adj_list:
                    adj_list.remove('   ')
                building_score['SHP'].append(len(adj_list))

            #Score for 4.5. Highway (HWY)
            elif board[row][column]=='HWY':
                #building to the left is HWY - skip beacuse this is counted already
                if board[row][column-1]=='HWY':
                    continue

                score=0
                while board[row][column]=='HWY':
                    score+=1
                    column+=1
                for squares in range(score):
                    building_score['HWY'].append(score)
        

            #Score for 4.3. House (HSE)            
            elif board[row][column]=='HSE':
                if board[row][column+1]=='FAC' and board[row][column-1]=='FAC' and board[row+1][column]=='FAC' and board[row-1][column]=='FAC':
                    building_score['HSE'].append(1)
                
                
                elif board[row][column+1]=='HSE' or board[row][column-1]=='HSE' or board[row+1][column]=='HSE' or board[row-1][column]=='HSE' or \
                     board[row][column+1]=='SHP' or board[row][column-1]=='SHP' or board[row+1][column]=='SHP' or board[row-1][column]=='SHP':
                    building_score['HSE'].append(1)

                    
                if board[row][column+1]=='BCH' or board[row][column-1]=='BCH' or board[row+1][column]=='BCH' or board[row-1][column]=='BCH':
                    building_score['HSE'].append(2)

                                    
    #Scores for each type of building and the total score
    total_score=0
    for key in building_score:
        building_type=key
        score_list=building_score[key]
        print(building_type, end=' : ')

        for index in range(len(score_list)):
            if index!=(len(score_list)-1):
                print(score_list[index],end=' + ')
            else:
                print(score_list[index],end=' = ')                
        print(sum(score_list))
        total_score+=sum(score_list)
    print('Total Score:',total_score)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------    
#Main Program
    
board=[['   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   '],
       ['   ','   ','   ','   ','   ','   ']]

turn=1
building()

while True:
    game_menu()
    choice=int(input("Your choice?"))
    if choice==1:
        start_new_game()
    elif choice==2:
        load_game()
    elif choice==0:
        print("Bye.")
        break
    else:
        print("Please choose either Option 1 or 2 or 0.\n")
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


    
