# musicbrainz_search

## Install

- To start the project create a virtualenv: `virtualenv musicbrainz_dev -p python3`

- Once in your virtualenv run `pip install -r requirements_<environment>_.txt`

- To run the project `python manage.py runserver <your_host>:<your_port> --settings=musicbrainz.settings.<environment>`

    We use LocalMemCached for development environment and Memcache for qa environment.  
    You must install memcache in order to be able to cache on QA env
