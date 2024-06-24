# FROM ubuntu:trusty
#
# RUN sudo apt-get -y update
# RUN sudo apt-get -y upgrade
# RUN sudo apt-get install -y sqlite3 libsqlite3-dev
# RUN mkdir /db
# RUN /usr/bin/sqlite3 /db/s1.db
#
# CMD /bin/bash
FROM postgres

WORKDIR /

COPY dbdata.sql /docker-entrypoint-initdb.d/tables.sql

EXPOSE 5432
