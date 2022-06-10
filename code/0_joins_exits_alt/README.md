# Join Exit Pool Data

All Join/Exit Pool Events from V9 upgrade `4707300` to halt `4713064`.

This script is alternative way to generate the `joins_exists` data.
It has been used to verify the correctness of the data.

## Usage

Generate the data with `make start`

The command will spin up 4 docker containers that start from different heights and query the data.

You can stop at any time with:

```bash
make stop
```
