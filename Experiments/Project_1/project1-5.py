verse = """ 
怪 奴 底 事 倍 伤 神 ? 半 为 怜 春 半 恼 春 。怜 春 忽 至 恼 忽 去 ，至 又 无 言 去 不
闻 。  
昨 宵 庭 外 悲 歌 发 ，知 是 花 魂 与 鸟 魂 ? 花 魂 鸟 魂 总 难 留 ，鸟 自 无 言 花 自
羞 ;
愿 奴 胁 下 生 双 翼 , 随 花 飞 到 天 尽 头 。 天 尽 头 , 何 处 有 香 丘 ?
未 若 锦 囊 收 艳 骨 ，一 抔 净 土 掩 风 流 ；质 本 洁 来 还 洁 去 ，强 于 污 淖 陷 渠
 3 
沟 。  
尔 今 死 去 侬 收 葬 ，未 卜 侬 身 何 日 丧 ? 侬 今 葬 花 人 笑 痴 ，他 年 葬 侬 知 是
谁 ?  
试 看 春 残 花 渐 落 ，便 是 红 颜 老 死 时 。一 朝 春 尽 红 颜 老 ，花 落 人 亡 两 不
知 ! 
""" 
template = "虚 词 : {0:-^5}出 现 了 : {1:-^5}次 " 
empty_word1 = "为 " 
result1 = verse.count(empty_word1) 
empty_word2 = "以 " 
result2 = verse.count(empty_word2) 
empty_word3 = "何 " 
result3 = verse.count(empty_word3) 
print(template.format(empty_word1,result1)) 
print(template.format(empty_word2,result2)) 
print(template.format(empty_word3,result3)) 