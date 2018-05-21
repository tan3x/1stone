import java.util.HashMap;
import java.util.Map;

public class myThread implements Runnable{
	private int end;
	private String name;

	
	// List<String> arrList = new ArrayList<String>();
 //      arrList.add("Osman");
 //      arrList.add("Ayse");
 //      arrList.add(0, "Ozan");
 //      if(arrList.contains("Osman")) {
 //         System.out.println("Osman bulundu");
	//     }
	
	// Map<String,String> userMap = new HashMap<String, String>();
 //      userMap.put("email", "ahmet@example.com");
 //      userMap.put("name", "Ahmet Zan");
 //      userMap.put("address", "İstanbul 34000");
 //      userMap.put("mobile", "5322100000");

	public myThread(String name, int end){
		this.end = end;
		this.name = name;
	}

	@Override 

	public void run(){
		for(int i=0; i<end ; i++){
			System.out.println(name+":"+i);

		}
	}

}
