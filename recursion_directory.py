import os
import csv
import json
import pickle
def rec_dir():
    f = open('bufer.txt','w')
    for root, dirs, files in os.walk("."):
        path = root.split(os.sep)
        f.write((len(path) - 1) * '---' + os.path.basename(root) +
             " Folder size: " + str(os.path.getsize(root)) + " bytes " + "\n")
        for file in files:
            f.write(len(path) * '---' + file + " File size: " +
                 str(os.path.getsize(file)) + " bytes " + "\n")
    print("Дерево сохранено в папку bufer.txt")
    f.close() 
    f = open('bufer.txt','r')
    contentt = f.readlines()
    with open("data.json", "w") as write_file:
        json.dump(contentt, write_file)
    with open("data.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = "/", lineterminator="\r")
        file_writer.writerow(contentt)       
    with open('data.pickle', 'wb') as f:
        pickle.dump(contentt, f)
    f.close() 

