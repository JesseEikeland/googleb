import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
import logging

logging.basicConfig(filename='script_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def start_tor_browser():
    options = Options()
    options.add_argument('-headless')
    browser = webdriver.Firefox(options=options)
    return browser

def read_data_from_google_sheet(sheet_url, column_name):
    data = pd.read_csv(sheet_url, sep='\t')
    return data[column_name].dropna().tolist()

def search_google(query, browser):
    try:
        logging.info(f"Navigating to Google and searching for '{query}'...")
        browser.get(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        logging.info("Search performed.")
        return browser
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def find_and_open_link(browser, search_terms):
    try:
        logging.info(f"Looking for link with search terms: {search_terms}...")

        for term in search_terms:
            try:
                link = browser.find_element(By.PARTIAL_LINK_TEXT, term)
                logging.info(f"Link found: {link.get_attribute('href')}")

                logging.info("Clicking the link...")
                link.click()
                logging.info("Link clicked.")

                # Sleep for a random time between 1 to 2 minutes
                sleep_time = random.randint(60, 120)
                logging.info(f"Sleeping for {sleep_time} seconds...")
                time.sleep(sleep_time)

                return
            except NoSuchElementException:
                continue

        logging.info(f"No link found for any of the search terms: {', '.join(search_terms)}.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main_loop():
    sheet_url = 'yougooglelinkhere'

    keywords = read_data_from_google_sheet(sheet_url, 'Key')
    search_terms = read_data_from_google_sheet(sheet_url, 'Link')

    while True:
        try:
            logging.info("Starting Tor Browser...")
            browser = start_tor_browser()
            logging.info("Tor Browser started.")

            query = random.choice(keywords)
            logging.info(f"Selected query: '{query}'")

            browser = search_google(query, browser)

            if browser is not None:
                page_number = 1

                while True:
                    logging.info(f"Checking page {page_number}...")
                    find_and_open_link(browser, search_terms)

                    try:
                        next_page = browser.find_element(By.PARTIAL_LINK_TEXT, "Next")
                        next_page.click()
                    except NoSuchElementException:
                        try:
                            more_results = browser.find_element(By.PARTIAL_LINK_TEXT, "More results")
                            more_results.click()
                        except NoSuchElementException:
                            logging.info("No 'Next' or 'More results' button found. Exiting page check loop.")
                            break

                    page_number += 1
                    time.sleep(5)  # Wait for the page to load

        except Exception as e:
            logging.error(f"An error occurred: {e}")

        finally:
            if browser is not None:
                try:
                    browser.quit()
                    logging.info("Tor Browser closed.")
                except Exception as e:
                    logging.error(f"An error occurred while closing Tor Browser: {e}")

        random_sleep_time = random.randint(15, 30)
        logging.info(f"Sleeping for {random_sleep_time} seconds...")
        time.sleep(random_sleep_time)

if __name__ == "__main__":
    main_loop()


