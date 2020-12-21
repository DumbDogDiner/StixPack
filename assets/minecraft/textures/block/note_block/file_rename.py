#%%
import os
import re
for file in os.listdir():
    if file != os.path.basename(__file__):
        pos = re.search(r"\d*(?=\.)", file).start()
        dot = re.search(r"(?!\d)\.",file).start()
        fname_start = file[:pos]
        num = int(file[pos:dot]) -1
        os.rename(file, fname_start + str(num) + ".xx")
for file in os.listdir():
    if file != os.path.basename(__file__):
        dot = re.search(r"(?!\d)\.",file).start()
        os.rename(file, file[:dot]+post)
# %%
