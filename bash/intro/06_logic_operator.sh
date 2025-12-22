#!/bin/bash

# ****For numeric comparison****, prefer -lt, -gt, -eq, -ne, -le, -ge operators within [ ].
# -lt: less than, -gt: greater than, -eq: equal, -ne: not equal, -le: less than or equal, -ge: greater than or equal

echo "Enter numbers: "
read X
read Y

if [ "$X" -lt "$Y" ];
then
    echo "X is less than Y";
fi

if [ "$X" -gt "$Y" ];
then
    echo "X is greater than Y";
fi
    
if [ "$X" -eq "$Y" ];
then
    echo "X is equal to Y";
fi
