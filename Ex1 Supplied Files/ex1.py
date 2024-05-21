import csv
import pandas as pd
from zipfile import ZipFile

DIRECTED_BY_COLUMNS = ['Film ID', 'Directors']
DIRECTEDBY_NAMES_SQL = {'Film ID': 'film_id', 'Directors': 'name'}
# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
    with ZipFile('oscars.zip') as zf:
        with zf.open('oscars.csv', 'r') as infile:
            df = pd.read_csv(infile)
    load_simple_csv(df, DIRECTED_BY_COLUMNS, DIRECTEDBY_NAMES_SQL, "FilmStudio.csv")

def load_simple_csv(main_df ,list_columns_from_zip, names_columns_csv, name_csv:str):
    selected_columns = main_df[list_columns_from_zip].dropna().drop_duplicates()
    selected_columns.rename(columns=names_columns_csv)
    selected_columns.to_csv(name_csv, index=False)

def load_columns_list(main_df ,list_columns_from_zip, columns_to_explode, names_columns_csv, name_csv:str):
    df_exploded = main_df.explode(columns_to_explode).reset_index(drop=True)
    load_simple_csv(df_exploded, list_columns_from_zip, names_columns_csv, name_csv)


def get_names():
    return ["Actor", "Director", "Author", "Film Studio", "Film"]

def split_list_value(list_value):
    return list_value.split("&&")
	
if __name__ == "__main__":
    process_file()

