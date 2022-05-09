server:
		flask run

migrations:
		flask db init

init:
		flask db migrate

upgrade:
		flask db upgrade