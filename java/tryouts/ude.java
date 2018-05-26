import java.util.*;


public class ude{
    public static void main(String[] args){

        String aName = "dalton";
        String aSurname = "isaRabel";
        int aFav = 5;
        double aDouble = 10.55;
        float aFloat= (float)1.5;
        boolean isNumber = true;

        System.out.println(aName+ "was here" + "sum of some numbers" +aFav+aFloat+aDouble);
        System.out.println(isNumber);
        System.out.println(aName.length());

        int [] numbers = {1,2,3,4,5,6,7,8,9};

        System.out.println(numbers[1]);

        List<int> myList = new ArrayList<int>();

        myList.add(2);
        myList.add(3);

//        System.out.println(myList(0));
    }
}