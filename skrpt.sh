#!/bin/bash

PLIK=${1}

# Jeżeli plik „sakwa” istnieje i jest katalogiem, należy go usunąć przed rozpoczęciem pracy.

if [[ -d sakwa ]]; then
    rm -r sakwa
fi
cd pies
mkdir sakwa

LISTA=$(cat "${PLIK}")
for SLOWO in ${LISTA}; do

    touch sakwa/${SLOWO}

done


for ITEM in $(ls sakwa); do
    echo "Mam ${ITEM}"
done

if [[ 5 -gt 3 ]]; then
    echo "5 greater then 7"

else
    jamnik
fi

ILOSC=$(ls sakwa | wc -w)
