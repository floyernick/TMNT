CREATE TABLE "users" (
  "id" bigserial PRIMARY KEY,
  "name" varchar(100),
  "username" varchar(20),
  "photo" varchar(250),
  "password" varchar(32)
);
CREATE TABLE "channels" (
  "id" bigserial PRIMARY KEY,
  "creator_id" bigint,
  "name" varchar(100),
  "photo" varchar(250)
);
CREATE TABLE "channel_relations" (
  "user_id" bigint,
  "channel_id" bigint,
  "role" smallint
);
CREATE TABLE "posts" (
  "id" bigserial PRIMARY KEY,
  "creator_id" bigint,
  "channel_id" bigint,
  "name" varchar(100),
  "text" varchar(5000),
  "photos" [] varchar(250)
);
CREATE TABLE "replies" (
  "id" bigserial PRIMARY KEY,
  "creator_id" bigint,
  "post_id" bigint,
  "text" varchar(5000),
  "photos" [] varchar(250)
);