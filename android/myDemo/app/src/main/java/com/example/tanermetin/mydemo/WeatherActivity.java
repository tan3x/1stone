package com.example.tanermetin.mydemo;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

public class WeatherActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_weather);

//        TODO: Intent:Season between main activity and weather activity.

        Intent intent = getIntent();

        String season = intent.getStringExtra(MainActivity.SEASON);

        EditText seasonEdit = (EditText) findViewById(R.id.EditTextSeason);
        TextView seasonView = (TextView) findViewById(R.id.textViewSeason);

        seasonView.setText(season);




    }
}
