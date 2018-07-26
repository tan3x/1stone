package com.example.tanermetin.clientudp;


import java.io.*;
import java.net.*;



class UDPServer{


    public static void main(String args[]) throws Exception
    {
        DatagramSocket serverSocket = new DatagramSocket(9876);

        byte[] receiveData = new byte[1024];
        byte[] sendData = new byte[1024];

        System.out.println("LISTENING AT: " +  serverSocket.getLocalSocketAddress());


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

