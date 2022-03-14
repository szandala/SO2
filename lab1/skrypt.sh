#!/bin/bash

CATALOG=${1}
# cześc, jestem komentarzem
rm -rf ${CATALOG}
mkdir ${CATALOG}

# echo "Cześć świecie"

FILES=$(cat "sprzet")

echo "---"
echo "${FILES}"

ITER=0

for FILE in ${FILES}; do
    echo "tworze ${FILE}"

    if [[ $((ITER % 2)) -eq 0 ]]; then
        echo "parzyste"
        touch ${CATALOG}/${FILE}
    else
        mkdir ${CATALOG}/${FILE}
    fi
    ITER=$((ITER + 1))
done


# do debugowania:
# set -x
for FILE in $(ls ${CATALOG}); do
    if [[ -d ${CATALOG}/${FILE} ]]; then
        echo "${FILE} jest katalogiem"
    fi

    if [[ ! -d ${CATALOG}/${FILE} ]]; then
        echo "${FILE} nie jest katalogiem"
    fi
done

echo "A.D. $(date +"%Y") utworzyłem $(ls ${CATALOG} | wc -w) plików"

# Co chcę byście zapamiętali po dzisiaj:
# co to jest she-bang / hash-bang
# jak przypisywać zmiennej:
# - wartość stałą (linijka 15.)
# - inną zmienną (linijka 3.)
# - wynik polecenia (linijka 10.)
# polecenia:
# - ls, cd, pwd
# - mkdir, touch, rm, cp
# - man (manual) np. man mkdir
# konstrukcję pętli for do done
# konstrukcję warunku if/else fi
# i "złote zasady": https://docs.google.com/spreadsheets/d/1bSIvNF2279aayISTfDmuAS-VUpGC3LnJ2rA_NPLtmQM/edit#gid=0&range=A19:A24
# polecam też stronę:
# https://explainshell.com/

# aaaa, bo pewnie się z tym zderzycie, niczym kierowca z namalowanym tunelem
# https://thoughtnova.com/wp-content/uploads/2021/01/Driver-Crashes-Into-Wall-After-It-Was-Painted-To-Look-Like-A-Tunnelfsst.jpg
# if :spacja: [[ :spacja: jakiś_warunek :spacja: ]]:średnik: :spacja: do
# tam są spacje i średnik.

# Powodzenia!
