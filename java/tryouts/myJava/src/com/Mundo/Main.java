package com.Mundo;

import Colores.myRojo;
import Colores.myAzul;
import Contactos.Contact;
import Contactos.ContactManager;

public class Main {
    public static void main(String[] args) {
        // write your code here
        System.out.println("empezamos");

        myRojo.main();
        myAzul.main();
        myClass.main();

        ContactManager objContactManager = new ContactManager();

        Contact elTio = new Contact() ;
        Contact laTia = new Contact() ;

        elTio.name = "miTio";
        elTio.phone = "01123581321";
        elTio.genero = "mano";

        laTia.name  = "miTia";
        laTia.email = "quesera@sera.com";
        laTia.genero = "mujer";

        objContactManager.addContact(elTio);
        objContactManager.addContact(laTia);

        System.out.println("\nName:"+elTio.name+"\nPhone:"+elTio.phone+"\nLanguage:"+elTio.language+"\nMail:"+elTio.email);
        System.out.println("\nName:"+laTia.name+"\nPhone:"+laTia.phone+"\nLanguage:"+laTia.language+"\nMail:"+laTia.email);

        Contact repuesto = objContactManager.searchContact("miTio");
        Contact repuesta = objContactManager.searchContact("miTia");


    }
}