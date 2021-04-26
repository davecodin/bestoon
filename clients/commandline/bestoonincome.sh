#!/bin/bash

mytoken=9269134245




curl --data "token=$mytoken&amount=$1&text=$2" http://localhost:8009/submit/income/


