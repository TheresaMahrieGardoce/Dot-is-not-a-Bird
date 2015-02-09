## Python for Windows

1. Install Python 2.7.8 (https://www.python.org/downloads/release/python-278/)
2. Install PyGame for Python 2.7 (http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)
3. Install Py2Exe for Python 2.7 (http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download)
4. Copy the Python script from (http://www.pygame.org/wiki/Pygame2exe) to make your PyGame an executable Windows app (.exe) 
5. Modify the Python script
```python
  class BuildExe:
    def __init__(self):
        self.script = "MyPyGame.py"
        self.project_name = "MyPyGame"
        self.project_url = "http://yourname.github.io/MyPyGame"
        self.project_version = "1.0"
        self.license = "Free"
        self.author_name = "Juan Dela Cruz"
        self.author_email = "juan@delacruz.com"
        self.copyright = "Copyright (c) 2015"
        self.project_description = "MyPyGame is about blah blah blah"
        self.icon_file = None
        self.extra_datas = []
        self.extra_modules = []
        self.exclude_modules = []
        self.exclude_dll = ['']
        self.extra_scripts = []
        self.zipfile_name = None
        self.dist_dir ='dist'
```
6. Save as **pygame2exe.py** in the same folder of your **MyPyGame.py** then Run the script to build a .exe under ```dist``` folder
7. Make sure all your assets *(images, fonts, sounds)* are included in the ```dist``` folder.
  Create a zip file of your ```dist``` folder and rename it as **MyPyGame.zip** or whatever you named your PyGame.

## Recording a Video Demo

1. Run your executable **MyPyGame.exe**
2. Use a screen recorder of your choice, or
3. Install [TechSmith SnagIt for Chrome] (http://www.techsmith.com/snagit-google-chrome.html) | [TechSmith Snagit (Extension)] (https://chrome.google.com/webstore/detail/techsmith-snagit-extensio/annopcfmbiofommjmcmcfmhklhgbhkce) | [TechSmith Snagit] (https://chrome.google.com/webstore/detail/techsmith-snagit/fcnghgbgmemnlbckdipnmelbanpgneik)
4. Once installed on your Chrome Browser, click its icon ![snagit] (https://lh4.googleusercontent.com/gdWhxJhDvmnEztRF_5DPSmNRZREhFyPIWzSD2sqm_ajAXbq_JIxGAI6OxDI1tlSE3tO9Fyg7=s50-h50-e365-rw) to start recording your screen.
5. On the right side, choose **Screen**, then select the ```MyPyGame.exe``` window
6. Start playing the game then click the **Stop Sharing** button.
7. Test and play the recorded video. And once you're satisfied, click on the lower rightmost and choose **Send to Youtube**.
8. If you already have a Google account, then use that to signup for a Youtube account.
9. Your video will be uploaded. Input the necessary fields as needed *(title, desc, etc)*.

## Github for Windows
*(The basic purpose of Git is to sync your local and online copy of your project and all its assets)*

1. Login or Signup on [Github.com] (http://github.com)
2. Install [Github for Windows] (https://github-windows.s3.amazonaws.com/GitHubSetup.exe)
3. Create a new repository on your local PC, or
4. Clone an exisitng repository on your Github account
5. If unsure, Learn How to Use Github for Windows. [Getting Started] (https://help.github.com/articles/getting-started-with-github-for-windows/) / [Synchronizing repositories] (https://help.github.com/articles/synchronizing-repositories/)
6. On your Github account on your browser, go to your ```MyPyGame``` repository or folder.
7. On the right side, look for the **Settings** icon and click it.
8. Scroll down and look for Github Pages, then click the **Automatic Page Generator**.
9. Scroll down the page editor and click **Continue to Layouts**, choose a theme and click **Publish**.
10. You will see a message saying that *your project page has been created* and a URL ```http://yourname.github.io/your-project```
11. Look under the ```branch```, below ```master```, you will see a new branch created called ```gh-pages```
12. Edit the ```index.html```, copy paste the Youtube embed code and Facebook Like Button, then to save your changes, click **Commit**
13. Go to your uploaded Youtube demo of your PyGame.
14. Choose Embed, and copy the code:
```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/YOUR-YOUTUBE-VIDEO-ID" frameborder="0" allowfullscreen></iframe>
```
15. Go to (https://developers.facebook.com/docs/plugins/like-button)
16. Edit the **URL to Like** with your project's github page. Something like: ```http://yourname.github.io/MyPyGame```
17. Keep the **Layout** set to *Standard*, and **Action Type** is set to *Like*
18. Click **Get the Code** and choose **IFRAME**
19. Copy paste that to your ```index.html``` under ```branch: gh-pages``` Something like this:
```html
<iframe src="//www.facebook.com/plugins/like.php?href=http%3A%2F%2Fyourname.github.io%2FMyPyGame&amp;width&amp;layout=standard&amp;action=like&amp;show_faces=true&amp;share=true&amp;height=80" scrolling="no" frameborder="0" style="border:none; overflow:hidden; height:80px;" allowTransparency="true"></iframe>
```
20. Upload the ZIP file of your Windows executable MyPyGame.exe on GitHub
21. On your repository, you will see your number of ```"commits", "branches", "release", and "contributor"```
22. Choose **release** and click **Create new release**
23. Drag and drop your ZIP file **MyPyGame.zip** or click "select them" to open a dialog to choose your file manually.
24. Once uploaded, you can now add a download link or button. Example: 
```html
<a href="https://github.com/yourname/MyPyGame/releases/download/1/MyPyGame.zip">Download App</a>
```
# Good luck COMPROG! PyGame pa!
