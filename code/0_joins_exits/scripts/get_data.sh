#!/bin/bash

DAEMON_NAME="osmosisd"
RANGE_START=$1
RANGE_END=$(( RANGE_START + 10 ))
for (( b=$RANGE_START; b<$RANGE_END; b++ )); do echo $b
        BLOCK="$(${DAEMON_NAME} q block --node https://rpc.osmosis.interbloc.org:443 $b)"
        NUM_TXS="$(echo $BLOCK | jq -r '.block.data.txs | length')"
        if [[ $NUM_TXS > 0 ]]; then
                TX_HASHES="$(for i in $(echo "${BLOCK}" | jq -r .block.data.txs[]); do echo -n $i | base64 -d | sha256sum -b - | cut -d ' ' -f 1; done)"
                for TXN in $TX_HASHES; do
                        if [ ! -e "/app/data/tx/$TXN.json" ]; then
                                ${DAEMON_NAME} q tx $TXN --output json --node https://rpc.osmosis.interbloc.org:443 > /app/data/tx/$TXN.json
                        fi
                        MSGS="$(jq -r '.tx | select(.["@type"]=="/cosmos.tx.v1beta1.Tx") | .body' "/app/data/tx/$TXN.json")"
                        NUM_MSGS="$(echo $MSGS | jq -r '.messages | length')"
                        if [[ $NUM_MSGS > 0 ]]; then
                                for (( m=0; m<$NUM_MSGS; m++ )); do
                                        echo $MSGS | jq -r " .messages[$m] | select( .[\"@type\"]==\"/osmosis.gamm.v1beta1.MsgJoinPool\" ) | [ $b, .sender, .poolId, .shareOutAmount, .tokenInMaxs[0].amount, .tokenInMaxs[0].denom, .tokenInMaxs[1].amount, .tokenInMaxs[1].denom ] | @csv" | tee -a nitrogen_joins.csv
                                done
                        fi
                done
        fi
done