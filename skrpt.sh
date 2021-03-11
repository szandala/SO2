#!/bin/bash


# co tu zrobilismy:
#Napisz skrypt, który przeczyta zadany plik,
#utworzy katalog o nazwie „sakwa”
#i utworzy w nim pliki o nazwach odpowiadających kolejnym linijkom w pliku.
#
#Jeżeli plik „sakwa” istnieje i jest katalogiem, należy go usunąć przed rozpoczęciem pracy.
#Potem wypisz zawartość „sakwy” po kolei, pisząc:
#mam NAZWA_PLIKU1
#mam NAZWA_PLIKU2
#mam NAZWA_PLIKU3






PLIK=${1}

# Jeżeli plik „sakwa” istnieje i jest katalogiem, należy go usunąć przed rozpoczęciem pracy.

if [[ -d sakwa ]]; then
    rm -r sakwa
fi

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
