# SemanticSimilarityETL
## 專案說明
### 專案名稱: ETL 語意相似度分析(詳情請參閱 SemanticSimilarityETL實作說明 pdf 檔案)
### ETL實作
* 使用社群平台資料集作為MetaData建置於PostgreSQL
* 利用Sentence-BERT語言模型將資料集進行語意相似度分析
* 將分析結果匯入至MongoDB
* 將流程整合為一自動化API
#### 資料集(可自行收集任意文本資料進行實作)
* 某社群平台貼文資料集
* 資料筆數: 32266004

### 套件安裝
```python
pip install -r requirements.txt
```
### 前置準備
* 自行準備任意有文本的資料集
* 建置PostgreSQL資料庫
* 建立資料表(table) & 索引(index)
* 匯入資料集
* 建置MongoDB Atlas資料庫
* 建立MongoDB Atlas資料庫中之Collection

### 實務知識
* ETL流程
* 大數據處理
* PostgreSQL搜尋效能提升
* Python Flask後端開發
* API開發
* PostgreSQL
* MongoDB

### ETL Flow
![ETLflow](https://github.com/jerry7776112/SemanticSimilarityETL/blob/main/etlflow/etlFlow.png "ETLflow")

### 專案目錄
```
SemanticSimilarityETL:.
│  main.py
│  requirements.txt
│  
├─package
│  │  ExtractPostgreSQL.py
│  │  LoadMongoDB.py
│  │  sentenceBERT.py
│  │  TransformData.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          ExtractPostgreSQL.cpython-310.pyc
│          LoadMongoDB.cpython-310.pyc
│          sentenceBERT.cpython-310.pyc
│          TransformData.cpython-310.pyc
│          __init__.cpython-310.pyc
│          
└─test
        integration_test.py
        test_ExtractPostgreSQL.py
        test_LoadMongoDB.py
        test_sentenceBERT.py
```
