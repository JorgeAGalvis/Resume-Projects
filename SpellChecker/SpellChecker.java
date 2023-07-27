/**
 * @author Jorge Galvis 
 * Uni: jag2425
 */

import java.util.*;
import java.io.File;
import java.io.FileNotFoundException; 
import java.util.Scanner;

public class SpellChecker implements SpellCheckerInterface {

    HashSet<String> dictionarySet; 
    List<String> incorrectWords;
    HashSet<String> wordSuggestionsSet; 

    /**
     * Constructor 
     * @param String filename, a word dictionary 
     */
    public SpellChecker( String filename ) {

        File f = new File( filename );
        Scanner in = null;

        try {
            in = new Scanner(f);
        } catch(FileNotFoundException e) {
            throw new RuntimeException("File: " + filename + " not found.");
        }

        dictionarySet = new HashSet<>(); 

        while( in.hasNextLine() ) {

            String line = in.nextLine();
            line = line.strip().toLowerCase();
            line = line.replaceAll("\\p{Punct}", ""); 
            line = line.replaceAll("\\d", ""); 
            //System.out.println( line ); //for testing

            dictionarySet.add( line ); //add word to a set 

        }


    }


    /**
     * This method checks for incorrect words in the provide file 
     * @param String filename contains the name of the file to be spell-checked.
     * @return a list of all words in the input file that are incorrectly spelled
     */
    public List<String> getIncorrectWords( String filename ) {

        File f = new File( filename );
        Scanner in = null;

        try {
            in = new Scanner(f);
        } catch(FileNotFoundException e) {
            throw new RuntimeException("File: " + filename + " not found.");
        }

        incorrectWords = new ArrayList<>();

        while( in.hasNextLine() ) {

            String line = in.nextLine();
            String[] words = line.split(" ");

            for( String word: words ) {
                
                word = word.strip().toLowerCase();
                word = word.replaceAll("\\p{Punct}", "");
                //System.out.println( word ); for testing 

                if( !dictionarySet.contains(word) && word.length() != 0 ) {

                    incorrectWords.add(word);

                }
            }


        }

        return incorrectWords; 

    }


    /**
     * This method provides suggestion for misspelled words 
     * @param String word.
     * @return a set of all potential suggestions for the incorrectly spelled word 
     * if not suggestions then return an empty set 
     */
	public Set<String> getSuggestions( String word ) {
        
        wordSuggestionsSet = new HashSet<>();
        String wordCopy = word;
        wordCopy = wordCopy.strip().toLowerCase().replaceAll("\\p{Punct}", "");
        

        if( wordCopy.length() == 0 ) {
            return wordSuggestionsSet;
        }

        String[] alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};

        //Add one character - add a character at every point in the string (including at the very beginning and end)
        //for example: theer (a-z every letter in the lower alphabeth)
        //a-ztheer, ta-zheer, tha-zeer, thea-zer, theea-zr, theera-z
        for( int i=0; i<wordCopy.length() + 1; i++ ) {
            StringBuilder str1 = new StringBuilder( wordCopy );
            for(int j=0; j<alphabet.length; j++) {

                str1.insert(i, alphabet[j]);
                //System.out.println(str1.toString()); for testing
                if( dictionarySet.contains( str1.toString() ) ) {   
                    wordSuggestionsSet.add( str1.toString() );
                }
                str1 = new StringBuilder( wordCopy );
                
            }

            //System.out.println("-------"); for testing

        }


        //Remove one character - remove one character at a time from each position in the string
        //for example: theer 
        // heer, teer, ther, ther, thee
        for( int i=0; i<wordCopy.length(); i++ ) {
            StringBuilder str2 = new StringBuilder( wordCopy );
            str2.deleteCharAt(i);
            //System.out.println( str2.toString() ); //for testing
            if( dictionarySet.contains( str2.toString() ) ) {   
                wordSuggestionsSet.add( str2.toString() );
            }

        }
        

        //System.out.println("---------"); for testing


        //Swap adjacent characters - swap every pair of adjacent characters in the string
        //for example: theer 
        //hteer, teher, theer, there
        for( int i=1; i<wordCopy.length(); i++ ) {
            StringBuilder str3 = new StringBuilder( wordCopy );
            String x = str3.toString().valueOf( str3.toString().charAt(i) ) + str3.toString().valueOf( str3.toString().charAt(i-1) );
            str3 = str3.replace( i-1, i+1, x);
            //System.out.println( str3.toString() ); for testing
            if( dictionarySet.contains( str3.toString() ) ) {   
                wordSuggestionsSet.add( str3.toString() );
            }

        }


        return wordSuggestionsSet;

    }


}

