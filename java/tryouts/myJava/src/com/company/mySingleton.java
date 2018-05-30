package com.company;

/**
 * Created by tanermetin on 30.05.18.
 */
public class mySingleton {
    private static mySingleton ourInstance = new mySingleton();

    public static mySingleton getInstance() {
        return ourInstance;
    }

    private mySingleton() {
    }
}
