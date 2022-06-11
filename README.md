<h1>
    <img src="https://docs.osmosis.zone/img/osmologo.svg" align="left" width="100" style="margin-right: 20px"/>
    Osmosis Halt Data
</h1>

This repository contains the code to reproduce the data used after the v9 incident.

## Notebooks 

| Data                                 | Description                                                              |
|--------------------------------------|--------------------------------------------------------------------------|
| [transactions](./transactions.ipynb) | Download and process all Join/Exit Pool from `4707300` to halt `4713064` |
| [pools](./pools.ipynb)               | Get shares information of every pool at every height                     |

## Final Data

### Transaction data

All data can be located at [csv/txs.csv](./csv/txs.csv)

The following documents what each column of the transaction params represent: 

| Name          | Description                                                |
|---------------|------------------------------------------------------------|
| height        | Block height                                               |
| txhash        | Transaction hash                                           |
| code          | Transaction error code: 0 for passed, if not zero, failed. |
| send          | Sender address                                             |
| @type         | Transaction type                                           |
| poolId        | The target pool that was operated on                       |
| Shares        | LP Shares of the pool                                      |
| token0_amount | Amount of token 0                                          |
| token0_denom  | Token 0                                                    |
| token1_amount | Amount of token 1                                          |
| token1_denom  | Token 1                                                    |