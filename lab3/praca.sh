# usuniecie 1 linijki
cat ludzie.csv | sed 1d

# znajdujemy czwartek NP
cat ludzie.csv | sed 1d | grep "czwartek NP"


 grep -Povr # te 3 macie znać

 for REPO in $(cat ludzie.csv | sed 1d | grep "czwartek NP" | cut -d',' -f1,3 | sed 's|https*://github.com/|git@github.com:|'); do echo "Klonuje ${REPO}"; done

LISTA=$(cat ludzie.csv | sed 1d | grep "czwartek NP" | cut -d',' -f1,3 | sed 's|https*://github.com/|git@github.com:|')
 for REPO in ; do
    echo "Klonuje ${REPO}";
 done


* ? +
[0-9] [1,3,5,7] [a-z] [s-z]
() - grupy
^ - początek linijki
$ - koniec linijki
