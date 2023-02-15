# yamdb_final
yamdb_final
[![yamdb_workflow](https://github.com/{iPROJEKT}/{yamdb_final}/workflows/yamdb_workflow.yaml/badge.svg)
# Описание проекта
Этот проект направлен на изучение Dockera, для того чтоб было проще работать на удаленных серверах
# Заполнение .env
*Шаблон env файла*
- EMAIL_HOST_PASSWORD= пароль от почты с которой будет отправляться код для подтверждения 
- EMAIL_HOST_USER= логин почты
- DB_ENGINE= испольщзуемая база данных
- DB_NAME= имя базы
- POSTGRES_USER= имя для захода в базу
- POSTGRES_PASSWORD= пароль от базы
- DB_HOST=db
- DB_PORT= порт
# Описание команд для запуска приложения в контейнерах
- ```docker-compose up -d --build``` - для того чтоб забилдить и контейнеры (без логов -d)
- ```docker-compose exec web python manage.py migrate``` (миграции)
- ```docker-compose exec web python manage.py createsuperuser``` (создание суперюзера)
- ```docker-compose exec web python manage.py collectstatic --no-input``` (сбор статических файлов)
