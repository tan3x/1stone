package com.example.tanermetin.udpserver;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.EditText;
import android.widget.TextView;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class MainActivity extends AppCompatActivity {

    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView = (TextView) findViewById(R.id.text1);
        runUDPServer();
        finish();

        final int UDP_SERVER_PORT = 11111;
        final int MAX_DATAGRAM_LENGTH = 1500;
    }

        public void runUDPServer(){
            String text;
            byte[] message = new byte[1500];
            DatagramPacket packet = new DatagramPacket(message, message.length);
            DatagramSocket socket = null;

            try {
                socket = new DatagramSocket(11111);
                socket.receive(packet);
                text = new String(message, 0, packet.getLength());
                Log.i("Received UDP packet: ", text);
                textView.setText(text);
            }
            catch (SocketException e) {
                e.printStackTrace();
            }
            catch (IOException e){
                e.printStackTrace();
            }
            finally{
                if (socket != null){
                    socket.close();
                }
            }
        }
    }

