import java.util.Date;
import java.util.GregorianCalendar;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Scanner;

// import sun.security.util.Length;

public class h2{
    public static void main(String[] arg){
        Scanner input = new Scanner(System.in);
        String st1="Veridis";

        int leng=st1.length();
        System.out.println(leng);
        int i;
        
        if(st1.equals("Veridis")) {
            System.out.println("");
            System.out.println("Veridis.");
        }
        
        if(st1.equals("VERIDIS")) {
            System.out.println("");
            System.out.println("VERIDIS.\n");
        }
        
        if(st1.equalsIgnoreCase("VERIDIS")) {
            System.out.println("");
            System.out.println("VERIDIS.");
        }
        
        for(i=0; i<=st1.length()-1; i++) {
            System.out.print("\n");
            System.out.println("LETTER\t"+"INDEX");
            System.out.println(st1.charAt(i)+"\tindex: "+i);   
        }
        
        int comp=st1.compareTo("Aquarious");
        String intheway="something-in-the-way";
        System.out.println("Comparison value: "+comp); //veridis comes later than aquarius, thus pos value.
        String parts[] = intheway.split("-");
        
        String part1 = parts[0];
        String part2 = parts[1];
        String part3 = parts[2];
        String part4 = parts[3];

        System.out.println(part1+"X"+part2+"X"+part3+"X"+part4);

        char charArr[];
        charArr = new char[7];
        st1.getChars(0, 7, charArr,0);
        System.out.print(charArr);

        if (st1.startsWith("Ve")){
            System.out.print("\nstarts with Ve");
            
            if (st1.endsWith("is")){
                System.out.print("\tends with is\n");
                System.out.print("\tSo it is Veridis\n");
            }
            if (st1.startsWith("ri",2)){
                System.out.print("from 2nd starts with 'ri'\n");
            }

        }

        Date date = new Date();
        System.out.print("\nTime:\n"+ date);
        System.out.print("\nTimex:\n"+ date);

        
        Calendar caly = new GregorianCalendar();


    int arR[] = new int [5];
    
    for(int j = 0 ; j<4; j++){
        arR[j] = 5;
    }

    System.out.println("\n"+Arrays.toString(arR));
    System.out.print(arR[1]+1 );

    int matx[][] = new int[5][5];

    System.out.println(matx.length);

    for(int k1=0; k1<matx.length; k1++){
        for(int k2=0; k2<matx.length; k2++){
            matx[k1][k2] = k1 ;
        }
    }
    System.out.println(factorial(5));
    }

    
    public static long factorial(int number) {
        long result = 1;

        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }
            return result;
    }
}