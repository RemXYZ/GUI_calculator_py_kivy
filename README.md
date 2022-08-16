# GUI_calculator_py_kivy

![App_img](/app_img/app_img.png)

I'm just learning <b>Kivy python library</b> and <b> pyinstaller python library</b> :)

This is just GUI calculator, and it was created precisely according to the <b>Codemy.com guides</b>, and here is a link to it: https://www.youtube.com/watch?v=dLgquj0c5_U&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=1&ab_channel=Codemy.com 

##To run this calculator, you must download kivy library and pyinstaller

> pip install kivy<br>
> pip instal pyinstaller

If you want to make the .exe file, you can repeat as here: https://www.youtube.com/watch?v=NEko7jWYKiE&ab_channel=Codemy.com
and > just copy my whole repository > install packeges > after enter this in cmd: <br>
>pyinstaller main.py -w<br>
>pyinstaller main_pub.spec -y<br>

<br><b>or</b><br><br>

You can do it in a different, better way. In this option our application size will be 25MB unlike 180 MB, and in the app dir we won't have our code(main.py), so enter this in cmd:
>pyinstaller --onefile -w --icon=calculator.ico --add-data "./calc.kv;." main.py

after that you will have ONE file - main.exe. But it won't work, because you'll have to put necessary library next to this file, so go in addition_lib, copy these files and put it in the same directory as main.exe. 

You can check how I did this in ready_app directory, download this and try it yourself 

Or follow this guide for more explanation of this option: https://www.youtube.com/watch?v=k9Hx0q5Sopg&list=PLj_vDrEwBZlJbbZkYAyVdKwzvGRgJPUnZ&index=5&ab_channel=Marv
