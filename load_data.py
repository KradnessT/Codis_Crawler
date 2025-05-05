import os
import time

station  = "C0AC70"
year = "2024"
monthSearch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def cdateList(year):
    # days31 (1,3,5,7,8,10,12) days30(2,4,6,9,11)
    month31=[1,3,5,7,8,10,12]
    yearData=[]
    s=""
    for month in monthSearch:
        if month in month31:
            for day in range(1, 32):
                s = year + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)
                yearData.append(s)
        else :
            for day in range(1, 31):
                s = year + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)
                yearData.append(s)
    return yearData

date = cdateList(year)

def main():
    for i in date:
        os.system(f"python -m codis_crawler httpx-crawler  --station {station} --date {i}")
        print(f"--station {station} --date {i}")
        time.sleep(0.1)

main()
