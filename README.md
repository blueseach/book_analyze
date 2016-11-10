
## 项目手记

这是我的第一个完整的python程序，纪念一下。

### 初衷
阳老师在《工作谈》中推荐了主题学习方法，把某一学科的10多本书拿来，看它们共同提到最多的概念是哪些，通常就是这一领域里最重要的知识。我想，能否用机器人来做这件事？收集书籍的目录信息，分词后进行统计，自动显示某一领域的知识图，甚至是知识树（目前做不到，往这个方向努力^_^）。我希望这个不仅仅是课程的作业，而是后面持续钻研的一个项目。

豆瓣读书上有的书目录不完整，但是书比较全；豆瓣阅读上的书目录完整，只是数量少。先拿豆瓣阅读来作为学习。

总共抓取了2w多本书，为了提高速度，分析的时候把免费公版书和小说拿掉了。

### 开发记录
 
 D1-D2（1030-1031）:看上期学员作品代码，理解功能。调试在本地成功运行。
 
 D3-D7（1101-1105）:D3完成基本代码，开始捉取信息后遇到一个问题，耽搁了D4、D5整整两天。
 
 现象：每个类别下的书籍只能捉取前六页，第七页开始抓取失败。返回的网页源码是要求输入用户名和密码。
 
 应对方法：以为是豆瓣的反爬虫机制，只要发现操作频繁就要求登陆，于是尝试增加时延、伪装浏览器头部、用代理登陆，甚至切换到另一个网络获得新ip，统统没有效果。
 直到我把抓出来的某一页地址放到浏览器里面查看，发现也被要求登陆。原来用浏览器浏览时，豆瓣阅读的前6页是不要求登陆的，我以为都不需要，没有考虑cookie的问题。
 但是第7页开始，就必须登陆才能查看。在代码中添加自己的cookie后，问题解决。是我想多了，这么个小程序还不足以触发豆瓣的反爬虫。

D8-D11（1106-1109）:对抓取的数据进行分析。

豆瓣阅读上的目录也不规范，有的分了一级到三级目录，有的把所有目录都放在一级目录的标签里面，靠代码无法区分。为了简化问题，只取了最深一层的目录。如果能分目录层次，对不同级别目录里的词语赋予不同权重，会更合理。

分析思路：用jieba对每本书的目录分词，提取权重靠前的作为关键词。再对指定的某一类书求关键词。
算法过于简单，准备接下来进行文本的聚类和分类分析。

网上查了一下，[豆瓣上的书有多少本](https://www.zhihu.com/question/19583157)，据说一共有上百万本，如能获取它们的完整目录，可以作为一个很好的分析对象。只是目前水平不足，具体应该从哪些角度入手，通过哪些算法来分析，都是要解决的问题，也希望老师和各位同学多提建^_^。

## 致谢

感谢肖凯老师。上完数据分析课，我不敢说自己已经入门了，但至少知道接下来要朝哪些方向努力。

感谢三位助教的指导。从[yongle](https://github.com/lyltj2010)同学的项目中借鉴了许多，写代码过程中也经常叨扰。
  
  
