package com.example.tanermetin.udpclient;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class MainActivity extends AppCompatActivity {

    EditText editTextServerIP, editTextServerPort;
    Button buttonConnect;
    TextView textViewStatus, textViewPacket;

    public static final int UDP_SERVER_PORT = 11111;

    byte[] buffer = new byte[512];

    DatagramSocket udpSocket = null;
//    DatagramPacket udpRequest = new DatagramPacket(buffer, buffer.length, );
    DatagramPacket udpResponse = new DatagramPacket(buffer, buffer.length);




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editTextServerIP = (EditText) findViewById(R.id.ServerIP);
        editTextServerPort = (EditText) findViewById(R.id.ServerPort);

        textViewStatus = (TextView) findViewById(R.id.Status);
        textViewPacket =(TextView) findViewById(R.id.Packet);

        buttonConnect = (Button) findViewById(R.id.ButtonConnect);

        runUdpClient();


    }

    private void runUdpClient(){
        String message = "salut desde UDP client.";
        DatagramSocket socket = null;
        try{
            socket = new DatagramSocket();
            DatagramPacket packet;

//            InetAddress serverAddr = InetAddress.getByAddress(editTextServerIP.toString().getBytes());
            InetAddress serverAddr = (InetAddress.getByName("127.0.0.1"));


            String strIP = editTextServerPort.getText().toString();
            int udpServerPort = Integer.parseInt(strIP);

            packet = new DatagramPacket(message.getBytes(), message.length(), serverAddr, udpServerPort);
            socket.send(packet);
        }

        catch(SocketException e){
            e.printStackTrace();
        }
        catch(UnknownHostException e){
            e.printStackTrace();
        }
        catch(IOException e){
            e.printStackTrace();
        }
        catch(Exception e){
            e.printStackTrace();
        }
        finally {
            if(socket != null){
                socket.close();
            }
        }
    }

}
