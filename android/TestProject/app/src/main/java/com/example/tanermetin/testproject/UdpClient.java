package com.example.tanermetin.testproject;

public class UdpClient {

    static UdpClient singleton2;
    static String nodeAddress;

    private UdpClient() {
    }


    static UdpClient getInstance(String nodeAddress) {
        if (singleton2 == null) {
            singleton2 = new UdpClient();
        }
        return singleton2;
    }


}
