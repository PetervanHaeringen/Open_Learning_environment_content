# 模块5 — 在本地工作

你已经看过Git、体验过Git、也画过Git了。
现在，你要真正动手做了。在终端里，在一个真实的仓库上。

---

## 准备工作：安装与配置

**安装Git**
- Windows：[git-scm.com/download/win](https://git-scm.com/download/win)
- Mac：打开终端，输入 `git --version`（会自动安装，或给出安装说明）
- Linux：`sudo apt install git`

**设置你的名字和邮箱**（这些信息会出现在你所做的每一次commit中）：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

检查你的设置：

```bash
git config --list
```

---

## 练习仓库

在这个学习路径中，我们使用一个专门的练习仓库：

**`git-garden-playground`**

你的老师会给你确切的URL地址。
它以 `https://github.com/...` 开头。

这个仓库专门用来练习——你不可能把它弄坏。

---

## 第一步：克隆（Clone）

克隆就是把一个仓库下载到你自己的电脑上。

```bash
git clone https://github.com/...url.../git-garden-playground
```

克隆完成后：

```bash
cd git-garden-playground
ls
```

你会看到仓库里的文件。还有一个隐藏的 `.git` 文件夹——这就是那台时间机器。

---

## 第二步：查看状态

`git status` 是你的指南针，要经常使用它。

```bash
git status
```

你会看到自己现在在哪个分支上，以及是否有文件被修改过。

---

## 第三步：进行一次修改

在编辑器中打开这个文件夹（或者使用终端）。
在 `deelnemers/` 文件夹中创建一个新文件：

```bash
mkdir -p deelnemers
echo "Naam: [你的名字]" > deelnemers/[你的名字].txt
```

然后再查看一下状态：

```bash
git status
```

Git会把这个新文件标记为"未跟踪"（untracked）——它确实存在，但Git还没有开始追踪它。

---

## 第四步：暂存（Staging）

暂存的意思是告诉Git："我想把这个文件包含进下一次commit里。"

```bash
git add deelnemers/[你的名字].txt
```

或者一次性添加所有文件：

```bash
git add .
```

再次查看状态。这个文件现在已经在"暂存区"（staging area）——准备好可以提交了。

![工作流程：工作目录 → 暂存区 → 仓库](images/werkstroom.png)

---

## 第五步：提交（Commit）

现在，你要创建这个快照了。

```bash
git commit -m "把[你的名字]加入参与者列表"
```

一条好的commit信息应该：
- 以一个动词开头："添加"、"修复"、"更新"、"删除"
- 描述的是*改了什么*，而不是*怎么改的*
- 简短（最多约72个字符）

---

## 第六步：查看历史记录

```bash
git log
```

你会看到所有的commit：哈希值、作者、日期、提交信息。

想要一个更紧凑的概览：

```bash
git log --oneline
```

想要一个带分支的可视化概览：

```bash
git log --oneline --graph --all
```

---

## 第七步：查看差异

想在提交之前看看到底改了什么？

```bash
git diff
```

暂存之后、提交之前：

```bash
git diff --staged
```

---

## 小结：日常工作流程

```
[进行一次修改]
      ↓
git add .
      ↓
git commit -m "..."
      ↓
git push   （将在模块6中学习）
```

每天重复这个模式几十次。
慢慢地，它就会变成一种习惯。
