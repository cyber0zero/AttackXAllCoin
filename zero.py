MMDRZA = '''

              ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗
              ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║
              ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║
              ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║
              ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║
              ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
'''

import hashlib
import json
import random
import bit
import requests
from bit import *
from bit.format import bytes_to_wif
from bitcoinlib.encoding import addr_bech32_to_pubkeyhash, change_base, pubkeyhash_to_addr_bech32
from hdwallet import HDWallet
from hdwallet.symbols import ETH as eth
from hdwallet.symbols import TRX as trx
from lxml import html
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console(safe_box="None")


def HASH160(pubk_bytes):
	return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest()).digest()


def ethbal(eth_addr):
	api1 = "&apikey=1MGMZPHPNI34C7V3E46ARYSKC77D624PFC"
	api2 = "&apikey=UDHAMNFNFVI2GKZWMHMIK4TKH7YZF3994R"
	api3 = "&apiKey=AQM65BKZZWN1GFN6U8QIFQKXTEPF8CNAXQ"
	api4 = "&apiKey=GEUXKH2YSMXCE3CANB86DUX8JVHPWFSHI7"
	api5 = "&apiKey=KPASVKCF6DEMHM7YCCS9FMGMCP1D4CUFT8"
	api6 = "&apiKey=HN1VFMTXPITYEWGV3EQ9RY8NE7KZCTJZTA"
	api7 = "&apiKey=A44QE42ZZBC2VTF5JENNCP4VQK53C1M4F3"
	api8 = "&apiKey=87GCRHQ6RZFE5XHEAHHUIXUETQW216I1GI"
	api9 = "&apiKey=RHS9361K4NSWHUFTISGPJAC2I1NN5KFFXK"
	api10 = "&apiKey=1U33RG5RXPRGEZTM7G4GDP5X9MRE4N45W6"
	api11 = "&apiKey=NMY19WIUTVY5HD2UXWGSJCP6U5QQM9JMK8"
	api12 = "&apiKey=B7N679YIW9Y44DDAR9N3MBXT755T7IBCJ9"
	mylistb = [str(api1), str(api2), str(api3), str(api4), str(api10), str(api11), str(api12), str(api5), str(api6),
	           str(api7), str(api8), str(api9)]
	apikeys = random.choice(mylistb)
	# =======================================================
	blocs = requests.get("https://api.etherscan.io/api?module=account&action=balance&address=" + eth_addr + apikeys)
	ress = blocs.json()
	baleth = dict(ress)["result"]
	return baleth


def bnbbal(bnb_addr):
	apibnb1 = "&apikey=XYIHJCC11R3ZA44QNNKIJCTR4BTK4PG223"
	apibnb2 = "&apikey=F758RSYUCABKJWFC49S7DGXHMCHAKDU33Z"
	apibnb3 = "&apikey=D8XIUNBDP1N3E6372SPYAVBFVG51TB7J1F"
	apibnb4 = "&apikey=R442SQ12ZKDD3K83XTTNQMMCDPAIIRTYR7"
	apibnb5 = "&apikey=2K51JPB4TZ3YWHF3M2FI9NCGUXY8ZUKTGJ"
	apibnb6 = "&apikey=2YV8XPH5I4YEM5UW5SRTAEMEDZQA6QH5Y2"
	mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3), str(apibnb4), str(apibnb5), str(apibnb6)]  # 6 API KEYS
	apikeysbnb = random.choice(mylist1)
	blocs1 = requests.get("https://api.bscscan.com/api?module=account&action=balance&address=" + bnb_addr + apikeysbnb)
	ress1 = blocs1.json()
	bal1 = dict(ress1)["result"]
	return bal1


def trxbal(trx_addr):
	block = requests.get("https://apilist.tronscan.org/api/account?address=" + trx_addr)
	res = block.json()
	balances = dict(res)["balances"][0]["amount"]
	return balances
	
x = int(input('[*] Min Num : 1 --------------------------------------------------------------------------------->> '))
y = int(input('[*] Max Num : 115792089237316195423570985008687907852837564279074904382605163141518161494336 ---->> '))
F = []
P = x
z = 1
w = 0
while P < y:
	
	P += 1
	ran = P
	pk = Key.from_int(ran)
	key = Key.from_int(ran)
	hasher = key.to_hex()
	PRIVATE_KEY = str(hasher)
	trx1: HDWallet = HDWallet(symbol=trx)
	ethx: HDWallet = HDWallet(symbol=eth)
	ethx.from_private_key(private_key=PRIVATE_KEY)
	trx1.from_private_key(private_key=PRIVATE_KEY)
	eth_addr = ethx.p2pkh_address()
	trx_addr = trx1.p2pkh_address()
	bnb_addr = str(eth_addr)
	trxbalx = trxbal(trx_addr)
	ethbalx = ethbal(eth_addr)
	bnbbalx = bnbbal(bnb_addr)
	amount_trx = '0.000000'
	if int(ethbalx) > 0.000000 or int(bnbbalx) > 0.000000 or str(trxbalx) != str(amount_trx):
		console.print('[red1 on white]ETH Addr:[white on blue]' + str(eth_addr) + '[/][gold1 on dark_green]  ETH:[white]' + str(ethbalx) + '[/][green]  BNB:[white]' + str(bnbbalx) + '[/]\n[white on green]TRX: ' + str(trx_addr) + '[white]  BALANCE: ' + str(trxbalx) + '[/]\n[white on grey30]PrivateKey: [grey62]' + str(PRIVATE_KEY) + '[/]')
		w += 1
		z += 1
		f = open("win.txt", "a")
		f.write('\nAddress ETH: ' + str(eth_addr) + '         BAL:' + str(ethbalx))
		f.write('\nAddress BNB: ' + str(bnb_addr) + '         BAL:' + str(bnbbalx))
		f.write('\nAddress TRX: ' + str(trx_addr) + '         BAL:' + str(trxbalx))
		f.write('\nPRIVATEKEY: ' + str(PRIVATE_KEY))
		f.close()
	else:
		console.print('[yellow4]Total Checked:[white]' + str(z) + '[/] [red1]  ---------------------- [/][yellow4]  WiN:[white]' + str(w) + '[red1]\nETH Addr:[white]' + str(eth_addr) + '[/][gold1]  ETH:[white]' + str(ethbalx) + '[/][gold1]  BNB:[white]' + str(bnbbalx) + '[/]\n[gold1]TRX: [white]' + str(trx_addr) + '[sky_blue3]  BALANCE: ' + str(trxbalx) + '[/]')
		z += 1


