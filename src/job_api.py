from apify_client import ApifyClient
import os 
from dotenv import load_dotenv
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Fetch LinkedIn jobs based on search query and location
def fetch_linkedin_jobs(search_query, location = "india", rows=60):
    run_input = {
    "title": search_query,
    "location": location,
    "rows": 20,
    "proxy": {
        "useApifyProxy": True,
        "apifyProxyGroups": ["RESIDENTIAL"]
    },
    "urls": [],
    "datePosted": "anyTime",
    "companyIds": [],
    "under10Applicants": False,
    "autoConvertToAiSearch": True,
    "scrapeCompany": False,
    "splitByLocation": False
    }
    run = apify_client.actor("hKByXkMQaC5Qt9UMN").call(run_input=run_input)
    jobs = list(apify_client.dataset(run.default_dataset_id).iterate_items())
    return jobs


# Fetch Naukri jobs based on search query and location
def fetch_naukri_jobs(search_query, location = "india", rows=60):
    run_input = {
        "keyword": search_query,
        "maxJobs": 60,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all",
    }
    run = apify_client.actor("U5tcRMY1heBYd1FYF").call(run_input=run_input)
    jobs = list(apify_client.dataset(run.default_dataset_id).iterate_items())
    return jobs