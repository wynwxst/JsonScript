import sys
import os
import subprocess
import json

def run(command):
    subprocess.check_output(command,shell=True)

def download(url, filename):
    import functools
    import pathlib
    import shutil
    import requests
    import tqdm

    r = requests.get(url, stream=True, allow_redirects=True)
    if r.status_code != 200:
        r.raise_for_status()  # Will only raise for 4xx codes, so...
        raise RuntimeError(f"Request to {url} returned status code {r.status_code}")
    file_size = int(r.headers.get('Content-Length', 0))

    path = pathlib.Path(filename).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    desc = "(Unknown total file size)" if file_size == 0 else ""
    r.raw.read = functools.partial(r.raw.read, decode_content=True)  # Decompress if needed
    with tqdm.tqdm.wrapattr(r.raw, "read", total=file_size, desc=desc) as r_raw:
        with path.open("wb") as f:
            shutil.copyfileobj(r_raw, f)

    return path



def main():
  
  if len(sys.argv) != 1:
    opt = sys.argv[1]
    arg = ""
    args = ""

    if len(sys.argv) == 3:
      arg = sys.argv[2]
    else:
      arg = None
    if arg != None:
      if len(sys.argv) > 4 or len(sys.argv) == 4:
        args = sys.argv[4:]
    
    # stuff starts now
    db = {}
    files = []
    for file in os.listdir(os.getcwd()):
      files.append(file)
    if opt.startswith("--") == False and opt.endswith(".mdb"):
      arg = opt

      files = []

      for file in os.listdir(os.getcwd()):
        files.append(file)
      if arg not in files:
        return FileNotFoundError(f"ERROR: {arg} NOT FOUND")
      else:
        x = open(f"{os.getcwd()}/{arg}","r")
        lines = []

        for di in x.readlines():
          lines.append(di.rstrip())
        toselect = []
        FROM = ""
        toshow = None     


        for lzma in lines:


          
          
          
          item = lzma

          



          if item.startswith("SELECT"):
            
            item = item.replace("SELECT ","")
            item = item.replace(" ","")
            toselect = item.split(",")
            if toselect == []:
              raise RuntimeError("No data given to SELECT")
          elif item.startswith("FROM"):
            item = item.replace("FROM ","")
            FROM = item
            if f"{FROM}.json" not in files:
              raise FileNotFoundError(f"ERROR: FROM {FROM} NOT FOUND")
            

          elif item.startswith("SHOW"):

            toshow = item.replace("SHOW ","")
            toshowe = item.replace("SHOW","")

            if toshow == "" or toshowe == "":
              
              
              with open(f"{os.getcwd()}/{FROM}.json","r") as zl:
                contj = json.load(zl)
                cont = zl.read()

              
              if toselect == [] or "*" in toselect:
                return print(contj)
              for val in toselect:
                try:
                  if ":" in val:
                    y = val.split(":")
                    if len(y) == 1:
                      db[val] = contj[val]
                    else:
                      linez = "db"
                      toexec = ""
                      for vals in y:
                        loc = {}
                        locel = {}
                        toexec += f"['{vals}']"
                        if vals != y[len(y)-1]:
                          exec(f"ll = False\ntry:\n  db{toexec}\nexcept KeyError:\n  ll = True",{"db":db,"dict":contj,"todo":"{}"},locel)
                          if locel["ll"]:

                            exec(f"def dbx():\n db{toexec} = {dict({})}\n return db\nll = dbx()",{"db":db,"dict":contj,"todo":"{}"},loc)
                            if vals != y[len(y)-1]:
                              toadd = f"[{vals}] = " + "{}"
                        else:

                          exec(f"def drx():\n db{toexec} = dict{toexec}\n return db\nll = drx()",{"db":db,"dict":contj,"todo":"{}"},loc)
                          if vals != y[len(y)-1]:
                            toadd = f"[{vals}] = " + "{}"

                        
                          


                  else:
                    db[val] = contj[val]
                except KeyError:
                  raise KeyError(f"KEYERROR: VALUE {val} NOT FOUND")

              return print(db)

          elif item.startswith("INSERT"):

            toshow = item.replace("INSERT ","")
            toshowe = item.replace("INSERT","")

            if toshow == "" or toshowe == "":
              
              
              with open(f"{os.getcwd()}/{FROM}.json","r") as zl:
                contj = json.load(zl)
                cont = zl.read()
                y = val.split(":")
                if len(y) == 1:
                  db[val] = contj[val]
                else:
                  linez = "db"
                  toexec = ""
                  for vals in y:
                    loc = {}
                    toexec += f"['{vals}']"
                    if vals != y[len(y)-1]:

                      exec(f"def dbx():\n db{toexec} = {dict({})}\n return db\nll = dbx()",{"db":db,"dict":contj,"todo":"{}"},loc)
                      if vals != y[len(y)-1]:
                        toadd = f"[{vals}] = " + "{}"
                    else:

                      exec(f"def drx():\n db{toexec} = dict{toexec}\n return db\nll = drx()",{"db":db,"dict":contj,"todo":"{}"},loc)
                      if vals != y[len(y)-1]:
                        toadd = f"[{vals}] = " + "{}"

                    
                      






          




main()




  
