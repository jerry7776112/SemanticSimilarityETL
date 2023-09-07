import re
import pandas as pd


class dataclean():
    def first_clean(totalData):
        df = pd.DataFrame(totalData)
        """將url轉為domain"""
        df['caption'] = df['related_link'].str.extract('//(www\.){0,1}(.*?)/')[1]

        """資料案時間排序"""
        df = df.sort_values(by=['post_time'])
        df.reset_index(inplace=True, drop=True)

        """時間轉為字串"""
        df["post_time"] = df["post_time"].apply(str)
        
        """資料清洗"""
        df = df.dropna(subset=["page_name"])
        df = df.dropna(subset=["body"])
        df = df[["page_name", "body", "post_time"]]
        df.reset_index(inplace=True, drop=True)
        df['body']=df['body'].apply(lambda x: cleanbody.clean_body(x))

        return df

    def second_clean(pairs):
        result = pd.DataFrame(pairs, columns = ["sentence1", "sentence2", "similarity"])

        result['similarity'] = result['similarity'].astype(float, errors = 'raise')

        cols = ["page_name1", "sentence1", "post_time1"]
        a = pd.DataFrame(result["sentence1"].tolist(), columns=cols)

        cols = ["page_name2", "sentence2", "post_time2"]
        b = pd.DataFrame(result["sentence2"].tolist(), columns=cols)

        c = pd.concat([a, b, result["similarity"]], axis = 1)

        return c 


class cleanbody():
    def clean_body(text):
        """lower-case all characters"""
        text=text.lower()
                
        """remove handles"""
        text= re.sub(r'@\S+', '',text) 
                
        """remove urls"""
        text= re.sub(r'http\S+', '',text) 
        text= re.sub(r'pic.\S+', '',text)
                
        text= re.sub(r'[^\w\s]+', '  ',text)
        text= re.sub(r'br', '  ',text)

        text=re.sub(r'\s+[a-zA-Z]\s+', ' ', text+' ') 

        text= re.sub("\s[\s]+", " ",text).strip()  
                
        return text