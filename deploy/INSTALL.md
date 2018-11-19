
sudo apt install git python3-pip nginx uwsgi supervisor virtualenv virtualenvwrapper

virtualenv -p python3.6 env

pip install -r requirements.txt

source env/bin/activate

./manage.py collectstatic --noinput

sudo ln -sf /usr/local/topevent/deploy/nginx.conf /etc/nginx/conf.d/topevent.conf

sudo ln -sf /usr/local/topevent/deploy/supervisor.conf /etc/supervisor/conf.d/topevent.conf

sudo supervisorctl reload 

sudo supervisorctl restart topevent

sudo /etc/init.d/nginx restart
