# 使用说明
## 1 准备数据文件data.txt
- data.txt文件的格式是
问题1 答案1
问题2 答案2
- 每行一个问题与答案，问题和答案之间空格隔开
## 2 将项目部署到服务器上，就可以访问了

# 参数调节
## 参考答案显示数量
- 在文件index.html第65行的数字5，可以调节显示数量
for (let i = 0; i < res.length && i < 5; i++) {