umleter
===============
The utility for obtaining statistics of the load on the Linux host by users.

Current repository containing source code for create rpm package via docker container.

Create rpm
----------
1. You need instal docker-ce (and docker-compose) on your machine.
2. Pull this repo
3. Go to repo home and run container
  ```shell
  cd ulmeter
  docker-compose up -d
  ```
4. Pick up rpm package from RPMS directory
5. Stop docker container

Using rpm
---------
```shell
sudo rpm -ivh ulmeter-1.0-1.x86_64.rpm
```
Verify that folder /var/log/user-load-meter contain data

Data processing
---------------
Utility contain two script `ulmeter` and `ulmeter-stat`.

`ulmeter` get load data and writing it in `/var/log/user-load-meter/ultmr` log file. It run every 5 minutes.

`ulmeter-stat` get on input data from `/var/log/user-load-meter/ultmr` file and calculate total load per user. It safe result data in `/var/log/user-load-meter/stat` folder. It run every day.
