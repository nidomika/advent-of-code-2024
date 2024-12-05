if [ -z "$1" ]
then
    echo "Please provide a name for the folder"
    exit
fi

if [ -d "$1" ]
then
    echo "Folder already exists"
    exit
fi

mkdir "$1"
cd "$1" || exit
touch day"$1".py

# shellcheck disable=SC2028
echo "from aocd import data\n\nlines = data.split('\\\n')" >> day"$1".py
echo "Folder $1 created"