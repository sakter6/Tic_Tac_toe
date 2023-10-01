#prolog
#Samia Akter
#sakter6@student.gsu.edu
#section:28
#lab 6

def main():
    # Initialize row vaeiables
    row0= input('ROW0>')
    row1= input('ROW1>')
    row2= input('ROW2>')

    Horizontal = False
    Vertical = False
    Diagonal = False

    #check to see if x wins horizontally
    if row0[0]==row0[1]==row0[2]=='X' or row1[0]==row1[1]==row1[2]=='X' or row2[0]==row2[1]==row2[2]=='X':
        Horizontal = True
        print(' X IS GOOD IN HORIZONTAL')
    # Check to see if o win horizontally
    elif row0[0]==row0[1]==row0[2]=='O' or row1[0]==row1[1]==row1[2]=='O' or row2[0]==row2[1]==row2[2]=='O':
        Horizontal = True
        print('O IS GOOD IN HORIZONTAL')

    #Check to see if x wins vertically
    if row0[0]==row1[0]==row2[0]=='X' or row0[1]==row1[1]==row2[1]=='X' or row0[2]==row1[2]==row2[2]=='X':
        Vertical = True
        print('X IS GOOD IN VERTICAL')
    # Check to see if O win vertically
    elif row0[0]==row1[0]==row2[0]=='O' or row0[1]==row1[1]==row2[1]=='O' or row0[2]==row1[2]==row2[2]=='0':
        Vertical = True
        print('O IS GOOD IN VERTICAL')
        
    # Check to see if x win diagonally
    if row1[1]=='X':
        if row0[0]=='X' and row2[2]=='X':
            Diagonal = True
            print('X IS GOOD IN DIAGONAL')
    # Check to see if O win diagonally
    elif row1[1]=='O':
        if row0[0]=='O' and row2[2]=='O':
           Diagonal = True
           print('O IS GOOD IN DIAGONAL')

    #tie
    if Horizontal==False and Vertical==False and Diagonal==False:
        print('THIS IS TIE')
main()
        
