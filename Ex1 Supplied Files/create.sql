create table FilmStudio(
  name varchar,
  PRIMARY KEY(name)
);

create table Film(
  film_id varchar,
  film_name varchar,
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
  Foreign KEY(studio) REFERENCES FilmStudio(name),
  PRIMARY KEY(film_id)
);

create table Participant(
  name varchar,
  PRIMARY KEY(name)
);

create table Author(
  name varchar,
  Foreign KEY(name) REFERENCES Participant(name)
);

create table WrittenBy(
  film_id varchar,
  name varchar,
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Author(name)
);

create table Actor(
  name varchar,
  Foreign KEY(name) REFERENCES Participant(name)
);

create table ActedBy(
  film_id varchar,
  name varchar,
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Actor(name)
);

create table Director(
  name varchar,
  Foreign KEY(name) REFERENCES Participant(name)
);

create table DirectedBy(
  film_id varchar,
  name varchar,
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Director(name)
);

