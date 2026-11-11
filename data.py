"""기본 제공 파이썬 상식 퀴즈 데이터."""

from quiz import Quiz


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