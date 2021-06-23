import os
import glob

def prepare():
  os.system("rm src/test_runners/test_*_Runner.c")
  os.system("rm src/*.o")
  files = glob.glob("./src/test_cases/test_*.c")
  
  for index, item in enumerate(files):
    if item == "./src/test_cases/test_config.c":
        files.pop(index)
        break
        
  files.insert(0, "./src/test_cases/test_config.c")
  print(files)
  
  
  for f in files:
    r = f[:-2] + "_Runner.c"
    r = r.replace("/test_cases/", "/test_runners/")
    os.system("ruby unity/generate_test_runner.rb " + f + " " + r + " config.yml") 
  return files  