#!/bin/bash


# please set these variables
TOKEN=9269134245
BASE_URL=http://bestoon.ir

curl --data "token=$TOKEN&amount=$1&text=$2" $BASE_URL/submit/expense/


