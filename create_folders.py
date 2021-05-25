fh = open("cs190j-students.txt")

for name in fh:
#print(name)
    clean_name = name.split()
    pathname =""
    for each in clean_name:
        pathname += each.strip() + "-"
    print("cs190j-" + pathname+"teaching-demo")

fh.close()
