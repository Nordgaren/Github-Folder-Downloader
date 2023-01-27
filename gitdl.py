import os
from github import Github, Repository
import requests
from argparse import ArgumentParser, Namespace


def download_repo(repo: Repository, folder: str, out: str, recursive: bool):
    contents = repo.get_contents(folder)
    for c in contents:
        if c.download_url is None:
            if recursive:
                download_repo(repo, c.path, out, recursive)
            continue
        r = requests.get(c.download_url)
        output_path = f'{out}/{c.path}'
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as f:
            print(f'downloading {output_path}')
            f.write(r.content)


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('repo')
    parser.add_argument('folder')
    parser.add_argument('-o', '--out', default='downloads', required=False)
    parser.add_argument('-r', '--recursive', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    g = Github()
    repo = g.get_repo(args.repo)
    download_repo(repo, args.folder, args.out, args.recursive)
