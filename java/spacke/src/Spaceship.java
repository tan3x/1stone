/**
 * Created by tanermetin on 24.06.18.
 */
public interface Spaceship {

    boolean launch();
    boolean land();
    boolean canCarry(Item myItem);
    int carry(Item myItem);

}
