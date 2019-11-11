##################
#Set game to be on or off
from random import randint
import time
import sys
game = True
newnames = 1



def printcleanspace(howmanyyouwant = 1):
  print('\n'*howmanyyouwant)



def cointoss():
  cointossresult = ""
  cointoss = randint(0, 100)
  for i in range(0,2):
    if cointoss%2==0:
      return("heads")
    if cointoss%2==1:
      return("tails")
  if cointoss.lower() == "heads":
    return("heads")
  if cointoss.lower() == "tails":
    return("tails")

def onerCalc(one):
  if one == 1:
    oner = "one"
    return(oner)
  elif one == "X" or one == "x":
    oner = "X"
    return(oner)
  elif one == "O" or one == "o":
    oner = "O"
    return(oner)
  else:
    return False


def board(one = 1, two = 2, three = 3, four = 4, five = 5, six = 6, seven =  7, eight = 8, nine = 9):
  winner = 0

  def boardface():
    print(f"      |   |   ")
    print(f"    {one} | {two} | {three} ")
    print(f"|||||||||||||||||")
    print(f"    {four} | {five} | {six} ")
    print(f"|||||||||||||||||")
    print(f"    {seven} | {eight} | {nine} ")
    print(f"      |   |   ")

  boardface()

def win(one = 1, two = 2, three = 3, four = 4, five = 5, six = 6, seven =  7, eight = 8, nine = 9):
    PlayerX = 0
    PlayerO = 0
    onerOne = onerCalc(one)
    onerTwo = onerCalc(two)
    onerThree = onerCalc(three)
    onerFour = onerCalc(four)
    onerFive = onerCalc(five)
    onerSix = onerCalc(six)
    onerSeven = onerCalc(seven)
    onerEight = onerCalc(eight)
    onerNine = onerCalc(nine)


    if (onerOne == "X" and onerFour == "X" and onerSeven == "X") or (onerFour == "X" and onerFive == "X" and onerSix == "X") or (onerOne == "X" and onerTwo == "X" and onerThree == "X") or (onerOne == "X" and onerFive == "X" and onerNine == "X") or (onerThree == "X" and onerSix == "X" and onerNine == "X") or (onerThree == "X" and onerFive == "X" and onerSeven == "X") or (onerSeven == "X" and onerEight== "X" and onerNine == "X") or(onerTwo == "X" and onerFive == "X" and onerEight == "X"):
      return(1)
    if (onerOne == "O" and onerFour == "O" and onerSeven == "O") or (onerFour == "O" and onerFive == "O" and onerSix == "O") or (onerOne == "O" and onerTwo == "O" and onerThree == "O") or (onerOne == "O" and onerFive == "O" and onerNine == "O") or (onerThree == "O" and onerSix == "O" and onerNine == "O") or (onerThree == "O" and onerFive == "O" and onerSeven == "O") or (onerSeven == "O" and onerEight== "O" and onerNine == "O") or(onerTwo == "O" and onerFive == "O" and onerEight == "O"):
      return(2)

def cointosswinner(cointossresult, fplayer, fname):
  print(f"Flipping Coin in ")
  time.sleep(.75)
  print(f"\n 3 . . . ")
  time.sleep(.75)
  print(f"\n 2 . . . ")
  time.sleep(.75)
  print(f"\n 1 . . . \n")
  time.sleep(.75)
  print(f"{cointossresult}. Congrats {fname} you're first!")
  time.sleep(1.5)
  #printcleanspace(1)

