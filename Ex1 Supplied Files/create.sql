create table FilmStudio(
  name varchar
);

create table Film(
  film_id varchar UNIQUE NOT NULL,
  film_name varchar,
  imdb_rating varchar,
  imdb_votes varchar,
  content_rating varchar,
  release_year varchar,
  duration varchar,
  genres varchar,
  imdb_rating varchar,
  imdb_votes varchar,
  content_rating varchar,
  studio varchar,
  oscar_year varchar,
  award varchar,
  Foreign KEY(studio) REFERENCES FilmStudio(name)
);

create table Participant(
  name varchar UNIQUE NOT NULL
);

create table Author(
  name varchar,
  Foreign KEY(name) REFERENCES Director(name)
);

create table WrittenBy(
  film_id varchar,
  name varchar,
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Film(name),
);

create table Actor(
  name varchar,
  Foreign KEY(name) REFERENCES Director(name)
);

create table ActedBy(
  film_id varchar,
  name varchar,
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Film(name),
);

create table Director(
  name varchar,
  Foreign KEY(name) REFERENCES Director(name)
);

create table DirectedBy(
  film_id varchar,
  name varchar,
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Film(name),
);

