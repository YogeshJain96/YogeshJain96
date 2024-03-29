from datetime import datetime
import json

# datetime object containing current date and time
now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)	

  
# Data to be written
dictionary ={
    "date-time" : dt_string
}
  
# Serializing json 
json_object = json.dumps(dictionary)
  
# Writing to json file
with open("draft_files/time.json", "w") as outfile:
    outfile.write(json_object)
  
# Writing to md file
with open("draft_files/time.md", "w") as outfile:
    outfile.write('# DateTime'+ '\n')
    outfile.write('## ' + dt_string)
