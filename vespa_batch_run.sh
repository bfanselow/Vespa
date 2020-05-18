#!/bin/sh
#
# File: vespa_batch_run.sh
#
# Description:
#  This script will read an input file of "package-version-host" lists and POST each 
#  package-version-host list to the VESPA service. 
#
# Input file format:
#   Each line of the input file has the following JSON list format:
#   [{"package": "<pkgA>", "version": "<pkgA_ver>", "host": "<host>"}, {"package": "<pkgB>", "version": "<pkgB_ver>", "host": "<host>"}, {"package": "pkgC", "version": "<pkgC_ver>", "host": "<host>"}]
#
# NOTE:
#  While the input file is suffixed with ".json", the full contents of the file 
#  do NOT represent a single valid JSON. Rather, each line of the file contains 
#  a valid JSON.
#
# Usage (make sure Vespa-Service is running!):
#  $ ./vespa_batch_run.sh file=<input_file_path> [options]
#
# Options:
#   -d  (turn debug on)
#   -v  (turn verbose on) ## NOT currently in use
#
#############################################################################################

MYNAME='vespa_batch_run.sh'

DEBUG=1
VERSION='v2.0'

CURL='/usr/bin/curl'

VESPA_BASE_URI='http://127.0.0.1:8080/vespa'

VESPA_VULN_URI="${VESPA_BASE_URI}/api/${VERSION}/vuln"

VERBOSE=0 ## toggle this to show/supress the command executed and stats

##-----------------------------------------------------------------------------
## Print all usage details
usage()
{
    exit_code=$1

    echo "Usage:"
    echo ""
    echo "./$MYNAME"
    echo "  -h --help"
    echo "  file=<file-path>"
    echo "  -v --verbose"
    echo ""

    if [ "X${exit_code}" != "X" ]; then
      exit $exit_code
    fi
}
##-----------------------------------------------------------------------------
## main()
##-----------------------------------------------------------------------------
if [ "$1" = "" ]; then
   echo ""
   echo "$MYNAME: Cmd-line ERROR: must specify an input file" 
   usage 1 
fi

## Parse the args: options specified by --<option> (or -o); key/value pairs specified by "<key>=<val>"
while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    case $PARAM in
        -h | --help)
            usage 0
            exit
            ;;
        -v | --verbose)
            VERBOSE=1
            ;;
        file)
            FILE=$VALUE
            ;;
        *)
            echo "$MYNAME: Cmd-line ERROR: unknown parameter \"$PARAM\""
            usage 0
            exit 1
            ;;
    esac
    shift
done

N_lines=`wc -l $FILE` 
## Perfom the script's purpose based on input options
if [ -r $FILE ]; then
  dt_start=`date -u`
  cat $FILE | while read input_line
  do
    payload="{\"data\": $input_line}"
    cmd="$CURL -s ${VESPA_VULN_URI} -d '$payload'"
    if [ $VERBOSE -eq 1 ]; then
      echo "$cmd" 
    fi
    echo "$cmd" | sh
    if [ $VERBOSE -eq 1 ]; then
      echo "" 
    fi
  done 
  dt_end=`date -u`
  if [ $VERBOSE -eq 1 ]; then
    echo "STATS: lines-processed: $N_lines.  Start: $dt_start   End: $dt_end"
  fi
else
  echo ""
  echo "$MYNAME: ERROR - Failed to read input file [${FILE}]. Check file-path and permissions."
  echo ""
  exit 1
fi

exit 0



