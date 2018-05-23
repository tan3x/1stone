package com.example.tanermetin.mydemo;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Display;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import static android.provider.AlarmClock.EXTRA_MESSAGE;

public class MainActivity extends AppCompatActivity {

    public static final String  EXTRA_MESSAGE = "com.example.tanermetin.mydemo.MESSAGE";


    public void buttonMeLlamoClick(View view){
        EditText nombreEditText = (EditText) findViewById(R.id.nombreEditText);

        Log.i("test","button mellamo clicked");

//      When the button pressed, image is changed from caballo-->mundo
        ImageView image = (ImageView) findViewById(R.id.caballoID);
        image.setImageResource(R.drawable.munnndo);

        Toast.makeText(MainActivity.this, "Saludo "+ nombreEditText.getText().toString(), Toast.LENGTH_SHORT).show();

    }


//      Creates 2nd activity when the converter button is pressed.
    public void converterButton(View view2){
        Log.i("test","button converter clicked");

        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText nombreEditText = (EditText) findViewById(R.id.nombreEditText);
        String message = nombreEditText.getText().toString();

        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);




    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}