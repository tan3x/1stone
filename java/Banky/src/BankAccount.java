/**
 * Created by tanermetin on 11.06.18.
 */
public class BankAccount {

    String account;
    double balance;

    public static void main(String [] args){
        CheckingAccount myCheck = new CheckingAccount();
        CertificateofDeposit myCert = new CertificateofDeposit();
        SavingsAccount mySaving = new SavingsAccount();

        BankAccount myBanky = new CheckingAccount();

        myCheck.account = "Je pense";
        myCert.account = "d'onc";
        mySaving.account = "je suis";
        myBanky.account = "a plus";

        myCheck.limit = 500;
        mySaving.limit = 300;


        System.out.println("∂"+ myCheck.account);
        System.out.println("∂"+ myCert.account);
        System.out.println("∂"+ mySaving.account);
        System.out.println("∂"+ myBanky.account);
        System.out.println("∂"+ myCheck.limit);
        System.out.println("∂"+ mySaving.limit);

    }

}

class CheckingAccount extends BankAccount{
    int limit;
}

class CertificateofDeposit extends BankAccount{
    int limit;
}

class SavingsAccount extends BankAccount{
    int limit;
}