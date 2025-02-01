# 命令语法


```bash
## mac https://formulae.brew.sh/formula/gnu-sed#default
##brew install gnu-sed
## osx 使用 gsed
$sed 's/unix/linux/' geekfile.txt
sed [-hnV][-e<script>][-f<script>][文本文件]
```

参数说明

1. -e<script> --expression=<script> 以选项中指定的 script来处理输入的文本文件 

## sed 命令

1. a 新增, a 的后面可以接字串，而这些字串会在新的一行出现(目前的下一行)
2. c 取代,  c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行！
3. d 删除 因为是删除啊，所以 d 后面通常不接任何东东；
4. i 插入  i 的后面可以接字串，而这些字串会在新的一行出现(目前的上一行)
5. p 打印 亦即将某个选择的数据印出。通常 p 会与参数 sed -n 一起运行
6. s 取代 可以直接进行取代的工作哩！通常这个 s 的动作可以搭配正则表达式！例如 1,20s/old/new/g 就是啦 



## awk

```bash
awk -W version
mawk 1.3.4 20200120
Copyright 2008-2019,2020, Thomas E. Dickey
Copyright 1991-1996,2014, Michael D. Brennan

random-funcs:       srandom/random
regex-funcs:        internal
compiled limits:
sprintf buffer      8192
maximum-integer     2147483647
```
## 参考

1. https://zlibrary-china.se/book/19285997/e25863/sed-and-awk-101-hacks-%E4%B8%AD%E6%96%87%E7%89%88.html
1. https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/
1. https://www.runoob.com/linux/linux-comm-sed.html