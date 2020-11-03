# Author: Kylie Chambers
# Date: 3/12/2020
# Description: A chinese chess game following the standard rules for Xiangqi, with moving pieces,
# checks for being in check and winning the game, and updates which players turn it is and if the
# game has been won.

class XiangqiGame:
    def __init__(self):
        """
        Initializes a new chess board
        """
        # board property, 2Darray containing pieces
        self.__board = set_board()  # creates and sets the board

        # winner property, always set to UNFINISHED initially, can change to RED_WON or BLACK_WON
        self.__finish_state = "UNFINISHED"

        # other properties...
        self.__current_player = 'red'

    # function that prints out the board
    def print_board(self):
        for i in self.__board:
            print(i)
        print("Current state: " + self.__finish_state)
        print("Current player: " + self.__current_player)

    # function that returns the current state of the game
    def get_game_state(self):
        return self.__finish_state

    # function that returns True if a player is in check (else False)
    # takes in parameter self as well as player, which should be set
    # to either red or black
    def is_in_check(self, player):
        player_locations = []  # holds the coordinates of all the pieces of the other player
        general_location = ()  # holds the coordinates of the general of the current player

        ### FIND GENERAL AND OTHER PLAYER'S PIECES ###
        for x in range(0, 10):  # go through the 10 rows of the board
            for y in range(0, 9):  # go through the 11 columns of the board
                if (player == "red" and self.__board[x][y] == "Gr") or (
                        player == "black" and self.__board[x][y] == "Gb"):
                    general_location = (x, y)
                if (player == "red" and "b" in self.__board[x][y]) or (player == "black" and "r" in self.__board[x][y]):
                    player_locations.append((x, y))

        ### CONVERT COORDINATES ###
        rows = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

        # convert general's location using the arrays rows and columns
        general_location = columns[general_location[1]] + rows[general_location[0]]

        # convert other player's locations

        converted_locations = []
        for x in player_locations:  # get one coordinate at a time from player_locations
            converted_locations.append(columns[x[1]] + rows[x[0]])  # add the converted location to the new array

        ### SEE IF ANY PIECES CAN MOVE TO THE GENERAL'S LOCATION ###
        for x in converted_locations:
            if self.can_move(general_location, x) == True:  # a piece can move to capture the general
                return True  # return True, the general is in check!
        return False  # no piece can capture the general, he's safe!

    def make_move(self, to, frm):
        """
        accepts the spot the piece being moved is in, and the space to move it to
        and moves the piece, while replacing the from spot with an empty space
        """
        # check if self.__finish_state is UNFINISHED. if so...
        if self.__finish_state == 'UNFINISHED':
            ### CHECK IF THE PIECE CAN MOVE ###
            if self.can_move(to, frm) == False:
                print("This move is not valid.")
                return False

            if self.can_move(to, frm) == True:
                ### MOVE THE PIECE ###
                rows = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
                columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
                # convert 'to' to real coordinates
                x = 0
                y = 0

                for i in range(0, 9):
                    if to[0] == columns[i]:
                        y = i

                for i in range(0, 10):
                    if to[1:] == rows[i]:
                        x = i

                to = (x, y)

                # convert 'frm' to real coordinates
                for i in range(0, 9):
                    if frm[0] == columns[i]:
                        y = i

                for i in range(0, 10):
                    if frm[1:] == rows[i]:
                        x = i

                frm = (x, y)

                ### CHANGE THE POSITION OF THE PIECE ###
                self.__board[to[0]][to[1]] = self.__board[frm[0]][frm[1]]
                # set the board at 'frm' to '--'
                self.__board[frm[0]][frm[1]] = '--'

                ### CHANGE PLAYERS ###
                if self.__current_player == 'red':
                    self.__current_player == 'black'
                    # check for checkmate
                    if self.check_endgame() == True:
                        print('Red player won!')
                    else:
                        print('Black player: Your turn')
                if self.__current_player == 'black':
                    self.__current_player == 'red'
                    if self.check__endgame() == True:
                        print('Black player won!')
                    else:
                        print('Red player: Your turn')
                return True
            return False  # piece cannot move
        return False  # game is already over!

    def fake_check(self, to, frm):
        """
        moves to to frm and checks if the copied board leaves
        the general in check
        """
        rows = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        # convert 'to' to real coordinates
        x = 0
        y = 0

        for i in range(0, 9):
            if to[0] == columns[i]:
                y = i

        for i in range(0, 10):
            if to[1:] == rows[i]:
                x = i

        to = (x, y)

        # convert 'frm' to real coordinates
        for i in range(0, 9):
            if frm[0] == columns[i]:
                y = i

        for i in range(0, 10):
            if frm[1:] == rows[i]:
                x = i

        frm = (x, y)

        for x in self.__board:
            new_board.append(x.copy())
        new_board[to[0]][to[1]] = new_board[frm[0]][frm[1]]
        new_board[frm[0]][frm[1]] = '--'
        player = self.__current_player
        player_locations = []  # holds the coordinates of all the pieces of the other player
        general_location = ()  # holds the coordinates of the general of the current player

        ### FIND GENERAL AND OTHER PLAYER'S PIECES ###
        for x in range(0, 10):  # go through the 10 rows of the board
            for y in range(0, 9):  # go through the 11 columns of the board
                if (player == "red" and new_board[x][y] == "Gr") or (
                        player == "black" and new_board[x][y] == "Gb"):
                    general_location = (x, y)
                if (player == "red" and "b" in new_board[x][y]) or (player == "black" and "r" in new_board[x][y]):
                    player_locations.append((x, y))

        ### CONVERT COORDINATES ###
        rows = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

        # convert general's location using the arrays rows and columns
        general_location = columns[general_location[1]] + rows[general_location[0]]

        # convert other player's locations

        converted_locations = []
        for x in player_locations:  # get one coordinate at a time from player_locations
            converted_locations.append(columns[x[1]] + rows[x[0]])  # add the converted location to the new array

        ### SEE IF ANY PIECES CAN MOVE TO THE GENERAL'S LOCATION ###
        for x in converted_locations:
            if self.can_move(general_location, x) == True:  # a piece can move to capture the general
                return True  # return True, the general is in check!
        return False  # no piece can capture the general, he's safe!

    def check_endgame(self):
        """
        finds every single current location of the current player's pieces.
        brings it to every single location on the board. sees if it is possible
        to move there. if it is, makes a copy of the board with it there and checks
        if it is still in check. If it is still in check, don't do anything.
        If it is no longer in check, return False. If you get out of
        this loop, there is a winner! somebody has been checkmated. Set the
        game state to the winner
        """
        ### GET ALL THE PLAYER'S PIECES ###
        piece_tracker = []
        for x in range(0, 10):
            for y in range(0, 9):
                if self.__current_player[0] == self.__board[x][y][1]:
                    piece_tracker.append((x, y))

        ### CONVERT COORDINATES ###
        rows = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        converted_locations = []
        for x in piece_tracker:  # get one coordinate at a time from piece_tracker
            converted_locations.append(columns[x[1]] + rows[x[0]])

            ### CHECK IF PIECES CAN MOVE ANYWHERE ###
        # create a for loop that loops through every converted_location
        for x in converted_locations:
            for y in rows:
                for z in columns:
                    if self.can_move(z + y, x) == True:
                        # check if moving the piece gets the general out
                        # of check
                        if self.fake_check(z + y, x) == False:
                            # return False, the game is not over
                            return False
        # none of the pieces can move to get us out of check
        # change the state of the game (self.__finish_state) to
        # RED_WON if current_player is 'black' or BLACK_WON if cur_p is 'red'
        if self.__current_player == 'black':
            self.__finish_state = 'RED_WON'
        if self.__current_player == 'red':
            self.__finish_state = 'BLACK_WON'
        return True
        # return True, the game is over

    def general_facing(self, to, frm):
        for x in self.__board:
            new_board.append(x.copy())
        new_board[to[0]][to[1]] = new_board[frm[0]][frm[1]]
        new_board[frm[0]][frm[1]] = '--'
        player_locations = []  # holds the coordinates of all the pieces of the other player
        gR_loc = ()  # holds the coordinates of one general
        gB_loc = ()
        ### FIND GENERALS AND OTHER PPIECES ###
        for x in range(0, 10):  # go through the 10 rows of the board
            for y in range(0, 9):  # go through the 11 columns of the board
                if new_board[x][y] == "Gr":
                    gR_loc = (x, y)
                if new_board[x][y] == "Gb":
                    gB_loc = (x, y)
                elif new_board[x][y] != '--':
                    player_locations.append((x, y))
        # check if the columns of the generals are the same
        if gR_loc[1] != gB_loc[1]:
            return False  # if they aren't, return False

        for x in player_locations:  # if they are, loop through all the other pieces
            if x[1] == gR_loc[1]:
                return False
        return True
        # check the column number of all the other pieces and see
        # if it matches the column of the generals
        # if it does, return False
        # outside the loop, return True because
        # the generals are facing with nothing blocking them

    def can_move(self, to, frm):
        rows = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        # convert 'to' to real coordinates
        x = 0
        y = 0

        for i in range(0, 9):
            if to[0] == columns[i]:
                y = i

        for i in range(0, 10):
            if to[1:] == rows[i]:
                x = i

        to = (x, y)

        # convert 'frm' to real coordinates
        for i in range(0, 9):
            if frm[0] == columns[i]:
                y = i

        for i in range(0, 10):
            if frm[1:] == rows[i]:
                x = i

        frm = (x, y)

        if self.__board[frm[0]][frm[1]] == '--':
            return False

        # check if the board at to has a piece in it
        # does the piece's second letter match the frm piece's first letter?
        # if so, return False

        if self.__board[to[0]][to[1]] != '--':
            if self.__board[to[0]][to[1]][1] == self.__board[frm[0]][frm[1]][1]:
                return False


        if self.__board[frm[0]][frm[1]][0] == 'G':
            return self.general_move(to, frm)

        if self.__board[frm[0]][frm[1]][0] == 'A':
            return self.advisor_move(to, frm)

        if self.__board[frm[0]][frm[1]][0] == 'E':
            return self.eleph_move(to, frm)

        if self.__board[frm[0]][frm[1]][0] == 'H':
            return self.horse_move(to, frm)

        if self.__board[frm[0]][frm[1]][0] == 'R':
            return self.rook_move(to, frm)

        if self.__board[frm[0]][frm[1]][0] == 'C':
            return self.cannon_move(to, frm)

        if self.__board[frm[0]][frm[1]][0] == 'P':
            return self.pawn_move(to, frm)

        else:
            return False

    def general_move(self, to, frm):
        """
        Checks if the general can move from frm to to. Must stay in the palace
        and can only move orthogonally one at a time.
        """
        if to[0] == frm[0]:  # if the x coord didn't change
            if to[1] != frm[1] + 1 and to[1] != frm[1] - 1:  # check y coord
                return False  # bc the above statement MUST be true for a move to be possible
        elif to[1] == frm[1]:  # if the y coord didn't change
            if to[0] != frm[0] + 1 and to[0] != frm[0] - 1:  # check x coord
                return False
        else:  # general is moving to an invalid space
            return False
        if to[1] >= 3 or to[1] <= 5:  # check palace
            if (to[0] >= 0 and to[0] <= 2) or (to[0] >= 8 and to[0] <= 10):
                if self.general_facing(to, frm) == True or self.fake_check(to, frm) == True:
                    return False
                else:
                    return True
            else:  # general is moving to an invalid row
                return False
        else:  # general is moving to an invalid column
            return False

    def advisor_move(self, to, frm):
        # make sure they stay in the palace
        if to[1] >= 3 or to[1] <= 5:
            if (to[0] >= 0 and to[0] <= 2) or (to[0] >= 8 and to[0] <= 10):
                # make sure they're only moving one diagonally
                if (to[0] == frm[0] + 1 or to[0] == frm[0] - 1) and (to[1] == frm[1] + 1 or to[1] == frm[1] - 1):
                    if self.general_facing(to, frm) == True or self.fake_check(to, frm) == True:
                        return False  # generals are facing due to this move or are left in check
                    else:  # valid move!
                        return True
                else:  # not moving one diagonally
                    return False
            else:  # not in the palace rows
                return False
        else:  # not in the palace columns
            return False

    def eleph_move(self, to, frm):
        # makes sure the move does not cross the river
        if self.__board[frm[0]][frm[1]][1] == 'b':
            if to[0] >= 5:
                return False
        if self.__board[frm[0]][frm[1]][1] == 'r':
            if to[0] <= 4:
                return False
        # checks if piece is moving up and left diagonally and if there is a piece between
        if to[0] == frm[0] + 2 and to[1] == frm[1] - 2:
            if self.__board[frm[0] + 1][frm[1] - 1] == '--':
                if self.general_facing(to, frm) == True:
                    return False
                return True
        # checks if piece is moving up and right diagonally and if there is a piece between
        if to[0] == frm[0] + 2 and to[1] == frm[1] + 2:
            if self.__board[frm[0] + 1][frm[1] + 1] == '--':
                if self.general_facing(to, frm) == True:
                    return False
                return True
        # checks if piece is moving down and left diagonally and if there is a piece between
        if to[0] == frm[0] - 2 and to[1] == frm[1] - 2:
            if self.__board[frm[0] - 1][frm[1] - 1] == '--':
                if self.general_facing(to, frm) == True:
                    return False
                return True
        # checks if piece is moving down and right diagonally and if there is a piece between
        if to[0] == frm[0] - 2 and to[1] == frm[1] + 2:
            if self.__board[frm[0] - 1][frm[1] + 1] == '--':
                if self.general_facing(to, frm) == True:
                    return False
                return True

    def horse_move(self, to, frm):
        # case 1 - moving up and left
        if to[0] == frm[0] - 2 and to[1] == frm[1] - 1:
            if self.__board[[frm[0] - 1][frm[1]]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # case 2 - moving up and right
        if to[0] == frm[0] - 2 and to[1] == frm[1] + 1:
            if self.__board[[frm[0] - 1][frm[1]]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # case 3 - moving down and left
        if to[0] == frm[0] + 2 and to[1] == frm[1] - 1:
            if self.__board[[frm[0] + 1][frm[1]]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # case 4 - moving down and right
        if to[0] == frm[0] + 2 and to[1] == frm[1] + 1:
            if self.__board[[frm[0] + 1][frm[1]]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # case 5 - moving left and down
        if to[0] == frm[0] - 1 and to[1] == frm[1] - 2:
            if self.__board[[frm[0]][frm[1] - 1]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # case 6- moving left and up
        if to[0] == frm[0] + 1 and to[1] == frm[1] - 2:
            if self.__board[[frm[0]][frm[1] - 1]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # case 7 - moving right and down
        if to[0] == frm[0] - 1 and to[1] == frm[1] + 2:
            if self.__board[[frm[0]][frm[1] + 1]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # case 8 - moving right and up
        if to[0] == frm[0] + 1 and to[1] == frm[1] + 2:
            if self.__board[[frm[0]][frm[1] + 1]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True

    def rook_move(self, to, frm):
        # see if the rook moved vertically
        if to[0] == frm[0]:
            for x in range((min(to[1], frm[1]) + 1), max(to[1], frm[1])):
                if self.__board[to[0]][x] != '--':
                    return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # see if the rook moved horizontally
        if to[1] == frm[1]:
            for x in range((min(to[0], frm[0]) + 1), max(to[0], frm[0])):
                if self.__board[x][to[1]] != '--':
                    return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        # if neither of the above are true, return false
        return False

    def cannon_move(self, to, frm):
        if to[0] == frm[0] and to[1] == frm[1] - 2:
            if self.__board[frm[0]][frm[1] - 1] != '--':
                # checks if the generals are facing
                if self.general_facing(to, frm) == True:
                    return False
                return True
        if to[0] == frm[0] and to[1] == frm[1] + 2:
            if self.__board[frm[0]][frm[1] + 1] != '--':
                # checks if the generals are facing
                if self.general_facing(to, frm) == True:
                    return False
                return True
        if to[0] == frm[0] + 2 and to[1] == frm[1]:
            if self.__board[frm[0] + 1][frm[1]] != '--':
                # checks if the generals are facing
                if self.general_facing(to, frm) == True:
                    return False
                return True
        if to[0] == frm[0] - 2 and to[1] == frm[1]:
            if self.__board[frm[0] - 1][frm[1]] != '--':
                # checks if the generals are facing
                if self.general_facing(to, frm) == True:
                    return False
                return True

        # check moving in one direction, no jumping, no capturing
        if to[0] == frm[0]:
            for x in range((min(to[1], frm[1]) + 1), max(to[1], frm[1])):
                if self.__board[to[0]][x] != '--':
                    return False
            if self.__board[to[0]][to[1]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True

        if to[1] == frm[1]:
            for x in range((min(to[0], frm[0]) + 1), max(to[0], frm[0])):
                if self.__board[to[x]][1] != '--':
                    return False
            if self.__board[to[0]][to[1]] != '--':
                return False
            if self.general_facing(to, frm) == True:
                return False
            return True
        return False

    def pawn_move(self, to, frm):
        if self.__board[frm[0]][frm[1]][0] == 'P':
            # handling for black pawns
            if self.__board[frm[0]][frm[1]][1] == 'b':
                # if pawn is staying on it's own side of the board
                if to[1] >= 0 and to[1] <= 4:
                    # checks that pawn is moving one space forward
                    if to[0] == frm[0] + 1:
                        if self.general_facing(to, frm) == True:
                            return False
                        return True
                # if pawn has crossed the river
                if to[1] >= 5 and to[1] <= 9:
                    # checks if pawn is moving one space forward
                    if to[0] == frm[0] + 1:
                        return True
                    elif to[1] == frm[1] + 1 or to[1] == frm[1] - 1:
                        # checks that the space contains a piece to capture
                        if self.__board[to[0]][to[1]] != '--':
                            if self.general_facing(to, frm) == True:
                                return False
                            return True
            # handling for red pawns
            if self.__board[frm[0]][frm[1]][1] == 'r':
                # if pawn is staying on it's own side of the board
                if to[1] >= 5 and to[1] <= 9:
                    # checks that pawn is moving one space forward
                    if to[0] == frm[0] - 1:
                        if self.general_facing(to, frm) == True:
                            return False
                        return True
                # if pawn has crossed the river
                if to[1] <= 4 and to[1] >= 0:
                    # checks if pawn is moving one space forward
                    if to[0] == frm[0] - 1:
                        if self.general_facing(to, frm) == True:
                            return False
                        return True
                    elif to[1] == frm[1] + 1 or to[1] == frm[1] - 1:
                        # checks that the space contains a piece to capture
                        if self.__board[to[0]][to[1]] != '--':
                            if self.general_facing(to, frm) == True:
                                return False
                            return True
        return False


def set_board():
    # create a blank 9x10 board
    board = [['--'] * 9 for n in range(10)]
    # add the generals G (5th spot on top and bottom row)
    board[0][4] = "Gb"
    board[9][4] = "Gr"

    # add the advisors A (4th and 6th spots on top and bottom row)
    board[0][3] = "Ab"
    board[0][5] = "Ab"
    board[9][3] = "Ar"
    board[9][5] = "Ar"

    # add the elephants E (3rd and 7th spots on top and bottom row)
    board[0][2] = "Eb"
    board[0][6] = "Eb"
    board[9][2] = "Er"
    board[9][6] = "Er"

    # add the horses H
    board[0][1] = "Hb"
    board[0][7] = "Hb"
    board[9][1] = "Hr"
    board[9][7] = "Hr"

    # add the chariots R
    board[0][0] = "Rb"
    board[0][8] = "Rb"
    board[9][0] = "Rr"
    board[9][8] = "Rr"

    # add the cannons  C
    board[2][1] = "Cb"
    board[2][7] = "Cb"
    board[7][1] = "Cr"
    board[7][7] = "Cr"
    # add the soldiers (pawns) P
    board[3][0] = "Pb"
    board[3][2] = "Pb"
    board[3][4] = "Pb"
    board[3][6] = "Pb"
    board[3][8] = "Pb"
    board[6][0] = "Pr"
    board[6][2] = "Pr"
    board[6][4] = "Pr"
    board[6][6] = "Pr"
    board[6][8] = "Pr"

    return board

    # main function for testing


#if __name__ == '__main__':
#     practice_board = XiangqiGame()
#     practice_board.print_board()
#     practice_board.is_in_check('red')
#     practice_board.is_in_check('black')
#     game = XiangqiGame()
#     print("Start game")
#     print("Pawn red start move")
#     move_result = game.make_move('c4', 'c5')
#     print("Pawn red moved")
#     black_in_check = game.is_in_check('black')
#     game.make_move('e7', 'e6')
#     state = game.get_game_state()
