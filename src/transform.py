import csv
import os
 
def read_file(file):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=';', skipinitialspace=True)
        output = []
        for rowind, row in enumerate(reader):
            # cut off the volksbank preamble stuff, also don't handle empty lines
            if rowind > 12 and len(row) > 11:
            
                date = row[0]
                payee = row[3]
                category = row[0]
                memo = ""
                outflow = "0"
                inflow = "0"
                
                if row[12] == "S":
                    outflow = row[11]
                
                if row[12] == "H":
                    inflow = row[11]
            
                if payee:
            
                    # build new row the ynab way
                    newrow = []
                    newrow.append(date.replace(',','.'))
                    newrow.append(payee.replace(',','.'))
                    newrow.append(category.replace(',','.'))
                    newrow.append(memo.replace(',','.'))
                    newrow.append(outflow.replace(',','.'))
                    newrow.append(inflow.replace(',','.'))
                    
                    output.append(newrow)
        
        # csv writer with correct delimiter and no additional newlines
        writer = csv.writer(open('output/result.csv', 'w', newline='', encoding='utf-8'), delimiter=',')
        
        # write the exact header ynab requires
        writer.writerow(["Date", "Payee", "Category", "Memo", "Outflow", "Inflow"])
        
        # all rows without 
        for row in output:
            writer.writerow(row)
 
if __name__ == '__main__':
    for entry in os.scandir("input"):
        if entry.path.endswith(".csv") and entry.is_file():
            read_file(entry)