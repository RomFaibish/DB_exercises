import csv
import pandas as pd
from io import TextIOWrapper
from zipfile import ZipFile

# opens file.
oscars_outfile = open("oscars.csv", 'w' , encoding='UTF8',newline='')
oscars_outwriter = csv.writer(oscars_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)


# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
  # with ZipFile('oscars.zip') as zf:
  #     with zf.open('oscars.csv', 'r') as infile:
  #         reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
  #         for row in reader:
  #             # TO DO splits row into the different csv table files
  #             oscars_outwriter.writerow(row)
  # oscars_outfile.close()
  df = pd.read_csv('filename.zip')
  load_directed_by(df)

def load_directed_by(df):
    selected_columns = df[['Film ID', 'Year of Release']].dropna()
    selected_columns.to_csv('directed_by.csv', index=False)

def get_names():
    return ["Actor", "Director", "Author", "Film Studio", "Film"]

def split_list_value(list_value):
    return list_value.split("&&")
	
if __name__ == "__main__":
    process_file()

