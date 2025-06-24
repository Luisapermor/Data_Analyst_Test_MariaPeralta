# Data Source API Analyst Homework 

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
  - `api_research.md`: Summary of the endpoints used and logic behind their selection.
  - `error_handling_notes.md`: Notes on handling 401 errors, token verification, rate limit management and pagination.
  - `github_api_extract.py`: Core Python code for authentication, data extraction, and handling errors.

- `github_api_colab_MariaPeralta.ipynb`: Colab notebook with the full implementation, step-by-step.
- `README.md`: This file.

---

## Tools Used

- [Google Colab](https://colab.research.google.com/): Main environment for code development and testing.
- GitHub REST API: [Docs](https://docs.github.com/en/rest)
- Python Libraries: `requests`, `json`, `time`, `pandas` 

---

## How to Use

1. Clone this repository.
2. Open `github_api_colab_MariaPeralta.ipynb` in Google Colab.
3. Add your GitHub personal access token in the setup cell (Step 1).
4. Run each section to test endpoints and review data output.

---

## Reflection

In this project, I explored the GitHub REST API to search for public repositories related to marketing analytics. Using the /search/repositories endpoint and handling pagination, I retrieved a list of popular repositories, including plausible/analytics with over 22,000 stars, which stood out the most and I selected for the next steps. I analyzed recent commits and README plausible/analytics for the plausible/analytics repo to understand their current development activity and documentation quality. For instance, the latest updates focused on improving team switching and SSO features, showing a collaborative development team. This exercise demonstrated how GitHub’s API can provide valuable insights into project popularity, contributor dynamics, and ongoing feature development.

---

