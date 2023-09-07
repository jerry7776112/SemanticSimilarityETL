import warnings
from flask import *
from datetime import *
import package.ExtractPostgreSQL
import package.TransformData
import package.sentenceBERT
import package.LoadMongoDB

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="any string but secret"

"""錯誤處理"""
@app.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({"code": "500", "msg": "Oops! Can not find any data "}),500)

warnings.filterwarnings("ignore")
# ===============================================================================================
"""API 路徑"""
@app.route('/api/socialnetwork/v1/similarity')
def searchkeyword():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    search = request.args.get("search")
    """
    參數說明: 
    start_date: 起始日期 ex: 2021-12-01
    end_date: 結束日期 ex: 2021-12-20
    search: 關鍵字(語言不限) ex: 萊豬
    """

    if None not in (start_date, end_date, search):
        """利用searchKeyword()函式 進入 PostgreSQL 資料庫搜尋"""
        totalData = package.ExtractPostgreSQL.searchKeyword(start_date, end_date, search)
        """根據搜尋結果將資料利用first_clean()函式進行資料處理並轉換為DataFrame"""
        df = package.TransformData.dataclean.first_clean(totalData)

# 相似度分析========================================================================================================================

        """將DataFrame轉換為list以便後續進行語意相似度分析"""
        df_list = df.values.tolist()
        """
        Semantic Similarity Analysis
        將 df_list 利用 semanticSimilarity函式 進行語意相似度分析 並存為 pairs變數
        """
        pairs = package.sentenceBERT.semanticSimilarity(df_list)
        """利用 second_clean函式 進行第二次資料處理 以便後續匯入MongoDB"""
        pairs = package.TransformData.dataclean.second_clean(pairs)

        """將做完語意相似度分析的資料匯入MongoDB"""
        pairs = package.LoadMongoDB.insertData(pairs)

        """匯入成功於網頁顯示成功訊息"""
        result = Response({"code": "200", "msg": "Success!!"})
        
        return result



#====================================================================================================
"""啟動伺服器"""
# app.config['JSON_AS_ASCII'] = False
app.run(port=8080)

