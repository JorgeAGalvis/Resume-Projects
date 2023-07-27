/**
	@author Jorge Galvis
	uni: jag2425 
	This class plays Video Poker Gamer 
 */
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class Game {
	
	private Player p;
	private Deck cards;
	// you'll probably need some more here
	
	
	public Game(String[] testHand){
		// This constructor is to help test your code.
		// use the contents of testHand to
		// make a hand for the player
		// use the following encoding for cards
		// c = clubs
		// d = diamonds
		// h = hearts
		// s = spades
		// 1-13 correspond to ace-king
		// example: s1 = ace of spades
		// example: testhand = {s1, s13, s12, s11, s10} = royal flush
		p = new Player();
		cards = new Deck();

		String cardSuit = "";
        int cardSuitInt = 0;
        String cardRank = "";
        int cardRankInt = 0;
        Card card;


		for(int i=0; i<testHand.length; i++) {

			if(testHand[i].length() == 2) {
                cardSuit = testHand[i].substring(0,1); 
                cardRank = testHand[i].substring(1,2);
                cardRankInt = Integer.parseInt(cardRank);
            } else if(testHand[i].length() == 3) {
                cardSuit = testHand[i].substring(0,1); 
                cardRank = testHand[i].substring(1,3);
                cardRankInt = Integer.parseInt(cardRank);
            }

            if(cardSuit.equals("c")) {
                cardSuitInt = 1;
            } else if(cardSuit.equals("d")) {
                cardSuitInt = 2;
            } else if(cardSuit.equals("h")) {
                cardSuitInt = 3;
            } else {
                cardSuitInt = 4;
            }

            card = new Card(cardSuitInt, cardRankInt);
            p.addCard(card);
        }
		
		
	}
	
	public Game(){
		// This no-argument constructor is to actually play a normal game
		p = new Player();
		cards = new Deck();
	}
	
	public void play(){
		// this method should play the game
		System.out.printf("Welcome to 1004 Video Poker\n");
		System.out.println("Initial bankroll available: " + p.getBankroll());
		/* //remember to remove this since the errorcheck works
		System.out.print("Bet between 1-5 tokens: ");	
		Scanner s = new Scanner(System.in);
		p.bets(s.nextDouble());
		*/ 

		//NEW PART ERROR CHECK 
		Scanner s = new Scanner(System.in);
		boolean betRange = false;
		while(!betRange) {
			System.out.print("Bet between 1-5 tokens: ");	
			double userBet = s.nextDouble();
			if(userBet>= 1 && userBet<= 5){
				p.bets(userBet);
				betRange = true;
			} else {
				System.out.println("Warning!! Bet must be between 1-5");
				betRange = false;
			}
		}
		

		boolean flag = true;

		while(flag) {
			//A hand has been create and filled 
			ArrayList<Card> hand = p.getHand();
			if (hand.size() == 0) {
                cards.shuffle();
				for(int i=1;i<6;i++) {
					//cards.shuffle();
					p.addCard(cards.deal());
				}
			} 


			//Output the current hand 
			System.out.printf("\nDealt hand: \n");
			for(Card c: hand) {
				System.out.println(c);
			}

			//Prompt the user for removing cards
			System.out.println("");
			System.out.print("Do you want to reject any card?(yes or no): ");
			String answer = s.next().toLowerCase();
			
			
			int rejectNum;
			int rejectCard;

			if (answer.equals("yes")) {
				System.out.print("How many cards do you want to reject?(1-5): ");
				rejectNum = s.nextInt();
				//this ArrayList stores the card objects I want to remove 
				ArrayList<Card> cardsToRemove = new ArrayList<>();
				for(int i=0; i<rejectNum; i++) {
					System.out.print("What card do you want to reject?(1-5): ");
					rejectCard = s.nextInt();
                    //FOR CHECKING the REMOVE BUG I had 
					//System.out.println("Index of card to remove: " + rejectCard);
					//System.out.println("Card being removed: " + hand.get(rejectCard - 1).toString());
					//here nothing gets remove from my hand but added to cardsToRemove 
					cardsToRemove.add(hand.get(rejectCard-1)); 
				}

				//iterate through the card object added and remove each card object from hand
				//add the same number of cards I remove 
				for(Card card: cardsToRemove)
				{
					hand.remove(card);
					p.addCard(cards.deal());
				}
				

				System.out.println("");
				System.out.println("Final hand: ");
				for(Card c: hand) {
					System.out.println(c);
				}
				System.out.println("");
				System.out.println(checkHand(hand));

			} else {
				System.out.println(checkHand(hand));
			}

			//new
			if(p.getBankroll() == 0.0) {
				System.out.printf("\nNo $ available\nGame Over!\n");
				break; //should I break if not more money available or prompt for more money
			}

			System.out.println("");
			System.out.print("Do you want to play again?(yes or no): ");
			String playAgain = s.next().toLowerCase();

			if(playAgain.equals("yes") && p.getBankroll() > 0.0) {
                hand.clear();
				flag = true;
			} else {
                System.out.printf("\nTotal winnings: " + p.getBankroll() + "\n");
				System.out.printf("Game over!\n");
				flag = false;
			}

		}


	}

	
	public String checkHand(ArrayList<Card> hand){
		// this method should take an ArrayList of cards
		// as input and then determine what evaluates to and
		// return that as a String
		Collections.sort(hand);
		String result = "";


		if (royalFlush(hand) == true) {
    		p.winnings(250);
			result = "Winner! You got a royal flush. bankroll: " + p.getBankroll();
		} else if (straightFlush(hand) == true) {
    		p.winnings(50);
			result = "Winner! You got a stright flush. bankroll: " + p.getBankroll();
		} else if (fourOfaKind(hand) == true) {
  			p.winnings(25);
			result = "Winner! You got four of a kind. bankroll: " + p.getBankroll();
		} else if (fullHouse(hand) == true) {
    		p.winnings(6);
			result = "Winner! You got a full house. bankroll: " + p.getBankroll();
		} else if (flush(hand) == true) {
    		p.winnings(5);
			result = "Winner! You got a flush. bankroll: " + p.getBankroll();
		} else if (straight(hand) == true) {
    		p.winnings(4);
			result = "Winner! You got a stright. bankroll: " + p.getBankroll();
		} else if (threeOfaKind(hand) == true) {
    		p.winnings(3);
			result = "Winner! You got three of a kind. bankroll: " + p.getBankroll();
		} else if (twoPair(hand) == true) {
    		p.winnings(2);
			result = "Winner! You got two pairs. bankroll: " + p.getBankroll();
		} else if(onePair(hand) == true) {
			p.winnings(1);
			result = "Winner! You got one pairs. bankroll: " + p.getBankroll();
		} else {
			p.winnings(0);
			result = "No pair. bankroll: " + p.getBankroll();
		} 

		return result;
	}
	
	
	// you will likely want many more methods here
	// per discussion in class




	//there are 10 ways in which the game ends up 

	//No pair - The lowest hand, containing five separate cards that do not match up to create any of the hands below.

    //One pair - Two cards of the same value, for example two queens. Payout: 1
    public boolean onePair(ArrayList<Card> hand) {
		int checkPair = 0;
		for(int i=0; i<hand.size()-1; i++) {
			if(hand.get(i).getRank() == hand.get(i+1).getRank()) {
				checkPair = 1;
			} 
		}

		if(checkPair == 1) {
			return true;
		} else {
			return false;
		}
		
    }

	
    //Two pair - Two pairs, for example two queens and two 5’s. Payout: 2
    public boolean twoPair(ArrayList<Card> hand) {
		int checkPair = 0;

		if(hand.get(0).getRank() == hand.get(1).getRank()
		&& hand.get(2).getRank() == hand.get(3).getRank()) {
			checkPair = 2;
		} else if(hand.get(4).getRank() == hand.get(3).getRank()
		&& hand.get(2).getRank() == hand.get(1).getRank()) {
			checkPair = 2;
		} else if (hand.get(0).getRank() == hand.get(1).getRank()
		&& hand.get(3).getRank() == hand.get(4).getRank()) {
			checkPair = 2;
        }

		if (checkPair == 2) {
			return true;
		} else {
			return false;
		}
		
    }
    

	
    //Three of a kind - Three cards of the same value, for example three queens. Payout: 3
    public boolean threeOfaKind(ArrayList<Card> hand) {
		int checkPair = 0;
		
		if(hand.get(0).getRank() == hand.get(1).getRank() 
        && hand.get(1).getRank() == hand.get(2).getRank()) {
			checkPair = 1;
		} else if (hand.get(1).getRank() == hand.get(2).getRank() 
        && hand.get(2).getRank() == hand.get(3).getRank()){
			checkPair = 1;
		} else if (hand.get(2).getRank() == hand.get(3).getRank() 
        && hand.get(3).getRank() == hand.get(4).getRank()){
			checkPair = 1;
		}
		
		
		if (checkPair == 1) {
			return true;
		} else {
			return false;
		}
        
    }
	
	
    //Straight - Five cards with consecutive values, not necessarily of the same suit, such as 4, 5, 6, 7, and 8.
    //The ace can either precede a 2 or follow a king. Payout: 4
    public boolean straight(ArrayList<Card> hand) {
		int checkPair = 0;
		
		if(hand.get(0).getRank() < hand.get(1).getRank() 
        && hand.get(0).getRank() - hand.get(1).getRank() == -1
        && hand.get(1).getRank() < hand.get(2).getRank() 
        && hand.get(1).getRank() - hand.get(2).getRank() == -1
        && hand.get(2).getRank() < hand.get(3).getRank()
        && hand.get(2).getRank() - hand.get(3).getRank() == -1
        && hand.get(3).getRank() < hand.get(4).getRank()
        && hand.get(3).getRank() - hand.get(4).getRank() == -1) {
			checkPair = 1;
		} else if (hand.get(0).getRank() == 1 
        && hand.get(1).getRank() == 10
        && hand.get(2).getRank() == 11
        && hand.get(3).getRank() == 12
        && hand.get(4).getRank() == 13) {
			checkPair = 1;
		}
		
		if (checkPair == 1) {
			return true;
		} else {
			return false;
		}   
        
    }


    //Flush - Five cards, not necessarily in order, of the same suit. Payout: 5
    public boolean flush(ArrayList<Card> hand) {
        int checkPair = 0;
		
		if(hand.get(0).getSuit() == hand.get(1).getSuit()
        && hand.get(1).getSuit() == hand.get(2).getSuit()
        && hand.get(2).getSuit() == hand.get(3).getSuit()
        && hand.get(3).getSuit() == hand.get(4).getSuit()) {
			checkPair = 1;
		} 
		
		
		if (checkPair == 1) {
			return true;
		} else {
			return false;
		}
        
    }


    //Full house - Three of a kind and a pair, for example three queens and two 5’s. Payout: 6
    public boolean fullHouse(ArrayList<Card> hand) {
        int checkPair = 0;

		if((hand.get(0).getRank() == hand.get(1).getRank()
		&& hand.get(1).getRank() == hand.get(2).getRank())
		&& (hand.get(3).getRank() == hand.get(4).getRank())){
			checkPair =1;
		} else if((hand.get(2).getRank() == hand.get(3).getRank()
		&& hand.get(3).getRank() == hand.get(4).getRank())
		&& (hand.get(0).getRank() == hand.get(1).getRank())) {
			checkPair =1;
		}

		if (checkPair == 1) {
			return true;
		} else {
			return false;
		}

    }


    //Four of a kind - Four cards of the same value, such as four queens. Payout: 25
    public boolean fourOfaKind(ArrayList<Card> hand) {
		int checkPair = 0;
		
		if(hand.get(0).getRank() == hand.get(1).getRank() 
        && hand.get(1).getRank() == hand.get(2).getRank() 
        && hand.get(2).getRank() == hand.get(3).getRank()) {
			checkPair = 1;
		} else if (hand.get(1).getRank() == hand.get(2).getRank() 
        && hand.get(2).getRank() == hand.get(3).getRank() 
        && hand.get(3).getRank() == hand.get(4).getRank()){
			checkPair = 1;
		} 
		
		if (checkPair == 1) {
			return true;
		} else {
			return false;
		}
    }
    
    
    //Straight Flush - A straight and a flush: Five cards with consecutive values of the same suit. Payout: 50
    public boolean straightFlush(ArrayList<Card> hand) {
        int checkPair = 0;
		if(straight(hand) == true && flush(hand) == true) {
			checkPair = 1;
		}

		if (checkPair == 1) {
			return true;
		} else {
			return false;
		}

    }
    

    //Royal Flush - he best possible hand in poker. A 10, jack, queen, king, and ace, all of the same suit. Payout: 250
    public boolean royalFlush(ArrayList<Card> hand) {
        int checkPair = 0;
		
		if(hand.get(0).getSuit() == hand.get(1).getSuit()
        && hand.get(1).getSuit() == hand.get(2).getSuit()
        && hand.get(2).getSuit() == hand.get(3).getSuit()
        && hand.get(3).getSuit() == hand.get(4).getSuit()) {
			checkPair++;
		} 

        if(hand.get(0).getRank() == 1
        && hand.get(1).getRank() == 10
        && hand.get(2).getRank() == 11
        && hand.get(3).getRank() == 12
        && hand.get(4).getRank() ==13 ) {
			checkPair++;
		} 
		
		
		if (checkPair == 2) {
			return true;
		} else {
			return false;
		}
    }


}
