import base64
import binascii
import json

def unicode_str_flow1(input):
    try:
        print("unicode1:"+json.loads(f'"{input}"'))
    except Exception as e:
        pass

def unicode_str_flow2(input):
    try:
        unicode_str=''
        b = [input[i:i+4] for i in range(0,len(input),4)]
        for i in b:
            unicode_str+='\\u'+i
        print("unicode2:"+json.loads(f'"{unicode_str}"'))
    except Exception as e:
        pass

#二进制字节流
def func_binaries_flow(input):
    try:
        b = [input[i:i+8] for i in range(0,len(input),8)]
        flag=''
        for i in b:
            ch1=chr(int(i,2))
            flag+=ch1
        if(flag.isprintable()):
            print("2tostr:%r" %flag)
    except Exception as e:
        pass

#八进制字节流
def func_8_flow(input):
    try:
        flag=hex(int(input,base=8))
        if(flag.isprintable()):
            print("8tostr:%r" %flag)
    except Exception as e:
        pass

#十进制字节流
def func_10_flow(input):
    try:
        b = [input[i:i+2] for i in range(0,len(input),2)]
        flag=''
        for i in b:
            ch1=chr(int(i,10))
            flag+=ch1
        if(flag.isprintable()):
            print("10tostr:%r" %flag)
    except Exception as e:
        pass

#十六进制字节流
def func_hex_flow(input):
    try:
        flag=binascii.a2b_hex(input).decode()
        if(flag.isprintable()):
            print("16tostr: %r" %flag)
    except Exception as e:
        pass

#base64流
def func_base64_flow(input):
    #input='MTIzCg=='
    try:
        flag=base64.b64decode(input)
        print('base64decode:%r' %(str(flag, encoding='utf-8')))
    except Exception as e:
        pass

#base32流
def func_base32_flow(input):
    #input='JEQGY33WMUQHS33V'
    try:
        flag=base64.b32decode(input)
        print("base32decode:%r" %(str(flag, encoding='utf-8')))
    except Exception as e:
        pass

#base16流
def func_base16_flow(input):
    try:
        flag=base64.b16decode(input)
        print("base16decode:%r" %(str(flag, encoding='utf-8')))
    except Exception as e:
        pass

if __name__ == "__main__":

    f=open('enc.txt','r')
    enc_str=f.read()
    print("original:"+enc_str)
    
    #unicode \u4f60\u597d
    unicode_str_flow1(enc_str)
    #unicode 4f60597d
    unicode_str_flow2(enc_str)
    #binaries 
    func_binaries_flow(enc_str)
    
    func_8_flow(enc_str)
    
    func_10_flow(enc_str)
    
    #hex decode
    func_hex_flow(enc_str)
    
    #base64 SGVsbG8sd29ybGQh
    func_base64_flow(enc_str) 
    
    #base32
    func_base32_flow(enc_str)
    
    #base16
    func_base16_flow(enc_str)
