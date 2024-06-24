FROM postgres

WORKDIR /

COPY dbdata.sql /docker-entrypoint-initdb.d/tables.sql

EXPOSE 5432
