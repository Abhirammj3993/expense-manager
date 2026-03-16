def write_expences(data):
    fp=open("expence_data","w")
    for item in data:
        line1=item[0]+"#"+str(item[1])+"#"+item[2]+"\n"
        fp.write(line1)
def read_expences():
    expenses = []

    with open("expence_data", "r") as file:
        for line in file:
            line = line.strip()              # remove newline
            parts = line.split("#")          # split by #

            if len(parts) == 3:
                category = parts[0]
                amount = int(parts[1])
                date = parts[2]

                record = (category, amount, date)   # create tuple
                expenses.append(record)

    return expenses

