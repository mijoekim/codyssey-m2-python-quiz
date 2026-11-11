# 🧠 파이썬 상식 퀴즈 (CLI)

## 1. 프로젝트 개요

파이썬 상식 문제를 풀고 점수를 기록하는 커맨드라인(CLI) 퀴즈 프로그램입니다.
사용자는 퀴즈를 풀고, 직접 문제를 추가·삭제하며, 자신의 점수 기록을
날짜별로 확인할 수 있습니다. 퀴즈와 점수는 JSON 파일에 영구 저장되어
프로그램을 다시 실행해도 데이터가 유지됩니다.

## 2. 퀴즈 주제 선정 이유

파이썬을 처음 배우는 사람이 **핵심 상식을 재미있게 복습**할 수 있도록
파이썬 기초 상식을 주제로 선정했습니다. 단순히 읽는 공부보다
직접 문제를 풀어보면 기억에 더 오래 남고, 힌트·점수 기능을 통해
학습 동기를 높일 수 있다고 생각했습니다.

## 3. 개발 환경

| 항목 | 사용 환경 |
|---|---|
| 프로그래밍 언어 | Python 3.10 이상 |
| 개발 도구 | Visual Studio Code |
| 운영 환경 | Windows / PowerShell |
| 버전 관리 | Git |
| 원격 저장소 | GitHub |
| 데이터 저장 | JSON |
| 라이브러리 | Python 표준 라이브러리 |

## 4. 실행 방법

### 4-1. 저장소 복제

```bash
git clone https://github.com/mijoekim/codyssey-m2-python-quiz.git
```

### 4-2. 프로젝트 폴더 이동

```bash
cd codyssey-m2-python-quiz
```

### 4-3. 프로그램 

```bash
py main.py
```
실행 후 메뉴 번호를 입력해 원하는 기능을 선택합니다.

## 5. 기능 목록

### 5-1. 기본 기능
- 퀴즈 풀기 및 자동 채점
- 새로운 퀴즈 추가
- 등록된 퀴즈 목록 조회
- 퀴즈 삭제
- 점수 기록 저장 및 조회
- 프로그램 종료

### 5-2. 보너스 기능
- 🎲 **랜덤 출제**: 매번 다른 순서로 문제 출제
- 🔢 **문제 수 선택**: 풀고 싶은 문제 개수를 직접 선택
- 💡 **힌트 기능**: 힌트를 보면 점수가 일부 차감
- 🗑️ **퀴즈 삭제**: 번호를 골라 퀴즈 삭제 (파일에 반영)
- 📊 **점수 히스토리**: 날짜/시간·문제 수·점수를 영구 저장

## 6. 파일 구조


```
.
├── main.py          # 프로그램 실행 및 메뉴 관리
├── quiz.py          # Quiz 클래스 정의 (to_dict/from_dict 지원)
├── quiz_data.py     # 기본 퀴즈 데이터, 추가/삭제/목록, JSON 저장·불러오기
├── game.py          # 퀴즈 풀이 및 채점 로직 (랜덤·힌트 포함)
├── score.py         # 점수 기록 저장/불러오기
├── quiz_data.json   # 저장된 퀴즈 데이터
├── scores.json      # 저장된 점수 기록
├── docs/            # 스크린샷 등 문서 자료
└── README.md
```

## 6. 데이터 파일 설명

프로그램은 두 개의 JSON 파일에 데이터를 영구 저장합니다.

### `quiz_data.json` — 퀴즈 데이터
등록된 모든 퀴즈 문제를 저장합니다. 퀴즈를 추가·삭제하면
이 파일에 자동으로 반영됩니다.

