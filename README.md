# flask-application
This is simple login and signup application

we are using flask use server (web framework) and used mysql as database and used html and css as frontend .All are integrated in flask framework.
Artifactory are stored in files directory

Full application:
  Image: sarsh/flask-application:v1
  Dockerfile-name: Dockerfile
  How to run:  docker run -it -d -p 5000:5000 sarsh/flask-application:v1
  This image integrated with mysql as well.
  we can tail the container logs and see the output while login and signup

Frontend and flask:
   This image contained only flask and frontend artifate
   This image useful when we work with docker compose
   This is act as separate component 
   Dockerfile-name: Flaskapplication
   Image: sarsh/flask-application:v2_without_db

Docker compose:
   Require_file: docker-compose.yml , init.sql
   init.sql : 
      This file contained the table creation when mysql container start. we attaching this file as volumn
   docker-compose.yml:
       This file reuse the image sarsh/flask-application:v2_without_db as separete component and mysql as separete componet
       You can change the mysql_password as your wish
    How to build: docker-compose up -d