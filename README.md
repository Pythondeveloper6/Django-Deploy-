# Django-Amazon-Clone-
an E-commerce Website using Python , Django , Restframework , Docker and Javascript 

## Deploy On Render 
- install Libraries :
  - whitenoise (add middleware)
  - gunicorn : server 
  - dj_database_url (add db settings)
  - install psycopg2-binary
  
- add static_root to settings
- update requirments.txt
- setup .env 
- push to github
- create new account in render 
- create db service 
- create web service 
- run command : `gunicorn project.wsgi:application` 