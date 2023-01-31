import os
from github import Github, Repository, ContentFile
import requests
from argparse import ArgumentParser, Namespace


def download(c: ContentFile, out: str):
    r = requests.get(c.download_url)
    output_path = f'{out}/{c.path}'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        print(f'downloading {output_path}')
        f.write(r.content)


def download_folder(repo: Repository, folder: str, out: str, recursive: bool):
    contents = repo.get_contents(folder)
    for c in contents:
        if c.download_url is None:
            if recursive:
                download_folder(repo, c.path, out, recursive)
            continue
        download(c, out)


def download_file(repo: Repository, folder: str, out: str):
    c = repo.get_contents(folder)
    download(c, out)


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('repo', help='The repo where the file or folder is stored')
    parser.add_argument('path', help='The folder or file you want to download')
    parser.add_argument('-o', '--out', default='downloads', required=False, help='Path to folder you want to downoad '
                                                                                 'to.')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursively download directories. Folder '
                                                                       'downloads, only!')
    parser.add_argument('-f', '--file', action='store_true', help='Set flag to download a single file, instead of a '
                                                                  'folder.')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    g = Github()
    repo = g.get_repo(args.repo)
    if args.file:
        download_file(repo, args.path, args.out)
    else:
        download_folder(repo, args.path, args.out, args.recursive)
