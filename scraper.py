import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

emails = set()
companies = []

for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        found = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", href)
        for email in found:
            emails.add(email)

for h in soup.find_all("h2"):
    companies.append(h.text.strip())

with open("companies.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Company", "Email"])

    for i in range(min(len(companies), len(emails))):
        writer.writerow([companies[i], list(emails)[i]])

print("Done! Data saved to companies.csv")
