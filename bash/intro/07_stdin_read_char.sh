#!/bin/bash

# This script reads one character from STDIN and responds appropriately to 'Y'/'y' with "YES" or 'N'/'n' with "NO"
# ****For string comparison****, use '=' operator within [ ]
# -n 1 flag reads exactly one character without waiting for Enter

echo -e "Enter camelCase letter y or n: \n"

read -n 1 char

if [ "$char" = "y" ] || [ "$char" = "Y" ];
then
    echo "YES";
fi

if [ "$char" = "n" ] || [ "$char" = "N" ];
then
    echo "NO";
fi
