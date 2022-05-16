# instant_quiz


## import csvファイルフォーマット
1. ヘッダーレコード
`string`
基本的に区切りを示す用．

2. 基本レコード(quizを記述する)
`idx,type,…`
idx: 問題番号(uniqueが望ましい)
type: quiz形式を示す，その後の形式もこれに依存する．
(caption: 問題の注意とかとか)
正解の[]は別解扱い

### nsフォルダ内のtype一覧
- select: n択空所補充，レコード`idx\t,select\t,問題,選択肢数,選択肢,…,正解番号`
- sort: 語句整序，レコード`idx\t,sort\t,問題,語句数,語句,…,正解文字列`
- equal: 連立完成，レコード`idx\t,equal\t,問題a,問題b,空所数,正解,…`
- tof: 正誤指摘，レコード`idx\t,tof\t,問題,指摘語句数,指摘語句,…,正解番号,正解文字列`
- fill: 適語補充，レコード`idx\t,fill\t,問題,空所数,正解,…`