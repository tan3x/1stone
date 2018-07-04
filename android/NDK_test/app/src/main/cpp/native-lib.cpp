#include <jni.h>
#include <string>
#include "PrimeNumber.h"

extern "C"
JNIEXPORT jboolean


JNICALL
Java_com_example_tanermetin_ndk_1test_MainActivity_isPrime(
        JNIEnv *env,
        jobject /* this */, jint number) {
    std::string hello = "Hello from C++";
    PrimeNumber primeNumber(number);
    return primeNumber.isPrime;
}
