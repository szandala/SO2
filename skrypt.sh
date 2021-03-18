#!/bin/bash

PLIK=${1}
# echo "otwieram ${PLIK}"
if [[ -d sakwa ]]; then
    rm -r sakwa/
else
    echo "katalog nie istniał"
fi

mkdir sakwa

LISTA=$(cat ${PLIK})
for ITEM in ${LISTA}; do
    touch "sakwa/${ITEM}"
    echo "${ITEM}"
done

CONTENT=$(ls sakwa/)

for PRZEDMIOT in ${CONTENT}; do
    echo "Mam ${PRZEDMIOT}"
done

if [[ $(ls | wc -w ) -gt 2 ]]; then
    echo "wiecej niz 2"
fi
