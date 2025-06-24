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
  - `error_handling_notes.md`: Notes on handling 401 errors, token verification, rate limit management and pagination.

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
3. Add your GitHub personal access token in the setup cell.
4. Run each section to test endpoints and review data output.

---

## Reflection

This assignment demonstrates real-world API integration skills. Using GitHub’s API provided a good exercise in managing rate limits, authentication, and data pagination. Choosing repositories related to marketing technology (e.g., dbt, Looker, Superset) also simulated a relevant client use case for Improvado’s business model — identifying tool usage trends or repository health.

Google Colab was ideal for this task, offering a reproducible, shareable way to document and test API logic.

---

