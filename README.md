# Github-Folder-Downloader
This python script will allow you to download a specific folder from a github repo, without downloading the entire repo.

## How to use
Extract the contents of the release to where you would like to keep the script, and open up a terminal in that directory. Run this command in the termal to install the required packages.  
```sh
python -m pip install -r ./requirements.txt
```

There are two required args. The repo and the folder.  

The repo will be `username/reponame` ex: `nordgaren/Github-Folder-Downloader` and the folder will be the path from the root directory of that repo, 
ex: `.idea/inspectionProfiles` with no slash on the end. The folder structure of the repo will be recreated, but only the files in the folder specify will be downloaded.  

## Usage: 
### gitdl.py [-h] [-o] [-r] [-f] repo path
```
positional arguments:
  repo               The repo where the file or folder is stored
  path               The folder or file you want to download

options:
  -h, --help         show this help message and exit
  -o OUT, --out OUT  path to folder you want to download to.
  -r, --recursive    Recursively download directories. Folder downloads, only!
  -f, --file         set flag to download a single file, instead of a folder.
```

Folder - path must not end with a slash.
```sh
python gitdl.py nordgaren/Github-Folder-Downloader .idea/inspectionProfiles
```  
Single File
```sh
python gitdl.py nordgaren/Github-Folder-Downloader -f .idea/.gitignore
```

The other two optional arguments are:  
`-o` or `--output` which lets you specify an output path (the defualt is `./downloads/`)  
`-r` or `--recursive` which tells the script to recursively download all subfolders, as well.  
