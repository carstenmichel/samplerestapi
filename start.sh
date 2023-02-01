SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Get python installation
PY_CMD=""
if command -v python3 &> /dev/null
then
    PY_CMD=$(command -v python3)
elif command -v python &> /dev/null
then
    PY_CMD=$(command -v python)
else
  >&2 echo "Could not find python on your system"
  exit 1
fi

echo "Using python binary: $PY_CMD"


export PYTHONUNBUFFERED=1
export PYTHONPATH=$PYTHONPATH:$SCRIPT_DIR/..

cd $SCRIPT_DIR/

$PY_CMD $SCRIPT_DIR//main.py

exit 0
