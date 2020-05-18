#!/bin/sh
#
# Remote testing of the Vespa service. Primary goal of this script is to check
# our Flask app's handling of errors/exceptions. We want all errors to be
# returned in a proper JSON format.
#
# Testing of successful responses is done be the vespa_batch_run.sh script
# in the project base dir  
#
# Tests:
#  GET /vespa/api/v1.0/data/refresh
#    * invalid resource 
#    * no api-key
#    * invalid api-key header name
#    * invalid api-key header value 
#  --------------------------------
#  GET /vespa/api/v1.0/data/timestamp
#    * valid response 
#  --------------------------------
#  POST /vespa/api/v1.0/vuln
#    * no payload
#    * empty payload
#    * bogus payload
#
#################################################################
CURL='/usr/bin/curl'
VERSION='v2.0'

VESPA_BASE_URI='http://127.0.0.1:8080/vespa'
VESPA_REFRESH_URI="${VESPA_BASE_URI}/api/${VERSION}/data/refresh"
VESPA_TIMESTAMP_URI="${VESPA_BASE_URI}/api/${VERSION}/data/timestamp"
VESPA_VULN_URI="${VESPA_BASE_URI}/api/${VERSION}/vuln"

VESPA_INVALID_URI="${VESPA_BASE_URI}/vulnerable"

APIKEY='William.Fanselow.Vespa.1.0'
BAD_APIKEY='William.Fanselow.Vespa.1.0.bad'
#################################################################

#---------------------------------
# GET to /data/refresh
#---------------------------------
echo "Invalid URI"
cmd="$CURL -s ${VESPA_INVALID_URI}" 
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "No API-key"
cmd="$CURL -s ${VESPA_REFRESH_URI}" 
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Invalid API-key keyname"
cmd="$CURL -s ${VESPA_REFRESH_URI} -H 'API-KEY: ${APIKEY}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Invalid API-key value"
cmd="$CURL -s ${VESPA_REFRESH_URI} -H 'X-Api-Key: ${BAD_APIKEY}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Valid API-key value"
cmd="$CURL -s ${VESPA_REFRESH_URI} -H 'X-Api-Key: ${APIKEY}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
# GET to /data/timestamp/
#---------------------------------
echo "Valid Timestamp response"
cmd="$CURL -s ${VESPA_TIMESTAMP_URI}"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
# POST to /vuln
#---------------------------------
echo "No payload"
cmd="$CURL -s ${VESPA_VULN_URI}"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Empty payload"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Bogus payload 1"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{\"foo\":\"bar\"}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Bogus payload 2 (missing host)"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{\"data\": [{\"package\":\"pip\", \"version\":\"19.1\" }]}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Bogus payload 3 (missing version)"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{\"data\": [{\"package\":\"pip\", \"host\":\"myhost\" }]}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Bogus payload 4 (missing package)"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{\"data\": [{\"version\":\"1.0\", \"host\":\"myhost\" }]}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Valid payload with no affected packages"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{\"data\": [{\"host\":\"foobar\", \"package\":\"pip\", \"version\":\"19.1\" }]}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Valid payload parameters with additional parameters"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{\"data\": [{\"date\": \"2020-05-14\", \"package\": \"freeciv\", \"version\": \"1.1.2\", \"host\": \"74d2d85b57664f819ccea15b57fed5c0.example.org\"}]}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Valid payload single object with affected packages"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{\"data\": [{\"package\": \"freeciv\", \"version\": \"1.1.2\", \"host\": \"74d2d85b57664f819ccea15b57fed5c0.example.org\"}]}'"
echo $cmd
echo $cmd | sh
echo ""

#---------------------------------
echo "Valid payload single object with affected packages"
cmd="$CURL -s ${VESPA_VULN_URI} -d '{ \"data\": [{\"package\": \"freeciv\", \"version\": \"1.1.2\", \"host\": \"74d2d85b57664f819ccea15b57fed5c0.example.org\"}, {\"package\": \"photoshop\", \"version\": \"2.1.1\", \"host\": \"74d2d85b57664f819ccea15b57fed5c0.example.org\"}, {\"package\": \"freeciv\", \"version\": \"1.0.9\", \"host\": \"74d2d85b57664f819ccea15b57fed5c0.example.org\"}, {\"package\": \"flash\", \"version\": \"78.3.9\", \"host\": \"74d2d85b57664f819ccea15b57fed5c0.example.org\"}, {\"package\": \"mint-linux\", \"version\": \"2015.2.0\", \"host\": \"74d2d85b57664f819ccea15b57fed5c0.example.org\"}]}'"
echo $cmd
echo $cmd | sh
echo ""
