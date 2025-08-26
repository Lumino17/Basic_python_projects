import random

# striping whitespaces 
def strip_space(msg : str)->str:
    for i, char in enumerate(msg):
        if char == ' ':
            metadata.append(i)
    return metadata and msg.replace(" ","")

def insert_space(r_enc : str, metadata)->str:
    r_enc = list(r_enc)
    for position in sorted(metadata):
        r_enc.insert(position,' ')
    return ''.join(r_enc)    
      
# 1st layer : reversing of string
def rev_enc(msg : str)-> str:
    return msg[::-1]
def r_rev_enc(msg : str)-> str:
    return msg[::-1]

# 2nd layer : rotation of elements to right by 7 
def rotate_enc(msg : str, n : int = 7 )->str:
    return msg[n:]+msg[:n]
def r_rotate_enc(msg : str, n : int = 7)->str:
    return msg[-n:]+msg[:-n]

# 3rd layer : mirror and reverse
def mirror_enc(msg : str)->str:
    half = len(msg)//2
    return msg[half:]+msg[:half]
def r_mirror_enc(msg : str)->str:
    return mirror_enc(msg)

# 4th layer : replacement 
def replace_enc(msg : str)->str:
    for old,new in replacements.items():
        msg = msg.replace(old,new)
    return msg 
def r_replace_enc(msg : str)->str:
    for old, new in replacements.items():
        msg = msg.replace(new,old)
    return msg    



# code necessities 
msg = "hi my name is om, i am in first year in branch cse "
metadata =[]
replacements = {
        "a":"/",
        "b":"?",
        "c":"=",
        "d":"+",
        "e":"_",
        "f":"-",
        "g":"9",
        "h":"6",
        "i":"5",
        "j":"8",
        "k":"7",
        "l":"!",
        "m":"#",
        "n":"%",
        "o":"@",
        "p":"$",
        "q":"^",
        "r":"4",
        "s":"2",
        "t":"1",
        "u":"3",
        "v":"0",
        "w":"&",
        "x":"*",
        "y":"|",
        "z":"."
    } 
# functions dictionary
fuctions ={
    "s":(rev_enc,r_rev_enc),
    "g":(rotate_enc,r_rotate_enc),
    "W":(mirror_enc,r_mirror_enc),
    "o":(replace_enc,r_replace_enc)
}

# main functions (encryption, decryption)
def enc_msg(msg : str, depth: int = 4):
    key = random.sample(list(fuctions.keys()),depth)
    enc = msg
    for k in key:
        f, _ = fuctions[k]
        enc = f(enc)
    return enc,key
def r_enc_msg(enc : str, key : list):
    r_enc = enc
    for k in reversed(key):
        _, f_inv = fuctions[k]
        r_enc = f_inv(r_enc)
    return r_enc

# encryption and decryption function calling
print(msg)
msg = strip_space(msg)
enc, key = enc_msg(msg,depth=4)

r_enc = r_enc_msg(enc,key)
result =insert_space(r_enc, metadata)

# printing results
print(enc)
print(key)
print(result)



           



                     
  





     

