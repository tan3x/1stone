/**
 * Created by tanermetin on 03.06.18.
 */

import java.util.Scanner;

public class NumberGame{

    public static void main(String[] args){

        int randomNumber = (int) (Math.random() * 100) + 1 ;
        boolean exito = false;

        System.out.println("Hay uno numero entra la 1-100, tiempo para adivinar.");
        Scanner myScn = new Scanner(System.in);
        for(int i = 10; i > 0; i--){
            System.out.print("\tGuesso: "+ i + "\nOtra vez: ");
            int guess = myScn.nextInt();
            System.out.print("Numero: \n" + guess);

            if (randomNumber < guess){
                System.out.print("\nel numero aleatorio es mas pequeno que tu conjetura.\n");
            }
            else if(randomNumber > guess){
                System.out.print("\nel numero aleatorio es mas grande que tu conjetura.\n");
            }
            else{
                System.out.print("\nPapi! el numero aleatorio es igual que tu conjetura.\n");
                exito = true;
                break;
            }

            if(exito){
                System.out.print("\nCORRECTO");
            }
            else{
                System.out.print("\nEl numero aletario era: "+randomNumber);
            }


        }
    }

}
