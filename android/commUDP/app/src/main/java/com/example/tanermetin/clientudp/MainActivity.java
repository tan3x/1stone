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
    EditText ipAddress;
    EditText portUDP;
    Button buttonSend;
    TextView replyMessage;

    byte [] buffer = new byte[512];

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textMessage = (EditText) findViewById(R.id.EditTextMessage);
        ipAddress = (EditText) findViewById(R.id.EditTextIP);
        portUDP = (EditText) findViewById(R.id.EditTextPortUDP);
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

                DatagramSocket socket= null;
                DatagramPacket packet;

                try {
                    InetAddress serverAddress = InetAddress.getByName(ipAddress.getText().toString());
                    int portUdp = Integer.parseInt(portUDP.getText().toString());

                    socket = new DatagramSocket();
                    packet = new DatagramPacket(message.getBytes(), message.length(),serverAddress, portUdp );
                    socket.send(packet);

                } catch (IOException e){
                    e.printStackTrace();

                } finally{
                    if(socket != null){
                        socket.close();
                    }
                }
            }
        });
    sendThread.start();
    }
}
