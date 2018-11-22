import os,glob

def fileCount(a):
  count=0
  os.chdir(a)
  for file in glob.glob("*.*"):
    count=count+1
  print("Number of files : ",count)

fileCount("F:/Pics")
