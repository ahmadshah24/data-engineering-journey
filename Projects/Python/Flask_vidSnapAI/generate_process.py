from text_to_audio import text_to_speech_file
import os
import time
import subprocess



def text_to_audio(folder):
    print("TTA ->", folder)

    file_path = f"user_uploads/{folder}/desc.txt"

    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    print("Text found:")
    print(text)

    # later you can enable this
    # text_to_speech_file(text, folder)


def create_reel(folder):
    
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell=True, check=True)

    print("CR ->", folder)

if __name__ == "__main__":
    while True:
        print("Checking for new folders to process...")

        if not os.path.exists("done.txt"):
            open("done.txt", "w").close()

        with open("done.txt", "r") as f:
            done_folders = [line.strip() for line in f.readlines()]

        folders = os.listdir("user_uploads")

        print("Folders Found:", folders)
        print("Done Folders:", done_folders)

        for folder in folders:
            print("Checking ->", folder)

            if folder not in done_folders:
                print("Processing ->", folder)
                text_to_audio(folder)
                create_reel(folder)

                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
            else:
                print("Skipping ->", folder)

        print("FINISHED CHECKING QUEUE")
        print("Sleeping for 4 seconds...\n")
        time.sleep(4)