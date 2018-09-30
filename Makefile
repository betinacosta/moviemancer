run:
	python manage.py runserver

unit-test:
	./manage.py test

# Database tasks
setup_db:
	psql -c "CREATE DATABASE moviemancer;" && \
	psql -c "CREATE USER moviemancer WITH ENCRYPTED PASSWORD 'moviemancer';" && \
	psql -c "grant all privileges on database moviemancer to moviemancer ;"

drop_db:
	psql -c "DROP DATABASE moviemancer"

drop_db_user:
	psql -c "DROP USER moviemancer"

# This task expect that you have a db dump with the name 'lastest.dump'
restore_db:
	pg_restore --verbose --clean --no-acl --no-owner -h localhost -U moviemancer -d moviemancer latest.dump

recreate_db: drop_db drop_db_user setup_db restore_db