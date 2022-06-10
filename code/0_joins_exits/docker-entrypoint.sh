#!/bin/bash

# 4707300 V9 UPGRADE HEIGHT
# 4713064 HALT HEIGHT
seq 4707300 10 4713064 | xargs -n 1 -P 10 -I {} /app/get_data.sh {}