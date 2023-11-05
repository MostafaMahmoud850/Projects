import os 
import shutil 

current_dir = os.path.dirname(os.path.realpath(__file__))

print("welcome in organize.py script - happy clean folder ")

for filename in os.listdir(current_dir):

    ## organize images into Images folder
    if filename.endswith(( ".png" , "jpg" , "jpeg" , "gif" )):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename , "Images")
        os.remove(filename)
        print("Images Done")

## organize video into Videos folder
    if filename.endswith(( ".mp4" , "flv" , "mkv" , "webm" , "mp3" )):
        if not os.path.exists("Videos"):
            os.mkdir('Videos')
        shutil.copy(filename , "Videos")
        os.remove(filename)
        print("Videos Done")  

## organize code into Codes folder
    if filename.endswith(( ".py" , "html" , "css" , "js" , "bash" )):
        if not os.path.exists("Codes"):
            os.mkdir('Codes')
        shutil.copy(filename , "Codes")
        os.remove(filename)
        print("Codes Done")        

## organize document into Documents folder
    if filename.endswith(( ".pdf" , "xlsx" , "xls" , "docx" , "pptx" , "ppt" , "accdb" , "doc")):
        if not os.path.exists("Documents"):
            os.mkdir('Documents')
        shutil.copy(filename , "Documents")
        os.remove(filename)
        print("Documents Done")    

## organize app into Apps folder
    if filename.endswith(( "exe" )): 
        if not os.path.exists("Apps"):
            os.mkdir('Apps')
        shutil.copy(filename , "Apps")
        os.remove(filename)
        print("Apps Done")     

## organize Archive into Archives folder
    if filename.endswith(( ".zip" , "torrent" , "rar" , "tar" )):
        if not os.path.exists("Archives"):
            os.mkdir('Archives')
        shutil.copy(filename , "Archives")
        os.remove(filename)
        print("Archives Done")         