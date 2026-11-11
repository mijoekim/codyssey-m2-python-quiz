# 🧠 파이썬 상식 퀴즈 (CLI)

파이썬 상식 문제를 풀고 점수를 기록하는 커맨드라인 퀴즈 프로그램입니다.

## ✨ 주요 기능

- 퀴즈 풀기 및 자동 채점
- 새로운 퀴즈 추가
- 등록된 퀴즈 목록 조회
- 점수 기록 저장 및 조회 (JSON 파일에 영구 저장)

## 📁 파일 구성

| 파일 | 설명 |
|------|------|
| `main.py` | 프로그램 실행 및 메뉴 관리 |
| `quiz_model.py` | Quiz 클래스 정의 |
| `quiz_data.py` | 기본 퀴즈 데이터, 추가/목록 기능 |
| `scoring.py` | 퀴즈 풀이 및 채점 로직 |
| `score.py` | 점수 기록 저장/불러오기 |

## 🚀 실행 방법

```bash
python main.py
```
## 🛠 개발 환경
Python 3.x

## 👤 만든 사람
mijoekim

## 📜 개발 기록 (Git History)

### 커밋 히스토리

| # | 커밋 메시지 | 내용 |
|---|------------|------|
| 1 | Init: 프로젝트 초기 설정 | 레포 생성, 기본 구조 |
| 2 | Feat: 메뉴 시스템 구현 | CLI 메뉴 출력/선택 |
| 3 | Feat: Quiz 클래스 정의 | 퀴즈 데이터 모델 |
| 4 | Feat: 채점 로직 구현 | 퀴즈 풀이/채점 |
| 5 | Feat: 점수 기록 조회 | 점수 출력 |
| 6 | Feat: 점수 JSON 저장 | scores.json 영구 저장 |
| 7 | Feat: 퀴즈 추가/목록 기능 | 퀴즈 추가·목록 보기 |
| 8 | Feat: 퀴즈 데이터 JSON 저장 | quiz_data.json 영구 저장 |
| 9 | Docs: README 작성 | 문서화 |



### 브랜치 워크플로

```
main
 │
 ├─ feature/play-quiz   (퀴즈 풀기 기능 개발)
 │       │
 │       └─ 작업 완료 후 main에 병합(merge)
 │
 └─ (이후 main에서 계속 개발)
```

- `main`: 안정 버전 브랜치
- `feature/play-quiz`: 퀴즈 풀기 기능을 별도 브랜치에서 개발 후 병합

### git log 결과

![alt text](docs/screenshots/git-log-oneline.png)
![alt text](docs/screenshots/git-log--graph--all.png)

```
User@4F-92 UCRT64 /c/mijoek/codyssey-m2-python-quiz (main)
$ git log --graph --all
* commit 2c883ae7fd5a12b8488a8e71ae2a90e5c95b1a3f (HEAD -> main, origin/main, origin/HEAD)
| Author: mijoekim <mijoekkim@gmail.com>
| Date:   Wed Nov 11 15:01:36 2026 +0900
|
|     Feat: 퀴즈 데이터 JSON 파일 영구 저장
|
* commit a9796d228af2b3e93efaad70cf16b1f2ecd0546e
| Author: mijoekim <mijoekkim@gmail.com>
| Date:   Wed Nov 11 14:32:18 2026 +0900
|
|     Feat: 퀴즈 추가 및 목록 보기 기능 구현
|
* commit 6c8ba281fc2c3376d92ec8cbcf28c6328e8c8d24
| Author: mijoekim <mijoekkim@gmail.com>
| Date:   Wed Nov 11 14:11:27 2026 +0900
|
|     Feat: 점수 JSON 파일 저장 및 불러오기 구현
|
* commit 10664a6a68ff273c6030b1c50299b39975ac9798
| Author: mijoekim <mijoekkim@gmail.com>
| Date:   Wed Nov 11 13:55:28 2026 +0900
|
|     Feat: 점수 기록 및 확인 기능 구현
|
* commit 9618f52dd8ba1746be31521d2f7ddea8312c8c68 (feature/play-quiz)
| Author: mijoekim <mijoekkim@gmail.com>
| Date:   Wed Nov 11 13:34:22 2026 +0900
|
|     Feat: 퀴즈 풀기 및 채점 기능 구현
|
* commit cb03ca0a339027996754d162cdbf1bb3c32ad1d7
| Author: mijoekim <mijoekkim@gmail.com>
| Date:   Wed Nov 11 13:23:49 2026 +0900
|
|     Feat: 기본 파이썬 상식 퀴즈 5개 데이터 추가
|
* commit 691104884d73a7be916fdc930bfc9efb5f8fe2f4
| Author: mijoekim <mijoekkim@gmail.com>
| Date:   Wed Nov 11 13:15:52 2026 +0900
|
|     Feat: 개별 퀴즈를 표현하는 Quiz 클래스 구현
|
* commit 6279a720f2ec98ed9a0e31ae25d9c55ad0466240
| Author: mijoekim <mijoekkim@gmail.com>
| Date:   Wed Nov 11 13:05:11 2026 +0900
|
|     Feat: 메뉴 출력 및 입력 검증 기능 구현
|
* commit 2c80d0ef11ff57e8dbf98a98db9ab6ea5e65ab04
  Author: mijoekim <mijoekkim@gmail.com>
  Date:   Wed Nov 11 12:52:44 2026 +0900

      Initial commit

```