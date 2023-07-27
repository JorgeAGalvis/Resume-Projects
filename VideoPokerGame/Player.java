/**
	@author Jorge Galvis
	uni: jag2425
	This class creates the player  
 */

import java.util.ArrayList;

public class Player {
	
		
	private ArrayList<Card> hand; // the player's cards
	private double bankroll;
    private double bet;

	// you may choose to use more instance variables
		
	public Player(){		
	    // create a player here
		hand = new ArrayList<Card>();
		//bankroll = 50.0; //as indicated on Ed
		bankroll = 50.0; //trial
		bet = 0.0;
	}

	public void addCard(Card c){
	    // add the card c to the player's hand
		hand.add(c);
	}


	public void removeCard(Card c){
	    // remove the card c from the player's hand
		hand.remove(c);

        }
		
        public void bets(double amt){
            // player makes a bet
			bet = amt;
			bankroll = bankroll - amt;
        }

        public void winnings(double odds){
            //	adjust bankroll if player wins
			if(odds >= 1) {
				bankroll = bankroll + (bet * odds); 	
			} else if (odds == 0) {
				odds = 1.0;
				bankroll = bankroll - (bet * odds); 
			}
			
        }

        public double getBankroll(){
            // return current balance of bankroll
			return bankroll;
        }

        // you may wish to use more methods here


		public ArrayList<Card> getHand() {
			return hand;
		}

}


