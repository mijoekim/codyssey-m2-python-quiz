"""퀴즈 풀기(진행 + 채점) 기능."""


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
    """전체 퀴즈를 순서대로 진행하고 최종 점수를 반환한다.

    매개변수:
        quizzes (list): Quiz 객체들의 리스트
    반환값: 맞힌 개수(int)
    """
    if not quizzes:
        print('⚠️ 풀 수 있는 퀴즈가 없습니다.')
        return 0

    score = 0
    total = len(quizzes)

    print()
    print(f'총 {total}문제를 풉니다. 시작합니다!')

    for number, quiz in enumerate(quizzes, start=1):
        print()
        print(f'--- {number}번 문제 ---')
        if ask_one_quiz(quiz):
            score += 1

    # 최종 결과 출력
    print()
    print('========================================')
    print(f'🎯 결과: 총 {total}문제 중 {score}개 정답!')
    print('========================================')

    return score