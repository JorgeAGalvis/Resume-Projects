/**
	@author Jorge Galvis
	uni: jag2425 
	This class creates a poker card
 */

public class Card implements Comparable<Card>{
	
	private int suit; // use integers 1-4 to encode the suit
	private int rank; // use integers 1-13 to encode the rank
	
	public Card(int s, int r){
		//make a card with suit s and value v
		suit = s;
		rank = r;
	}
	
	public int compareTo(Card c){
		// use this method to compare cards so they 
		// may be easily sorted

		//based on rank not suit 
		int result; 
		if(this.getRank() == c.getRank()){
			result = 0;
		} else if(this.getRank() > c.getRank()){
			result = 1;
		} else {
			result = -1;
		}
		
		return result;
	}
	
	public String toString(){
		// use this method to easily print a Card object
		String card = "";

		if (rank == 1) {
			card += "Ace";
		} else if (rank == 11) {
			card += "Jack";
		} else if (rank == 12) {
			card += "Queen";
		} else if (rank == 13) {
			card += "King";
		} else {
			card += rank;
		}

		card += " of ";

		if (suit == 1) {
			card += "Clubs";
		} else if (suit == 2) {
			card += "Diamonds";
		} else if (suit == 3) {
			card += "Hearts";
		} else if (suit == 4) {
			card += "Spades";
		}

		return card;
	}
	// add some more methods here if needed

	public int getRank() {
		return rank;
	}

	public int getSuit() {
		return suit;
	}


}
