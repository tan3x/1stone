/**
 * Created by tanermetin on 03.06.18.
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import  java.lang.Exception;

public class Archivo {

    public static void main(String [] args) throws Exception{

        File misGastos = new File("gastos.txt");
        Scanner miEscaner = new Scanner(misGastos);

//        try{
//            File nosGastos = new File("nosGastos.txt");
//        } catch (Exception exception){
////            System.out.print("archivo no existe");
//            throw exception;
//        }

        int wordsTotal = 0 ;

        while(miEscaner.hasNextLine()==true){
            String line = miEscaner.nextLine();
            //            prints the word count of each line
            System.out.println(line.split(" ").length);
            wordsTotal += line.split(" ").length;
        }
        //        prints the total word number
        System.out.println("Archivo contiene "+wordsTotal+ "palabras");

    }

}
