# Data Source API Analyst Homework Assignment

## Overview

This repository contains my submission for the Data Source API Analyst homework assignment from Improvado. The objective is to demonstrate my knowledge and ability to interact with REST APIs, extract relevant data, and document the process with a focus on reliability, troubleshooting, and scalability.

---

## Objectives

- Understand customer requirements for accessing public GitHub data.
- Use the GitHub REST API to extract repository, commit, and file content information.
- Handle authentication, pagination, and rate limits efficiently.
- Implement the solution using Google Colab.
- Provide clean and understandable code and documentation.

---

## Repository Structure

- `/Content/`
  - `github_api_extract.py`: Core Python code for authentication, data extraction, and handling edge cases.
  - `api_research.md`: Summary of the endpoints used and logic behind their selection.
  - `error_handling_notes.md`: Notes on handling 401/403 errors, token verification, rate limit management, and retries.

- `github_api_colab_MariaPeralta.ipynb`: Colab notebook with the full implementation, step-by-step.
- `README.md`: This file.

---

## API Endpoints Used

These endpoints were selected to simulate common use cases for marketing or product analytics teams:

1. **Search Repositories**  
   `GET /search/repositories?q=...`  
   Used to discover public repositories related to tools (e.g., marketing analytics, ELT).

2. **List Commits**  
   `GET /repos/{owner}/{repo}/commits`  
   Used to analyze contribution activity, release cycles, or team velocity.

3. **Get Repository Contents**  
   `GET /repos/{owner}/{repo}/contents/{path}`  
   Used to access documentation or configuration files.

Details and logic can be found in `/Content/api_research.md`.

---

## Features of the Implementation

- **Authentication**: Securely handled using personal access tokens and headers.
- **Pagination**: Implemented to fetch complete data from paginated endpoints.
- **Rate Limit Management**: Automatically handles GitHub’s hourly rate limits by reading response headers and pausing requests if necessary.
- **Error Handling**: Handles common issues such as expired/invalid tokens or missing permissions.
- **Reusable Functions**: All requests are modularized into Python functions for clarity and reuse.

---

## Tools Used

- [Google Colab](https://colab.research.google.com/): Main environment for code development and testing.
- GitHub REST API: [Docs](https://docs.github.com/en/rest)
- Python Libraries: `requests`, `json`, `time`, `pandas` 

---

## How to Use

1. Clone this repository.
2. Open `github_api_colab_MariaPeralta.ipynb` in Google Colab.
3. Add your GitHub personal access token in the setup cell.
4. Run each section to test endpoints and review data output.

---

## Troubleshooting Highlights

- **401 Unauthorized**: Ensure your token is active and passed correctly in headers.
- **Rate Limits**: Implemented a pause-and-retry logic if the request limit is reached.
- **Pagination**: Handled using the `Link` header and iterative fetching.

More details are in `/Content/error_handling_notes.md`.

---

## Reflection

This assignment demonstrates real-world API integration skills. Using GitHub’s API provided a good exercise in managing rate limits, authentication, and data pagination. Choosing repositories related to marketing technology (e.g., dbt, Looker, Superset) also simulated a relevant client use case for Improvado’s business model — identifying tool usage trends or repository health.

Google Colab was ideal for this task, offering a reproducible, shareable way to document and test API logic.

---

