import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
JOBS_FILE = os.path.join(BASE_DIR, 'jobs.html')
OUTPUT_FILE = os.path.join(BASE_DIR, 'jobs_data.json')

def extract_job_details():
    if not os.path.exists(JOBS_FILE):
        print("❌ Error: jobs.html file nahi mili!")
        return

    with open(JOBS_FILE, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    extracted_jobs = []
    
    headings = soup.find_all(['h2', 'h3', 'h4'])
    ignore_list = {"Quick Links", "Contact", "Account", "Find Jobs", "Jobie", "Navigation"}

    for index, h in enumerate(headings):
        title = h.text.strip()
        if title and title not in ignore_list:
            job_card = {
                "id": index + 1,
                "title": title,
                "company": "Tech Solutions Ltd",
                "location": "Remote / On-site",
                "type": "Full-time",
                "apply_url": f"/jobs.html#job-{index + 1}"
            }
            extracted_jobs.append(job_card)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_f:
        json.dump(extracted_jobs, out_f, indent=4)

    print(f"✅ Scraping Complete! Total {len(extracted_jobs)} jobs save ho gayi hain '{OUTPUT_FILE}' me.\n")

if __name__ == '__main__':
    extract_job_details()
