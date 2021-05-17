import os


def check_dir(dir_name: str) -> str:
    input_video_path = dir_name

    if not os.path.isdir(input_video_path):
        os.mkdir(input_video_path)
        print(f'{dir_name} directory is created and now put a video in the directory')
        return False
    if len(os.listdir(input_video_path)) == 0:
        print(f'{dir_name} directory is empty!')
        return False
    return True
