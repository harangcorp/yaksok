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
    run_files({
        "인스타그램.yak": """
약속 계정"로/으로" 내용 "스토리 올리기"
    "인스타중독자" 보여주기    
""",
        "test.yak": """
@인스타그램 "@rycont"로 "코딩 공부😍" 스토리 올리기
"""
    }, 'test.yak')
