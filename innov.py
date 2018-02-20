import glob, os
from operator import itemgetter
from os import listdir
from os.path import isfile, join

def getSize(fileobject):
    fileobject.seek(0,2)
    size=fileobject.tell()
    return size

#CODE1-DESKTOP Organize
#__________________________________________________________________________________________________

print("Messy Desktop?\nNo time to clean it?\nBut love to see it organized?\nI assure you, you are at the right place :)\n")

import shutil

indir="/home/vaibhav/Desktop"
os.chdir("/home/vaibhav/Desktop")

#word files
for file in glob.glob("*.txt") or glob.glob("*.doc") or glob.glob("*.docx") or glob.glob("*.odt") or glob.glob("*.rtf") or glob.glob("*.wpd") or glob.glob("*.wks") or glob.glob("*.wps"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/DOC'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)    
        
#Music files
for file in glob.glob("*.mp3") or glob.glob("*.aif") or glob.glob("*.cda") or glob.glob("*.mid") or glob.glob("*.midi") or glob.glob("*.mpa") or glob.glob("*.ogg") or glob.glob("*.wav") or glob.glob("*.wma") or glob.glob("*.wpl"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/MP3'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)
        
#PDF files    
for file in glob.glob("*.pdf") or glob.glob("*.wpd") or glob.glob("*.tex"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/PDF'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)    

    
#compressed files    
for file in glob.glob("*.7z") or glob.glob("*.arj") or glob.glob("*.deb") or glob.glob("*.pkg") or glob.glob("*.rar") or glob.glob("*.rpm") or glob.glob("*.tar.gz") or glob.glob("*.z") or glob.glob("*.zip"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/COMPRESSED'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)    
    
#database files    
for file in glob.glob("*.csv") or glob.glob("*.dat") or glob.glob("*.db") or glob.glob("*.dbf") or glob.glob("*.log") or glob.glob("*.mdb") or glob.glob("*.sav") or glob.glob("*.sql") or glob.glob("*.tar") or glob.glob(".xml"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/DATABASE'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)
                
#executables    
for file in glob.glob("*.apk") or glob.glob("*.bat") or glob.glob("*.bin") or glob.glob("*.cgi") or glob.glob("*.pl") or glob.glob("*.com") or glob.glob("*.exe") or glob.glob("*.jar"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/EXECUTABLE_FILES'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)        
    
#presentation files
for file in glob.glob("*.key") or glob.glob("*.odp") or glob.glob("*.pps") or glob.glob("*.ppt") or glob.glob("*.pptx"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/PPT'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)
        

#programming files
for file in glob.glob("*.c") or glob.glob("*.class") or glob.glob("*.cpp") or glob.glob("*.cs") or glob.glob("*.h") or glob.glob("*.java") or glob.glob("*.sh") or glob.glob("*.swift") or glob.glob("*.vb") or glob.glob(".py") or glob.glob(".m"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/PROGRAMMING'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)            
        
#video files
for file in glob.glob("*.3g2") or glob.glob("*.3gp") or glob.glob("*.avi") or glob.glob("*.flv") or glob.glob("*.h264") or glob.glob("*.m4v") or glob.glob("*.mkv") or glob.glob("*.mov") or glob.glob("*.mp4") or glob.glob(".mpg") or glob.glob(".mpeg") or glob.glob(".rm") or glob.glob(".swf") or glob.glob(".vob") or glob.glob(".wmv"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/VIDEOS'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)   


#system files
for file in glob.glob("*.bak") or glob.glob("*.cab") or glob.glob("*.cfg") or glob.glob("*.cpl") or glob.glob("*.cur") or glob.glob("*.dll") or glob.glob("*.dmp") or glob.glob("*.drv") or glob.glob("*.icns") or glob.glob(".ico") or glob.glob(".ini") or glob.glob(".lnk") or glob.glob(".msi") or glob.glob(".sys") or glob.glob(".tmp"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/SYSTEM_FILES'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)   
        
#spreadsheet files
for file in glob.glob("*.ods") or glob.glob("*.xls") or glob.glob("*.xlr") or glob.glob("*.ods"):
        location=os.path.join(indir,file)
        newpath = r'/home/vaibhav/Documents/SPREADSHEETS'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        os.chdir(newpath)
        shutil.move(location,newpath)             
#_____________________________________________________________________________________________________

#CODE2-top 10 files
path = raw_input("You need top 10 files from which directory?(Please mention the path):")
F=[]
count=0
if os.path.exists(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp=os.path.join(dirpath,f)
            F.append([0]*2)
            F[count][0]=f
            F[count][1]=os.path.getsize(fp)
            count+=1
            Sizes=sorted(F,key=itemgetter(1))

    for j in range(min(count,10)):
        print Sizes[count-j-1][0],"                size =",Sizes[count-j-1][1],"B"

    if count==0:
        print("\nThe directory is empty!!")
             
else:
    print("The given path doesn't exists!!")
    

#____________________________________________________________________________________________________















