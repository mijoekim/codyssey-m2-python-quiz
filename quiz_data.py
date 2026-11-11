"""기본 제공 파이썬 상식 퀴즈 데이터."""
import json

QUIZ_FILE = 'quiz_data.json'   # 퀴즈를 저장할 파일

from quiz import Quiz
# def quiz_to_dict(quiz):
#     """Quiz 객체를 저장 가능한 딕셔너리로 변환한다."""
#     return {
#         'question': quiz.question,
#         'choices': quiz.choices,
#         'answer': quiz.answer,
#     }


# def dict_to_quiz(data):
#     """딕셔너리를 Quiz 객체로 복원한다."""
#     return Quiz(data['question'], data['choices'], data['answer'])

def save_quizzes(quizzes):
    """퀴즈 리스트를 JSON 파일로 저장한다."""
    data = [q.to_dict() for q in quizzes]   # Quiz의 to_dict 사용 (hint 포함!)
    with open(QUIZ_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_quizzes():
    """JSON 파일에서 퀴즈를 불러온다."""
    try:
        with open(QUIZ_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Quiz.from_dict(d) for d in data]   # Quiz의 from_dict 사용
    except FileNotFoundError:
        quizzes = get_default_quizzes()
        save_quizzes(quizzes)
        return quizzes



def get_default_quizzes():
    """프로그램 시작 시 기본으로 제공되는 Quiz 객체 리스트를 반환한다."""
    return [
        Quiz(
            question='파이썬을 만든 사람은 누구일까요?',
            choices=['귀도 반 로섬', '제임스 고슬링', '리누스 토르발스', '비야네 스트롭스트룹'],
            answer=1,
            hint='네덜란드 출신 프로그래머입니다.',
        ),
        Quiz(
            question='파이썬에서 리스트를 만들 때 사용하는 괄호는?',
            choices=['( )', '{ }', '[ ]', '< >'],
            answer=3,
            hint='대괄호입니다.',
        ),
        Quiz(
            question='파이썬에서 주석을 작성할 때 사용하는 기호는?',
            choices=['//', '#', '--', '/* */'],
            answer=2,
            hint='샵(우물 정) 기호입니다.',
        ),
        Quiz(
            question='다음 중 파이썬의 자료형이 아닌 것은?',
            choices=['int', 'float', 'char', 'str'],
            answer=3,
            hint='파이썬에는 문자 하나만을 위한 전용 타입이 없습니다.',
        ),
        Quiz(
            question='파이썬에서 True와 False를 나타내는 자료형의 이름은?',
            choices=['boolean', 'bit', 'bool', 'binary'],
            answer=3,
            hint='4글자로 줄여서 부릅니다.',
        ),
    ]

def show_quiz_list(quizzes):
    """등록된 퀴즈들의 '질문'만 목록으로 보여준다."""
    print()
    print('===== 📋 퀴즈 목록 =====')
    for number, quiz in enumerate(quizzes, start=1):
        print(f'{number}. {quiz.question}')
    print(f'총 {len(quizzes)}개의 퀴즈가 있습니다.')
    print('========================')

def add_quiz(quizzes):
    """사용자 입력을 받아 새 퀴즈를 quizzes에 추가한다."""
    print()
    print('===== ➕ 퀴즈 추가 =====')

    question = input('질문을 입력하세요: ').strip()
    if not question:
        print('⚠️ 질문이 비어 있어 취소합니다.')
        return

    # 보기 4개 입력받기
    options = []
    for i in range(1, 5):
        option = input(f'보기 {i}: ').strip()
        options.append(option)

    # 정답 번호 입력받기
    answer_input = input('정답 번호(1~4): ').strip()
    if answer_input not in ['1', '2', '3', '4']:
        print('⚠️ 정답 번호가 올바르지 않아 취소합니다.')
        return

    answer = int(answer_input)

    # 새 Quiz 객체 생성 후 추가
    new_quiz = Quiz(question, options, answer)
    quizzes.append(new_quiz)
    save_quizzes(quizzes)        # ← 추가 직후 바로 저장!
    print('✅ 퀴즈가 추가되었습니다!')

