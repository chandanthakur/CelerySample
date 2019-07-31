#Python3 required
#Tutorial followed http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

#run below commands from the root of the project
rabbitmq-server #start rabbitmq server on localhost, use dedicated terminal window for this operation
celery worker -A proj.celery_app:app -l INFO # workers are initialized and start waiting for work. Requires active RabbitMQ on the localhost
python3 -m proj.test #sample test.py being run.