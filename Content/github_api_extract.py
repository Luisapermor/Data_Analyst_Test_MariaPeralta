import requests
import time
impor json

# Authentication headers
HEADERS = {"Authorization": "Bearer <your_token_here>",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"}

def search_repositories(query, max_pages, per_page=10): #This search includes pagination to select te desired amount of pages
    all_results = []
    for page in range(1, max_pages + 1):
        url = "https://api.github.com/search/repositories"
        params = {"q": query,
            "per_page": per_page,
            "page": page}
        response = requests.get(url, headers=HEADERS, params=params)
        data = response.json()
        items = data.get("items", [])
        all_results.extend(items)
        
        if len(items) < per_page:  # Break early if there are no more results
            break
            time.sleep(1)  # avoid rate limit if looping many times
        return all_results

def list_commits(owner, repo, per_page=5):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    return requests.get(url, headers=HEADERS, params={"per_page": per_page}).json()

def get_contents(owner, repo, path="README.md"):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    return requests.get(url, headers=HEADERS).json()

def check_rate_limit():
    url = "https://api.github.com/rate_limit"
    data = requests.get(url, headers=HEADERS).json()
    rate = data.get('rate', {})
    print("Remaining requests:", rate.get('remaining'))
    print("Reset time (UTC):", time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(rate.get('reset'))))
