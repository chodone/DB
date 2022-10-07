-- DDL.sql

CREATE TABLE contacts (
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL,
);

ALTER TABLE contacts RENAME TO new_contacts;

ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;

ALTER TABLE new_contacts DROP COLUMN address;

DROP TABLE new_contacts;