def gameturn(fplayer, splayer, themove, gameonORoff, fname, sname):
    countturn = 0

    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

    while gameonORoff == 1:
        WINNER = win(one, two, three, four, five, six, seven, eight, nine)
        if countturn%2==0:
          countturn += 1
          if countturn == 10:
            break
          if WINNER == 1:
              break
          printcleanspace(10)
          board(one, two, three, four, five, six, seven, eight, nine)
          themove = int(input(f'Enter the number of your move {fname}: '))
          if themove == 1:
            if one == "X" or one == "O":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              one = "X"

          if themove == 2:
            if two == "X" or two == "O":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              two = "X"

          if themove == 3:
            if three == "X" or three == "O":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              three = "X"

          if themove == 4:
            if four == "O" or four == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              four = "X"

          if themove == 5:
            if five == "O" or five == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              five = "X"

          if themove == 6:
            if six == "O" or six == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              six = "X"

          if themove == 7:
            if seven == "O" or seven == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              seven = "X"

          if themove == 8:
            if eight == "O" or eight == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              eight = "X"

          if themove == 9:
            if nine == "X" or nine == "O":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              nine = "X"

          WINNER = win(one, two, three, four, five, six, seven, eight, nine)
          if WINNER == 1:
              printcleanspace(10)
              if WINNER == 1:
                print("X's is the Winner!")
              if WINNER == 2:
                print("O's is the Winner!")
              board(one, two, three, four, five, six, seven, eight, nine)
              break


        if countturn % 2 == 1:
          countturn += 1
          if countturn == 10:
            break
          if WINNER == 1:
              break
          printcleanspace(10)
          board(one, two, three, four, five, six, seven, eight, nine)
          themove = int(input(f'Enter the number of your move {sname}: '))
          if themove == 1:
            if one == "X" or one == "O":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              one = "O"

          if themove == 2:
            if two == "X" or two == "O":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              two = "O"

          if themove == 3:
            if three == "X" or three == "O":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              three = "O"

          if themove == 4:
            if four == "O" or four == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              four = "O"

          if themove == 5:
            if five == "O" or five == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              five = "O"

          if themove == 6:
            if six == "O" or six == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              six = "O"

          if themove == 7:
            if seven == "O" or seven == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              seven = "O"

          if themove == 8:
            if eight == "O" or eight == "X":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              eight = "O"

          if themove == 9:
            if nine == "X" or nine == "O":
              countturn -= 1
              print("Another player has played in this space. Please select another")
              continue
            else:
              nine = "O"

          WINNER = win(one, two, three, four, five, six, seven, eight, nine)
          if WINNER == 1:
              printcleanspace(10)
              if WINNER == 1:
                print("X's is the Winner!")
              if WINNER == 2:
                print("O's is the Winner!")
              board(one, two, three, four, five, six, seven, eight, nine)
              break

while game == True:
  ###This is the main menu where you welcome players, they pick names, and then they pick who goes first.
  ### or do a coin flip thingie to pick who goes first
  game = True
  if newnames == 1:
    player1 = input("Hey player 1 welcome to Tic Tac Toe! Please Input your name: ")
    printcleanspace()
    player2 = input("Alrighty player 2 you know the drill! Name please.: ")
    printcleanspace()

  print("Do you want to flip for who gets X's "
                              "and goes first or do you want to simply pick who goes first?")
  printcleanspace()
  decide_for_cointoss = input("Press Enter to Continue with the coin flip. "
                              f"Or enter 1 for ({player1}) or 2 for ({player2}) to select which player goes first and gets X's: ")

  cointoss_result_to_pick_coin = cointoss()
  print(cointoss_result_to_pick_coin)


  if decide_for_cointoss == "":
    if cointoss_result_to_pick_coin == "tails":
      cointoss_to_decide_the_game = input(f"{player1}, please select if you'd like heads or tails: ")
      fplayer = 1
      fnameActual = player1
      splayer = 2
      snameActual = player2

    if cointoss_result_to_pick_coin == "heads":
      cointoss_to_decide_the_game = input(f"{player2}, please select if you'd like heads or tails: ")
      fplayer = 2
      fnameActual = player2
      splayer = 1
      snameActual = player1
  #if decide_for_cointoss.lower() == "1" or decide_for_cointoss.lower() == "2":
   # if int(decide_for_cointoss) == 1:
      #add game func second part to finish
    #  first_turn = input("Player 1, you're first!: ")
     # fplayer = 1
      #splayer = 2
      #cointoss()


    #if (decide_for_cointoss) == 2:
    #  call_for_the_coin = input("Player 2, you're first! ")
    #  fplayer = 2
    #  splayer = 1
    #else:
    #  call_for_the_coin = input("Player 1, you're first!: \n"
    #                            "you know since the both of you can't follow directions... ")
    #  fplayer = 1
    #  splayer = 2
  if decide_for_cointoss == "1":
    gameon = 1
    fplayer = 1
    fnameActual = player1
    splayer = 2
    snameActual = player2
    gameturn(fplayer, splayer, "", gameon, fnameActual, snameActual)

  elif decide_for_cointoss == "2":
    gameon = 1
    fplayer = 2

    fnameActual = player2
    splayer = 1
    snameActual = player1
    gameturn(fplayer, splayer, "", gameon, fnameActual, snameActual)

  elif cointoss_result_to_pick_coin.lower() == cointoss_to_decide_the_game.lower():
    cointosswinner(cointoss_result_to_pick_coin, fplayer, fnameActual)
    #finish this out first
    gameon = 1
    gameturn(fplayer, splayer, "", gameon, fnameActual, snameActual)
    #print("Game over")

  elif cointoss_result_to_pick_coin.lower() != cointoss_to_decide_the_game.lower():
    cointosswinner(cointoss_result_to_pick_coin, splayer, snameActual)
    #finish this out first
    gameon = 1
    gameturn(fplayer, splayer, "", gameon, snameActual, fnameActual)
    #print("Game over")



  quit = int(input("Would you like to play another round or quit, enter (1 for Yes or 2 for No) for another round: "))
  if quit == 1:
    newnames = int(input("Do you new names? (1 for Yes or 2 for No): "))
    printcleanspace(100)
  if quit == 2:
    print("Good Bye!")
    game = False
    break



