# 文章をBlockChaineで管理する

## BlockChaineとは
- BitCoinに代表される仮想通貨の分散データベースシステム
- sha256というハッシュアルゴリズムにより、事実上の改竄が不可能
- ドキュメントによって合意形成や、ブロックチェーンが意図しない方向にチェーンが伸びてしまった場合の取扱まで含んだりする

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
