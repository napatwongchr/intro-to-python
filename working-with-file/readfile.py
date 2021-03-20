from pathlib import Path

import json

def read_text_file(): 
  filepath =  Path().absolute() / "working-with-file" / "hello.txt"

  with open(filepath) as my_file:
      contents = my_file.read()
      print(contents)

def read_json_file():
  filepath =  Path().absolute() / "working-with-file" / "users.json"

  with open(filepath) as users_file:
      users_raw_data = users_file.read()
      users_json = json.loads(users_raw_data)
      print(users_json)


read_json_file()