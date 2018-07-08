//
// Created by Taner Metin on 08.07.18.
//

#include <jni.h>
#include <string.h>

jstring Java_com_example_tanermetin_commudp_ndk_MainActivity_hello(JNIEnv* env, jobject obj){

return (*env)-->NewStringUTF(env, "Salut");

}

