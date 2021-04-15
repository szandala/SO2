#!/bin/bash -eu

#set +e

#cd ${1}

#set -e
#rm plik

# RCs
DIR_NOT_FOUND=3
FILE_NOT_FOUND=200

pushd
popd

echo ${*}
echo ${@}

TARGET_DIR=${1}
FILE=${2}

if [[ ! -d ${TARGET_DIR} ]]; then
    echo "${TARGET_DIR} is not a dir"
    exit "${DIR_NOT_FOUND}"
    # RC == 0 - 255
fi

cd "${TARGET_DIR}"

if [[ ! -f ${FILE} ]]; then
    echo "${FILE} not found"
    exit ${FILE_NOT_FOUND}
fi
