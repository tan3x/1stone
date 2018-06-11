import java.util.Queue;

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



        if (queen.isValidMove(testPos)){
            System.out.println("Vamos a tomar algo.");
        }
        else{
            System.out.println("A donde Yolanda?");

        }
        Position actualPosQueen = new Position(0,0);
        Position newPosQueen = new Position(5,5);

//        Queen iqueen = new Queen(3,4);
//        System.out.println("iqueen:"+iqueen.position.row);

//        if (iqueen.isValidMove(newPosQueen)){
//            System.out.println("Go on darling.");
//        }
//        else{
//            System.out.println("Wait for your hero.");
//        }

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


