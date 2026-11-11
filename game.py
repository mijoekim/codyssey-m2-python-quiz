"""퀴즈 풀기(진행 + 채점) 기능."""
import random   # ← 맨 위에 추가

def ask_one_quiz(quiz):
    """퀴즈 1개를 출제하고 사용자의 답을 입력받아 정답 여부를 반환한다.

    반환값: True(정답) 또는 False(오답)
    """
    quiz.show()  # 문제와 선택지 출력

    # 1~4 사이 올바른 번호가 들어올 때까지 반복
    while True:
        user_input = input('정답 번호를 입력하세요 (1-4): ').strip()

        if not user_input.isdigit():
            print('⚠️ 숫자만 입력하세요.')
            continue

        user_answer = int(user_input)

        if user_answer < 1 or user_answer > 4:
            print('⚠️ 1-4 사이의 숫자를 입력하세요.')
            continue

        # 올바른 입력이면 반복 종료
        break

    # Quiz 클래스의 is_correct 메서드로 채점
    if quiz.is_correct(user_answer):
        print('✅ 정답입니다!')
        return True
    else:
        print(f'❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.')
        return False


def play_quiz(quizzes):
    """전체 퀴즈를 진행하고 (맞힌 개수, 푼 문제 수)를 반환한다."""
    if not quizzes:
        print('⚠️ 풀 수 있는 퀴즈가 없습니다.')
        return 0, 0   # ← 점수, 푼 문제 수 둘 다 반환

    # 5.1 랜덤 출제: 원본 보호를 위해 복사 후 섞기
    quiz_list = quizzes.copy()
    random.shuffle(quiz_list)

    # 5.2 문제 수 선택
    max_count = len(quiz_list)
    print()
    print(f'총 {max_count}개의 문제가 있습니다.')
    count_input = input(f'몇 문제를 푸시겠습니까? (1~{max_count}): ').strip()

    if count_input.isdigit() and 1 <= int(count_input) <= max_count:
        count = int(count_input)
    else:
        print('⚠️ 올바른 숫자가 아니므로 전체 문제를 출제합니다.')
        count = max_count

    quiz_list = quiz_list[:count]   # 앞에서 count개만 선택

    score = 0
    total = len(quiz_list)

    print()
    print(f'총 {total}문제를 풉니다. 시작합니다!')

    for number, quiz in enumerate(quiz_list, start=1):
        print()
        print(f'--- {number}번 문제 ---')
        if ask_one_quiz(quiz):
            score += 1

    print()
    print('========================================')
    print(f'🎯 결과: 총 {total}문제 중 {score}개 정답!')
    print('========================================')

    return score, total   # ← 점수와 푼 문제 수 반환