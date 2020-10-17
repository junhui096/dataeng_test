FROM postgres:latest
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB car
ADD CreateTables.sql /docker-entrypoint-initdb.d/