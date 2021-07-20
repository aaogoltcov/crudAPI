# Тестовое задания - Backend Developer
##### Есть пользователь, у которого есть фотографии с комментариями и датой загрузки. Необходимо разработать приложение, через которое посредством API пользователь смог бы управлять своими фотографиями. (id photo comment date)
##### У сущности Пользователь добавить параметр, который отвечает за возможность пользователя загружать изображения (выставлять из django- admin). Если флаг не стоит, то пользователь может только смотреть свои изображения.
##### CRUD API работы с фотографиями:
- Update - только текст комментария.
- Delete - когда юзер удаляет фотографию, не удалять ее физически, делать soft delete.
- Create - при загрузке новой фотографии необходимо ее модерировать, для упрощения берем hash(image.content) и если делится целочисленно на 2, то модерация пройдена, иначе говорим пользователю, что его фотография не может быть загружена.
#####Требования:
Django, DRF, пример под docker compose, тесты (все тесты можно не писать, но хорошо если будут комментарии, что бы хотел проверить)

Комментарий: в части тестов сделал бы следующие проверки:
 - Update - проверка на то, что при обновлении старый комментарй затирается новым
 - Delete - проверка на то, что происходит soft delete
 - Create - проверка на то, что в БД добавляется новое фото, + дополнительная проверка на то, что пользователь без разрешения не сможет добавлять фото, а также проверка того, что валидация работает верно (деления хэша на 2)
 - List - проверка на то, что метод возвращает те же данные, что получаем напрямую из БД с помощью select

DB

sudo -u postgres psql postgres
create user postgres with password 'postgres';
alter role postgres set client_encoding to 'utf8';
alter role postgres set timezone to 'Europe/Moscow';
create database postgres owner postgres;
alter user postgres createdb;

PROJECT DOCKER-COMPOSE

docker-compose up
docker-compose run web /usr/local/bin/python manage.py makemigrations photo
docker-compose run web /usr/local/bin/python manage.py makemigrations user
docker-compose run web /usr/local/bin/python manage.py migrate
docker-compose run web /usr/local/bin/python manage.py createsuperuser
login: admin
email: admin@admin.ru
password: admin
