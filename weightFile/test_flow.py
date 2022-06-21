import time
import datetime
import sys
import os
import csv
import random

#預設值給3
def getWeight(limit = 3):
    
    weight = []
    cnt = 0

    while cnt < limit:
        #亂數產生數字
        weight.append(random.randint(1, 20))
        cnt = cnt +1

    print(weight)

    # 檔案路徑+檔名.csv
    filepath = "weightFile\\test2.csv"
    if len(weight) > 0 :

        if not os.path.exists(filepath):
            print("檔案不存在。")
            #建立檔案並寫入重量
            with open(filepath,'w',newline='') as csvFile:
                w = csv.writer(csvFile)
                w.writerow(['Date','Weight']) #header
                w.writerow([datetime.datetime.today(),weight[0]])
                w.writerow([datetime.datetime.today(),weight[1]])
                w.writerow([datetime.datetime.today(),weight[2]])

        else:
            print("檔案存在。")
            #寫入最新的重量
            with open(filepath,'a',newline='') as f_object:
                w = csv.writer(f_object)
                w.writerow([datetime.datetime.today(),weight[0]])
                w.writerow([datetime.datetime.today(),weight[1]])
                w.writerow([datetime.datetime.today(),weight[2]])
                f_object.close()

    # 印出檔案內容
    with open(filepath, "r") as my_file:
    # pass the file object to reader()
        file_reader = csv.reader(my_file)
        # do this for all the rows
        for i in file_reader:
            # print the rows
            print(i)
    return  weight


print('go test...')

#不給參數，預設為3
weigth = getWeight()

#給參數
# weigth = getWeight(10)

print(weigth)