# 模块8 — 测试人员的Git

作为测试人员，你使用Git的方式可能和开发者不太一样。
你打交道的是测试脚本、bug报告、发现的问题以及文档。
在这个模块中，你会看到Git和GitHub是如何直接支持你作为测试人员的日常工作的。

---

## 1. GitHub Issues：工作流程的核心

**Issue（议题）**是在GitHub中被记录下来的一个任务、bug报告或问题。

作为测试人员，你会为以下情况创建issue：
- 发现的bug
- 需要向团队提出的测试相关问题
- 请求额外的测试数据
- 对测试脚本的改进建议

**一份好的bug报告（以issue形式）应该包含：**

```markdown
## 描述
点击表单中的"保存"按钮，出现500错误。

## 复现步骤
1. 打开 /formulier
2. 填写所有字段
3. 点击"保存"

## 预期行为
表单应该被保存，并显示确认信息。

## 实际行为
错误提示：Internal Server Error (500)

## 环境信息
- 浏览器：Chrome 124
- 操作系统：Windows 11
- 测试环境：staging
```

---

## 2. 标签（Labels）：建立结构

标签用来给issue分类。
GitHub中默认的标签有：

| 标签 | 用途 |
|-------|---------|
| `bug` | 某些功能没有按预期工作 |
| `enhancement` | 改进建议 |
| `question` | 向团队提出的问题 |
| `documentation` | 文档缺失或不正确 |
| `duplicate` | 之前已经报告过 |
| `won't fix` | 有意选择不修复 |

你也可以创建自己的标签，例如：
- `优先级: 高`
- `测试: 回归测试`
- `环境: staging`

---

## 3. 里程碑（Milestones）：与版本或Sprint关联

**里程碑（milestone）**把属于同一个版本或Sprint的issue归为一组。

举例：
- 里程碑 `Sprint 4 — Release 2.1`
- Issue：12个bug，3个测试请求
- 进度：15个中已完成7个

对测试人员来说，里程碑能给你一个整体概览：发布之前还有哪些工作要完成？

---

## 4. 在Git中管理测试脚本

测试脚本其实就是普通文件（YAML、txt、Python等）。
因为它们保存在Git仓库中，你就能拥有：

- **历史记录**：这个测试脚本是谁、在什么时候修改的？
- **回退**：测试脚本出错了？回到之前的版本就行。
- **协作**：同事可以通过拉取请求（pull request）来审查测试脚本。
- **可追溯性**：你可以把一个测试脚本关联到某个issue。

**测试脚本的良好文件夹结构：**

```
testscripts/
  regressie/
    module1_login.yaml
    module2_formulieren.yaml
  smoke/
    dagelijkse_check.yaml
  exploratory/
    notities_sprint4.md
```

---

## 5. 把bug报告关联到某次commit

在commit信息中，你可以引用某个issue：

```bash
git commit -m "修复登录验证问题 (#42)"
```

GitHub会识别 `#42`，并自动创建到42号issue的链接。
使用 `Closes #42`，可以在合并时自动关闭该issue：

```bash
git commit -m "修复：表单中损坏的保存按钮 (Closes #58)"
```

---

## 6. Git中的测试工作流程

测试人员的一个典型循环是这样的：

```
1. 编写或修改测试脚本
       ↓
2. 创建分支：test/sprint4-regressie
       ↓
3. Commit：小的改动，配上清晰的提交信息
       ↓
4. 发起拉取请求 → 由同事审查
       ↓
5. 发现了bug？ → 创建一个包含复现步骤的issue
       ↓
6. 开发者修复了bug → 你在PR分支上再次测试
       ↓
7. PR被合并 → 里程碑随之更新
```

Git不是一项额外的行政负担。
它是让你的工作变得可见、可追溯的地方。
