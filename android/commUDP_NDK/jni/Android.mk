LOCALPATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := ndktest
LOCAL_SRC_FILE := ndktest

include $(BUILD_SHARED_LIBRARY)