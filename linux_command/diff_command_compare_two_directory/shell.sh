比较两个目录下内容的不同:
方法1:
diff <(tree -Ci --noreport ./kibana-5.5.1-linux-x86_64) <(tree -Ci --noreport ./kibana-5.6.3-linux-x86_64)

-C: 表示输出颜色，如果不指定，则输出的文本不会有任何颜色，看起来麻烦
-i: 表示输出结果不考虑缩进，如果不指定，则考虑缩进
--noreport: 表示不希望得到比较报告，报告中包含不同的目录下有多少个目录和文件

方法2:
find ./kibana-5.5.1-linux-x86_64 -printf "%P\n" | sort > file1
find ./kibana-5.6.3-linux-x86_64 -printf "%P\n" | sort | diff file1 -

-printf "%P\n" : %P表示find结果中去掉前缀路径

方法3:
 (cd ./kibana-5.5.1-linux-x86_64;find . | sort > ~/file1)
 (cd ./kibana-5.6.3-linux-x86_64;find . | sort | diff ~/file1 -)

在括号中执行是为了在子shell中执行换目录，而不影响当前所在目录

方法4:
rsync -rvn --delete kibana-5.5.1-linux-x86_64/ kibana-5.6.3-linux-x86_64 | sed -n '2,/^$/{/^$/!p}'
结果中delete后面多出的是kibana-5.6.3-linux-x86_64中多出的文件
加上参数-i可在结果中区别出不同的是文件还是目录
其中:
    1. -n:表示try run，试着运行rsync同步，不会真的同步;
    2. 第一个目录后的斜线不能少，否则会把第一个目录同步到第二个目录中;
    3. sed的作用是过滤掉和文件不相关的内容;


安装vimdiff时遇到无法安装的解决方法:
sudo apt-get remove vim-common
sudo apt-get install vim
