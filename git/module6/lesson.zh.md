# 模块6 — 分支与协作

你已经掌握了基本的工作流程。现在，你要加入协作了。
在Git中协作，核心是分支（branch）和拉取请求（pull request）——正是这两个工具，让团队能够同时在同一个项目上工作，而不至于陷入混乱。

---

## 1. 创建一个分支

每次做新任务时，都要创建一个分支。
永远不要直接在`main`上工作。

```bash
git branch 我的分支
git switch 我的分支
```

或者一步完成：

```bash
git switch -c 我的分支
```

检查你现在在哪个分支上：

```bash
git branch
```

前面带`*`的那个分支就是当前分支。

好的分支名称应该简短且具有描述性，例如：
- `add-readme`
- `fix-typo-introductie`
- `update-versienummer`

---

## 2. 在分支上提交更改

就像在模块5中那样正常工作：

```bash
# 对某个文件进行修改
git add .
git commit -m "变更说明"
```

你的commit现在保存在你的分支上——而不是`main`上。
`main`保持不变。

---

## 3. 推送到GitHub

现在，把你的分支发送到GitHub：

```bash
git push origin 我的分支
```

第一次执行时，Git会要求你确认GitHub账号。
推送之后，这个分支就出现在GitHub上了——其他人也能看到。

---

## 4. 发起一个拉取请求（Pull Request）

**拉取请求（PR）**是一种提议："我想把我的分支合并到main中。"

在GitHub上：
1. 进入 `git-garden-playground` 仓库
2. 你会看到一条黄色提示条："my-branch — Compare & pull request"
3. 点击它
4. 写一段描述：
   - 你改了什么？
   - 为什么这么改？
   - 有没有什么是审查者需要知道的？
5. 点击 **"Create pull request"**

![在GitHub上创建拉取请求](images/pull_request_aanmaken.png)

拉取请求是一场对话，而不是一张表格。
描述写得越好，审查过程就越顺畅。

---

## 5. 协作的工作流程

```
main（稳定版本）
 |
 ├── 分支 A（Developer A 在这里工作）
 |        → 提交 → 推送 → PR → 审查 → 合并
 |
 ├── 分支 B（Developer B 在这里工作）
 |        → 提交 → 推送 → PR → 审查 → 合并
 |
main（合并后更新）
```

每个人都在自己的分支上工作。
`main`只通过被批准的拉取请求来更新。
这样，`main`就能始终保持稳定。

---

## 6. 获取他人的更改

如果有人的分支已经被合并了，你也会想拿到那些更改。

```bash
git switch main
git pull
```

`git pull` 会从GitHub上拉取最新版本的`main`。

想知道GitHub上有什么变化，但又不想改动本地文件？

```bash
git fetch
git status
```

`git fetch` 只获取信息。`git pull` 则既获取信息，又同时更新你的文件。

---

## 7. 实践作业

1. 克隆 `git-garden-playground` 仓库（如果你还没克隆过）。
2. 用你的名字创建一个分支：`bijdrage-[你的名字]`
3. 在 `bijdragen/` 文件夹中创建一个文件：`[你的名字].md`
4. 在文件中写下：
   - 你期望从Git中学到什么
   - 一个你还有的疑问
5. 用一条清晰的提交信息提交这个文件。
6. 把这个分支推送到GitHub。
7. 打开一个拉取请求，并附上简短的描述。

完成作业后：你的老师或同学会审查这个PR。
