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


## 参考文献
- [1] [Twitter](https://twitter.com/komiya_atsushi/status/971657543717068800)

