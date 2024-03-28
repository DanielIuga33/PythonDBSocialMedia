<div style="text-align: center;">
    <span style="font-size: 30px; color: silver">
        <u>Hello and welcome to PostgresSQL Database Scripts</u>&#x1F917;
    </span>
</div> 
<br>
<br>
<span style="font-size: 22px; color: lightgrey; text-align: center; margin-left: 30px">
    First you need to crate the database with the following script:
</span>

```postgresql
CREATE DATABASE PythonSocialMedia;
--The following command is an extension for auto-generating the uuid
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"
```
<span style="font-size: 22px; color: lightgrey;  margin-left: 30px">
        Now you need to create the tables:
</span>

### For *_Person Table:_*
```postgresql
create table "Person"
(
    id_person uuid default uuid_generate_v4(),
    name      varchar,
    surname   varchar,
    email     varchar,
    password  varchar,
    cnp       varchar,
    birthday  varchar,
    country   varchar,
    province  varchar,
    city      varchar,
    street    varchar,
    nr       varchar
);

alter table "Person"
    owner to postgres;
```
<br>

### For *_Request Table:_*
```postgresql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
create table "Request"
(
    id_request uuid default uuid_generate_v4(),
    sender     uuid,
    receiver   uuid
);

alter table "Request"
    owner to postgres;
```
<br>

### For *_Friendship Table:_*
```postgresql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
create table "Friendship"
(
    id_friendship uuid default uuid_generate_v4(),
    person1       uuid,
    person2       uuid,
    conversation  varchar
);

alter table "Friendship"
    owner to postgres;
```
<br>

### For *_Notification Table:_*
```postgresql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
create table "Notification"
(
    id_notification uuid default uuid_generate_v4(),
    person          uuid,
    tip            varchar,
    message         varchar,
    data           varchar
);

alter table "Notification"
    owner to postgres;
```



