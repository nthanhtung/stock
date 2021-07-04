###############

import pandas as pd
import glob

def csv_path_to_df(path: str = "C:/data"):
    all_files = glob.glob(path + "/*.csv")

    l = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        l.append(df)

    frame = pd.concat(l, axis=0, ignore_index=True)
    return frame


