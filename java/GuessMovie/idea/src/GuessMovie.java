
//Por que me sale un error si agrego esto abajo?

//package com.example.tanermetin.guessmovie ;

import java.io.*;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class GuessMovie {
    public static void main(String [] args) throws Exception{

        FileInputStream fs = new FileInputStream("/opt/1stone/java/GuessMovie/idea/src/movies");
        BufferedReader br = new BufferedReader(new InputStreamReader(fs));

        File file = new File("/opt/1stone/java/GuessMovie/idea/src/movies");
        Scanner scnr = new Scanner(file);

//      reads and prints text file

        Random rand = new Random();
        String line;
        ArrayList<String> textList  = new ArrayList<>();
        ArrayList<String> guessList  = new ArrayList<>();
        ArrayList<String> correctoList = new ArrayList<>();


//  adds text inputs to a list and picks a random title
        while((line = br.readLine())!= null){
            textList.add(line) ;
        }

        int randInd = rand.nextInt(textList.size());
        String movie = textList.get(randInd);

        System.out.println(movie);

        int guesses = 10;
        int score = 100;


        String movieHidden = movie.replaceAll("[A-Za-z0-9]", "_");
        StringBuilder movieResolve = new StringBuilder(movieHidden);

        while( guesses > 0 ) {

            Scanner reader = new Scanner(System.in);
            System.out.println("Enter a letter ");

            String letter = reader.nextLine();

            guessList.add(letter);


            int pos = movie.indexOf(letter.charAt(0));

            String movieRes = "";


            for (int j = -1; (j = movie.indexOf(letter, j + 1)) != -1; j++) {
                if (movie.contains(letter)) {
                    correctoList.add(letter);
                    movieResolve.setCharAt(j, letter.charAt(0));
                }
            }

            System.out.println("Correctos: " + correctoList);
            System.out.println("Movie: " + movieResolve);

            if (!movie.contains(letter)) {
                score = score - 10;
            }

            if (!letter.equals("")) {
                guesses -= 1;

                if (guesses == 0) {
                    System.out.println("You lost tomadachi.");
                    System.out.println("The movie name was: " + movie + "\nYour score is: " + score);
                }
            }

            System.out.println("Remaining guesses:" + guesses);
            System.out.println("Score:" + score);


            movieRes = movieResolve.toString();

            System.out.println("Score:" + movie);
            System.out.println("Score:" + movieRes);


            if (movie.equals(movieRes)) {
                System.out.println("Me alegro verte!");
                System.exit(0);
            }
        }
    }
}


