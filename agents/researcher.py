import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
serpapi_key = os.getenv("SERPAPI_API_KEY")

def research_task(plan_steps):
    if not serpapi_key:
        raise Exception("⚠️ SERPAPI_API_KEY not found in .env")

    search_query = plan_steps[0]  # Use the first task step (e.g., "Search for NYC housing form")

    params = {
        "engine": "google",
        "q": search_query,
        "api_key": serpapi_key,
        "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    links = []
    if "organic_results" in results:
        for result in results["organic_results"]:
            links.append({
                "title": result.get("title"),
                "link": result.get("link"),
                "snippet": result.get("snippet")
            })

    return {
        "query": search_query,
        "top_results": links
    }

