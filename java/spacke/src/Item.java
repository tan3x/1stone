import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringJoiner;

/**
 * Created by tanermetin on 24.06.18.
 */


public class Item {

    String name;
    int weight;

    public static void main(String[] args) throws Exception {

            ArrayList<String> phase1_List = new ArrayList<>();
            ArrayList<String> phase2_List = new ArrayList<>();
            ArrayList<Item> Item1List = new ArrayList<>();
            ArrayList<Item> Item2List = new ArrayList<>();

            FileReader phase1_file = new FileReader("./phase-1.txt");
            FileReader phase2_file = new FileReader("./phase-2.txt");

            Scanner scanner1 = new Scanner(phase1_file);
            Scanner scanner2 = new Scanner(phase2_file);


        int i = 0;
        while (scanner1.hasNext()) {

            phase1_List.add(scanner1.nextLine());
            i++;
        }
        scanner1.close();

        System.out.println("\nPHASE-1-LIST\n "+ phase1_List);

        }
    }

    interface Spaceship{
        boolean launch();
        boolean land();
        boolean canCarry(Item myItem);
        int carry(Item myItem);
        }

    class Rocket implements Spaceship{

        @Override
        public boolean launch(){
        return true;
        }

        public boolean land(){
        return true;
        }

        public boolean canCarry(Item myItem){
            return true;
        }
        public int carry(Item myItem){
            return 0;
        }
     }

    class U1 extends Rocket{

        @Override
        public boolean launch(){
            return true;
        }
        public boolean land() {
            return true;
        }

    }class U2 extends Rocket{

        @Override
        public boolean launch(){
            return true;
        }
        public boolean land() {
            return true;
        }
    }


    class Simulation {

    ArrayList<String> phase1List = new ArrayList<String>();
    ArrayList<String> phase2List = new ArrayList<String>();

        ArrayList loadPhase1Items() throws IOException{

            /* call within this class*/

            return phase1List ;
        }

        ArrayList loadPhase2Items() throws IOException{

            FileReader phase2 = new FileReader("./phase-2.txt");

            Scanner scanner2 = new Scanner(phase2);

            System.out.println("\nPHASE-2\n");

            while(scanner2.hasNext()){
                System.out.println(scanner2.nextLine());
            }
            return phase2List ;
        }
    }






