from selenium import webdriver
from pynput.mouse import Controller
from pynput.mouse import Button
import os
import shutil
import time
import subprocess
import zipfile
from pathlib import Path
from multiprocessing import Process, current_process

start = time.time()
print(start)
# Opening firefox
driver = webdriver.Firefox(executable_path=r'C:\Users\Helium\Desktop\Python\geckodriver-v0.26.0-win64\geckodriver'
                                           r'.exe')
mouse_point = Controller()


def youtube_dl_download():
    # Opening youtube-dl.org site in firefox

    print('Youtube-dl.exe starts download')
    driver.get('https://youtube-dl.org/')
    driver.find_element_by_link_text('youtube-dl.exe').click()

    # Download the file
    # print("Current position: " + str(mouse_point.position))
    # click the save file button
    mouse_point.position = (756, 430)
    mouse_point.click(Button.left, 1)
    time.sleep(8)


def ffmpeg_download():
    # Opening ffmpeg site in firefox

    print('ffmpeg.zip file starts download')

    driver.get('https://www.videohelp.com/software/ffmpeg')
    driver.find_element_by_link_text('Download ffmpeg 4.3 Windows 64-bit').click()

    # Download the ffmpeg file
    # print("Current position: " + str(mouse_point.position))

    # click the save file radio button
    mouse_point.position = (528, 393)
    mouse_point.click(Button.left, 1)

    # click the save file button
    mouse_point.position = (749, 474)
    mouse_point.click(Button.left, 1)
    time.sleep(20)


def download_path():
    # Destination of youtube-dl.exe file
    downloads_folder = os.listdir(str(os.path.join(Path.home(), r"Downloads")))
    time.sleep(15)
    driver.close()
    # print(downloads_folder)
    print('Check to see if the downloaded files exists in Downloads folder or not')

    x = 'youtube-dl.exe'
    y = 'ffmpeg-4.3-win64-static.zip'

    if x in downloads_folder and y in downloads_folder:
        print(x, y)

        # Copy the youtube-dl.exe file from Downloads folder to the Python Environment
        shutil.move(str(os.path.join(Path.home(), r"Downloads\youtube-dl.exe")), os.getcwd())

        # Path to the Current Working Directory
        print(os.getcwd())

        # Execute the youtube-dl.exe file
        os.startfile(os.path.join(os.getcwd(), r'youtube-dl.exe'))

        # Copy the ffmpeg file from Downloads folder to the Python Environment
        shutil.move(str(os.path.join(Path.home(), r"Downloads\ffmpeg-4.3-win64-static.zip")), os.getcwd())

        # Unzip the ffmpeg file
        with zipfile.ZipFile(os.path.join(os.getcwd(), r'ffmpeg-4.3-win64-static.zip'), 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())

            # Execute the ffmpeg.exe file
            os.startfile(os.path.join(os.getcwd(), r'ffmpeg-4.3-win64-static\bin\ffmpeg.exe'))
    else:
        print('error: Download File  is not present in the Downloads Folder')


# Download  Video/Audio

def video(cmd):
    subprocess.Popen(["start", "cmd", "/k", cmd], shell=True)


def audio(cmd):
    subprocess.Popen(["start", "cmd", "/k", cmd], shell=True)


if __name__ == "__main__":
    youtube_dl_download()
    ffmpeg_download()

    r'''
    # Multiprocessing
    p1 = Process(target=ffmpeg_download)
    p2 = Process(target=youtube_dl_download)
    p1.start()
    time.sleep(30)
    p2.start()
    p1.join()
    p2.join()
    '''
    download_path()

    av = str(input("You want to download VIDEO or AUDIO : "))

    try:
        if av in ['audio', 'Audio', 'AUDIO', 'video', 'Video', 'VIDEO']:
            print('your input is :{}'.format(av))
        else:
            print('You have entered wrong input...\n'
                  'input should be either audio or video')

    finally:
        i = input("Enter the string after this  https://www.youtube.com/watch?v= in URL:")

        if av in ['audio', 'Audio', 'AUDIO']:
            print('Audio download starts...\n')
            audio(r"youtube-dl -i --extract-audio --audio-format mp3 --ffmpeg-location "
                  r"C:\Users\Helium\PycharmProjects\DownloadAV\ffmpeg-4.3-win64-static\bin {0} && exit".format(i))

        elif av in ['video', 'Video', 'Video']:
            print('Video download Starts...\n')
            video(r"youtube-dl -i --playlist-start 1 {0} && exit ".format(i))

    # Execute time
    end = time.time()
    x = end - start
    print('time diff  {0}:'.format(x))
