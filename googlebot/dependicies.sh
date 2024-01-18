#!/bin/bash

# Update package lists
sudo apt-get update

# Install Python3
sudo apt-get install python3.8 -y

# Install pip3
sudo apt-get install python3-pip -y

# Install Selenium
pip3 install selenium webdriver-manager

# Install Firefox
sudo apt-get install firefox -y

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

# Install ChromeDriver
wget https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

# Install Java
sudo apt install default-jdk

# Install Xvfb
sudo apt install -y unzip xvfb libxi6 libgconf-2-4

#install bs4
pip install requests beautifulsoup4

pip install pandas gspread_dataframe

pip install requests

apt --fix-broken install -y

