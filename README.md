# unifiedCoding -- Python转码
## 问题复原
在一个目录下有多个文件，这些文件的文件名以不同的编码方式存在在于目录下，通过此程序可以大致识别出各个**文件名**的编码方式，以及将编码的格式统一到utf-8.
## 难点
- 文件名非文件 问题相当于一个文件中有各种编码文字混杂在一起造成乱码 怎么解析这个文件
## Python环境
- Python 2.7
- chardet
## 采用的方法
Python库里自带了chardet库，可以用来预测编码类型，但是由于chardet预测准确率不高，另外引入了汉字和繁体字的Unicode编码集，在chardet预测率较低时，使用探测的方式，以预测编码集->utf-8编码集->gb2312编码集->big5编码集的探测顺序探测文件编码，对解码结果进行库查找，判断结果是否具有合法性。
## 可利用处
- 较为完整的汉字编码集
- 较为完整的繁体字编码集
- chardet
- 用户可以通过修改生成的文件来自定义重命名规则
## 短板
- 在编码集交叉的部分表现不够优秀 解决思路：词法预测
- 在有其他编码的时候表现较差 解决思路：加入更多的编码集
- 由于程序含编码集，显得较为臃肿 解决：放入文件(效率问题？)
- 缺少文件交互阶段  找时间修改ing...
