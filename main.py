"""파이썬 상식 퀴즈 게임 - 메인 진입점"""
# from quiz_data import get_default_quizzes, add_quiz, show_quiz_list   # 추가
from quiz_data import load_quizzes, add_quiz, show_quiz_list
from game import play_quiz             # 추가

from score import add_record, show_records, save_records, load_records
def show_menu():
    """메뉴를 화면에 출력한다."""
    print()
    print('========================================')
    print('        🐍 파이썬 상식 퀴즈 게임 🐍')
    print('========================================')
    print('1. 퀴즈 풀기')
    print('2. 퀴즈 추가')
    print('3. 퀴즈 목록')
    print('4. 점수 확인')
    print('5. 종료')
    print('========================================')


def get_menu_choice():
    """메뉴 번호를 입력받아 1~5 사이 정수로 반환한다.

    잘못된 입력이면 안내 후 다시 입력받는다(재입력 흐름).
    """
    while True:
        # 입력 앞뒤 공백 제거
        user_input = input('선택: ').strip()

        # 빈 입력 처리
        if user_input == '':
            print('⚠️ 입력이 비어 있습니다. 1-5 사이의 숫자를 입력하세요.')
            continue

        # 숫자 변환 실패 처리 (예: abc)
        if not user_input.isdigit():
            print('⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.')
            continue

        choice = int(user_input)

        # 허용 범위 밖 숫자 처리 (예: 9)
        if choice < 1 or choice > 5:
            print('⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.')
            continue

        return choice


def main():
    """프로그램의 메인 반복 루프."""
    quizzes = load_quizzes()     # 기본 퀴즈 불러오기
    records = load_records()            # 시작할 때 파일에서 불러오기

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            score = play_quiz(quizzes)            # 점수 받아오기
            add_record(records, score, len(quizzes))  
            save_records(records)      # 기록 추가 후 바로 저장!
        elif choice == 2:
            add_quiz(quizzes)            # 퀴즈 추가
        elif choice == 3:
            show_quiz_list(quizzes)      # 퀴즈 목록
        elif choice == 4:
            show_records(records)                 # 기록 조회!
        elif choice == 5:
            print('👋 게임을 종료합니다. 안녕히 가세요!')
            break

if __name__ == '__main__':
    main()