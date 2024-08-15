import os, csv

def tt(sd, oc):
    with open(oc, mode='w', newline='') as f:
        writer = csv.writer(f)
        for r, _, fs in os.walk(sd):
            rp = r.split(os.sep)
            for fi in fs:
                fp = rp + [fi]
                ft = os.path.splitext(fi)[1]
                writer.writerow(fp + [ft])

if __name__ == "__main__":
    sd = r"C:\Program Files\ASUS"
    oc = "directory_structure.csv"
    tt(sd, oc)
    print("Done")

