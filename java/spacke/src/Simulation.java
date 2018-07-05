import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by tanermetin on 24.06.18.
 */

public class Simulation {

    ArrayList<String> phase1List = new ArrayList <String>();
    ArrayList<String> phase2List = new ArrayList<String>();
    ArrayList<Item> ItemList1  = new ArrayList<Item>();


    public Simulation(){}

    public static void main(String [] args)throws  IOException{
        Simulation mySim = new Simulation();
        ArrayList<Item> myItems1 = mySim.loadPhase1Items();
        ArrayList<Item> myItems2 = mySim.loadPhase2Items();

    }


        public ArrayList<Item> loadPhase1Items () throws IOException {

            FileReader phase1_file = new FileReader("./phase-1.txt");
            Scanner scanner_1 = new Scanner(phase1_file);
            ArrayList<Item> phase1_items = new ArrayList<>();

            while (scanner_1.hasNextLine()) {

                String string = scanner_1.nextLine();

                String[] splitted = string.split("=");

                System.out.println(splitted);

                Item item1 = new Item(splitted[0], Integer.parseInt(splitted[1]));

                phase1_items.add(item1);
                System.out.println(phase1_items);

            }
            return phase1_items;
        }



        public ArrayList<Item> loadPhase2Items () throws IOException {

            FileReader phase2_file = new FileReader("./phase-2.txt");
            Scanner scanner_2 = new Scanner(phase2_file);
            ArrayList<Item> phase2_items = new ArrayList<>();

            while (scanner_2.hasNextLine()) {

                String string = scanner_2.nextLine();

                String[] splitted = string.split("=");

                System.out.println(splitted);

                Item item1 = new Item(splitted[0], Integer.parseInt(splitted[1]));

                phase2_items.add(item1);
                System.out.println(phase2_items);
            }
            return phase2_items;
        }



        ArrayList<Rocket> loadU1(ArrayList<Item> itemList) {
            ArrayList<Rocket> fleet1 = new ArrayList<Rocket>();
            Rocket rocket1 = new U1();

            for(Item item:itemList){
                while(!rocket1.canCarry(item)){
                    fleet1.add(rocket1);
                }
            }
            return fleet1;
        }



        ArrayList<Rocket> loadU2(ArrayList<Item> itemList) {
            ArrayList<Rocket> fleet2 = new ArrayList<Rocket>();
            Rocket rocket2 = new U2();

            for(Item item:itemList){
                while(!rocket2.canCarry(item)){
                    fleet2.add(rocket2);
                }
            }
            return fleet2;
        }

}
