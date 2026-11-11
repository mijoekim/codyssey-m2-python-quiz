"""퀴즈 풀기(진행 + 채점) 기능."""
import random   # ← 맨 위에 추가

def ask_one_quiz(quiz):
    """퀴즈 1개를 출제하고, 이 문제에서 획득한 점수를 반환한다.

    반환값(float): 정답+힌트X=1.0, 정답+힌트O=0.5, 오답=0.0
    """
    quiz.show()  # 문제와 선택지 출력

    used_hint = False   # 힌트 사용 여부 기록

    while True:
        user_input = input("정답 번호 입력 (1-4), 힌트는 'h': ").strip().lower()

        # 힌트 요청 처리
        if user_input == 'h':
            if used_hint:
                print('💡 이미 힌트를 사용했습니다.')
            elif quiz.hint:
                print(f'💡 힌트: {quiz.hint} (점수 0.5 차감)')
                used_hint = True
            else:
                print('⚠️ 이 문제에는 힌트가 없습니다.')
            continue   # 힌트만 보고 다시 입력받기

        if not user_input.isdigit():
            print("⚠️ 숫자 또는 'h'를 입력하세요.")
            continue

        user_answer = int(user_input)

        if user_answer < 1 or user_answer > 4:
            print('⚠️ 1-4 사이의 숫자를 입력하세요.')
            continue

        break

    # 채점 + 점수 계산
    if quiz.is_correct(user_answer):
        if used_hint:
            print('✅ 정답입니다! (힌트 사용으로 0.5점)')
            return 0.5
        else:
            print('✅ 정답입니다!')
            return 1.0
    else:
        print(f'❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.')
        return 0.0

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
    print("💡 힌트를 보려면 'h'를 입력하세요. (0.5점 차감)")

    for number, quiz in enumerate(quiz_list, start=1):
        print()
        print(f'--- {number}번 문제 ---')
        score += ask_one_quiz(quiz)   # ← 반환된 점수(0/0.5/1)를 누적
    # for number, quiz in enumerate(quiz_list, start=1):
    #     print()
    #     print(f'--- {number}번 문제 ---')
    #     if ask_one_quiz(quiz):
    #         score += 1

    print()
    print('========================================')
    print(f'🎯 결과: 총 {total}문제 중 {score}점 획득!')
    print('========================================')

    return score, total   # ← 점수와 푼 문제 수 반환