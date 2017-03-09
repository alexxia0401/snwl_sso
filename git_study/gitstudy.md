# git 简明教程
> 环境：ubuntu 16.04.2 LTS  
作者：Qing Xia

### 安装 git
```shell
$ sudo apt install git -y
```
### 查看 git 版本
```shell
$ git --version
git version 2.7.4
```
### git 全局配置
```shell
$ git config --global user.email "alexxia@outlook.com"
$ git config --global user.name "Alex Xia"
```
### 初始化 git 仓库
```shell
$ mkdir alexproject
$ cd alexproject/
$ git init
$ Initialized empty Git repository in /home/alex/alexproject/.git/
```
### 创建一个文件
```shell
$ echo 'hello, world' > hello
$ cat hello
hello, world
```
### 查看此时的 git status
```shell
$ git status
On branch master
    
Initial commit
    
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    hello

nothing added to commit but untracked files present (use "git add" to track)
```
### 提交一个文件到暂存区（stage）
```shell
$ git add hello
```
### 查看 git status 的变化
```shell
$ git status
On branch master
    
Initial commit
    
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    
    new file:   hello
```
### 从已经是 stage 状态的文件提交到仓库（repository）
> -m 'xxx' 代表提交说明

```shell
$ git commit -m 'add hello file'
[master (root-commit) 0fef7d4] add hello file
 1 file changed, 1 insertion(+)
 create mode 100644 hello
```
### 再次查看 git status 的变化
```shell
$ git status
On branch master
nothing to commit, working directory clean
```
### 更新 hello 文件
```shell
$ sed -i '1a how are you' hello
$ cat hello
hello, world
how are you
```
### 通过 git diff 查看文件对比
```shell
$ git diff hello
diff --git a/hello b/hello
index 4b5fa63..46fed20 100644
--- a/hello
+++ b/hello
@@ -1 +1,2 @@
 hello, world
+how are you
```
### 再次 add 以及 commit
```shell
$ git add hello
$ git commit -m 'add how are you'
[master b021e04] add how are you
 1 file changed, 1 insertion(+)
```
### 查看提交 log
```shell
$ git log
commit b021e046fae1bc6bf818539ddf9e1a6180fabae2
Author: Alex Xia <alexxia@outlook.com>
Date:   Wed Feb 22 08:05:13 2017 -0800

    add how are you

commit 0fef7d4484a8f985b0b2ff25c8bf914ddcbebf54
Author: Alex Xia <alexxia@outlook.com>
Date:   Wed Feb 22 08:00:30 2017 -0800

    add hello file
```
### 每个 commit 显示一行 log
```shell
$ git log --pretty=oneline
b021e046fae1bc6bf818539ddf9e1a6180fabae2 add how are you
0fef7d4484a8f985b0b2ff25c8bf914ddcbebf54 add hello file
```
### 从版本2切换到版本1
> commit id 不用写全

```shell
$ git reset --hard 0fef7d4484a
HEAD is now at 0fef7d4 add hello file
$ cat hello 
hello, world
```
> 也可以使用，HEAD 代表当前版本，HEAD^ 代表上一个版本，HEAD^^ 代表上上一个版本，HEAD~100 代表前100个版本

```shell
$ git reset --hard HEAD^
```
### 回到版本2
```shell
$ git reflog
0fef7d4 HEAD@{0}: reset: moving to 0fef7d4484a
b021e04 HEAD@{1}: commit: add how are you
0fef7d4 HEAD@{2}: commit (initial): add hello file
$ git reset --hard b021e04
HEAD is now at b021e04 add how are you
$ cat hello
hello, world
how are you
```
### 撤销修改，还未提交到 stage 的情况
```shell
$ sed -i '2a have a good day' hello
$ cat hello
hello, world
how are you
have a good day
$ git checkout -- hello
$ cat hello
hello, world
how are you
```
### 撤销修改，已经提交到 stage 的情况，先 unstage，再用上一种情况的命令
```shell
$ sed -i '2a have a good day' hello
$ git add hello
$ git reset HEAD hello
Unstaged changes after reset:
M	hello
$ git checkout -- hello
```
### 当文件已 commit 进 repositoy 时如何撤销到上一个版本
> 等同于切换到上一版本

```shell
$ sed -i '2a have a good day' hello
$ git add hello
$ git commit -m 'add have a good day'
[master 6304f02] add have a good day
 1 file changed, 1 insertion(+)
$ git log --pretty=oneline
6304f02ecf3a7641fd3c9aef580856477310c0f7 add have a good day
b021e046fae1bc6bf818539ddf9e1a6180fabae2 add how are you
0fef7d4484a8f985b0b2ff25c8bf914ddcbebf54 add hello file
$ git reset --hard b021e046
HEAD is now at b021e04 add how are you
```