import requests
import zipfile
import os
import sys

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = os.path.join(dest_folder, url.split('/')[-1])

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return filename

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def download_data(output_folder):
    url = url = "https://www.dropbox.com/scl/fi/ina6ybbd2cipjd95ttfe9/RENI_HDR.zip?rlkey=4zrouszs5wx5b3wfmqxoi9hkl&dl=1"  # dl=1 is important for direct download

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("Downloading...")
        zip_path = download_file(url, output_folder)

        print("Unzipping...")
        unzip_file(zip_path, output_folder)

        print("Done!")
    else:
        print("The folder already exists")
