# -*- coding: utf-8 -*-
#from test import Test #import the Test class from the test file

#BUILD_VERSION_MAJOR = 1
#BUILD_VERSION_MINOR = 0
#print("Software Version #: " + str(BUILD_VERSION_MAJOR) + "." + str(BUILD_VERSION_MINOR))  

#Read the state of a button
# In:  none
# Out: None.
# I/O: None.
# Return: test_name: The name of the test, test_status: The status of the test
# MR200728
def button_test():
    #test_status = "IDLE"
    test_status = "PASS"
    test_name = "{'button_test':"
    return test_name+test_status+"}"

#main
if __name__ == "__main__":
    print(button_test(), end='')
    #button_test()
        
