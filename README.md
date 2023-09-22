# DISCLAIMER:
This is for tutorial purposes only. I do not condone/encourage unethical web scrapping.
### Please scrape ethically

# Intro:
This project demos various webscrapping methods. Meant to help those interested in the topic easily follow along. 

# File Descriptions
- **app**:  Shows basic Selenium functionality.
- **auto**:  Demos more advance Selenium functionality.
- **indeed**:  A real world example that shows Selenium and Beautifulsoup working together. Selenium for interaction BeautifulSoup for static HTML parsing.
- **soup**:  Shows basic BeautifulSoup functionality. Prints out a list of mock job descriptions and relative links.

# Setup:
Everybody's environemnt is different. This was programmed in a **WSL environment** using **Google Chromes** [chromedriver](https://chromedriver.chromium.org/downloads). You will need a web browser's driver!

1. [How to install Selenium in WSL](https://stackoverflow.com/questions/63290844/how-to-run-selenium-chromedriver-from-python3-on-wsl2?newreg=d040c37cdde449899783cddf34b00e32).
    - Resource for [troubleshooting](https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/)
    ## Major Key Alert:
    - Make sure that in your .bashrc file you have `export DISPLAY=<your WSL ip address>:0.0` at the end of the file. **Dont want to use WSL?** Change WSL address to Windows address if you wish to not use Vcxsrv.
    - This has worked for me as well too, replacing the code above: `export DISPLAY=$(grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}'):0`.

2. When you run `echo $DISPLAY` in your WSL terminal it should give you your WSL ip address or your devices ip address.
3. In wsl terminal run `sudo apt-get install x11-apps`.
4. Run `xclock` in wsl to test if the Xserver is connected.
    - Make sure you have Vcxsrv running before you run this test.
5. If xclock pops up then your good to go! Vcxsrv is working properly and you can start running Selenium.

If still confused/troubleshooting watch this helpful video [here](https://www.youtube.com/watch?v=4SZXbl9KVsw&t=166s)!

# Note:
In order to see the web scrapper actually perform the programmed tasks, you need to install [Vcxsrv](https://sourceforge.net/projects/vcxsrv/).

After installation, when you run the app, you'll get to a window that says **"Extra Settings"**. Make sure **"Disable access control"** is **checked**!
