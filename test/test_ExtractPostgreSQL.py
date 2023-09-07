import sys
""".. 代表到上一層資料夾,從上一層去找對應的package"""
sys.path.append("..")
import package.ExtractPostgreSQL

start_date = "2021-12-15"
end_date = "2021-12-20"
search = "萊豬"

"""Test_ExtractPostgreSQL.searchKeyword()"""
try:
    totalData = package.ExtractPostgreSQL.searchKeyword(start_date, end_date, search)
    print("PostgreSQL connection successful!")
except Exception as e:
    print(e)