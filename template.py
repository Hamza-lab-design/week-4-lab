"""
RECORD CHECK  -  my version
===========================

Name  :hamza
Lane  :  AI /     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# ===== FUNCTIONS =====
def check_record(value,limit):
    """Return the difference, percent and status for one value aginst its limit."""
    diffrence = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return diffrence,percent,status



  
def print_report(label,value,limit,diffrence,percent,status):
    """ print one formatted report line for a record."""
    print(f"{label}: {value}/{limit}({percent:.1f}%, diff{diffrence:+d}) - {status}")
def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open (path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label,value,limit = line.split(",")
            records.append({"label": label, "value": int(value),"limit": int(limit)})
    return records

def write_results(path,results):
    """Write one label,status line per record to a new file."""
    with open(path,"w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")



# ==== STORE ====
try:
    records = load_records("records.txt")
except FileNotFoundError:
      print("could not find records.txt - starting with an empty list.")
      records = []


# ===== PROCESS + OUTPUT =====
results = []
over_count = 0

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"],record["limit"], difference,percent,status)
    results.append ((record["label"], status))
    if status == "OVER LIMIT":
     over_count += 1

print(f"{over_count} record(s) OVER LIMIT")
write_results("results.txt", results)
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
