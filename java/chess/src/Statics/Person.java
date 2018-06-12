package Statics;

/**
 * Created by tanermetin on 11.06.18.
 */
public class Person {
//    local count will only be equal to 1 for each of the objects since its seperate variable for each object,
//    while instanceCount is shared and will continue to increment to become 4.
//    static fields updates itself within the class even class block is over, localCount is only for an instance
//    just like static fields static methods belong to the class rather than object.
//    final fields mean constant variables, final methods prevent to be overwritten.

    public static int instanceCount;
    public int localCount;

    public Person() {
        instanceCount++;
        localCount++;
//         but non-static variables are destroyed once the block is over with below line'}'
    }

        public static void main(){
            Person person1 = new Person();
            Person person2 = new Person();
            Person person3 = new Person();
            Person person4 = new Person();

            System.out.println("localCount: "+ person4.localCount + "\tinstanceCount: "+ Person.instanceCount+"\n");

    }

}
