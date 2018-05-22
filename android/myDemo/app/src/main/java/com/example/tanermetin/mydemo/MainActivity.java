package com.example.tanermetin.mydemo;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    public void buttonMeLlamoClick(View view){
        EditText nombreEditText = (EditText) findViewById(R.id.nombreEditText);

        Toast.makeText(MainActivity.this, "Saludo "+ nombreEditText.getText().toString(), Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
