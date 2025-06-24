# Error Handling Notes

## 1. 401 Unauthorized
- This error occurs when the GitHub token is invalid or missing.
- Ensure that the token is active and passed in the headers correctly.
- Headers must include:
  - `Authorization: Bearer <token>`
  - `X-GitHub-Api-Version: 2022-11-28`

## 2. Rate Limiting
- GitHub allows up to 5000 requests/hour for authenticated users.
- We check the `/rate_limit` endpoint to monitor usage.
- If remaining requests are 0, we can pause using `time.sleep()` until the reset time.

## 3. Pagination
- For endpoints like `search/repositories`, multiple pages may be returned.
- We can handle this by incrementing the `page` parameter and appending results.
