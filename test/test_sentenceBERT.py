import sys
# .. 代表到上一層資料夾，從上一層去找對應的package
sys.path.append("..")
import package.sentenceBERT

df_list = ['BRT長輩老人經文圖', '感謝新黨俊良哥和季節來探望 感謝智強 照新 士修 植斗 淑惠 巧芯等夥伴一路陪伴  感謝我的團隊在我絕食期間依然服務選民 感謝羅智強團隊辛苦在夜宿區照料 感謝以核養綠志工四處奔走發聲 感謝所有來探望為我們加油打氣的親朋好友 感謝所有投票的民眾 無論立場為何 願意出來投票 即是實踐民主 其實 衡諸世界 純粹對事的公民投票投票率不高是常見之事 多元社會中有一定對政治冷漠者 是正常狀態 而關鍵就在 我有打動這些對政治冷漠者嗎 一切都只能責怪自己不夠努力 沒有好抱怨敵人的地方 是我的行動不夠接地氣 是我的論述不夠親民 是我不夠從民生角度出發 我認真催票了嗎 我為公投真的盡心盡力了嗎 人民會覺得我真的為民發聲嗎 抑或是認為政治人物一樣爛 我信任四項題目為國家好 為人民好 我有如實的傳達了我的信念嗎 我有讓人民信任我是為人民著想嗎 打從十月底 我在節目上不斷強調 有嚴重的焦慮感 認 為公投可能四項都被翻盤 為此 我選擇盡我所能 投身宣傳四大公投的道路 最早製作四票同意的懶人圖卡 挺身開始街頭及市場演講 跟隨夜宿凱道及自由廣場 告發46名民代 去函ait 拍攝核電萊豬影片 赴桃園新竹高雄演講 最後絕食130小時 難過一天就好 因為我還有很多工作 為民請命不是選舉或公投的口號 而是不斷實踐的理念 由政府帶頭散播假資訊 網路側翼的聲量大於副總統的網路聲亮 台灣名副其實是 側翼治台 沒有責怪敵人太強的道理 哪怕戰敗 敗的漂亮嗎 從民調四票都領先 到全被翻盤  一切只有自己技不如人 台灣的民主不夠成熟 人民用自己的雙手殺死了公民投票 未來任何議題都難有成功的公民投票 連反萊 豬民進黨都能翻盤 可見當民進黨國家機器動員起來 未來台灣難有抵抗民進黨的對手 有效監督制衡執政黨的機關已然消失 公 民投票也無從制衡 民進黨正式走向黨政軍媒網五權合一的權力巨獸 令我有信心的是 在這次投票 我仍然看到許多年輕的朋友 更多的人 看穿民進黨的謊言 抱持正直是非 相信科學與邏輯 願意守護台灣的民主 願意對中華民國有信心 我也要呼籲 現在不是找戰犯的時候 戰犯心裡有數 我們要加緊時刻整備團隊 繼續監督 看這個政黨究竟能不能因為開放萊豬就加入cptpp 看能否 因為破壞藻礁就不再跳電 看核四廠到底會不會遇到超級大地震而爆炸 我們要上緊發條 繼續為民服務 找回人民的信任 真正讓人民願意信賴 抵抗威權 推翻說謊雙標的政黨 讓人民安居樂業 還有許多挑戰 還有很長的路要走 我希望大家繼續團結克服難 關 共同向前邁進 路漫漫其修遠兮 吾將上下而求索', '2021-12-19 20:42:40+08:00'], ['The News Lens 關鍵評論網', '四 大公投通通沒過關 接下來會怎麼樣 四大公投結果出爐 重啟核四 反萊豬 公投綁大選 珍愛藻礁皆未能通過 究竟 公投不通過 之後 將對我們的生活造成什麼影響 獨家專屬電子報 收藏文章等4大服務 加入會員即可享有 bit ly 3pzwdlz 公投 重啟核四 反萊豬 公投綁大選 珍愛藻礁', '2021-12-19 20:42:42+08:00'], ['BigEcon', '快速瞭解本週新聞大事 新聞不漏接 薪水往 上飛 明年恐怕升息三次 聯準會轉鷹派 中方近期也開始經濟制裁立陶宛 立陶宛撤回駐中人員 海地經歷總統遭殺 大地震 如今又遇到爆炸 海地油罐車爆炸 前三名分別為中國 緬甸 越南 全球488名記者遭關押創新高 沒高於最低門檻 四個公投皆不通過 四大公投投票 聯準會 fed fomc 升息 利率 中國 立陶宛 外交 海地 爆炸 中國 緬甸 越南 記者 公投 核四 萊豬 bigecon 一週新聞', '2021-12-19 21:07:08+08:00'], ['黑特南一中2.0', '黑特南一中50482 原來有400多萬人想吃萊豬啊', '2021-12-19 21:27:33+08:00'], ['今周刊', '與所有民調相反 反萊豬不同意票超過同意票的關鍵為何', '2021-12-19 21:30:01+08:00'], ['吵吵鬧鬧', '', '2021-12-19 21:33:10+08:00'], ['吵吵鬧鬧', '', '2021-12-19 21:36:59+08:00'], ['NTD 新唐人 電視台', '四大公投案結果揭曉 全都未通過 外媒分析這次公投 是民眾對總統蔡英文政府的信任投票', '2021-12-19 21:40:00+08:00'], ['芋傳媒 TaroNews', '4大公投案結果昨天出爐 全遭否決 民進黨主張4個不同意在宜蘭獲得全勝 民進黨宜蘭縣黨部今天掃街謝票 國民黨籍宜蘭縣長林姿妙說 公投是展現人民的權益 尊重民意', '2021-12-19 21:47:11+08:00'], ['吵吵鬧 鬧', '', '2021-12-19 21:48:05+08:00'], ['吵吵鬧鬧', '', '2021-12-19 21:53:29+08:00']

"""Test_sentenceBERT.semanticSimilarity"""
try:
    pairs = package.sentenceBERT.semanticSimilarity(df_list)
    print("SemanticSimilarity successful!")
except Exception as e:
    print(e)