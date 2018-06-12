import java.util.ArrayList;
import  java.util.HashMap;


/**
 * Created by tanermetin on 11.06.18.
 */

public class Book {
    String title;
    String author;
    int numOfPages;
    int publishedYear;
    int edition;
    String ISBN;
}


public class Library {

    HashMap<String, Book> allBooks  =new HashMap<String, Book>();



    Book braveNewWorld = new Book();

//    allBooks.put ("93290342", Book);
//    TODO: ***###***

    Book findBookbyId(String ISBN) {
        Book book = allBooks.get(ISBN);
        return book;
    }
}



