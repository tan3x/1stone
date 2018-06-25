/**
 * Created by tanermetin on 24.06.18.
 */
public class Rocket implements Spaceship {

    @Override
    public boolean launch() {
        return true;
    }

    public boolean land() {
        return true;
    }

    public boolean canCarry(Item myItem) {
        return true;
    }

    public int carry(Item myItem) {
        return 0;
    }
}
