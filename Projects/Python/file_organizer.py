import os


def arrange_files(files, ext):
    files_with_ext = [f for f in files if f.endswith(ext)]
    print(f"Files with extension '{ext}': {files_with_ext}")
    for i,file in enumerate(files_with_ext):
        os.rename(file, f"photo-{i+1}{ext}")



if __name__ == "__main__":
    files = os.listdir()
    print(f"Files in the current directory: {files}")
    arrange_files(files, ".jpg")