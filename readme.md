# 队式19

对战目前的计划：前端发送需要对战的队伍，后端检索到对应的代码文件名，
然后向容器里的另一个django应用发送http请求，比如直接访问：8888/battle/file1-file2，然后容器里的django在views里面写上当接收到这个http请求时，运行shell命令，然后把结果返回到本来的后端，再返回到前端