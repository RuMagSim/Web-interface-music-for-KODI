Вебинтерфейс для музыкальной коллекции KODI. Работает напрямую с базой данных, держать в активном режиме KODI не требуется.
Установить KODI.
Создать для KODI базу данных на основе MYSQL. Описание на официальном сайте .
Установить: 
 - apt-get install lamp-server^ phpmyadmin python-pip libapache2-mod-wsgi python-mysqldb libmysqlclient-dev python-dev
 - pip install django
 - a2enmod wsgi

Обслуживание файлов будет производить apache2 на одном порту, на другом порту находится вебинтерфейс, пример конфигурации:
   - 8000 порт на медиаресурсы. Приведен пример монтирования папки с музыкальными файлами в директорию /opt . Исправьте ссылку на собственную директорию нахождения папки медиатеки.
   - 80 порт - Вебинтерфейс для прослушивания музыки, желательно на стандартном порту для удобства. На данном примере проект расположен в папке:  /var/www/

<VirtualHost *:8888>

    ServerName localhost
    ServerAlias localhost
    Alias /media/ /opt/
    Alias /static/ /opt/
    DocumentRoot /opt
    ServerPath "/opt/"
    <Directory /opt/>
     AllowOverride All
    </Directory>


        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

<VirtualHost *:80>
     ServerName localhost
     ServerAlias localhost
     # axe from staic files django
    Alias  "/albums/static" /var/www/music/music/folder/static/
    Alias /static /var/www/music/music/folder/static
    Alias /search/static /var/www/music/music/folder/static
    Alias /songs/static /var/www/music/music/folder/static
    Alias /genres/static /var/www/music/music/folder/static
    Alias /artists/static /var/www/music/music/folder/static

    <Directory /var/www/music>
      Order deny,allow
      Allow from all
    </Directory>
    WSGIScriptAlias / /var/www/music/music/wsgi.py

    <Directory /var/www/music/music>
    <Files wsgi.py>
    Require all granted
    </Files>
    </Directory>
</VirtualHost>


- В файле settings.py в 97 строке MEDIA_URL = 'http://You_ip_address:port' назначьте свой адрес
