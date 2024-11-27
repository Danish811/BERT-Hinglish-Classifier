import os
import re
import csv
import json
path = "./conversations"

files = os.listdir(path)
output_csv = "conversations.csv"
count = 0
def clean():
    for file in files:
        filepath = os.path.join(path, file)
        with open(filepath,"r", encoding="utf-8") as f:
            filetext = f.read()
            filetext = re.findall(r': (.+)', filetext)
    
        processed_text = "\n".join(filetext)
        with open(filepath,"w", encoding="utf-8") as f:
            f.write(processed_text)
        print(f"File {file} done. Total {count} files")
        count += 1

def save_to_csv():
    with open(output_csv, "w", encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Conversation"])
        for file in files:
            filepath = os.path.join(path, file)
            with open(filepath,"r",encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        csv_writer.writerow([line])

def json_to_csv(json_file):
    csv_file = "English Conversations.csv"

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    with open(csv_file, "w", encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(["Message"])

        for key, value in data.items():
            if "content" in value:
                for entry in value["content"]:
                    if "message" in entry:
                        csv_writer.writerow([entry["message"]])
    
    print(f"Messages extracted and saved to {csv_file}.")


json_to_csv("train.json")