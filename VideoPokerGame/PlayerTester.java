/*

if (royalFlush(hand) == true) {
    p.winnings(1);
	result = "Royal Flush";
} else if (straightFlush(hand) == true) {
    p.winnings(1);
	result = "Straight Flush";
} else if (fourOfaKind(hand) == true) {
    p.winnings(1);
	result = "Four of a kind";
} else if (fullHouse(hand) == true) {
    p.winnings(1);
	result = "Full House";
} else if (flush(hand) == true) {
    p.winnings(1);
	result = "Flush";
} else if (stright(hand) == true) {
    p.winnings(1);
	result = "Stright";
} else if (threeOfaKind(hand) == true) {
    p.winnings(1);
	result = "Three of a kind";
} else if (twoPair(hand) == true) {
    p.winnings(1);
	result = "Winner! You got two pairs. bankroll: " + p.getBankroll();
} else if (onePair(hand) == true) {
    //the two will chsnge to match the correct odds 
    p.winnings(1);
    result = "Winner! You got one pair. bankroll: " + p.getBankroll();
} else {
    result = "No pair. bankroll: " + p.getBankroll();
}

*/
//original I had 
/*
		if(onePair(hand) == true) {
			//the two will chsnge to match the correct odds 
			p.winnings(1);
			result = "Winner! You got one pair. bankroll: " + p.getBankroll();
        } else if (twoPair(hand) == true) {
			result = "Winner! You got two pairs. bankroll: " + p.getBankroll();
		} else {
			result = "No pair. bankroll: " + p.getBankroll();
		} 
		/*
		else if (threeOfaKind(hand) == 1) {
			result = "Three of a kind";
		} else if (stright(hand) == 1) {
			result = "Stright";
		} else if (flush(hand) == 1) {
			result = "Flush";
		} else if (fullHouse(hand) == 1) {
			result = "Full House";
		} else if (fourOfaKind(hand) == 1) {
			result = "Four of a kind";
		} else if (straightFlush(hand) == 1) {
			result = "Straight Flush";
		} else if (royalFlush(hand) == 1) {
			result = "Royal Flush";
		} else {
			result = "No pair " + p.getBankroll();
		}
		return result;
        */
		
	}



		//ORIGINAL THAT I USED IN THE IMPLEMENTATION
		/*
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
		} else if (stright(hand) == true) {
    		p.winnings(4);
			result = "Winner! You got a stright. bankroll: " + p.getBankroll();
		} else if (threeOfaKind(hand) == true) {
    		p.winnings(3);
			result = "Winner! You got three of a kind. bankroll: " + p.getBankroll();
		} else if (twoPair(hand) == true) {
    		p.winnings(2);
			result = "Winner! You got two pairs. bankroll: " + p.getBankroll();
		} else if (onePair(hand) == true) {
    		//the two will chsnge to match the correct odds 
    		p.winnings(1);
    		result = "Winner! You got one pair. bankroll: " + p.getBankroll();
		} else {
    		result = "No pair. bankroll: " + p.getBankroll();
		}

			return result;
	}
		*/


			//OLD GETTING THE SUBSTRING OF THE TESTHAND
			/*

			/*
			String cardSuit;
			int cardSuitInt;
			String cardRank;
			int cardRankInt;
			Card card;
			*/
			/*
            cardSuit = testHand[i].substring(0,1); 
            cardRank = testHand[i].substring(1,3); //not working when ending in s1

            if(cardRank.substring(1).equals(",")) {
                cardRank = testHand[i].substring(1,2);
            } 
            cardRankInt = Integer.parseInt(cardRank);
			*/