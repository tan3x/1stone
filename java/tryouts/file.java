import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;


public class copy{
	String sourceFile, targetFile;
	BufferedReader sourceBuffer;
	BufferedWriter targetBuffer;
	String line;

	public static void main(String args[]){
		

		String sourceFile = "/opt/sourcefilepath";
		String targetFile = "/opt/destination";
		try{
			// some error ere with tree{}}

		FileInputStream fis = new FileinputStream(sourceFile);
		FileOutputStream f0s = new FileinputStream(sourceFile);

		int offset = 0;
		byte[] line = new byte[1024];
		int lineLength = 0;

		lineLength = fis.read(line);



		//Okunan satırların boyutu -1 değilse, yani sona gelinmediyse kopyalayın.
            while (lineLength != -1) {
                //Hedef dosyaya yazın.
                fos.write(line, offset, lineLength);
                //Yeni bir satır okuyun.
                lineLength = fis.read(line);
            }
            
            //Her iki dosyayı da kapatın.
            fis.close();
            fos.close();
            
        }

    }

        catch (IOException e) {
            //Bir hata durumunda programınıza uyarı verdirin.
            System.out.println("Bir hata oluştu " + e);
        }

}


		


	
