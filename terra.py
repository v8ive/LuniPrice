#from terra_sdk.client.lcd import LCDClient
#from terra_sdk.key.mnemonic import MnemonicKey
#from decouple import config
import requests

#mk = MnemonicKey('choose badge thumb hidden crisp client morning nose math cause provide actual later patrol adapt absorb popular race artwork learn tissue master hello shed')
#print(mk.mnemonic)
#print(mk.acc_address, '\n')
#print(mk.private_key)

#terra = LCDClient(
#    chain_id="columbus-5", 
#    url="https://lcd.terra.dev"
#    )
#wallet = terra.wallet(mk)

#my_wallet = 'terra1lnwtqxeq2nexavanglrf2ay4334e62nsdadnfx'

def get_balance(wallet):
    luni_contract = 'terra1m3tdguf59xq3pa2twk5fjte5g6szj5y9x5npy7'
    query_msg = '{"balance":{"address":"' + wallet + '"}}'
    response = requests.get(
        "https://lcd.terra.dev/wasm/contracts/" + luni_contract + "/store",
        params={"query_msg": query_msg},
    ).json()

    balance = response['result']['balance']
    #balance = "{:,}".format(balance)
    
    return balance

def get_value(wallet):
    balance = get_balance(wallet)
    query_msg = (
        '{"simulation":{"offer_asset":{"amount":"'
        + balance
        + '","info":{"token":{"contract_addr":"terra1m3tdguf59xq3pa2twk5fjte5g6szj5y9x5npy7"}}}}}'
    )

    luni_ust_pair_addr = 'terra1vayuttjw6z4hk5r734z9qatgs8vp6r5a2t043p'
    response = requests.get(
        "https://lcd.terra.dev/wasm/contracts/" + luni_ust_pair_addr + "/store",
        params={"query_msg": query_msg},
    ).json()

    value = response['result']['return_amount']
    
    return value

def swap(amount:int, type:str):
    amount = amount * 1000000
    if type == 'ust':
        query_msg = (
            '{"simulation":{"ask_asset":{"amount":"'
            + str(amount)
            + '","info":{"token":{"contract_addr":"terra1m3tdguf59xq3pa2twk5fjte5g6szj5y9x5npy7"}}}}}'
        )

        luni_ust_pair_addr = 'terra1vayuttjw6z4hk5r734z9qatgs8vp6r5a2t043p'
        response = requests.get(
            "https://lcd.terra.dev/wasm/contracts/" + luni_ust_pair_addr + "/store",
            params={"query_msg": query_msg},
        ).json()

        value = response['result']['return_amount']
        return value
    if type == 'luni':
        query_msg = (
            '{"simulation":{"offer_asset":{"amount":"'
            + str(amount)
            + '","info":{"token":{"contract_addr":"terra1m3tdguf59xq3pa2twk5fjte5g6szj5y9x5npy7"}}}}}'
        )

        luni_ust_pair_addr = 'terra1vayuttjw6z4hk5r734z9qatgs8vp6r5a2t043p'
        response = requests.get(
            "https://lcd.terra.dev/wasm/contracts/" + luni_ust_pair_addr + "/store",
            params={"query_msg": query_msg},
        ).json()
        value = response['result']['return_amount']
        return value

#balance = get_balance(my_wallet)
#print(balance)