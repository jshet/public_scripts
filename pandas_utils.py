import pandas as pd
import os
from datetime import datetime  

where_the_files_are = "C:\\data\\deskpass\\records\\"
where_to_save_the_report = "C:\\data\\deskpass\\"
file_list = os.listdir(where_the_files_are)
print(file_list)

def process_file(f):
    f_path = os.path.join(where_the_files_are, f)
    df = pd.read_csv(f_path)
    return df

frames = [process_file(f) for f in file_list]
combined = pd.concat(frames)

# timestamp = datetime.now().timestamp()
# date_time = datetime.fromtimestamp(timestamp)
# timestamp_str = date_time.strftime("%Y-%m-%d_%H%M%S")

timestamp_str = datetime.now().strftime("%Y-%m-%d_%H%M%S")
save_as = os.path.join(where_to_save_the_report, f"combined_{timestamp_str}.csv")

combined.to_csv(save_as, index=False)