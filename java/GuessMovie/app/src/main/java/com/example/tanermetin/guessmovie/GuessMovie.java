
import java.io.*;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class GuessMovie {
    public static void main(String [] args) throws Exception{

    FileInputStream fs = new FileInputStream("movies");
    BufferedReader br = new BufferedReader(new InputStreamReader(fs));
    
    File file = new File("movies");
    Scanner scnr = new Scanner(file);

//      reads and prints text file

//    while(scnr.hasNext()) {
//        System.out.println(scnr.nextLine());
//    }
    Random rand = new Random();
    String line;
    ArrayList<String> textList  = new ArrayList<>();

//  adds text inputs to a list and prints a random title
    while((line = br.readLine())!= null){
        textList.add(line) ;
    }
    
    int randInd = rand.nextInt(textList.size());
    String movie = textList.get(randInd);

    System.out.println(movie);
//    System.out.println("\nlength of the movie:" + movie.length());


    String movieHidden = movie.replaceAll("(?s).", "_");
    for (int i=0; i < movie.length(); i++){
        char c = movie.charAt(i);
        if (c != ' ' ){
        continue;
        }
//        TODO: read user input
//        TODO: reveal correct letters
//        TODO: calculate points
    }
    System.out.println(movieHidden);


    }

}
