from sentence_transformers import SentenceTransformer, util

"""將格式轉為list的資料匯入 Sentence-BERT 進行語意相似度分析"""
"""使用模型為 Sentence-BERT 中的 all-MiniLM-L6-v2"""
def semanticSimilarity(df_list):
    # Semantic analysis
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sentences = df_list
    paraphrases = util.paraphrase_mining(model, sentences, show_progress_bar=True)

    pairs = []
    for paraphrase in paraphrases:
        score, i, j = paraphrase
        pairs.append([sentences[i], sentences[j], "{:.3f}".format(score)])
    return pairs