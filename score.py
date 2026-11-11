"""점수 기록 관리 기능."""

from datetime import datetime


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