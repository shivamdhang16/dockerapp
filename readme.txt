=======docker project named two-tier-app with docker volume and network ========

docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=rootpassword -d mysql:latest


docker run -d -v mysql-data:/var/lib/mysql --network=twotier --name two-tier-app -p 5000:5000 -e MYSQL_HOST=m
ysql -e MYSQL_USER=root -e MYSQL_PASSWORD=rootpassword -e MYSQL_DB=shivamtest two-tier-app:latest



docker ps
CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS         PORTS                                       NAMES
725bf4179fe9   two-tier-app:latest   "python app.py"          4 minutes ago   Up 4 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   two-tier-app
dea10d424385   mysql:latest          "docker-entrypoint.s…"   18 hours ago    Up 8 minutes   3306/tcp, 33060/tcp                         mysql


docker exec -it dea10d424385 /bin/bash
bash-5.1# 

mysql -u root -p             
Enter password: 

show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| shivamtest         |
| sys                |
| test               |
+--------------------+
6 rows in set (0.03 sec)



show tables;
+----------------------+
| Tables_in_shivamtest |
+----------------------+
| messages             |
+----------------------+
1 row in set (0.00 sec)



select * from messages;
+----+---------+
| id | message |
+----+---------+
|  1 | kunaL   |
|  2 | kartik  |
|  3 |         |
+----+---------+
