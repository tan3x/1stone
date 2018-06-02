package com.Mundo;

import Colores.myRojo;
import Colores.myAzul;
import Contactos.ContactManager;

public class Main {
    public static void main(String[] args) {
        // write your code here
        System.out.println("empezamos");

        myRojo.main();
        myAzul.main();
        myClass.main();

        ContactManager objContactManager = new ContactManager();

    }
}