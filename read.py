import os
import slate3k as slate
import pandas as pd
import re

def clean_text(text):
    pattern = r"\n+"
    return re.sub(pattern,' ', str(text))
    

directory = os.getcwd()

pdf_files = []

for filename in os.listdir(directory)[:2]:
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # print(f)
        pdf_files.append(''.join(slate.PDF(open(f,'rb'))))

df = pd.DataFrame({
    "num": list(range(len(pdf_files))),
    "text": pdf_files
})        

df['text'] = df['text'].apply(clean_text)
df.to_csv('prueba.csv',index = False)