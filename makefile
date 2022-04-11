build:
	docker-compose build

run:
	docker-compose up

superuser:
	docker-compose run --rm web python manage.py createsuperuser