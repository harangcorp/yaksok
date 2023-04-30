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


run_files({
    "트위터.yak": """
약속 아이디"로/으로" 내용 "트윗하기"
    "트위터 그만해" 보여주기    
""",
    "test.yak": """
@트위터 "@rycont"로 "안녕하세요" 트윗하기
"""
}, 'test.yak')
