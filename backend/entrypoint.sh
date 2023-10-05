#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then

#     while ! nc -vz $POSTGRES_HOST $POSTGRES_PORT; do
#       sleep 0.1
#       echo "here"
#     done
# fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"
