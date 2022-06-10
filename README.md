This repository contains the code to reproduce the data used after the v9 incident.

## Steps to reproduce results

The following will generate data for all Join/Exit Pool Events from V9 upgrade 4707300 to halt 4713064.

```sh
cd code
cd 0_joins_exits
make start
```

Alternatively, another way to generate the transaction data is:

```sh
cd code
cd 0_joins_exits
make start
```

This has been used to verify the correctness of the data. 
This command will spin up 4 docker containers that start from different heights and query the data.


The [data](./data/) folder contains the final data used in the analysis in .csv format


| Data                                    | Description                                                           |
|-----------------------------------------|-----------------------------------------------------------------------|
| [joins_exits](./data/0_joins_exits.csv) | All Join/Exit Pool Events from V9 upgrade `4707300` to halt `4713064` |

### Transaction data

All data can be located at [this sheet](https://docs.google.com/spreadsheets/d/15aQWKFAZw07qVTvI8nZj1owiLLFVPP6ez9XnSKwmKXE/edit#gid=1966763120)
The following documents what each column of the transaction params represent: 

| Name              | Description                                                |
|-------------------|------------------------------------------------------------|
| Height            | Block height                                               |
|-------------------|------------------------------------------------------------|
| Code              | Transaction error code: 0 for passed, if not zero, failed. |
|-------------------|------------------------------------------------------------|
| Sender            | Sender address                                             |
|-------------------|------------------------------------------------------------|
| Type              | Transaction type                                           |
|-------------------|------------------------------------------------------------|
| Pool ID           | The target pool that was operated on                       |
|-------------------|------------------------------------------------------------|
| Shares            | LP Shares of the pool                                      |
|-------------------|------------------------------------------------------------|
| token[0].amount   | Amount of token 0                                          |
|-------------------|------------------------------------------------------------|
| token[0].denom    | Token 0                                                    |
|-------------------|------------------------------------------------------------|
| token[1].amount   | Amount of token 1                                          |
|-------------------|------------------------------------------------------------|
| token[1].denom    | Token 1                                                    |


### Excess GAMM data

The "Excess GAMM" related data shows how much excess GAMM shares was acquired by various attackers.
As a result of using buggy calculations, most attackers received excess "Total Shares Out" by about 50%.

| Name              | Description                                                        |
|-------------------|--------------------------------------------------------------------|
| Excess GAMM %     | % Excess GAMM shares calculated by `solveConstantFunctionInvariant`|
|-------------------|--------------------------------------------------------------------|
| Excess GAMM       | The excess GAMM # of shares from `solveConstantFunctionInvariant`. |
|-------------------|--------------------------------------------------------------------|

## Contributors

This repo is mainly a collection of other people work.
Huge thanks to all the people who contributed.

- [joeabbey](https://github.com/joeabbey)
- [Pharaon1993](https://github.com/Pharaon1993)