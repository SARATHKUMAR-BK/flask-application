# flask-application
This is simple login and signup application

we are using flask use server (web framework) and used mysql as database and used html and css as frontend .All are integrated in flask framework.
Artifactory are stored in files directory

Full application:
  * Image: sarsh/flask-application:v1
  * Dockerfile-name: Dockerfile
  * How to run:  docker run -it -d -p 5000:5000 sarsh/flask-application:v1
  * This image integrated with mysql as well.
  * we can tail the container logs and see the output while login and signup

Frontend and flask:
  * This image contained only flask and frontend artifate
  * This image useful when we work with docker compose
  * This is act as separate component 
  * Dockerfile-name: Flaskapplication
  * Image: sarsh/flask-application:v2_without_db

Docker compose:
   Require_file: docker-compose.yml , init.sql
   init.sql : 
      This file contained the table creation when mysql container start. we attaching this file as volumn
   docker-compose.yml:
       This file reuse the image sarsh/flask-application:v2_without_db as separete component and mysql as separete componet
       You can change the mysql_password as your wish
    How to build: docker-compose up -d


Install steps for docker:

1. There is multiple way to install docker : https://docs.docker.com/engine/install/ubuntu/
2. we can install docker using apt repo
   https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

3. After install check wheather it install properly by run below command:
   docker --version
4. We need to add current user to docker group for accessing docker without sudo
   sudo usermod -aG docker `whoami`
5. we need to install docker compose as well
   sudo curl -SL https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   docker-compose --version


Run Application:
1. Once docker and docker compose are installed properly ,then we good to deploy our application
2. Clone our repo
   git clone https://github.com/SARATHKUMAR-BK/flask-application.git
   cd flask-application
   docker-compose up
3. Go to browser and enter : http://<localhost or Public IP>:8080/
   Note: if you using ec2 instane then we need to open 8080 in inbound