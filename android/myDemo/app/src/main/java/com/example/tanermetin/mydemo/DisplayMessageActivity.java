package com.example.tanermetin.mydemo;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class DisplayMessageActivity extends AppCompatActivity {


    public void convertClick(View view){
        EditText dollarAmountEditText = (EditText) findViewById(R.id.dollarAmountEditText);
        Log.i("test", "Converter button is clicked");

        Double dollarAmountDouble = Double.parseDouble(dollarAmountEditText.getText().toString());

        Double poundAmountDouble = 0.75 * dollarAmountDouble ;
        Toast.makeText(DisplayMessageActivity.this,"£"+ poundAmountDouble.toString(), Toast.LENGTH_SHORT).show();

    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_message);

//        Get the intent that started that activity and extract the string
    Intent intent = getIntent();
    String message = intent.getStringExtra(MainActivity.EXTRA_MESSAGE);
//    Capture the layout's TextView and set the string as its text.
    TextView textView2 = findViewById(R.id.textView2);
    textView2.setText(message);

    }




}
