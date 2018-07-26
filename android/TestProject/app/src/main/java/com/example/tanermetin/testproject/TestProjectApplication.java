package com.example.tanermetin.testproject;

import android.app.Application;
import android.content.res.Configuration;

//Singleton Activity
//https://stackoverflow.com/questions/18002227/why-extend-an-application-class

public class TestProjectApplication extends Application {

    static UdpClient udpClient;

    @Override
    public void onCreate() {
        super.onCreate();

//        Required initialization logic here
        udpClient = UdpClient.getInstance("");

    }

//        Called by the system when the device configuration changes while the component is running.
//        Overriding the method is totally optional.
    @Override
    public void onConfigurationChanged(Configuration newConfig){
        super.onConfigurationChanged(newConfig);
    }
//    Called when the overall system is low on memory. To limit actively running processes.

    @Override
    public void onLowMemory(){
        super.onLowMemory();
    }

}


class Singleton {}











