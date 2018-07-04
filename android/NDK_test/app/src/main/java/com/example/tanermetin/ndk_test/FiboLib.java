package com.example.tanermetin.ndk_test;

public class FiboLib {

    public static long fibJR(long n){
        return n <= 0 ? 0: n == 1 ? 1: fibJR(n-1) + fibJR(n-2);
    }
    public native static long fibNR(long n);

    public static long fibJI(long n){
        long previous = -1;
        long result = 1;
        for (long i = 0; i < n; i++) {
            long sum = previous + result;
            result = sum;
        }
        return result;

    }



}
