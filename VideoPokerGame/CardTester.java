public class CardTester {

    public static void main(String[] args) {

        Card a = new Card(1,10);
        Card b = new Card(4,1);
        Card c = new Card(2,11);
        Card d = new Card(3,10);

        System.out.println(a.compareTo(b));

        System.out.println(a.getRank());
    }


}