import sys
import shutil
from pathlib import Path
from hw_5 import normalize
import os


def creating_sorting_folders(path):

    DIR_IMAGES = path / 'images'
    DIR_DOCUMENTS = path / 'documents'
    DIR_AUDIO = path / 'audio'
    DIR_VIDEO = path / 'video'
    DIR_ARCHIVES = path / 'archives'

    DIR_IMAGES.mkdir()
    DIR_DOCUMENTS.mkdir()
    DIR_AUDIO.mkdir()
    DIR_VIDEO.mkdir()
    DIR_ARCHIVES.mkdir()

    return (DIR_IMAGES, DIR_DOCUMENTS, DIR_AUDIO, DIR_VIDEO, DIR_ARCHIVES)


def normalization_stem(path):

    rename_stem = normalize(path.stem)
    return rename_stem


def sorting_files(path, sorting_folders):

    DIR_IMAGES, DIR_DOCUMENTS, DIR_AUDIO, DIR_VIDEO, DIR_ARCHIVES = sorting_folders
    rename_stem = normalization_stem(path)

    if path.suffix in ('.jpeg', '.png', '.jpg', '.svg'):

        new_path = DIR_IMAGES / (rename_stem + path.suffix)
        path.replace(new_path)

    elif path.suffix in ('.avi', '.mp4', '.mov', '.mkv'):

        new_path = DIR_VIDEO / (rename_stem + path.suffix)
        path.replace(new_path)

    elif path.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):

        new_path = DIR_DOCUMENTS / (rename_stem + path.suffix)
        path.replace(new_path)

    elif path.suffix in ('.mp3', '.ogg', '.wav', '.amr'):

        new_path = DIR_AUDIO / (rename_stem + path.suffix)
        path.replace(new_path)

    elif path.suffix in ('.zip', '.gz', '.tar'):

        new_path = DIR_ARCHIVES / rename_stem
        shutil.unpack_archive(path, new_path)


def folder_processing(path, sorting_folders):

    if path.is_dir() and path not in sorting_folders:

        for i in path.iterdir():
            folder_processing(i, sorting_folders)
        if not os.listdir(path):
            path.rmdir()

    else:
        sorting_files(path, sorting_folders)


def main():
    path = sys.argv[1]
    path = Path(path)

    if path.exists():
        sorting_folders = creating_sorting_folders(path)
        folder_processing(path, sorting_folders)


if __name__ == '__main__':
    main()
