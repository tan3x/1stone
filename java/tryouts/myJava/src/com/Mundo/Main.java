package com.Mundo;

import Colores.myRojo;
import Colores.myAzul;
import Contactos.Contact;
import Contactos.ContactManager;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // write your code here
        System.out.println("empezamos");

        myRojo.main();
        myAzul.main();
        myClass.main();

        ContactManager objContactManager = new ContactManager();
        Scanner myScanner = new Scanner(System.in);

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

        System.out.println("\nName:"+elTio.name+"\nPhone:"+elTio.phone+"\nLanguage: PRIVATE"+"\nMail:"+elTio.email);
        System.out.println("\nName:"+laTia.name+"\nPhone:"+laTia.phone+"\nLanguage:PRIVATE"+"\nMail:"+laTia.email);

        Contact repuesto = objContactManager.searchContact("miTio");
        Contact repuesta = objContactManager.searchContact("miTia");


        System.out.println("Quando tiempo bibes en la ciudad?\n");
        String duration = myScanner.nextLine();
        System.out.print("Bibo desde "+duration+" meses. ");
        System.out.print("Quantos anos tienes?");

        int ano = myScanner.nextInt();

        if(35 > ano && ano > 18){System.out.print("Feliz cumpleanos");}
        else if(ano < 18){   System.out.print("Aprender ja en verano. Hasta pronto");}
        else{System.out.println("Butique hostels Around Galata.");        }


    }
}