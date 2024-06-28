import csv
import re

import requests


class UrlFinder():
    def __init__(self):
        print("Email and Phone Number Scraping ")
        self.urls = []

    def add_url(self):
        content = input('Enter any file Path or url: ')
        with open(content, 'r') as file:
            self.urls = file.read().splitlines()

        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        contact_regex = r'(\+91-|\b0|\b91)?(\d{10})'#r'\+91-[6-9]\d{9}' #
        details = []

        for url in self.urls:
            response = requests.get(url).text
            emails = re.findall(email_regex, response)
            contacts = re.findall(contact_regex, response)
            details.extend([(email, contact[1]) for email in emails for contact in contacts])

        with open('output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Emails', 'Contact Numbers'])
            writer.writerows(details)
        
        print("Details have been scraped and saved in output.csv file.")

    def display_data(self):
        print("Show Scrapped Data ")
        temp = input('If Yes Enter Y / If NO Enter N: ')
        if temp.lower() == 'y':
            with open('output.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)

urlFinder = UrlFinder()
urlFinder.add_url()
urlFinder.display_data()

input('Enter Any Key To Exit:')


