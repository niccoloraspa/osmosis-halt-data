import requests
import os
from itertools import repeat
import concurrent.futures

UPGRADE_HEIGHT=4707300
HALT_HEIGHT=4713064 
API_ENDPOINT="https://api.osmosis.interbloc.org/cosmos/tx/v1beta1/txs?events=tx.height={}"
MSG_EXIT_POOL="/osmosis.gamm.v1beta1.MsgExitPool"
MSG_JOIN_POOL="/osmosis.gamm.v1beta1.MsgJoinPool"

START_HEIGHT = int(os.getenv("START_HEIGHT", UPGRADE_HEIGHT))
END_HEIGHT = int(os.getenv("END_HEIGHT", HALT_HEIGHT))

MAX_WORKERS = 10

def parse_msg(msg, height):

    m = {}

    if msg["@type"] == MSG_EXIT_POOL:
        m["Type"] = "Exit"
        m["Height"] = height
        m["Sender"] = msg["sender"]
        m["PoolId"] = msg["poolId"]
        m["Shares"] = msg["shareInAmount"]
        m["token[0].amount"] = msg["tokenOutMins"][0]["amount"]
        m["token[0].denom"] = msg["tokenOutMins"][0]["denom"]
        m["token[1].amount"] = msg["tokenOutMins"][1]["amount"]
        m["token[1].denom"] = msg["tokenOutMins"][1]["denom"]
    
    elif msg["@type"] == MSG_JOIN_POOL:
        m["Type"] = "Join"
        m["Height"] = height
        m["Sender"] = msg["sender"]
        m["PoolId"] = msg["poolId"]
        m["Shares"] = msg["shareOutAmount"]
        m["token[0].amount"] = msg["tokenInMaxs"][0]["amount"]
        m["token[0].denom"] = msg["tokenInMaxs"][0]["denom"]
        m["token[1].amount"] = msg["tokenInMaxs"][1]["amount"]
        m["token[1].denom"] = msg["tokenInMaxs"][1]["denom"]

    return m

def parse_tx(tx, height):
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = executor.map(parse_msg, tx["body"]["messages"], repeat(height))
        for m in results:
            if m:
                print(','.join(str(x) for x in m.values()))

def call_endpoint(url, headers = {'Accept': 'application/json'}):
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    for h in range(START_HEIGHT, END_HEIGHT):
        url = API_ENDPOINT.format(h)
        response_json = call_endpoint(url)

        for tx in response_json["txs"]:
            parse_tx(tx, h)
            
if __name__ == "__main__":
    main()


