# import requests
# import json

# url = "https://api.watcha.com/api/evaluations/movies"

# querystring = {"size": "100"}

# payload = ""
# headers = {
#     'accept': "application/vnd.frograms+json;version=20",
#     'accept-encoding': "gzip, deflate, br",
#     'accept-language': "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
#     'cache-control': "no-cache,no-cache",
#     'cookie': "_ga=GA1.2.904402677.1546843109; _gid=GA1.2.261986040.1546843109; fbm_126765124079533=base_domain=.watcha.com; fbsr_126765124079533=3zs1VYcSzvXQerBJoOqnUazbXfxM-GgYscEUdxKwbuc.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUNEdzZDU1dfaHREU1dQUjRQeXVENmhxaUp1RldxdzlNa3FJQ2RIb2RSZHVJVy1vbDNFTS15UTU2and4VGhSWnJ5SDB0UVd1bndMcmZWQTBwTXhsVWlLNkpoT2plV2R5dC1jSzZGc1FDYVBuYTBTVXV2eWNtZDc3RTdWand5MDBvd2NNWlkxNHVZUmhDZUxoVHFjTXh2N2F6WHFUZGM5MlJjdWp3dVhkQ1cyUk9SVUdEVF9oYzBQTU8tN2pPSnpvSkhRZXhlQnVsMlpKYktMTUZ5c3pBVXJXZXRQTUVDeVMzN19nYS1rdWV2Z0FqNW42dFNfc1JYUzRpMmk1Zzk4c3JXcXhyWDEzRVJqNkQ1WXJDcFNKckxVekYycGw4aktvczlmVzFyUVZVbFZMMWNzNGJzR0NjemJNSWFGZWJleldFdUpIN0Q3M1A4R2hDUDQ5a244RFU2am5mX29OdV9vZUY4bkNCTVl1bnhHTlEiLCJpc3N1ZWRfYXQiOjE1NDY4NTEwNzUsInVzZXJfaWQiOiIyMjU1MTM2ODQ0NzA5MDcyIn0; _s_guit=e929464b69bba1746e6bafd230e18780371c8e84dec9d5f10a5d07031a67; Watcha-Web-Client-Language=ko; _guinness_session=TUVBb0thK3VRcnlmdE9EcjVLRGlJM0Y5VVlrSS9DSXJGdVFnUllVVlhjMkRaZmR4dnlNcklVYlRWdm5wTHNVWVh3ODBKeTRhTk9FUmlFWm4rc3ZPcmxpbUVyZkMvZldnN2tOUVhqaGpDdHc9LS1zUmx5bTF3V0JnRWRyVG1iUE9kcVF3PT0%3D--142609434879b24bb723ba3d8a9a695002e9d907",
#     'dnt': "1",
#     'origin': "https://watcha.com",
#     'pragma': "no-cache",
#     'referer': "https://watcha.com/ko-KR/review?type=tutorial&referer_url=/ko-KR",
#     'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.53.4 Safari/537.36",
#     'x-watcha-client': "Watcha-WebApp",
#     'x-watcha-client-language': "ko",
#     'x-watcha-client-region': "KR",
#     'x-watcha-client-version': "1.0.0",
#     'Postman-Token': "e68df438-ccad-406d-bd13-59d27385a981"
# }

# movieCode = open('movieCodeRandom.txt', 'w')

# response = requests.request(
#     "GET", url, data=payload, headers=headers, params=querystring)
# next_uri = 'https://api.watcha.com' + \
#     json.loads(response.content)['result']['next_uri']

# for movie in json.loads(response.content, encoding='utf-8')['result']['result']:
#     data = movie['code'] + '\n'
#     movieCode.write(data)

# print('gogo')

# while True:
#     response = requests.request(
#         "GET", next_uri, data=payload, headers=headers, params=querystring)
#     for movie in json.loads(response.content)['result']['result']:
#         movieCode.write(movie['code'] + "\n")
#     if not json.loads(response.content)['result']['next_uri']:
#         break
#     else:
#         next_uri = 'https://api.watcha.com' + \
#             json.loads(response.content)['result']['next_uri']
#     print(next_uri)

# movieCode.close()
