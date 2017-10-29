import os
import time
import datetime as dt
import  schedule

def job():
    FRAMES = 168 # change to change the number of images taken
    FPS_IN = 10  # do not change
    FPS_OUT = 24 #output FPS of video
    TIMEBETWEEN = 50 # in seconds you can modify it to change the interval between the photos taken. Now 600 means 10 min
    FILMLENGTH = float(FRAMES / FPS_IN)
    print(FILMLENGTH)


    frameCount = 0
    while frameCount < FRAMES:
        imageNumber = str(frameCount).zfill(7)
        os.system("raspistill -o image%s.jpg"%(imageNumber))
        frameCount += 1
        time.sleep(TIMEBETWEEN - 6) #Takes roughly 6 seconds to take a picture
        nam=dt.now().date()
        nam1=str(dt.now().date()).replace('-','')
    os.system("avconv -r {} -i image{}.jpg -r {} -vcodec libx264 -crf 20 -g 15 -vf crop=2592:1458,scale=1280:720 video_{}.mp4".format(FPS_IN,'%7d',FPS_OUT, nam1))

    # The below code is to delete the images after the video is made.
    mydir=os.getcwd()
    filelist = [ f for f in os.listdir(mydir) if f.endswith(".jpg") ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))
schedule.every().day.at("5:00").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
