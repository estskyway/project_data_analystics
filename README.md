## 📃 Project : LDA 토픽 모델링을 활용한 앱 리뷰 분석

### 1. 개요
본 프로젝트에서는 건강 및 운동 관리를 위한 앱을 대상으로 고객 리뷰 텍스트를 분석하여 고객의 불편한 점을 파악하고, 이를 기반으로 개선된 운동 시설 검색 웹사이트를 제안합니다. 구글 플레이 스토어의 총 9개의 앱에서 약 2800 건의 리뷰를 수집했으며, LDA 토픽 모델링을 통해 고객의 다양한 요구 사항을 심층적으로 분석했습니다.

### 2. Dataset
- 구글 플레이 스토에 내 건강 및 운동 관리를 위한 앱 9개에서 리뷰 약 2800건 수집
- 데이터 수집 방법 : Data scraping
- 전처리 목적 데이터셋
  | 불용어 리스트 | 단어 치환 리스트 | 1글자 키워드 리스트 |
  |----|------|------|
  |[Stop_word]([https://github.com/estskyway/project_data_analystics/blob/main/datasets/stopword_concat.xlsx])| [Replace_word]([파일경로](https://github.com/estskyway/project_data_analystics/blob/main/datasets/replace_concat.xlsx))|[One_Word]([파일경로](https://github.com/estskyway/project_data_analystics/blob/main/datasets/oneword_concat.xlsx))|

### 😄 긍정적 리뷰 분석
1) 첫번째
2) 두번째
3) 세번째
<br>

### 😞 부정적 리뷰 분석 (num_words=7)
1) 
- '0.039*"사이트" + 0.024*"늘다" + 0.021*"개선" + 0.020*"오류" + 0.016*"시설" + 0.013*"불편" + 0.012*"접속"'
- 위의 단어들로 보아 "사이트 접속 오류와 시설 불편이 늘어 개선이 필요하다" 고 추측해볼수 있다. 

2) 
- '0.047*"늘다" + 0.025*"개선" + 0.016*"운동" + 0.016*"로그인" + 0.016*"사이트" + 0.015*"회원" + 0.015*"않다"'
- 위 단어들로 보아 "사이트의 로그인이 제대로 작동하지 않는 문제로 운동하는 회원들의 불편이 늘어 개선이 필요하다" 고 추측해볼수 있다.

3) 세번째 
