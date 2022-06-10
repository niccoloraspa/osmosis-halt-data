# Steps to reproduce results
Repository to reproduce the findings

data used for the v9 incident

## Steps to reproduce results

```sh
#!/bin/bash


```

### Transaction data

The following is the transaction data structure:
_______________________________________________________________________________
| Name | Description |
| Height | Block height |
| Code | Transaction error code: 0 for passed, if not zero, failed. |
| Sender | Sender address |
| Type | Transaction type |
| Pool ID | The target pool that was operated on |
| Shares | LP Shares of the pool |
| token[0].amount | Amount of token 0 |
| token[0].denom | Token 0 |
| token[1].amount | Amount of token 1 |
| token[1].denom | Token 1 |
_______________________________________________________________________________

### Excess GAMM data