```json
[
  {
    "question": "파이썬을 만든 사람은 누구일까요?",
    "choices": [
      "귀도 반 로섬",
      "제임스 고슬링",
      "리누스 토르발스",
      "비야네 스트롭스트룹"
    ],
    "answer": 1,
    "hint": "네덜란드 출신 프로그래머입니다."
  },
  {
    "question": "파이썬에서 리스트를 만들 때 사용하는 괄호는?",
    "choices": [
      "( )",
      "{ }",
      "[ ]",
      "< >"
    ],
    "answer": 3,
    "hint": "대괄호입니다."
  },
  {
    "question": "다음 중 파이썬의 자료형이 아닌 것은?",
    "choices": [
      "int",
      "float",
      "char",
      "str"
    ],
    "answer": 3,
    "hint": "파이썬에는 문자 하나만을 위한 전용 타입이 없습니다."
  },
  {
    "question": "파이썬에서 True와 False를 나타내는 자료형의 이름은?",
    "choices": [
      "boolean",
      "bit",
      "bool",
      "binary"
    ],
    "answer": 3,
    "hint": "4글자로 줄여서 부릅니다."
  }
]
```


### `scores.json` — 점수 기록
퀴즈를 풀 때마다 날짜/시간, 푼 문제 수, 획득 점수가 저장되어
히스토리로 조회할 수 있습니다.

```json
[
  {
    "score": 5,
    "total": 5,
    "date": "2026-11-11 14:04"
  },
  {
    "score": 2,
    "total": 2,
    "date": "2026-11-11 16:42"
  },
  {
    "score": 5,
    "total": 5,
    "date": "2026-11-11 16:43"
  },
  {
    "score": 1.0,
    "total": 2,
    "date": "2026-11-11 17:01"
  }
]
```


## 👤 만든 사람

mijoekim


## 7. Git 및 GitHub 버전 관리

Git과 GitHub를 활용하여 프로젝트 소스 코드를 관리했습니다.

- Git 저장소 초기화 및 원격 저장소 연결
- 기능별 커밋을 통한 변경 이력 관리
- 기능 개발 브랜치 생성
- 브랜치 작업 후 기본 브랜치에 병합
- GitHub 원격 저장소에 프로젝트 업로드
- `git clone`을 이용한 저장소 복제
- `git pull`을 이용한 원격 저장소 변경사항 가져오기

### 7-1. 커밋 메시지 작성 규칙

커밋 메시지는 변경 목적을 쉽게 파악할 수 있도록 다음 형식을 사용합니다.

```text
type: 변경 내용 요약
```

주요 접두사는 다음과 같습니다.

| 접두사 | 사용 목적 | 예시 |
|---|---|---|
| feat | 새로운 기능 추가 | feat: 퀴즈 플레이 기능 추가 |
| fix | 오류 수정 | fix: 메뉴 입력 오류 수정 |
| docs | 문서 수정 | docs: README 설명 보완 |
| refactor | 코드 구조 개선 | refactor: 퀴즈 데이터 처리 개선 |
| test | 테스트 추가 및 수정 | test: 퀴즈 입력 검증 테스트 |
| chore | 설정 및 기타 작업 | chore: gitignore 설정 추가 |

커밋 메시지는 한 커밋에서 변경한 핵심 내용을 간결하게 작성합니다.

### 7-2. 커밋 기록 확인

다음 명령어로 커밋 기록을 확인할 수 있습니다.

```bash
git log --oneline
```
![alt text](docs/screenshots/git-log-oneline.png)

전체 커밋 수를 확인하려면 다음 명령어를 사용합니다.

```bash
git rev-list --count HEAD
```
![alt text](docs/screenshots/git-rev-list.png)




### 7-3. 브랜치 및 병합 기록 확인

브랜치 목록 확인:

```bash
git branch -a
```
![alt text](docs/screenshots/git-rev-list.png)


브랜치 병합을 포함한 전체 커밋 그래프 확인:

```bash
git log --oneline --graph --decorate --all
```
![alt text](docs/screenshots/git-log--graph--all.png)


실제 브랜치 생성과 병합을 통해 기능 개발 이력을 관리했습니다.



### 7-4. GitHub 저장소

GitHub 저장소:

https://github.com/mijoekim/codyssey-m2-python-quiz
