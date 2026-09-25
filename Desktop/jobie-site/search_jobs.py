from bs4 import BeautifulSoup

def search_jobs():
    with open('jobs.html', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Heading tags se job titles nikalna
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
    job_titles = [h.text.strip() for h in headings if h.text.strip()]

    print("\n==========================================")
    print("     JOBIE PORTAL - DYNAMIC SEARCH ENGINE")
    print("==========================================")

    while True:
        query = input("\nEnter job title to search (or type 'exit' to quit): ").strip().lower()
        
        if query == 'exit':
            print("Exiting search script. Goodbye!")
            break
        
        if not query:
            print("⚠️ Please enter a valid search query.")
            continue

        # Matching results filter karna
        results = [job for job in job_titles if query in job.lower()]

        print(f"\n🔍 Searching for: '{query}'...")
        if results:
            print(f"✅ Found {len(results)} matching job(s):")
            for idx, job in enumerate(results, 1):
                print(f"  {idx}. {job}")
        else:
            print("❌ No matching jobs found.")

if __name__ == "__main__":
    search_jobs()
