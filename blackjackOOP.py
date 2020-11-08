from CardDeck import Card, Player, Deck
import time

#function that looks for ace in players deck
def look_for_ace(player):
    if player.hand[-1].symbol == "Ace":
        hi = 0
        # hi = int(input("You have drawn an Ace. Do you want it to use as 11 or 1?: "))
        while hi != 1 or hi != 11:
            hi = int(input("You have drawn an Ace. Do you want it to use as 11 or 1?: "))
            if hi == 1:
                break
            if hi == 11:
                break
        
        if hi == 1:
            player.hand[-1].value = 1
            print("The Ace has now the value of 1!")
        if hi == 11:
            print("The Ace has now the value of 11!")


#function that looks for ace in dealers deck
def look_for_ace_dealer(dealer, var):
    if dealer.hand[-1].symbol == "Ace":
        if var + 11 > 21:
            dealer.hand[-1].value = 1
        else:
            dealer.hand[-1].value = 11

def main():
    deck = Deck()
    player1 = Player("Player1")
    dealer  = Player("Dealer")



    money = 500
    while money > 0:
        deck.shuffle()
        hand_value_player = 0
        final_value_player = 0
        hand_value_dealer = 0
        final_value_dealer = 0
        txt = "How much you wanna bet?. You have {}€('-1' to quit): ".format(money)
        amount  = int(input(txt))
        print("\n")
        time.sleep(1)
        while amount > money:
            amount = int(input("You don't have as much money. You have {}€('-1' to quit): ".format(money)))
        if amount == -1:
            print("Thanks for playing")
            exit()
        if amount > 0 and amount <= money:
            player1.draw(deck)
            # player1.hand.append(Card("Heart", 11, "Ace"))
            look_for_ace(player1)
            player1.draw(deck)
            look_for_ace(player1)
            
            for x in player1.hand:
                hand_value_player += x.value
            print("You have the two cards: ")
            player1.showHand()
            while hand_value_player < 21 and hand_value_player != 21:
                another_card = input("\nDo you want another card?(yes/no): ")
                print('\n')
                time.sleep(1)
                if another_card == "yes" or another_card == "YES" or another_card == "Yes" or another_card == "y":
                    player1.draw(deck)
                    look_for_ace(player1)
                    print("You now have", len(player1.hand), "cards:")
                    player1.showHand()
                    hand_value_player += player1.hand[-1].value

                if another_card == "no" or another_card == "NO" or another_card == "No" or another_card == "n":
                    final_value_player = hand_value_player
                    print("Now is the dealers turn! You'r final score is {}\n".format(final_value_player))
                    break
                    
                if hand_value_player > 21:
                    money -= amount
                    print("\nYou mf lost. You still have {}€ left".format(money))
                    deck.allCards(player1)
                    break
                
            # if hand_value_player == 21:
            #     money += 2*amount
            #     print("\n You won. You now have {}€".format(money))
            #     deck.allCards(player1)
            #     break


        ##############################################
            if hand_value_player <= 21:
                dealer.draw(deck)
                look_for_ace_dealer(dealer, hand_value_dealer)
                dealer.draw(deck)
                # hand_value_dealer += dealer.hand[-1].value
                look_for_ace_dealer(dealer, hand_value_dealer)
                # hand_value_dealer += dealer.hand[-1].value
                for val in dealer.hand:
                    hand_value_dealer += val.value

                print("\nThe dealer has the cards: ")
                dealer.showHand()
                print("\n")
                time.sleep(1)
                if hand_value_dealer > 21 and hand_value_player <= 21:
                    money += 2*amount
                    print("\n You won. You now have {}€".format(money))
                    deck.allCards(player1)
                    deck.allCards(dealer)
                while hand_value_dealer <= 16:
                    dealer.draw(deck)
                    look_for_ace_dealer(dealer, hand_value_dealer)
                    hand_value_dealer += dealer.hand[-1].value

                    print("\nThe dealer is taking another card.The dealer has now", len(dealer.hand), "cards. The cards: ")
                    time.sleep(2)
                    dealer.showHand()

                    if hand_value_dealer > 21:
                        money += 2*amount
                        print("You won. You now have {}".format(money))

                if hand_value_dealer >= 17 and hand_value_dealer <= 21 and hand_value_player <= 21:
                    final_value_dealer = hand_value_dealer
                    if final_value_dealer > final_value_player:
                        money -= amount
                        print("\nYou lost. You still have {}€ left".format(money))
                        deck.allCards(dealer)
                        deck.allCards(player1)
                        
                    if final_value_dealer < final_value_player:
                        money += 2*amount
                        print("\nYou won. You now have {}€".format(money))
                        deck.allCards(dealer)
                        deck.allCards(player1)
                        
                    if final_value_dealer == final_value_player:
                        print("\nIts a tie. You get your money back. You now have {}€".format(money))
                        deck.allCards(dealer)
                        deck.allCards(player1)
                    
            
           



            
                
            
            



main()


# print(len(deck.cards))
# bob = Player("bob")
# bob.draw(deck)
# bob.draw(deck)


# bob.showHand()
# print(len(deck.cards))
# deck.allCards(bob)
# print("---------------------")
# bob.showHand()
