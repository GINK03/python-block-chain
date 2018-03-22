# 文章をBlockChaineで管理する

## BlockChaineとは
- BitCoinに代表される仮想通貨の分散データベースシステム
- sha256というハッシュアルゴリズムにより、事実上の改竄が不可能
- ドキュメントによっては、合意形成や、ブロックチェーンが意図しない方向にチェーンが伸びてしまった場合の取扱まで含んだりする

## BlockChaineを理解するには何を知っていると便利か
1. hash関数
2. hash関数を使った応用例各種
3. コンピュータにおけるhashmapの実装
4. 簡単なP2P

## コンピュータにおけるhashの使い方
hashはいろいろな値（文字列やなんでも）を、特定の数値の範囲にうまくエンベッティングする技術で、この仕組を使うと、キーからバリューの引き出しがO(1)の計算量で行えます。  

<div align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/37756254-28d073c6-2dec-11e8-9345-a00a3ed1993d.png">
</div>
<div align="center"> 図1. HashMapの構造 </div>

hashによる分散化はあらゆるところで行われており、エンジニアにとって馴染みのあるものでは、hashmap, KVS, Hadoopなどがキーをハッシュ化することでうまくやっています。
<div align="center">
  <img width="750px" src="https://user-images.githubusercontent.com/4949982/37756540-2f771d00-2ded-11e8-8a6d-a03c59d274bd.png">
</div>
<div align="center"> 図2. UbutuのISOサイトでは、md5というハッシュアルゴリズムの値を載せて改竄がないかユーザがチェックできる </div>

<div align="center">
  <img width="550px" src="https://user-images.githubusercontent.com/4949982/37757879-b8567c02-2df1-11e8-9924-46cc7bfdfcb9.png">
</div>
<div align="center"> 図3. 国会で説明された様子[1] </div>


## BlockChaineまで発展する
BlockChaineはこのhashによる鎖を連ねることで、鎖が維持できるているかどうかで、データが正しいかどうかの検証が行えます。  
<div align="center">
  <img width="750px" src="https://user-images.githubusercontent.com/4949982/37757573-da223408-2df0-11e8-996b-6ace35eac6bb.png">
</div>
<div align="center"> 図3. 正常系（不正がない場合）　</div>

<div align="center">
  <img width="750px" src="https://user-images.githubusercontent.com/4949982/37757619-fea62460-2df0-11e8-947a-f659c58d765f.png">
</div>
<div align="center"> 図4. 異常系（なんらかの編集があった場合）　</div>

単純なこの仕組に加えて、様々にP2Pで動作を確認と保証する仕組みをいれてBlockChaineというらしいです（広義すぎるので分散台帳技術はちょっと和訳として不適切だと思う）   

## BitCoinにある採掘という作業
BitCoinには採掘という作業があって、GPUをゴリゴリ回してお金を得るみたいなことをやっている人たちがいます。これは、ハッシュ値の先頭が0000000〜とかになるように、データの中にnonceというフィールドを追加して調整いています。  
最初に特定条件に一致するハッシュ値を計算できた人がインセンティブをもらい、次に繋がる鎖を生成します。これはマイニングしている人が、マイニングするモチベーションであり、ビットコインという通貨的特性と相性がいい理由でもあります。  

P2Pでは同時に生成してしまう可能性がありますが、同時に生成してしまったら、後続に続く鎖の数が大きい方が優先されます。  

国会で今話題になっている公文書偽造などの問題には転用可能でしょうか。  

