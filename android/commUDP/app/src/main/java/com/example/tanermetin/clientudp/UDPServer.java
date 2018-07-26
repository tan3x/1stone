<<<<<<< Updated upstream:android/commUDP/app/src/main/java/com/example/tanermetin/clientudp/UDPServer.java
package com.example.tanermetin.clientudp;

/**
=======
package com.example.tanermetin.clientudp; /**


>>>>>>> Stashed changes:android/clientUDP/app/src/main/java/com/example/tanermetin/clientudp/UDPServer.java
 * Created by tanermetin on 19.06.18.
 */
import java.io.*;
import java.net.*;

<<<<<<< Updated upstream:android/commUDP/app/src/main/java/com/example/tanermetin/clientudp/UDPServer.java
class UDPServer
{
=======

class UDPServer{


>>>>>>> Stashed changes:android/clientUDP/app/src/main/java/com/example/tanermetin/clientudp/UDPServer.java
    public static void main(String args[]) throws Exception
    {
        DatagramSocket serverSocket = new DatagramSocket(9876);

<<<<<<< Updated upstream:android/commUDP/app/src/main/java/com/example/tanermetin/clientudp/UDPServer.java
        byte[] receiveData = new byte[1024];
        byte[] sendData = new byte[1024];
=======
        byte[] receiveData = new byte[512];
        byte[] sendData = new byte[512];

        System.out.println("LISTENING AT: " +  serverSocket.getLocalSocketAddress());


>>>>>>> Stashed changes:android/clientUDP/app/src/main/java/com/example/tanermetin/clientudp/UDPServer.java
        while(true)
        {

            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

            serverSocket.receive(receivePacket);

            String message = new String( receivePacket.getData());

            InetAddress IPAddress = receivePacket.getAddress();

            System.out.println("RECEIVED: " + message);
            System.out.println("FROM: " + IPAddress);

            int port = receivePacket.getPort();

            String capitalizedSentence = message.toUpperCase();
            sendData = capitalizedSentence.getBytes();

            DatagramPacket sendPacket =
                    new DatagramPacket(sendData, sendData.length, IPAddress, port);
            serverSocket.send(sendPacket);

            if (receivePacket.getLength() > 10){
                System.out.println("oversize");
            }

            System.out.println("packet:" + receivePacket.getLength());
            System.out.println("message:"+message.length());
        }
    }
}

