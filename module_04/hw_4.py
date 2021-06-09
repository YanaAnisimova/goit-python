import sys
import pathlib


images = []
video_files = []
documents = []
music = []
archives = []
others = []
known_extensions = set()
unknown_extensions = set()


def folder_processing(path):
    if path.exists():
        if path.is_dir():
            for i in path.iterdir():
                folder_processing(i)
        else:
            if path.suffix in ('.jpeg', '.png', '.jpg', '.svg'):
                images.append(path.name)
                known_extensions.add(path.suffix)
            elif path.suffix in ('.avi', '.mp4', '.mov', '.mkv'):
                video_files.append(path.name)
                known_extensions.add(path.suffix)
            elif path.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
                documents.append(path.name)
                known_extensions.add(path.suffix)
            elif path.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
                music.append(path.name)
                known_extensions.add(path.suffix)
            elif path.suffix in ('.zip', '.gz', '.tar'):
                archives.append(path.name)
                known_extensions.add(path.suffix)
            else:
                others.append(path.name)
                unknown_extensions.add(path.suffix)

    return images, video_files, documents, music, archives, others, known_extensions, unknown_extensions


def main():
    path = sys.argv[1]
    path = pathlib.Path(path)
    images, video_files, documents, music, archives, others, known_extensions, unknown_extensions = folder_processing(
        path)
    print(f'Images: {images}\nVideo files: {video_files}\nDocuments: {documents}\nMusic: {music}\nArchives: {archives}\nOthers: {others}\nKnown extensions: {known_extensions}\nUnknown extensions: {unknown_extensions}')


if __name__ == '__main__':
    main()
