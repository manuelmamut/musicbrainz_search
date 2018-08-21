# musicbrainz_search

## Install

- To start the project create a virtualenv: `virtualenv musicbrainz_dev -p python3`

- Once in your virtualenv run `pip install -r requirements_<environment>_.txt`  
  (so far we have 'dev' an 'qa' environments)

- To run the project `python manage.py runserver <your_host>:<your_port> --settings=musicbrainz.settings.<environment>`


## Caching

   We use LocalMemCached for development environment and Memcache for qa environment.  
   You must install memcache in order to be able to cache on QA env.  

   Probably it could be already running if you are working of linux, you could check it  
   by running `netstat -antlp` on bash and search for a process listening on 127.0.0.1:11211

## Tests

  You can run the tests by going to the project folder 'musicbrainz' and run  
  `python manage.py test --settings=musicbrainz.settings.<environment>`
  
