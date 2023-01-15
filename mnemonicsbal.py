#mnemonicsbal.py Bitcoin Legacy compressed/uncompresses address. 04/07/2021
# Search for mnemonics
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import itertools
import urllib.request
import bitcoinlib
import random,os,hashlib
import atexit
from time import time
from datetime import timedelta, datetime

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'

const = "m/44'/0'/0'/0/"



def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))

def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)

def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))

start = time()
atexit.register(end_log)
log("Start Program")

print("mnemonicsbal.py. List loading Good Luck...")

filename ='en.txt'
with open(filename) as file:
    wordlist = file.read().split()


def create_valid_mnemonics(strength=128):
    rbytes = os.urandom(strength // 8)
    h = hashlib.sha256(rbytes).hexdigest()
    b = ( bin(int.from_bytes(rbytes, byteorder="big"))[2:].zfill(len(rbytes) * 8) \
         + bin(int(h, 16))[2:].zfill(256)[: len(rbytes) * 8 // 32] )
    result = []
    for i in range(len(b) // 11):
        idx = int(b[i * 11 : (i + 1) * 11], 2)
        result.append(wordlist[idx])
    return " ".join(result)

def mnem_to_seed(words):
 salt = 'mnemonic'
 seed = hashlib.pbkdf2_hmac("sha512",words.encode("utf-8"), salt.encode("utf-8"), 2048)
 return seed
 
def seed_to_privatekey(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b0=b.subkey_for_path(const + "0")
    return b0.address()
def seed_to_privatekey1(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b1=b.subkey_for_path(const + "1")
    return b1.address()
def seed_to_privatekey2(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b2=b.subkey_for_path(const + "2")
    return b2.address()
def seed_to_privatekey3(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b3=b.subkey_for_path(const + "3")
    return b3.address()
def seed_to_privatekey4(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b4=b.subkey_for_path(const + "4")
    return b4.address()
def seed_to_privatekey5(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b5=b.subkey_for_path(const + "5")
    return b5.address()
def seed_to_privatekey6(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b6=b.subkey_for_path(const + "6")
    return b6.address()
def seed_to_privatekey7(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b7=b.subkey_for_path(const + "7")
    return b7.address()
def seed_to_privatekey8(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b8=b.subkey_for_path(const + "8")
    return b8.address()
def seed_to_privatekey9(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b9=b.subkey_for_path(const + "9")
    return b9.address()
def seed_to_privatekey10(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b10=b.subkey_for_path(const + "10")
    return b10.address()
def seed_to_privatekey11(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b11=b.subkey_for_path(const + "11")
    return b11.address()
def seed_to_privatekey12(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b12=b.subkey_for_path(const + "12")
    return b12.address()
def seed_to_privatekey13(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b13=b.subkey_for_path(const + "13")
    return b13.address()
def seed_to_privatekey14(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b14=b.subkey_for_path(const + "14")
    return b14.address()
def seed_to_privatekey15(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b15=b.subkey_for_path(const + "15")
    return b15.address()
def seed_to_privatekey16(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b16=b.subkey_for_path(const + "16")
    return b16.address()
def seed_to_privatekey17(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b17=b.subkey_for_path(const + "17")
    return b17.address()
def seed_to_privatekey18(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b18=b.subkey_for_path(const + "18")
    return b18.address()
def seed_to_privatekey19(seed):
    b = bitcoinlib.keys.HDKey.from_seed(seed)
    b19=b.subkey_for_path(const + "19")
    return b19.address()
count=0
total=0
while True:
    try:
        line = create_valid_mnemonics()
        seed = mnem_to_seed(line)
        addr = seed_to_privatekey(seed)
        addr1 = seed_to_privatekey1(seed)
        addr2 = seed_to_privatekey2(seed)
        addr3 = seed_to_privatekey3(seed)
        addr4 = seed_to_privatekey4(seed)
        addr5 = seed_to_privatekey5(seed)
        addr6 = seed_to_privatekey6(seed)
        addr7 = seed_to_privatekey7(seed)
        addr8 = seed_to_privatekey8(seed)
        addr9 = seed_to_privatekey9(seed)
        addr10 = seed_to_privatekey10(seed)
        addr11 = seed_to_privatekey11(seed)
        addr12 = seed_to_privatekey12(seed)
        addr13 = seed_to_privatekey13(seed)
        addr14 = seed_to_privatekey14(seed)
        addr15 = seed_to_privatekey15(seed)
        addr16 = seed_to_privatekey16(seed)
        addr17 = seed_to_privatekey17(seed)
        addr18 = seed_to_privatekey18(seed)
        addr19 = seed_to_privatekey19(seed)
        count+=1
        total+=20
        
        contents = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr).read()

        if int(contents) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr + colour_green + ' : Balance : ' + str(contents.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents1 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr1).read()

        if int(contents1) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr1 + colour_green + ' : Balance : ' + str(contents1.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics: " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address :' + addr1)
            f.write('\n===============Bitcoin Address with Balance===================') 
            f.close()
            pass
        contents2 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr2).read()

        if int(contents2) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr2 + colour_green + ' : Balance : ' + str(contents2.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr2)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents3 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr3).read()

        if int(contents3) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr3 + colour_green + ' : Balance : ' + str(contents3.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr3)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents4 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr4).read()

        if int(contents4) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr4 + colour_green + ' : Balance : ' + str(contents4.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr4)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents5 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr5).read()

        if int(contents5) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr5 + colour_green + ' : Balance : ' + str(contents5.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr5)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents6 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr6).read()

        if int(contents6) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr6 + colour_green + ' : Balance : ' + str(contents6.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr6)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents7 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr7).read()

        if int(contents7) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr7 + colour_green + ' : Balance : ' + str(contents7.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr7)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents8 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr8).read()

        if int(contents8) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr8 + colour_green + ' : Balance : ' + str(contents8.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr8)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents9 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr9).read()

        if int(contents9) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr9 + colour_green + ' : Balance : ' + str(contents9.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr9)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents10 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr10).read()

        if int(contents10) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr10 + colour_green + ' : Balance : ' + str(contents10.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr10)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents11 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr11).read()

        if int(contents11) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr11 + colour_green + ' : Balance : ' + str(contents11.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr11)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents12 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr12).read()

        if int(contents12) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr12 + colour_green + ' : Balance : ' + str(contents12.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr12)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents13 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr13).read()

        if int(contents13) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr13 + colour_green + ' : Balance : ' + str(contents13.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr13)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents14 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr14).read()

        if int(contents14) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr14 + colour_green + ' : Balance : ' + str(contents14.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr14)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents15 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr15).read()

        if int(contents15) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr15 + colour_green + ' : Balance : ' + str(contents15.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr15)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents16 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr16).read()

        if int(contents16) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr16 + colour_green + ' : Balance : ' + str(contents16.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr16)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents17 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr17).read()

        if int(contents17) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr17 + colour_green + ' : Balance : ' + str(contents17.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr17)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents18 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr18).read()

        if int(contents18) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr18 + colour_green + ' : Balance : ' + str(contents18.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr18)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        contents19 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + addr19).read()

        if int(contents19) > 0:
            print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + addr19 + colour_green + ' : Balance : ' + str(contents19.decode('UTF8')) + colour_reset)
            print(colour_purple + "mnemonics ==== Found!!!\n mnemonics : " + line + colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n mnemonics: ' + line)
            f.write('\nBitcoin Address : ' + addr19)
            f.write('\n=============Bitcoin Address with Balance=====================') 
            f.close()
            pass
        else:
            print(colour_cyan + "mnemonicsbal.py---" + colour_red + "Random Scan for bitcoin Addresses and Balance---------mizogg.co.uk" + colour_cyan + "---mnemonicsbal.py"  + colour_reset + seconds_to_str())
            print(colour_green + 'Words for Wallet import : ' + '\n' + colour_yellow + line + colour_reset)
            print('Path : ' + colour_cyan + const + "0" + " : " + colour_red + addr + " : " + str(contents.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "1" + " : " + colour_red + addr1 + " : " + str(contents1.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "2" + " : " + colour_red + addr2 + " : " + str(contents2.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "3" + " : " + colour_red + addr3 + " : " + str(contents3.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "4" + " : " + colour_red + addr4 + " : " + str(contents4.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "5" + " : " + colour_red + addr5 + " : " + str(contents5.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "6" + " : " + colour_red + addr6 + " : " + str(contents6.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "7" + " : " + colour_red + addr7 + " : " + str(contents7.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "8" + " : " + colour_red + addr8 + " : " + str(contents8.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "9" + " : " + colour_red + addr9 + " : " + str(contents9.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "10" + " : " + colour_red + addr10 + " : " + str(contents10.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "11" + " : " + colour_red + addr11 + " : " + str(contents11.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "12" + " : " + colour_red + addr12 + " : " + str(contents12.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "13" + " : " + colour_red + addr13 + " : " + str(contents13.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "14" + " : " + colour_red + addr14 + " : " + str(contents14.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "15" + " : " + colour_red + addr15 + " : " + str(contents15.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "16" + " : " + colour_red + addr16 + " : " + str(contents16.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "17" + " : " + colour_red + addr17 + " : " + str(contents17.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "18" + " : " + colour_red + addr18 + " : " + str(contents18.decode('UTF8')) + colour_reset)
            print('Path : ' + colour_cyan + const + "19" + " : " + colour_red + addr19 + " : " + str(contents19.decode('UTF8')) + colour_reset)
            print (colour_green + "\nScan Number" + ' : ' + colour_reset + str (count) + ' : ' + colour_green + "Total Wallets Checked" + ' : ' + colour_reset + str (total))
    except:
        pass

