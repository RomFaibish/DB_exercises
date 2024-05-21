create table FilmStudio(
  name varchar,
  PRIMARY KEY(name)
);

create table Film(
  film_id varchar(100) UNIQUE NOT NULL,
  film_name varchar(100),
  imdb_rating float CHECK(imdb_rating >= 0.0 and imdb_rating <= 10.0),
  imdb_votes int,
  content_rating varchar CHECK(content_rating == "G" or content_rating == "PG" or
  content_rating == "PG-13" or content_rating == "R" or content_rating == "NR"),
  release_year int CHECK(release_year > 0),
  duration int CHECK(duration > 0),
  genres varchar(100),
  studio varchar(100),
  oscar_year int CHECK(oscar_year > 0),
  award varchar CHECK(award == "Winner" or award == "Nominee"),
  Foreign KEY(studio) REFERENCES FilmStudio(name),
  PRIMARY KEY(film_id)
);

create table Participant(
  name varchar(100),
  PRIMARY KEY(name)
);

create table Author(
  name varchar(100),
  PRIMARY KEY(name),
  Foreign KEY(name) REFERENCES Participant(name)
);

create table WrittenBy(
  film_id varchar(100),
  name varchar(100),
  PRIMARY KEY(film_id, name),
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Author(name)
);

create table Actor(
  name varchar(100),
  PRIMARY KEY(name),
  Foreign KEY(name) REFERENCES Participant(name)
);

create table ActedBy(
  film_id varchar,
  name varchar,
  PRIMARY KEY(film_id, name),
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Actor(name)
);

create table Director(
  name varchar,
  PRIMARY KEY(name),
  Foreign KEY(name) REFERENCES Participant(name)
);

create table DirectedBy(
  film_id varchar,
  name varchar,
  PRIMARY KEY(film_id, name),
  Foreign KEY(film_id) REFERENCES Film(film_id),
  Foreign KEY(name) REFERENCES Director(name)
);

