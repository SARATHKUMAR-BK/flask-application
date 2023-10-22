FROM ubuntu
RUN apt  update
RUN apt install  net-tools curl nginx python3 python3-pip python3-venv  mysql-server -y
RUN mkdir flask
COPY ./files/ /flask/
WORKDIR flask
RUN service mysql start && mysql -uroot  -h localhost -e "\
    ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'root123456'; \
    FLUSH PRIVILEGES; \
    create database user; \
    use user; \
    CREATE TABLE users (username VARCHAR(50) NOT NULL PRIMARY KEY,password VARCHAR(100) NOT NULL); " ; service mysql stop
RUN pip install Flask mysql-connector-python
EXPOSE 5000
ENV FLASK_APP=homepage.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG="true"
ENV MYSQL_HOST=localhost
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root123456
ENV MYSQL_DATABASE=user
ENTRYPOINT ["/bin/bash","-c","service mysql start && flask run"]

