Pan Miron:
- radzę zawsze używać wersji obrazu, przy `FROM python`
- używanie ENTRYPOINT i CMD też się stosuje, ale przy szczególnych przypadkach (gdzie planujemy nadpisywać punkt wejścia kontenera)
- szkoda, że nie dokończył Pan `docker-compose.yml` :p
- ale duży plus za użycie `--rm`, np. `docker run --rm -d --name=grafana -p 3456:3000 grafana/grafana`

Pan arczi1:
- proszę nie commitować plików `.pyc` (ogólnie binarnych)
- proszę korzystać z docker-compose w wersji 3.+
- baza danych nie ma trwałego zasobu

Pan perevist:
- readme zawsze w formacie `.md` :-)
- polecam zapoznać się z klauzulą `replicas` w docker-compose, porty wtedy:
```yml
ports:
- 8000-8003:80
```

Pan TG...87 i Pani Halszka:
- konsekwentność:
```yaml
volumes:
- "./frontend1:/code"
depends_on:
    - database
```
- te apki są podobne - rożnią się kolorem tła. Przerobić to na czytanie zmiennej środowiskowej i mieć jeden katalog.
- robiliście to razem?

Pan Bartosz H.:
- RUNy w Dockerfile'ach bym połączył
- samo Django jest duże, nie sprawdzałem wszystkiego. Ale miałbym kilka uwag. Np. `JOB_STATUS` nie mogłoby być enum'em?

Pan Bartosz R.:
- data storage do baz danych z reguły jest "Docker-maintained", natomiast jeżeli już chcesz podmontować lokalny katalog to raczej jakiś podkatalog, a nie `./`
- alpine, choć malutki, jest strasznie niedorobiony. Polecam inne dystrybucja. Ta nie ma nawet glibc'a

Daniel L.:
- nie mam uwag. Jestem pod wrażeniem
- ale za to do zadania z januszeXa:
```shell
function query_year () {
    # Returns list of movies from ${1} which are more recent than the YEAR given in ${2}
    local -r MOVIES_LIST=${1}
    local -r QUERY=${2}
    local CURRENT_YEAR
    local COUNTER=${QUERY}
    local RESULTS_LIST=()
    CURRENT_YEAR=$(date +'%Y')

    for MOVIE_FILE in ${MOVIES_LIST}; do
        while [ "${COUNTER}" -le "${CURRENT_YEAR}" ] ; do
            COUNTER=$((COUNTER + 1 ))
            if grep "| Year" "${MOVIE_FILE}" | grep -q "${COUNTER}"; then
                RESULTS_LIST+=( "${MOVIE_FILE}" )
            fi
        done
        COUNTER=${QUERY}
    done
}
```
Takiego rozwiązania nie widziałem jeszcze...
