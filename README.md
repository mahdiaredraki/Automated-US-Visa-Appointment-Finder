### What does this program do?
This program will automate the process of searching for US Visa appointments. Currently there are few appointment slots that get released at random times on random days. Instead of sitting there all day refreshing, you can use this program to do that for you.
Supported countries of application:
Armenia, UAE, Turkey, and Canada.
This was inspired by EasySlotBooking.com (https://easyslotbooking.com/) which has applied a similar bot for applicants in India.

This application will provide a similar service for applicants in Armenia, UAE, Turkey, and Canada.

I hope this bot can help you find an appointment!

### To run the program
- Supported browser: Google Chrome
- Supported Operating Systems: Windows, and MacOS
- To run the application, you need to download chromedriver.
Download chromedriver:
https://chromedriver.chromium.org/downloads
- Extract the chromedriver file and paste it into the same folder as this repository.
- It is important that "US_Visa_Appointment_Bot.exe" and "chromedriver.exe" are in the same folder.
- Double click on "US_Visa_Appointment_Bot.exe" and follow the prompts on the screen
- Your email and password are only stored temporarily on your computer. This information is destroyed once you close the program.


#### Advanced (read below if you know how to program in Python and want to modify the underlying source code.)

Libraries needed to run the Python code:

To install Selenium on Windows:
```
python -m pip install selenium=4.2.0
```

To install pyautogui on Windows:
```
python -m pip install pyautogui
```

To install pyinstaller on Windows:
```
python -m pip install pyinstaller
```

With these libraries installed, you can then modify the source code and run it as a python file.

#### Generate executable file from the python file

On the command window:

1. Go to the directory where you download this repository.
2. While hovering your mouse in the folder, Right Click -> Open in Terminal
3. This will open a black Windows PowerShell.
4. Paste the following code and press Enter to run: 
```
pyinstaller --onefile US_Visa_Appointment_Bot.py
```
5. After the code has executed, it will create a "build" and "dist" folder in the directory.
6. Go to the "dist" folder.
7. Copy the executable file, and paste it in to the main folder by clicking back.
8. Run the executable file by double clicking on it.

