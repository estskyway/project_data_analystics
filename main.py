# conda install -c conda-forge fastapi uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the 'resources' directory as '/images' endpoint
from fastapi.staticfiles import StaticFiles
# app.mount("/images", StaticFiles(directory="resources"), name="images") 
# EX) http://127.0.0.1:8000/images/thermometer.png
# <img src='http://127.0.0.1:8000/images/thermometer.png' /> # view
# <a href='http://127.0.0.1:8000/images/thermometer.png'> thermometer.png</a> # download

@app.get("/")
async def root():
    return {"message": "Hello World"}

import pickle

# /api_v1/mlmodelwithregression with dict params
# method : post
# {
#     "texture_mean": 18.5,
#     "perimeter_mean": 102.1
# }
@app.post('/api_v1/mlmodelwithregression') 
def mlmodelwithregression(data:dict) : # json
    print('data with dict {}'.format(data))
    
    # data dict to 변수 활당
    review = data['reviews']
    
    # pkl 파일 존재 확인 코드 필요

    # 리뷰 데이터 전처리(형태소 분석)
    from mecab import MeCab
    mecab = MeCab()
    def tokenize_reviews(review):
        tokens = mecab.morphs(review)
        return ' '.join(tokens)
    
    comment = tokenize_reviews(review)

    # 벡터 토큰화
    with open('datasets/sentiment_TfidfVectorizer.pkl', 'rb') as sentiment_TfidVectorizer_file:
        loaded_model = pickle.load(sentiment_TfidVectorizer_file)
        input_labels = [comment]
        vectorized_comment = loaded_model.transform(input_labels)

    result_predict = 0;   
    # 학습 모델 불러와 예측
    with open('datasets/sentiment_machine.pkl', 'rb') as sentiment_machine_file:
        loaded_model = pickle.load(sentiment_machine_file)
        input_labels = vectorized_comment # 학습했던 설명변수 형식 맞게 적용
        result_predict = loaded_model.predict(input_labels)
        print('Predict radius_mean Result : {}'.format(result_predict))
        pass

    # 예측값 리턴
    result = {'댓글 분석':result_predict[0]}
    return result  