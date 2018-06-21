/**
 * Created by tanermetin on 13.06.18.
 */

import java.net.*;
import java.io.*;

public class HttpClient {
    public static void main(String [] args) throws IOException{
//
        String host = "127.0.0.1";
        int port = 80;

        Socket socket = new Socket(host, port);

//        input and output sockets for the network socket.

        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

//        request to HTTP server:

        out.println("GET /basics.html HTTP/1.0");
        out.println(); // empty line to seperate header and body
        out.flush();

//        response from server:
        String line;
        while((line = in.readLine()) != null){
            System.out.println(line);
        }

//        close I/O streams
        in.close();
        out.close();
    }

}
