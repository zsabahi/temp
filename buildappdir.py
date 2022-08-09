import os, shutil

rawDataType =  "Pcap"
cwd = os.getcwd()
DSName = "Tor" #"unb-1gig" #"us-android-all"#"UT"#"recon99-30" #"UT" # "UNB_Final" # "recon99" #
basedir = cwd+"/../DataSets/%s"%DSName
dsdir = basedir + "/%s"% rawDataType
traffictype = [".pcap",".pcapng"]

  
print(dsdir)

for root, dirs, files in os.walk(dsdir):
    print("1")
    for filename in os.listdir(root): 
        print("2")
        if filename[filename.rfind ( '.' ):] in traffictype:           
            print(filename[:filename.rfind ( '.' )])
            path = os.path.join(root, filename[:filename.rfind ( '.' )])
            os.umask(0)
            os.makedirs(path,mode=0o777)
            path2= os.path.abspath(os.path.join(root, filename))
            shutil.copy(path2, path)
                # os.replace(

