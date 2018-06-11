package Interfaces;

/**
 * Created by tanermetin on 11.06.18.
 */
public abstract class Caravan implements  Movable, Liveable {

    int location;
    int max;

    public void move(int distance){
        location = location+distance;
    }

    public boolean canFit(int inhabitants){
        return max <= inhabitants;
    }
}
