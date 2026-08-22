# 모듈 5 — 로컬에서 작업하기

당신은 Git을 보았고, 느꼈고, 그려보았습니다.
이제 직접 해볼 차례입니다. 터미널에서, 실제 저장소를 가지고요.

---

## 준비: 설치와 설정

**Git 설치하기**
- Windows: [git-scm.com/download/win](https://git-scm.com/download/win)
- Mac: 터미널을 열고 `git --version`을 입력하세요 (자동으로 설치되거나 안내가 나옵니다)
- Linux: `sudo apt install git`

**이름과 이메일 설정하기** (당신이 만드는 모든 커밋에 이 정보가 기록됩니다):

```bash
git config --global user.name "당신의 이름"
git config --global user.email "your@email.com"
```

설정을 확인하세요:

```bash
git config --list
```

---

## 연습용 저장소

이 학습 과정에서는 별도의 연습용 저장소를 사용합니다:

**`git-garden-playground`**

정확한 URL은 선생님이 알려줄 것입니다.
`https://github.com/...`로 시작합니다.

이 저장소는 연습 전용입니다 — 무엇을 하든 망가뜨릴 걱정이 없습니다.

---

## 1단계: 클론(Clone)하기

클론이란 저장소를 자신의 컴퓨터로 다운로드하는 것을 말합니다.

```bash
git clone https://github.com/...url.../git-garden-playground
```

클론이 끝난 후:

```bash
cd git-garden-playground
ls
```

저장소의 파일들이 보일 것입니다. 그리고 숨겨진 `.git` 폴더도 있습니다 — 타임머신입니다.

---

## 2단계: 상태 확인하기

`git status`는 당신의 나침반입니다. 자주 사용하세요.

```bash
git status
```

지금 어떤 브랜치에 있는지, 변경된 파일이 있는지 알 수 있습니다.

---

## 3단계: 변경하기

에디터에서 폴더를 여세요 (또는 터미널을 사용하세요).
`deelnemers/` 폴더 안에 새 파일을 만드세요:

```bash
mkdir -p deelnemers
echo "Naam: [당신의 이름]" > deelnemers/[당신의-이름].txt
```

그런 다음 상태를 확인하세요:

```bash
git status
```

Git은 이 새 파일을 "추적되지 않음(untracked)"이라고 알려줍니다 — 파일은 존재하지만, Git이 아직 추적하고 있지 않다는 뜻입니다.

---

## 4단계: 스테이징(Staging)

스테이징은 "이 파일을 다음 커밋에 포함시키고 싶다"고 말하는 것입니다.

```bash
git add deelnemers/[당신의-이름].txt
```

또는 한 번에 모두 추가하세요:

```bash
git add .
```

상태를 다시 확인하세요. 이제 파일은 "스테이징 영역(staging area)"에 있습니다 — 커밋할 준비가 된 것입니다.

![워크플로우: 작업 디렉토리 → 스테이징 영역 → 저장소](images/werkstroom.png)

---

## 5단계: 커밋하기

이제 스냅샷을 만듭니다.

```bash
git commit -m "참가자 목록에 [당신의 이름] 추가"
```

좋은 커밋 메시지란:
- 동사로 시작합니다: "추가", "수정", "업데이트", "삭제"
- *무엇이* 바뀌었는지 설명하며, *어떻게* 바뀌었는지는 설명하지 않습니다
- 짧습니다 (최대 약 72자)

---

## 6단계: 이력 확인하기

```bash
git log
```

모든 커밋을 볼 수 있습니다: 해시, 작성자, 날짜, 메시지.

간결한 개요를 보려면:

```bash
git log --oneline
```

브랜치를 포함한 시각적 개요를 보려면:

```bash
git log --oneline --graph --all
```

---

## 7단계: 차이 확인하기

커밋하기 전에 무엇이 바뀌었는지 보고 싶나요?

```bash
git diff
```

스테이징 후, 커밋 전에:

```bash
git diff --staged
```

---

## 요약: 매일의 워크플로우

```
[변경하기]
      ↓
git add .
      ↓
git commit -m "..."
      ↓
git push   (모듈 6에서 배웁니다)
```

이 패턴을 하루에도 수십 번씩 반복하세요.
자연스럽게 몸에 익게 될 것입니다.