## 公文書管理におけるブロックチェーンの利用
[この資料によると、費用対効果の視点でコストが嵩みすぎる](http://givemegohan.pigboat.jp/2018/03/21/公文書偽造はブロックチェーン技術で防げるか/)という課題が挙げられていますが、それは、nonceによる採掘難易度に依存するし、衝突困難性は採掘と関係がないので、私はできると考えています。  

また、直接、データをブロックチェーンに入れるのではなく、公文書のハッシュ値やフィンガープリントに該当するものをいれればいいはずだと思うのですが。

## 夏目漱石の小説をブロックチェーンに組み込む  
このような簡単なコードを作成しました。  
前のhashの情報を記憶しつつ、データを持ち、nonceの条件を満たすものを探し、一致したら、ブロックをjsonで吐き出すものです。  
```python
def _gen_block(arg):
  source_host, data, prev_hash = arg

  now = time.time()
  loc = datetime.fromtimestamp(now)
  timestamp = loc.timestamp()
 
  while True:
    nonce = random.randint(0, 100000000000000) 
    block = { \
      'timestamp':timestamp, \
      'source_host':source_host, \
      'data':data, \
      'prev_hash': prev_hash,  \
      'nonce':nonce,
    }
    next_hash = hashlib.sha256(bytes(json.dumps(block),'utf8')).hexdigest()

    # 先頭のN字が"0"ならば、採用
    size = 1
    if next_hash[:size] == '0'*size:
      break
  open(f'cache/{next_hash}', 'w').write( json.dumps(block, indent=2, ensure_ascii=False) ) 
  return block, next_hash

start_block, next_hash = _gen_block(('http://localhost:1200', 'Ground Zero', hashlib.sha256(bytes('0', 'utf8')).hexdigest()))
for line in open('stash/kokoro.txt'):
  line = line.strip()
  block, next_hash = _gen_block(('http://localhost:1200', line, next_hash) )
```

## nonce値の難易度による夏目漱石の「坊っちゃん」を全部ブロックチェーン化するまでの計算時間
**CPU**  
```console
CPU MHz:                1550.000
CPU max MHz:            3800.0000
CPU min MHz:            1550.0000AMD
BogoMIPS:               7585.48en 5 1500X Quad-Core Processor
```
**uname**
```console
$ uname -a
Linux PrintzEugen 4.13.0-32-generic #35-Ubuntu SMP Thu Jan 25 09:13:46 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

<div align="center">
  <img width="400px" src="https://user-images.githubusercontent.com/4949982/37760041-de1fccde-2df8-11e8-8384-171e464e81b3.png">
</div>
<div align="center"> 図5. 計算の難易度ごとの必要計算時間</div>

インセンティブが働かない公文書管理などの環境では、nonce値はないか、小さい値でいいのではないかと考えいています。  

## 過去への遡及
BlockChaineはその名の通り、鎖状になっているので、偽造されたものでない限り、最初の発行者のデータにたどり着けるような仕組みになっています。  

坊っちゃんの最後のセリフから、最初データまで辿ってみましょう。  

**最後のセリフ**  
```cosnole
hash => 00ce7c3a81315250d7abc2d99f177b2ffb442334644044ea89f1d6e435845d86
っtimestamp': 1521708677.710969, 'source_host': 'http://localhost:1200', 'data': '私は私の過去を善悪ともに他ひとの参考に供するつもりです。しかし妻だけはた唯た一人の例外だと承知して下さい。私は妻には何にも知らせたくないのです。妻が己おのれの過去に対してもつ記憶を、なるべく純白に保存しておいてやりたいのが私の。一ゆいいつの希望なのですから、私が死んだ後あとでも、妻が生きている以上は、あなた限りに打ち明けられた私の秘密として、すべてを腹の中にしまっておいて下さい  」', 'prev_hash': '072c69c315bc6c2839122f1b5566df41dfb64f9c489b44441056bab8b0ed9104', 'nonce': 18180102876915}
```
「溯って、『フィリス』」（幻想再帰のアリュージョニストのネタ）
```console
$ python3 phyllis.py
私は私の過去を善悪ともに他ひとの参考に供するつもりです。しかし妻だけはたった一人の例外だと承知して下さい。私は妻には何にも知らせたくないのです。妻が己おのれの過去に対してもつ記憶を、なるべく純白に保存しておいてやりたいのが私の唯一ゆいいつの希望なのですから、私が死んだ後あとでも、妻が生きている以上は、あなた限りに打ち明けられた私の秘密として、すべてを腹の中にしまっておいて下さい。」
しかし私は今その要求を果たしました。もう何にもする事はありません。この手紙があなたの手に落ちる頃ころには、私はもうこの世にはいないでしょう。とくに死んでいるでしょう。妻は十日ばかり前から市ヶ谷いちがやの叔母おばの所へ行きました。叔母が病気で手が足りないというから私が勧めてやったのです。私は妻の留守の間あいだに、この長いものの大部分を書きました。時々妻が帰って来ると、私はすぐそれを隠しました。
私が死のうと決心してから、もう十日以上になりますが、その大部分はあなたにこの長い自叙伝の一節を書き残すために使用されたものと思って下さい。
...
...
...
私わたくしはその人を常に先生と呼んでいた。だからここでもただ先生と書くだけで本名は打ち明けない。これは世間を憚はばかる遠慮というよりも、その方が私にとって自然だからである。私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。筆を執とっても心持は同じ事である。よそよそしい頭文字かしらもじなどはとても夏目漱石と私ない。
こころ

Ground Zero 
```
Ground Zeroとは、今回、作成したblockchaineの最初の値になるシードのデータです。　　


## 参考文献
- [1] [Twitter](https://twitter.com/komiya_atsushi/status/971657543717068800)

