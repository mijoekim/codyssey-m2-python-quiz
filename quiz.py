"""개별 퀴즈 1개를 표현하는 Quiz 클래스."""


class Quiz:
    """문제 하나를 나타내는 클래스.

    속성:
        question (str): 문제 내용
        choices (list): 선택지 4개가 담긴 리스트
        answer (int): 정답 번호 (1~4)
        hint (str): 힌트 (보너스 기능용, 없으면 빈 문자열)
    """

    def __init__(self, question, choices, answer, hint=''):
        self.question = question      # 문제
        self.choices = choices        # 선택지 리스트 (4개)
        self.answer = answer          # 정답 번호 (1~4)
        self.hint = hint              # 힌트 (선택)

    def show(self):
        """문제와 선택지를 화면에 출력한다."""
        print(self.question)
        # enumerate로 1번부터 번호를 붙여 선택지 출력
        for index, choice in enumerate(self.choices, start=1):
            print(f'{index}. {choice}')

    def is_correct(self, user_answer):
        """사용자가 입력한 번호가 정답인지 True/False로 반환한다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리로 변환한다."""
        return {
            'question': self.question,
            'choices': self.choices,
            'answer': self.answer,
            'hint': self.hint,
        }

    @staticmethod
    def from_dict(data):
        """딕셔너리를 Quiz 객체로 변환한다. (파일에서 불러올 때 사용)"""
        return Quiz(
            question=data['question'],
            choices=data['choices'],
            answer=data['answer'],
            hint=data.get('hint', ''),  # 힌트가 없는 옛 데이터도 안전하게 처리
        )