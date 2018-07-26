package com.example.tanermetin.commudp_ndk;

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

public class MainActivity extends AppCompatActivity {

    public native String hello();

    static {
        System.loadLibrary("ndktest");

    }


<<<<<<< Updated upstream

    EditText textMessage ;
=======
    EditText textMessage;
>>>>>>> Stashed changes
    EditText ipAddress;
    EditText portUDP;
    Button buttonSend;
    TextView replyMessage;

    byte[] buffer = new byte[512];


    // Used to load the 'native-lib' library on application startup.
    static {
        System.loadLibrary("native-lib");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Example of a call to a native method
        TextView tv = (TextView) findViewById(R.id.sample_text);
        tv.setText(stringFromJNI());

        textMessage = (EditText) findViewById(R.id.EditTextMessage);
        ipAddress = (EditText) findViewById(R.id.EditTextIP);
        portUDP = (EditText) findViewById(R.id.EditTextPortUDP);
        Button buttonSend = (Button) findViewById(R.id.ButtonSend);
<<<<<<< Updated upstream
//        buttonSend.setOnClickListener(this);
=======

        buttonSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


            }
        });
>>>>>>> Stashed changes

//        calling native function
//        TextView()findViewById(R.id.helloNDK).setText(hello());
    }


    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.ButtonSend:
                sendMessage(textMessage.getText().toString());
        }
    }

    private void sendMessage(final String message) {
        final Handler handler = new Handler();
        Thread sendThread = new Thread(new Runnable() {

            String data;

            @Override
            public void run() {

                DatagramSocket socket = null;
                DatagramPacket packet;

                try {
                    InetAddress serverAddress = InetAddress.getByName(ipAddress.getText().toString());
                    int portUdp = Integer.parseInt(portUDP.getText().toString());

                    socket = new DatagramSocket();
                    packet = new DatagramPacket(message.getBytes(), message.length(), serverAddress, portUdp);
                    socket.send(packet);

                } catch (IOException e) {
                    e.printStackTrace();

                } finally {
                    if (socket != null) {
                        socket.close();
                    }
                }
            }
        });
        sendThread.start();
    }

    /**
     * A native method that is implemented by the 'native-lib' native library,
     * which is packaged with this application.
     */
    public native String stringFromJNI();
}
