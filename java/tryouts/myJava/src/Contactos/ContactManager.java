package Contactos;

public class ContactManager {
//    Fields
    Contact [] misAmigos;
    int amigoContador;

//    Constructor
//    ArrayList is faster for searches, LinkedList for add/remove.

    public ContactManager(){
        this.amigoContador = 0;
        this.misAmigos = new Contact[100];
    }

//ins: contact(in Contact type)
    void addContact(Contact contact){
        misAmigos[amigoContador]=contact;
        amigoContador++;

    }


//ins: searchName, outs: found contact
    Contact searchContact(String searchName){
        for (int i=0; i < amigoContador; i++){
            if(misAmigos[i].name.equals(searchName)){
                System.out.println("amigo aqui");
                return misAmigos[i];
            }
        }
        return null;
    }






}
