import pandas as pd
path = "resources/movies_metadata.csv"
data = pd.read_csv(path, low_memory=False)


del data["belongs_to_collection"]
dropped= data.dropna()

data_title = dropped.set_index("title")

clean_data = data_title.loc[:, ["budget", "genres","original_language","production_companies",
                                "production_countries","release_date","revenue","runtime"]]
clean_data.head()