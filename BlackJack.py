import random
import Dati 

Dati.spazi(1)
    
print("---Benvenuto nel Python BlackJack----")
print("-------Gioco vietato ai minori-------")

Dati.spazi(2)


Budget = Dati.ChiediReale("Inserisci il tuo budget: ")
Budget_iniziale = Budget

#################################################################################################################################################

def mazzo():
     
    b = "Banco"
    banco = random.randint(1,11)
    
    ############
    
    g1 = random.randint(1,11)
    g2 = random.randint(1,11)
    giocatore = g1 + g2
    
    ############
    
    print('{0:^16} = {1:5}'.format(b,banco))
    print('Totale tue carte = {:5}'.format(giocatore))
    
    Dati.spazi(1)
    ############

    return banco, giocatore

#################################################################################################################################################

def fine_partita(Budget, Budget_iniziale):
    
    print("---Sessione di Gioco finita---")
    
    Dati.spazi(1)
    
    print("Riepilogo:")
    while True :
        if Budget > Budget_iniziale:
            
            gaudagno = Budget - Budget_iniziale
            print(f"Il tuo Budget è di {Budget}, hai guadagnato {gaudagno} €")
            break
        elif Budget_iniziale > Budget:
            
            perdita = Budget_iniziale - Budget
            print(f"Il tuo Budget è di {Budget}, hai perso {perdita} €")
            break
        else:   
            
            print(f"Il tuo Budget è di {Budget}, sei rimasto in pari") 
            break

def gioca(Budget):
    ########################################################
    
    

    Puntata = Dati.ChiediReale("Inserisci puntata: ")
    
    while Puntata > Budget:
        Dati.spazi(1)
        print("Puntata impossibile, non puo essere piu alta del budget")
        Puntata = Dati.ChiediReale("Inserisci nuovamente puntata: ")
        
    vincita = Budget + Puntata * 2
    
    Budget -= Puntata
    ########################################################
    Dati.spazi(1)
    
    g = mazzo()

    cb = g[0]
    cg = g[1]
    ########################################################
    
    n = 0
    while 1 > n:

        print("'s' per stare, 'c' per carta")
        scelta = str(input())
        Dati.spazi(1)
        
        if scelta == "s":
            ########################################################
            if cb < 17:
            
                while cb < 17:
                    cb += random.randint(1,11)
            ########################################################
            if cb > 21:
                
                print("Hai vinto, il banco ha sballato")
                
                Dati.spazi(1)
                
                print("{0:^16} = {1:5}".format("Banco", cb))
                print("Il tuo punteggio = {:5}".format(cg))
                
                Dati.spazi(1)
                
                print(f'Hai vinto {Puntata * 2} €')
                print(f'Totale = {vincita} €')
                Budget = vincita
                ####
                
                nuova_partita = Dati.ChiediParola("Vuoi giocare ancora? [s/n]  ")

                if nuova_partita == 's':
                    
                    gioca(Budget)
                else:
                    
                    fine_partita(Budget, Budget_iniziale)
                    n = 2
            ########################################################
            elif cb > cg:
                
                print("Hai perso!")
                
                Dati.spazi(1)
                
                print("{0:^16} = {1:5}".format("Banco", cb))
                print("Il tuo punteggio = {:5}".format(cg))
                
                Dati.spazi(1)
                
                print(f'Hai perso {Puntata} €')
                print(f'Totale = {Budget} €')
                
                ####
                
                if Budget == 0:
                    fine_partita(Budget, Budget_iniziale)

                nuova_partita = Dati.ChiediParola("Vuoi giocare ancora? [s/n]  ")

                if nuova_partita == 's':
                    
                    gioca(Budget)
                else:
                    
                    fine_partita(Budget, Budget_iniziale)
                    n = 2
            ########################################################
            elif cg > cb:
            
                print("Hai vinto!!")
                
                Dati.spazi(1)
                
                print("{0:^16} = {1:5}".format("Banco", cb))
                print("Il tuo punteggio = {:5}".format(cg))
                
                Dati.spazi(1)
                
                print(f'Hai vinto {Puntata * 2} €')
                print(f'Totale = {vincita} €')
                Budget = vincita
                ####
                
                nuova_partita = Dati.ChiediParola("Vuoi giocare ancora? [s/n]  ")

                if nuova_partita == 's':
                    
                    gioca(Budget)
                else:
                    
                    fine_partita(Budget, Budget_iniziale)
                    n = 2
            ###########################################################################################
            elif cb == cg:
                parita = Budget + Puntata
                print("Parita")

                Dati.spazi(1)

                print("{0:^16} = {1:5}".format("Banco", cb))
                print("Il tuo punteggio = {:5}".format(cg))  

                Dati.spazi(1)              

                print(f'Hai ripreso {Puntata} €')
                print(f'Totale = {parita}')
                Budget = parita
                ####
                
                nuova_partita = Dati.ChiediParola("Vuoi giocare ancora? [s/n]  ")

                if nuova_partita == 's':
                    
                    gioca(Budget)
                else:
                    
                    fine_partita(Budget, Budget_iniziale)
                    n = 2
        ################################################################################################################
        else:
            
            cg += random.randint(1,11)

            ########################################################
            if cg < 21:
                
                print("{0:^16} = {1:5}".format("Banco", cb))
                print("Il tuo punteggio = {:5}".format(cg))
                
                Dati.spazi(1)
                
            ########################################################
            elif cg == 21:
                
                print("BlackJack, hai vinto!!")
                
                Dati.spazi(1)
                
                print("{0:^16} = {1:5}".format("Banco", cb))
                print("Il tuo punteggio = {:5}".format(cg))
                
                Dati.spazi(1)
                
                print(f'Hai vinto {Puntata * 2} €')
                print(f'Totale = {vincita} €')
                Budget = vincita
                ####
                
                nuova_partita = Dati.ChiediParola("Vuoi giocare ancora? [s/n]  ")

                if nuova_partita == 's':
                    
                    gioca(Budget)
                else:
                    
                    fine_partita(Budget, Budget_iniziale)
                    n = 2
            ########################################################
            else:
                print("Hai sballato!")

                Dati.spazi(1)

                print("{0:^16} = {1:5}".format("Banco", cb))
                print("Il tuo punteggio = {:5}".format(cg))

                Dati.spazi(1)

                print(f'Hai perso {Puntata} €')
                print(f'Totale = {Budget} €')

                if Budget == 0:
                    fine_partita(Budget, Budget_iniziale)

                nuova_partita = Dati.ChiediParola("Vuoi giocare ancora? [s/n]  ")

                if nuova_partita == 's':
                    
                    gioca(Budget)
                else:
                    fine_partita(Budget, Budget_iniziale)
                    n = 2
#################################################################################################################################################
   
gioca(Budget)
