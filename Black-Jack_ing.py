import random
import Dati 

Dati.spazi(1)
    
print("---Welcome to Python BlackJack----")
print("-------Forbidden to minors-------")

Dati.spazi(2)


Budget = Dati.ChiediReale("Insert your Budget: ")
First_Budget = Budget

 
    
#################################################################################################################################################

def deck():
     
    b = "Dealer"
    dealer = random.randint(1,11)
    
    ############
    
    g1 = random.randint(1,11)
    g2 = random.randint(1,11)
    player = g1 + g2
    
    ############
    
    print('{0:^16} = {1:5}'.format(b,dealer))
    print('Totale your card = {:5}'.format(player))
    
    Dati.spazi(1)
    ############

    return dealer, player

#################################################################################################################################################

def end_game(Budget, First_Budget):
    
    print("---Game session over---")
    
    Dati.spazi(1)
    
    print("Summing up:")
    while True :
        if Budget > First_Budget:
            
            gain = Budget - First_Budget
            print(f"Your Budget is {Budget}, you have earned {gain} €")
            break
        elif First_Budget > Budget:
            
            lost = First_Budget - Budget
            print(f"Your Budget is {Budget}, you lost {lost} €")
            break
        else:   
            
            print(f"Your Budget is {Budget}, you stayed on par") 
            break

def game(Budget):
    ########################################################
    
    

    Bet = Dati.ChiediReale("Insert Bet: ")
    
    while Bet > Budget:
        Dati.spazi(1)
        print("impossibile Bet, it can't be higher than budget")
        Bet = Dati.ChiediReale("Re-enter bet: ")
        
    win = Budget + Bet * 2
    
    Budget -= Bet
    ########################################################
    Dati.spazi(1)
    
    g = deck()

    dealer_card = g[0]
    player_card = g[1]
    ########################################################
    
    n = 0
    while 1 > n:

        print("'s' to stay, 'c' for card")
        choose = str(input())
        Dati.spazi(1)
        
        if choose == "s":
            ########################################################
            if dealer_card < 17:
            
                while dealer_card < 17:
                    dealer_card += random.randint(1,11)
            ########################################################
            if dealer_card > 21:
                
                print("you won, the dealer got bust")
                
                Dati.spazi(1)
                
                print("{0:^16} = {1:5}".format("Dealer", dealer_card))
                print("Total your card = {:5}".format(player_card))
                
                Dati.spazi(1)
                
                print(f'You won {Bet * 2} €')
                print(f'Total = {win} €')
                Budget = win
                ####
                
                new_game = Dati.ChiediParola("Do you want to play again? [y/n]  ")

                if new_game == 'y':
                    
                    game(Budget)
                else:
                    
                    end_game(Budget, First_Budget)
                    n = 2
            ########################################################
            elif dealer_card > player_card:
                
                print("you lost!")
                
                Dati.spazi(1)
                
                print("{0:^16} = {1:5}".format("Dealer", dealer_card))
                print("Total your card = {:5}".format(player_card))
                
                Dati.spazi(1)
                
                print(f'You lost {Bet} €')
                print(f'Total = {Budget} €')
                
                ####
                
                if Budget == 0:
                    end_game(Budget, First_Budget)

                new_game = Dati.ChiediParola("Do you want to play again? [y/n]  ")

                if new_game == 'y':
                    
                    game(Budget)
                else:
                    
                    end_game(Budget, First_Budget)
                    n = 2
            ########################################################
            elif player_card > dealer_card:
            
                print("You won!!")
                
                Dati.spazi(1)
                
                print("{0:^16} = {1:5}".format("Dealer", dealer_card))
                print("Total your card = {:5}".format(player_card))
                
                Dati.spazi(1)
                
                print(f'You won {Bet * 2} €')
                print(f'Total = {win} €')
                Budget = win
                ####
                
                new_game = Dati.ChiediParola("Do you want to play again? [y/n]  ")

                if new_game == 'y':
                    
                    game(Budget)
                else:
                    
                    end_game(Budget, First_Budget)
                    n = 2
            ###########################################################################################
            elif dealer_card == player_card:
                parity = Budget + Bet
                print("Parity")

                Dati.spazi(1)

                print("{0:^16} = {1:5}".format("Dealer", dealer_card))
                print("Totale your card = {:5}".format(player_card))  

                Dati.spazi(1)              

                print(f'You have taken back {Bet} €')
                print(f'Total = {parity}')
                Budget = parity
                ####
                
                new_game = Dati.ChiediParola("Do you want to play again? [y/n]  ")

                if new_game == 'y':
                    
                    game(Budget)
                else:
                    
                    end_game(Budget, First_Budget)
                    n = 2
        ################################################################################################################
        else:
            
            player_card += random.randint(1,11)

            ########################################################
            if player_card < 21:
                
                print("{0:^16} = {1:5}".format("Dealer", dealer_card))
                print("Totale your card = {:5}".format(player_card))
                
                Dati.spazi(1)
                
            ########################################################
            elif player_card == 21:
                
                print("BlackJack, you won!!")
                
                Dati.spazi(1)
                
                print("{0:^16} = {1:5}".format("Dealer", dealer_card))
                print("Total your card = {:5}".format(player_card))
                
                Dati.spazi(1)
                
                print(f'You won {Bet * 2} €')
                print(f'Total = {win} €')
                Budget = win
                ####
                
                new_game = Dati.ChiediParola("Do you want to play again? [y/n]  ")

                if new_game == 'y':
                    
                    game(Budget)
                else:
                    
                    end_game(Budget, First_Budget)
                    n = 2
            ########################################################
            else:
                print("Your high!")

                Dati.spazi(1)

                print("{0:^16} = {1:5}".format("Dealer", dealer_card))
                print("Total your card = {:5}".format(player_card))

                Dati.spazi(1)

                print(f'You have lost {Bet} €')
                print(f'Total = {Budget} €')

                if Budget == 0:
                    end_game(Budget, First_Budget)

                new_game = Dati.ChiediParola("Do you want to play again? [y/n]  ")

                if new_game == 'y':
                    
                    game(Budget)
                else:
                    end_game(Budget, First_Budget)
                    n = 2
#################################################################################################################################################
   
game(Budget)
    
   





