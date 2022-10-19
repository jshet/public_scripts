import os
import pandas as pd
from datetime import datetime  

def combine_csv_files(dir_of_files,save_to_dir):
    file_list = os.listdir(dir_of_files)

    def process_file(f):
        f_path = os.path.join(dir_of_files, f)
        df = pd.read_csv(f_path)
        return df
    frames = [process_file(f) for f in file_list]
    combined = pd.concat(frames)

    timestamp_str = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    save_as = os.path.join(save_to_dir, f"combined_{timestamp_str}.csv")

    combined.to_csv(save_as, index=False)

where_the_files_are = "path/to/files"
where_to_save_the_report = "path/to/save/report"

combine_csv_files(where_the_files_are, where_to_save_the_report)

