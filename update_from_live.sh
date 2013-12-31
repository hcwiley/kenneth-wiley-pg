git pull
cp -r ./destiny_resources /home/hcwiley/webapps/destiny_resources_django/
cd /home/hcwiley/webapps/destiny_resources_django/destiny_resources/
export PYTHONPATH=/home/hcwiley/webapps/destiny_resources_django/lib/python2.7/
#/usr/local/bin/python2.7 manage.py collectstatic --noinput
/usr/local/bin/python2.7 manage.py migrate
$HOME/bin/pip install -r requirements.txt
../apache2/bin/restart
exit
