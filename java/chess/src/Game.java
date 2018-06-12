import java.util.*;

import Statics.Person ;
/**
 * Created by tanermetin on 09.06.18.
 */

public class Game {

    Piece [][] board;

    //empty board
    Game(){
        board = new Piece [8][8];
    }


    public static void main(String [] args){

        Piece queen = new Piece();
        Position testPos = new Position(3,10);

        Person.main(); //comes from statics person

        if (queen.isValidMove(testPos)){
            System.out.println("Vamos a tomar algo.");
        }
        else{
            System.out.println("A donde Yolanda?");

        }
        Position actualPosQueen = new Position(0,0);


//TODO:####################################################

//        Queen iqueen = new Queen(3,4);
//        System.out.println("iqueen:"+iqueen.position.row);

//        if (iqueen.isValidMove(newPosQueen)){
//            System.out.println("Go on darling.");
//        }
//        else{
//            System.out.println("Wait for your hero.");
//        }

        ArrayList<String> testArray = new ArrayList<String>();

        testArray.add("10");
        testArray.add("20");
        testArray.add("30");
        testArray.add(0,"5");
        testArray.remove(2);

        int size = testArray.size();

        for(int i=0; i<size; i++){
            System.out.println("loop-1: "+ testArray.get(i));

        }

        for (String s : testArray){
            System.out.println("loop-2: "+ s);
        }

        System.out.println("\nDerdim basimdan askin, olmusum coktan saskin: " +testArray+"\n"+testArray.contains(14));


        Stack<String> newsFeed = new Stack<String>();
        newsFeed.push("s1");
        newsFeed.push("s2");
        newsFeed.push("s3");

        String flashNews =  newsFeed.pop();
        String peekNews =  newsFeed.peek(); // gets the top without popping

        System.out.println("Stack: " + newsFeed);
        System.out.println("Flash: " + flashNews);
        String flashNews2 =  newsFeed.pop();
        System.out.println("Flash2: " + flashNews2);
        System.out.println("Stack: " + newsFeed);

        Queue <String> myLink = new LinkedList<String>();

        myLink.add("node-1");
        myLink.add("node-2");
        myLink.add("node-3");

        System.out.println(myLink.poll());
        System.out.println(myLink.poll());
        System.out.println(myLink.poll());


    }
}

class Piece{
    Position position;

    boolean isValidMove(Position newPosition){
        if ( newPosition.row > 0 && newPosition.column > 0 && newPosition.column < 8 && newPosition.row < 8){
            return true;
        }
        else {
            return false;
        }
    }
}


class Position{
    int row;
    int column;

    Position(int r, int c){
        this.row = r;
        this.column = c;
    }
}

class Rock extends Piece{

    boolean isValidMove(Position newPosition){

        if(!super.isValidMove(position)){
            return false;
        }
        if (newPosition.column == this.position.column || newPosition.row == this.position.row) {
            return true;
        }
        else{
            return false;
        }
    }

}

class Bishop extends Piece{
    boolean isValidMove(Position newPosition){
        if(Math.abs(newPosition.column - this.position.column) == Math.abs(newPosition.row - this.position.row)){
            return true;
        }
        else {
            return false;
        }
    }
}

class Queen extends Piece{

    Queen(int posx, int posy){
        this.position.row = posx;
        this.position.column = posy;
    }

    boolean isValidMove(Position newPosition){
        if (newPosition.column == this.position.column || newPosition.row == this.position.row){
            return true;
        }
        else {
            return false;
        }
    }
}


