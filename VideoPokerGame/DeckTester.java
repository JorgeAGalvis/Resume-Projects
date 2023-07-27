public class DeckTester {

    public static void main(String[] args) {

        Deck d = new Deck();
        d.shuffle();

        for(int i=0; i<60; i++) {

            System.out.print(d.deal() + " (");
            System.out.println(i+")");
            
            
        }

    }

}