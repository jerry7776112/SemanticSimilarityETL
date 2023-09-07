import psycopg2

"""
連線至資料庫
host: 輸入host位址
database: 輸入資料庫名稱
user: 輸入使用者名稱
password: 輸入密碼
"""
con = psycopg2.connect(
    host = "輸入host位址",
    database = "輸入資料庫名稱",
    user = "輸入使用者名稱",
    password = "輸入密碼"
)

# cursor
cur = con.cursor()
"""根據start_date, end_date, search 三者參數 進入資料庫搜尋"""
def searchKeyword(start_date, end_date, search):
    cur.execute(
        f"""
        SELECT * FROM public.fb712
        WHERE post_time BETWEEN '{start_date}'AND '{end_date}'
        AND (title &@ '{search}'
        OR body &@ '{search}'
        OR description &@ '{search}')
        """)
    result = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    totalData = []
    for row in result:
        r = dict(zip(columns, row))
        totalData.append(r)
    return totalData