import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by tanermetin on 24.06.18.
 */


public class Item {

    public String name;
    public int weight;

    public Item(String name, int weight) {
        this.name = name;
        this.weight = weight;
    }

    public String getName() {
        return name;
    }

    public int getWeight() {
        return weight;
    }
}




//    public static void main(String[] args) throws Exception {
//
//            ArrayList<String> phase1_List = new ArrayList<>();
//            ArrayList<String> phase2_List = new ArrayList<>();
//            ArrayList<Item> Item1List = new ArrayList<>();
//            ArrayList<Item> Item2List = new ArrayList<>();
//
//            FileReader phase1_file = new FileReader("./phase-1.txt");
//            FileReader phase2_file = new FileReader("./phase-2.txt");
//
//            Scanner scanner1 = new Scanner(phase1_file);
//            Scanner scanner2 = new Scanner(phase2_file);
//
//
//        int i = 0;
//        while (scanner1.hasNext()) {
//
//            phase1_List.add(scanner1.nextLine());
//            i++;
//        }
//        scanner1.close();
//
//        System.out.println("\nPHASE-1-LIST\n "+ phase1_List);
//
//        }
//    }











