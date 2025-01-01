import os
import shutil

pics_extentions = ("gif", "jfif", "jpg", "jpeg", "webp")
text_ext = (".txt", ".lst", ".pdf")
video_ext = ("mp4", "mp3")

def makeNewFolder(name):
    os.mkdir(name)

dir_now = os.path.realpath(".")
counter = 0  # تعريف المتغير خارج الحلقة

# تحقق من وجود المجلد "Images" وإنشائه إذا لم يكن موجودًا
if not os.path.exists("Images"):
    makeNewFolder("Images")

for i in os.listdir(dir_now):
    if i.endswith(pics_extentions):
        source = os.path.join(os.getcwd(), i)
        destination = os.path.join(os.getcwd(), "Images", i)
        
        if not os.path.exists(destination):
            shutil.copy(source, destination)
            counter += 1
            print(f"Copied {i} to Images folder")
            os.remove(source)
        else:
            print(f"File already exists: {i}")

num_img = counter
counter = 0
    
for i in os.listdir(dir_now):
    if i.endswith(text_ext):
        source = os.path.join(os.getcwd() , i)
        if not os.path.exists("Text_Files"):
            makeNewFolder("Text_Files")
        destination = os.path.join(os.getcwd() , "Text_Files", i)
        if not os.path.exists(destination):
            shutil.copy(source, destination)
            counter +=1
            print(f"Copied {i} to Images folder")
        
            os.remove(source)
        
        else:
            print(f"file already Exists: {i}")
num_text = counter
counter = 0

for i in os.listdir(dir_now):
    if i.endswith(video_ext):
        #counter = 0
        source = os.path.join(os.getcwd() , i)
        if not os.path.exists("Videos"):
            makeNewFolder("Videos")
        destination = os.path.join(os.getcwd() , "Videos", i)
        if not os.path.exists(destination):
            shutil.copy(source, destination)
            counter +=1
            print(f"Copied {i} to Images folder")
        
            os.remove(source)
        
        else:
            print(f"file already Exists: {i}")

print(f"Number of image files copied: {num_img}")
print(f"Numbers Of Text Files: {num_text}")
print(f"Numbers Of Videos Files: {counter}")
    
         

