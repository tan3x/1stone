import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by tanermetin on 24.06.18.
 */
public class Simulation {



    ArrayList<String> phase1List = new ArrayList<String>();
    ArrayList<String> phase2List = new ArrayList<String>();
    ArrayList<Item> ItemList1  = new ArrayList<Item>();


    public static  void main (String [] args) {}


        public ArrayList<Item> loadPhase1Items () throws IOException {

            FileReader phase1_file = new FileReader("./phase-1.txt");
            Scanner scanner_2 = new Scanner(phase1_file);
            ArrayList<Item> phase1_items = new ArrayList<Item>();

            while (scanner_2.hasNextLine()) {

                String string = scanner_2.nextLine();

                String[] splitted = string.split("=");

                System.out.println(splitted);

                Item item = new Item(splitted[0], Integer.parseInt(splitted[1]));

                phase1_items.add(item);

            }
            return phase1_items;
        }


//    ArrayList loadPhase2Items() throws IOException{
//
//        FileReader phase2 = new FileReader("./phase-2.txt");
//
//        Scanner scanner2 = new Scanner(phase2);
//
//        System.out.println("\nPHASE-2\n");
//
//        while(scanner2.hasNext()){
//            System.out.println(scanner2.nextLine());
//        }
//        return phase2List ;
//    }
}
