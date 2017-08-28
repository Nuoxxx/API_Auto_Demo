#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【教程】如何用Python中的chardet去检测字符编码类型
http://www.crifan.com/python_chardet_example_show_how_to_use_to_detect_charset

Version:    2013-09-16
Author:     Crifan Li
Contact:    http://www.crifan.com/contact_me/
"""

import chardet

def chardet_detect_str_encoding():
    """
        Demo how to use chardet to detect string encoding/charset
    """
    inputStr = "\xe6\x89\xbe\xe4\xb8\x8d\xe5\x88\xb0\xe6\x8c\x87\xe5\xae\x9a\xe7\x9a\x84\xe6\xa8\xa1\xe5\x9d\x97\xe3\x80"
    detectedEncodingDict = chardet.detect(inputStr)
    print("type(detectedEncodingDict)=", type(detectedEncodingDict))  # type(detectedEncodingDict)= <type 'dict'>
    print("detectedEncodingDict=", detectedEncodingDict)  # detectedEncodingDict= {'confidence': 0.99, 'encoding': 'utf-8'}
    detectedEncoding = detectedEncodingDict['encoding']
    print("That is, we have %d%% confidence to say that the input string encoding is %s" % (
    int(detectedEncodingDict['confidence'] * 100), detectedEncoding))


if __name__ == '__main__':
    chardet_detect_str_encoding()