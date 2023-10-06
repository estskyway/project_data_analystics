## 📃 Project : LDA 토픽 모델링을 활용한 앱 리뷰 분석

### 1. 개요
본 프로젝트에서는 건강 및 운동 관리를 위한 앱을 대상으로 고객 리뷰 텍스트를 분석하여 고객의 불편한 점을 파악하고, 이를 기반으로 개선된 운동 시설 검색 웹사이트를 제안합니다. 구글 플레이 스토어의 총 9개의 앱에서 약 2800 건의 리뷰를 수집했으며, LDA 토픽 모델링을 통해 고객의 다양한 요구 사항을 심층적으로 분석했습니다.
<br>

### 2. Dataset
- 구글 플레이 스토에 내 건강 및 운동 관리를 위한 앱 9개에서 리뷰 약 2800건 수집
- 데이터 수집 방법 : Data scraping
- 전처리 목적 데이터셋
  
  | 불용어 리스트 | 단어 치환 리스트 | 1글자 키워드 리스트 |
  |----|------|------|
  |[Stop_word](https://github.com/estskyway/project_data_analystics/blob/main/datasets/stopword_concat.xlsx)| [Replace_word](https://github.com/estskyway/project_data_analystics/blob/main/datasets/replace_concat.xlsx)|[One_Word](https://github.com/estskyway/project_data_analystics/blob/main/datasets/oneword_concat.xlsx)|
<br>

### 3. LDA 토픽 모델링 수행
- LDA 토픽 모델링? 문서 데이터를 사용자가 지정한 토픽 개수만큼 토픽을 생성하고, 각 토픽별로 어떤 키워드가 어떤 비율로 구성되는지 정보를 제공
- 단계 : 데이터 수집 - 텍스트 전처리 - 토픽 개수 설정 - LDA 모델 학습 - 토픽 추출 - 토픽 시각화
- 토픽 개수 설정 : Coherence Scores (일관성 점수), Perplexity Scores (복잡도 점수) 를 비교하여 긍정적/부정적인 리뷰에서 모두 최적의 토픽수를 2개로 결정했습니다.
- 가장 높은 일관성 점수를 가지고 가장 낮은 복잡도 점수를 가지는 토픽 수를 선택합니다.
  
  ![image](https://github.com/estskyway/project_data_analystics/assets/132973368/fa5d3974-ed5d-402e-9118-57315350d2e1)

  | 긍정적 리뷰 토픽 갯수 | 부정적 리뷰 토픽 갯수 |
  |---|---|
  |![image](https://github.com/estskyway/project_data_analystics/assets/132973368/d8fa0f5f-9950-4e49-8625-562c8dcf7c77)| ![image](https://github.com/estskyway/project_data_analystics/assets/132973368/343b4af8-38bd-4672-bd37-74d8f8bab5dc)|
<br>

### 4. LDA 토픽 모델링 시각화
- 평점이 5점 만점인 리뷰를 분석하여 1-2점은 부정적, 3-5점은 긍정적으로 분류했습니다.
- 긍정적인 및 부정적인 리뷰에 대해 LDA 토픽 모델링을 수행하고 시각화 작업을 진행했습니다.
- 아래 그림은 pyLDAvis를 통해 시각화한 자료입니다.
  
  |❤️긍정적 평점의 리뷰 토픽 모델링 시각화 결과 [(링크)](https://github.com/estskyway/project_data_analystics/datasets/visualization_positive.html)|
  |---|
  | ![긍정리뷰 모델링](https://github.com/estskyway/project_data_analystics/blob/main/datasets/positive%EC%8B%9C%EA%B0%81%ED%99%94.gif) |
  
  |💔부정적 평점의 리뷰 토픽 모델링 시각화 결과 [(링크)](https://github.com/estskyway/project_data_analystics/datasets/visualization_negative.html)|
  |---|
  | ![부정리뷰 모델링](https://github.com/estskyway/project_data_analystics/blob/main/datasets/negative%EC%8B%9C%EA%B0%81%ED%99%94.gif)|
<br>

### 5. 인사이트 도출
#### &nbsp;&nbsp;😄 긍정적 리뷰 분석 (num_words=7)
&nbsp;&nbsp;![image](https://github.com/estskyway/project_data_analystics/assets/132973368/907f32f7-d5ce-4b01-bbd9-086d943eb0f6)

- 첫번째 : 위 단어들로 보아 "운동을 하는 사람들 사이에서 헬스와 관련된 사이트의 인기가 늘어나고 있으며, 그에 따른 불편함이 없어 사람들이 만족하고 있다"고 추측해 볼 수 있습니다.
- 두번째 : 위 단어들로 보아 "사이트와 시설 모두 좋다는 평가를 받고 있으며, 특히 헬스와 관련된 부분에서 만족도가 높아지고 있다"고 추측해 볼 수 있습니다.
- 개선방안 제시 : 사이트를 통해 헬스장의 홍보 영상, 이용후기 등을 제공하여 이용자들의 관심을 유도. 또한, 사이트를 통해 회원 가입 및 할인 혜택 등 다양한 이벤트를 진행하여 이용자 수 유치 & 증가
<br>

#### &nbsp;&nbsp;😞 부정적 리뷰 분석 (num_words=7)
&nbsp;&nbsp;![image](https://github.com/estskyway/project_data_analystics/assets/132973368/f7c6626f-e4ad-4f4b-82f3-160d1a4f9bcf)

- 첫번째 : 위의 단어들로 보아 "사이트 접속 오류와 시설 불편이 늘어 개선이 필요하다" 고 추측해 볼 수 있습니다.
- 두번째 : 위 단어들로 보아 "사이트의 로그인이 제대로 작동하지 않는 문제로 운동하는 회원들의 불편이 늘어 개선이 필요하다" 고 추측해 볼 수 있습니다.
