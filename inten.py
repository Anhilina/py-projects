#!/usr/bin/env python3
#coding: latin-1
import os, sys
import random

def random_pass():
    login = input()
    pswrd = ''
    for i in range(16):
        pswrd = pswrd + random.choice(list('!,.@#%^&*()1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return "Привет, " + str(login) + "! password sdfdsfsdfdsfdsfsdof yours: " + str(pswrd)


if __name__ == "__main__":
    password = random_pass()
    print(password)
