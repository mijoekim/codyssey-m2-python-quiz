"""점수 기록 관리 기능."""

import json
from datetime import datetime

SCORE_FILE = 'scores.json'   # 점수를 저장할 파일 이름

def add_record(records, score, total):
    """새 점수 기록을 records 리스트에 추가한다.

    매개변수:
        records (list): 점수 기록들을 담는 리스트
        score (int): 맞힌 개수
        total (int): 전체 문제 수
    """
    record = {
        'score': score,
        'total': total,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
    }
    records.append(record)


def show_records(records):
    """지금까지의 점수 기록을 보기 좋게 출력한다."""
    if not records:
        print('📭 아직 기록된 점수가 없습니다. 먼저 퀴즈를 풀어보세요!')
        return

    print()
    print('===== 📊 점수 기록 =====')
    for number, record in enumerate(records, start=1):
        score = record['score']
        total = record['total']
        date = record['date']
        print(f'{number}. {date} | {score} / {total}점')
    print('========================')

def save_records(records):
    """점수 기록 리스트를 JSON 파일로 저장한다."""
    with open(SCORE_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def load_records():
    """JSON 파일에서 점수 기록을 불러온다.

    파일이 없으면 빈 리스트를 반환한다.
    """
    try:
        with open(SCORE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # 처음 실행이라 파일이 아직 없는 경우
        return []