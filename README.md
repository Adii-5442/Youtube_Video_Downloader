# Youtube_Video_Downloader
**Prerequistes:** 
  You have to install these modules before running the project:
    a)pytube
    b)Tkinter
 
 **IMPORTANT**
 By default this project downloads only the files in 360p resolution.
 For downloading files in higher resolution you must change the following line:
  At line 27:
  
 Change :  **video = url.streams.filter(file_extension='mp4').first()**   to **video=url.streams.filter(resolution='720p').first()**
 
 Additional features and updates will be added soon
 
                                                                                                                      **By DARKFIRE**
