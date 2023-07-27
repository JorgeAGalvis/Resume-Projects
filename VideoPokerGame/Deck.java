/**
	@author Jorge Galvis
	uni: jag2425 
	This class creates a deck of poker cards
 */
import java.util.Random;

public class Deck {
	
	private Card[] cards;
	private int top; // the index of the top of the deck

	// add more instance variables if needed
	
	public Deck(){
		// make a 52 card deck here
		top = 0;
		int numCards = 0;
		cards = new Card[52];                                                               
		Card card;     

		for (int suit = 1; suit < 5; suit++) {            
			for (int rank = 1; rank < 14; rank++) {          
				card = new Card(suit, rank);
				cards[numCards] = card;
				numCards++;
			}
		}

	}
	
	public void shuffle(){
		// shuffle the deck here
		Card temp;
		Random r = new Random();

		for (int i=0; i<10000; i++){
			int r1 = r.nextInt(52);
			int r2 = r.nextInt(52);
			temp = cards[r1];
			cards[r1] = cards[r2];
			cards[r2] = temp;
		}
	
	}
	
	public Card deal(){
		// deal the top card in the deck
        Card c;
		
		if(top < 51) {
			c = cards[top++];
		} else {
			top = 0;
			c = cards[top++]; 
		}
		
		
		return c;
	}
	

	// add more methods here if needed


}
