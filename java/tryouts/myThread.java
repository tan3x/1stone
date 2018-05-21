public class myThread implements Runnable{
	private int end;
	private String name;

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
