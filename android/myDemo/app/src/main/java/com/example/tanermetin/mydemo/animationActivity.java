package com.example.tanermetin.mydemo;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class animationActivity extends AppCompatActivity {



//      Creates 3rd activity with the Animation button

    public void clickAnimation(View view){

        Log.i("test", "animation activity");

//        EditText nombreEditText = (EditText) findViewById(R.id.nombreEditText);
//
//        String messageAnimation = nombreEditText.getText().toString();
//
//        String message =  nombreEditText.getText().toString();



    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_animation);

//      Gets the intent that started and extracts the string
        Intent intent = getIntent();
        String message = intent.getStringExtra(MainActivity.EXTRA_MESSAGE);

        // Capture the layout's TextView and set the string as its text
        TextView textView = findViewById(R.id.textView2);
        textView.setText(message);

    }


}
