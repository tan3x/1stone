

// public class H2{
//     public static void main(String[] arg){
//         String s1="veridis";
//         if (s1.equals("veridis")){
//             System.out.println("String equals "+s1);
//         }
//         // else{
//         //     System.out.println("String is sth else");
//         // }
//     }
// }
public class H2{
    public static void main(String[] arg){
        String st1="melisa";

        if(st1.equals("melisa")) {
            System.out.println("");
            System.out.println("string melisa dir.");
        }

        if(st1.equals("MELISA")) {
            System.out.println("");
            System.out.println("string MELISA dir.");
        }

        if(st1.equalsIgnoreCase("MELISA")) {
            System.out.println("");
            System.out.println("string MELISA dir.");
        }
    }
}