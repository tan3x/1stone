import java.util.*;


public class ude{
    public static void main(String[] args){

        String aName = "dalton";
        String aSurname = "isaRabel";
        int aFav = 5;
        double aDouble = 10.55;
        float aFloat= (float) 10;
        boolean isNumber = true;

        System.out.println(aName+ "was here" + "sum of some numbers" +aFav+aFloat+aDouble);
        System.out.println(isNumber);
        System.out.println(aName.length());

        int [] numbers = {1,2,3,4,5,6,7,8,9};

        System.out.println(numbers[1]);


        List<Integer> myNumbers = new ArrayList<>();
        List<String> myCountries = new ArrayList<>();

        Map myMap = new java.util.HashMap<>();



        myMap.put("Jack", "Russell");
        myMap.put("Beck", "Crowe");
        myMap.remove("Beck");

        System.out.println(myMap.size());


        myNumbers.add(2);
        myNumbers.add(3);
        myNumbers.remove(0);

        myCountries.add("Cambodia");
        myCountries.add("Mozambique");
//        myCountries.remove(0);

        System.out.println(myCountries);
        System.out.println(myNumbers.get(0));
        System.out.println(myCountries);
        System.out.println(myCountries.toString());

    }
}