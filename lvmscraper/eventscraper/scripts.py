from .models  import Event
import pandas as pd
import math

def import_file(f):   
    #Import the file with pandas
    df = pd.read_csv(f, encoding = "ISO-8859-1")

    #loop over the rows and store them in an object
    for index, row in df.iterrows():
        if type(row.Time) is str:
            Event.objects.get_or_create(
                venue = row.Venue,
                title = row.Title,
                date  = row.Date,
                time  = row.Time,
                URL   = row.URL
            )
        else:
            Event.objects.get_or_create(
            venue = row.Venue,
            title = row.Title,
            date  = row.Date,
            URL   = row.URL
        )