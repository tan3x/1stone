
public class threadLesson{
	public static void main(String args[]){
		Thread thread1 = new Thread(new myThread("thread1", 6));
		Thread thread2 = new Thread(new myThread("thread2", 5), "thread2");
		Thread thread3 = new Thread(new myThread("thread3", 4), "thread3");
		
		thread3.setPriority(Thread.MAX_PRIORITY);
		thread1.setPriority(Thread.NORM_PRIORITY);
		thread2.setPriority(Thread.MIN_PRIORITY);

		thread1.start();
		thread2.start();
		thread3.start();


			
	}
}