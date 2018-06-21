package com.example.tanermetin.clientudp;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    EditText textMessage ;
    Button buttonSend;
    TextView replyMessage;

    byte [] buffer = new byte[512];

    public static final String IP_ADDRESS = "194.95.175.180";
    public static final int UDP_PORT = 9876;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textMessage = (EditText) findViewById(R.id.EditTextMessage);
        Button buttonSend = (Button) findViewById(R.id.ButtonSend);
        buttonSend.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.ButtonSend:
                sendMessage(textMessage.getText().toString());
        }
    }
    private void sendMessage(final String message){
        final Handler handler = new Handler();
        Thread sendThread = new Thread(new Runnable() {

            String data;

            @Override
            public void run() {

                DatagramSocket socket = null;
                DatagramPacket packet;

                try {
                    InetAddress serverAddress = InetAddress.getByName(IP_ADDRESS);

                    socket = new DatagramSocket();
                    packet = new DatagramPacket(message.getBytes(), message.length(),serverAddress, UDP_PORT );
                    socket.send(packet);

                } catch (IOException e){
                    e.printStackTrace();
                }finally{
                    if(socket != null){
                        socket.close();
                    }
                }
            }
        });

    sendThread.start();
    }
}
