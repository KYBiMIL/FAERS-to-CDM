import os
import sys
import pandas as pd


p = "H:/IRB/이독성-IRB/FAERS(2012.10-2018.12)/2012.10-2018.12/"

### Find all '.txt' extension file and add them to list
list = [os.path.join(dirpath, f) for dirpath, dirnames, files in os.walk(p) for f in files if all(s in f for s in ['.txt'])]
# list.sort()

### Make multiple list at once
DRUG, DEMO, INDI, OUTC, REAC, RPSR, THER = [[] for i in range(7)]

### Find specific text for full file name then append the file name to list
for i, l in enumerate(list):

    # m = str(l)

    if 'DRUG' in l or 'drug' in l:
        DRUG.append(l)
    elif 'DEMO' in l or 'demo' in l:
        DEMO.append(l)
    elif 'INDI' in l or 'indi' in l:
        INDI.append(l)
    elif 'OUTC' in l or 'outc' in l:
        OUTC.append(l)
    elif 'REAC' in l or 'read' in l:
        REAC.append(l)
    elif 'RPSR' in l or 'rpsr' in l:
        RPSR.append(l)
    elif 'THER' in l or 'ther' in l:
        THER.append(l)


demo = []
for i, l in enumerate(DEMO):
    if '12q' in l:
        demo.append(l)

        
### Read all single text file of table and concatenae to one
table = pd.concat([pd.read_csv(f,sep='$',dtype=object) for f in demo])

### Remove and rename the columns
table.drop(columns=['auth_num','lit_ref','age_grp'], axis=0, inplace=True)
table.rename(columns={'gndr_cod' : 'sex'}, inplace=True)

### Remove the index of file and export file to directory
table.reset_index()
table.to_csv(p+'demo.txt',index=False)
print(table)



