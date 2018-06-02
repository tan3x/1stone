package com.Mundo;

/**
 * Created by tanermetin on 30.05.18.
 */
public class myClass {


    int score;
//    default constructor

    myClass(){
        this.score = 0;
    }
//    parametrized cons
    myClass(int bonusScore){
        this.score = bonusScore;
    }

    public static void main() {

        myClass myObj = new myClass();
        myClass myObj2 = new myClass(500);
        myClass myObj3 = null;

        System.out.println("re\n"+ myObj.score);
        System.out.println("ra\n"+ myObj2.score);
//        System.out.println("ra\n"+ myObj3.score);  will trigger error since initialized with null and has no field or method.

    }

    public void cantar() {
        System.out.println("besame mucho");
    }

}







