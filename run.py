import os
from yaksok.yaksok import run_code


def run_files(files, entrypoint):
    if not os.path.exists('./codes'):
        os.mkdir('./codes')

    os.chdir('./codes')

    for file_name in files:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(files[file_name])

    run_code(files[entrypoint], entrypoint)

    for file_name in files:
        os.remove(file_name)

    os.chdir('..')


if __name__ == '__main__':
    print("Testing yaksok...")
    run_files(
        {
            "시계.yak": """
번역(python) seconds"초 기다리기"
***
    import time

    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= seconds:
            break
***
""",
            'main.yak': """
"안녕!" 보여주기
@시계 3초 기다리기
"뜨거운 안녕!" 보여주기
""",

        }, 'main.yak')
