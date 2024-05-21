import csv
import pandas as pd
from zipfile import ZipFile

DIRECTED_BY_COLUMNS = ['Film ID', 'Directors']
DIRECTED_BY_NAMES_SQL = {'Film ID': 'film_id', 'Directors': 'name'}

DIRECTOR_COLUMNS = ['Directors']
DIRECTOR_NAMES_SQL = {'Directors': 'name'}

ACTED_BY_COLUMNS = ['Film ID', 'Actors']
ACTED_BY_NAMES_SQL = {'Film ID': 'film_id', 'Actors': 'name'}

ACTOR_COLUMNS = ['Actors']
ACTOR_NAMES_SQL = {'Actors': 'name'}

WRITTEN_BY_COLUMNS = ['Film ID', 'Authors']
WRITTEN_BY_NAMES_SQL = {'Film ID': 'film_id', 'Authors': 'name'}

AUTHOR_COLUMNS = ['Authors']
AUTHOR_NAMES_SQL = {'Authors': 'name'}

PARTICIPANT_COLUMNS = ['Directors', 'Authors', 'Actors']
PARTICIPANT_NAMES_SQL = {'Directors': 'name', 'Authors': 'name', 'Actors': 'name'}

FILM_COLUMNS = ['Film ID', 'Film', 'IMDB Rating', 'IMDB Votes', 'Content Rating', 'Year of Release', 'Movie Time',
                'Movie Genre', 'Film Studio/Producer(s)', 'Oscar Year', 'Award']
FILM_NAMES_SQL = {'Film ID': 'film_id', 'Film': 'film_name', 'IMDB Rating': 'imdb_rating', 'IMDB Votes': 'imdb_votes',
                  'Content Rating': 'content_rating', 'Year of Release': ' release_year', 'Movie Time' : 'duration',
                  'Movie Genre' : 'genres', 'Film Studio/Producer(s)': 'studio',
                  'Oscar Year': 'oscar_year','Award': 'award'}

FILM_STUDIO_COLUMNS = ['Film Studio/Producer(s)']
FILM_STUDIO_NAMES_SQL = {'Film Studio/Producer(s)': 'name'}

# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
    with ZipFile('oscars.zip') as zf:
        with zf.open('oscars.csv', 'r') as infile:
            df = pd.read_csv(infile)
    load_simple_csv(df, FILM_STUDIO_COLUMNS, FILM_STUDIO_NAMES_SQL, "FilmStudio.csv")
    load_simple_csv(df, FILM_COLUMNS, FILM_NAMES_SQL, "Film.csv")

    load_participant(df, PARTICIPANT_COLUMNS, PARTICIPANT_NAMES_SQL, "Participant.csv")

    load_simple_csv(df, AUTHOR_COLUMNS, AUTHOR_NAMES_SQL, "Author.csv")
    load_columns_list(df,WRITTEN_BY_COLUMNS, WRITTEN_BY_NAMES_SQL, "WrittenBy.csv", 'Authors')

    load_simple_csv(df, DIRECTOR_COLUMNS, DIRECTOR_NAMES_SQL, "Director.csv")
    load_columns_list(df, DIRECTED_BY_COLUMNS, DIRECTED_BY_NAMES_SQL, "DirectedBy.csv", 'Directors')

    load_simple_csv(df, ACTOR_COLUMNS, ACTOR_NAMES_SQL, "Actor.csv")
    load_columns_list(df, ACTED_BY_COLUMNS, ACTED_BY_NAMES_SQL, "ActedBy.csv", 'Actors')


def load_participant(main_df, participant_columns, names_columns_csv,name_csv):
    for column in participant_columns:
        main_df[column] = main_df[column].str.split('&&')
    df_only_array = main_df[participant_columns]
    df_long = pd.concat([df_only_array['Authors'],df_only_array['Actors'],df_only_array['Directors']])
    df_long.rename("name", inplace=True)
    df_exploded = df_long.explode('name').reset_index(drop=True).dropna().drop_duplicates()
    df_exploded.to_csv(name_csv, index=False)

def load_simple_csv(main_df ,list_columns_from_zip, names_columns_csv, name_csv:str):
    selected_columns = main_df[list_columns_from_zip]
    selected_columns.dropna().drop_duplicates().rename(columns=names_columns_csv)
    selected_columns.to_csv(name_csv, index=False)

def load_columns_list(main_df ,list_columns_from_zip, names_columns_csv, name_csv:str, columns_to_explode):
    # main_df[columns_to_explode] = main_df[columns_to_explode].str.split('&&')
    df_exploded = main_df.explode(columns_to_explode).reset_index(drop=True)
    load_simple_csv(df_exploded, list_columns_from_zip, names_columns_csv, name_csv)


def get_names():
    return ["Film Studio", "Film", "Participant", "Author", "WrittenBy", "Actor", "ActedBy", "Director", "DirectedBy"]

def split_list_value(list_value):
    return list_value.split("&&")
	
if __name__ == "__main__":
    process_file()

