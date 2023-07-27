public class GameTester {

    public static void main(String[] args) {

        String cardSuit = "";
        int cardSuitInt = 0;
        String cardRank = "";
        int cardRankInt = 0;
        Card card;


        for(int i=0; i<args.length; i++) {

            if(args[i].length() == 2) {
                cardSuit = args[i].substring(0,1); 
                cardRank = args[i].substring(1,2);
                cardRankInt = Integer.parseInt(cardRank);
            } else if(args[i].length() == 3) {
                cardSuit = args[i].substring(0,1); 
                cardRank = args[i].substring(1,3);
                cardRankInt = Integer.parseInt(cardRank);
            }

            /*
            cardSuit = args[i].substring(0,1); 
            cardRank = args[i].substring(1,3);
        
            if(cardRank.substring(1).equals(",")) {
                cardRank = args[i].substring(1,2);
            } 
            */

            
            cardRankInt = Integer.parseInt(cardRank);


            if(cardSuit.equals("c")) {
                cardSuitInt = 1;
            } else if(cardSuit.equals("d")) {
                cardSuitInt = 2;
            } else if(cardSuit.equals("h")) {
                cardSuitInt = 3;
            } else {
                cardSuitInt = 4;
            }

            System.out.println(cardSuitInt);
            System.out.println(cardRank);

            //card = new Card(cardSuitInt, cardRankInt);
            //p.addCard(card);
        }

    } 

}


/*
String cardSuit;
        int cardSuitInt;
        String cardRank;
        int cardRankInt;
        Card card;

		for(int i=0; i<testHand.length; i++) {
            cardSuit = testHand[i].substring(0,1); 
            cardRank = testHand[i].substring(1,3);

            if(cardRank.substring(1).equals(",")) {
                cardRank = testHand[i].substring(1,2);

            }
            cardRankInt = Integer.parseInt(cardRank);


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
*/