## API Endpoints Used

This document outlines the GitHub REST API endpoints used in the assignment. The endpoints were selected to simulate common use cases for marketing or product analytics teams:

## 1. Search Repositories
**Endpoint**: `GET /search/repositories`  
**Purpose**: To find public repositories relevant to marketing and analytics.

## 2. List Commits
**Endpoint**: `GET /repos/{owner}/{repo}/commits`  
**Purpose**: To review commit activity in a selected repository.

## 3. Get Repository Contents
**Endpoint**: `GET /repos/{owner}/{repo}/contents/{path}`  
**Purpose**: To access key files like README or config files in a repository.

All endpoints were chosen based on a simulated use case where a client may want to evaluate a marketing analytics tool hosted on GitHub.

**Reference**: [GitHub REST API Docs](https://docs.github.com/en/rest)


