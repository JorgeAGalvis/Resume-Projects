import java.util.*;

public class SpellCheckerTester {

    /*
     * Tester main method 
     */
    public static void main(String[] args) {

        SpellChecker spellChecker = new SpellChecker( "words.txt" );

        System.out.println(" ");
        List<String> resultOfMisspelled = spellChecker.getIncorrectWords( "test.txt" );
        System.out.println( resultOfMisspelled );
        System.out.println( "" );


        for( String misspelledWord: resultOfMisspelled ) {
            
            Set<String> wordSuggestions = spellChecker.getSuggestions( misspelledWord);
            System.out.println("Suggestions for " + misspelledWord + ": " + wordSuggestions );

        }

    }


}
 
