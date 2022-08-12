# 📗 MyAnswerDiary 📗
<h3>내가 쓴 일기를 되돌아보며 나에 대해 알아가는 다이어리 웹사이트</h3>

> 🦁 2022 멋사 해커톤 3조🦁

</br>

|종류|내용|
|------|---|
|프론트|HTML, CSS|
|백|Django|


## 팀원
- 기획/디자인 : 박다비다</br>
- 프론트엔드 : 이소윤, 이지현, 전소정</br>
- 벡엔드 : 김민희, 양성원, 윤수윤</br>


## 주요 기능

### 😶 로그인 전 메인화면
회원가입과 로그인만 가능합니다.
![25 index html](https://user-images.githubusercontent.com/86403488/184388266-faa68c42-3351-493b-bf8e-46c4643ee9a3.png)

### 👩‍👧‍👧 회원가입
아이디, 비밀번호, 닉네임을 입력받습니다.
![20 signup html](https://user-images.githubusercontent.com/86403488/184384232-cb27db69-ba1f-44a4-8b3c-b3b389f8a153.png)

### 🔐 로그인, 로그아웃
![21 signin html](https://user-images.githubusercontent.com/86403488/184384275-b4457b8d-0d0e-4b26-b5b8-fca38da33b90.png)

### 🏡 로그인 후 메인화면
오늘과 같은 월, 일에 썼던 다른 연도의 일기들을 확인할 수 있습니다.</br>
오늘의 일기 작성과 오늘의 365 Q&A 페이지로 이동할 수 있습니다.
![메인페이지 main html](https://user-images.githubusercontent.com/86403488/184384417-b9e06aa7-2e0d-4f1a-9d2e-fb433160475f.png)

### ✏️ 일기 작성 
일기의 제목과 내용과 함께 자신이 느낀 감정을 해시태그로 등록합니다.</br>
현재 날짜가 자동 입력됩니다.</br>
감정 해시태그는 기쁨😄, 분노😠, 우울😢, 즐거움😊으로 이루어져 있습니다.</br>
이 해시태그는 감정 통계 페이지에서 활용됩니다.
![23 diary html](https://user-images.githubusercontent.com/86403488/184384444-fea2a9ab-9122-4a71-a931-317d9f54beb0.png)

### 🔎 일기 키워드 검색 
제목 혹은 본문에 검색 키워드와 일치하는 내용이 있다면 해당 일기의 제목, 본문, 쓴 날짜가 보입니다.</br>
검색페이지에서는 일기 본문을 간략하게 25글자 내로 띄워주었습니다.
자신이 작성한 글만 보입니다.
![19 search html](https://user-images.githubusercontent.com/86403488/184384565-c77129f9-e64d-4cd7-b641-691b73f643f0.png)

### 📗 일기 상세페이지
일기의 제목, 본문(전체 내용), 쓴 날짜가 보입니다.</br>
일기가 쓰여진 월, 일과 같은 날짜에 쓴 다른 연도의 일기들을 모두 확인할 수 있습니다.
![23 diary html (1)](https://user-images.githubusercontent.com/86403488/184386532-512f8d85-6e55-415f-b4fb-a958039b0dec.png)

### 📊 나만의 감정 통계 그래프 확인하기
일기 작성 시 등록한 자신의 감정을 바탕으로 기간별 자신의 감정 통계 그래프를 보여줍니다.</br>
자신의 감정 상태를 한눈에 확인할 수 있습니다.
![22 graph html](https://user-images.githubusercontent.com/86403488/184384595-ccc2d00d-a721-4184-89b2-8b97763b660f.png)

### 🤔 365 Q&A
365일 매일 달라지는 Question에 따른 매년 달라지는 자신의 Answer를 확인할 수 있습니다.</br>
매년 같은 날짜에 같은 질문이 주어져 매년 달라지는 자신의 답변 상태를 통해 자신에 대해 더 깊이 알아갈 수 있습니다.
![24 qna html](https://user-images.githubusercontent.com/86403488/184384629-1a3b5936-cfd2-43d3-adf1-934e2b80abb0.png)


## Manual

1️⃣ Git Clone </br>

```
$ git clone https://github.com/MyAnswerDiary/MyAnswerDiary.git
```

2️⃣ 가상환경 실행하기
```
$ source myvenv/Scripts/activate
```

3️⃣ 프로젝트로 폴더 이동

```
$ cd MyAnswerDiaryPrj/
```
4️⃣ 서버 실행
```
$ python manage.py runserver
```
