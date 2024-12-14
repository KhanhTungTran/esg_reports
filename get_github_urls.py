import requests

def get_repo_files(owner, repo, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        file_urls = []
        for item in data['tree']:
            if item['type'] == 'blob':
                file_path = item['path']
                if file_path.endswith('.DS_Store') or file_path.endswith('.py'):
                    continue
                raw_url = f'https://raw.githubusercontent.com/{owner}/{repo}/main/{file_path}'
                file_urls.append(raw_url)
        return file_urls
    else:
        print(f"Failed to retrieve files: {response.status_code}")
        return []

if __name__ == "__main__":
    owner = 'KhanhTungTran'
    repo = 'esg_reports'
    token = ''

    file_urls = get_repo_files(owner, repo, token)
    for url in file_urls:
        print(url)
