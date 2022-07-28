<h1>
    <img src="https://docs.osmosis.zone/img/osmologo.svg" align="left" width="100" style="margin-right: 20px"/>
    Osmosis Halt Data
</h1>

This repository contains the code to reproduce the data used after the v9 incident.

## Notebooks 

| Data                                 | Description                                                              |
|--------------------------------------|--------------------------------------------------------------------------|
| [analysis](./analysis.ipynb) | Download and process all relevant transactions from `4707300` to halt `4713064` |


## Quickstart

1. Download the csv containing all the transactions from [here](https://fra1.digitaloceanspaces.com/osmosis-halt-data/csv/tx/raw_txs.tar.gz) and place it under `csv/raw_txs.csv`

2. Open the `transactions.ipynb` and start executing from cell `1. Load raw txs into pandas DataFrame > Method 2. Download the Data and load it to a DataFrame`
