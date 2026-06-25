#!/usr/bin/env python3
"""Soo saar warbixin ku saabsan ardayda gudbisay Final Project-ka.

Script-kani wuxuu baadhaa folder-ka `submissions/`, oo arday kasta wuxuu ka
raadiyaa folder-ka final project-ka (magacyo kala duwan: "final project",
"final-project", "FinalProject", "FinalProjec", iwm.). Maadaama script-ku uu
ku shaqeeyo branch-ka `main`, folder kasta oo halkaas yaal waxaa loola jeedaa
in PR-kiisii horey loo aqbalay (merged).

Wax soo saar: `submissions/FINAL_PROJECT_REPORT.md`
"""

from __future__ import annotations

import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SUBMISSIONS_DIR = REPO_ROOT / "submissions"
REPORT_PATH = SUBMISSIONS_DIR / "FINAL_PROJECT_REPORT.md"


def is_final_project_dir(name: str) -> bool:
    """Ku celi True haddii magaca folder-ku uu tilmaamayo final project."""
    normalized = re.sub(r"[\s_\-]+", "", name).lower()
    return "final" in normalized


def find_final_project_dir(student_dir: Path) -> Path | None:
    """Ka raadi folder-ka final project-ka gudaha folder-ka ardayga."""
    for child in sorted(student_dir.iterdir()):
        if child.is_dir() and is_final_project_dir(child.name):
            return child
    return None


def git_last_commit(path: Path) -> tuple[str, str]:
    """Soo celi (qoraaga, taariikhda) commit-kii ugu dambeeyay ee taabtay path."""
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%an|%ad", "--date=short", "--", str(path)],
            cwd=REPO_ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        if out and "|" in out:
            author, date = out.split("|", 1)
            return author.strip(), date.strip()
    except subprocess.CalledProcessError:
        pass
    return "—", "—"


def load_merge_prs() -> dict[str, str]:
    """Samee map: username (yar) -> #PR number, laga soo bilaabo merge commits."""
    prs: dict[str, str] = {}
    try:
        out = subprocess.check_output(
            ["git", "log", "--merges", "--format=%s"],
            cwd=REPO_ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return prs
    pattern = re.compile(r"Merge pull request #(\d+) from ([^/]+)/")
    for line in out.splitlines():
        m = pattern.search(line)
        if m:
            number, user = m.group(1), m.group(2).strip().lower()
            # Kaydi kii ugu horeeyay (kan ugu dambeeyay ee log-ga) — most recent first
            prs.setdefault(user, f"#{number}")
    return prs


def count_files(directory: Path) -> int:
    return sum(1 for p in directory.rglob("*") if p.is_file())


def main() -> int:
    if not SUBMISSIONS_DIR.is_dir():
        print(f"ERROR: lama helin folder-ka submissions: {SUBMISSIONS_DIR}")
        return 1

    pr_map = load_merge_prs()

    students = sorted(
        (d for d in SUBMISSIONS_DIR.iterdir() if d.is_dir()),
        key=lambda p: p.name.lower(),
    )

    submitted: list[dict] = []
    missing: list[str] = []

    for student in students:
        final_dir = find_final_project_dir(student)
        if final_dir is None:
            missing.append(student.name)
            continue
        author, date = git_last_commit(final_dir)
        pr = pr_map.get(student.name.lower(), "—")
        submitted.append(
            {
                "student": student.name,
                "folder": final_dir.name,
                "files": count_files(final_dir),
                "author": author,
                "date": date,
                "pr": pr,
            }
        )

    total_students = len(students)
    total_submitted = len(submitted)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = []
    lines.append("# 🎓 Warbixinta Final Project-ka")
    lines.append("")
    lines.append(
        "> Warbixintan si toos ah ayaa loo abuuray. Folder kasta oo halkan ku jira "
        "waxaa loola jeedaa in PR-kiisii la aqbalay (merged into `main`)."
    )
    lines.append("")
    lines.append(f"**La cusbooneysiiyay:** {generated}")
    lines.append("")
    lines.append("## 📊 Koobid")
    lines.append("")
    lines.append("| Tirakoob | Tiro |")
    lines.append("| --- | --- |")
    lines.append(f"| Wadarta ardayda submissions leh | {total_students} |")
    lines.append(f"| Gudbiyay final project (la aqbalay) | {total_submitted} |")
    lines.append(f"| Weli ma gudbin final project | {len(missing)} |")
    lines.append("")

    lines.append("## ✅ Ardayda Gudbisay Final Project-ka")
    lines.append("")
    if submitted:
        lines.append(
            "| # | Arday (GitHub) | Folder-ka Project-ka | Faylal | Qoraaga | Taariikhda | PR |"
        )
        lines.append("| --- | --- | --- | --- | --- | --- | --- |")
        for i, row in enumerate(submitted, start=1):
            lines.append(
                f"| {i} | `{row['student']}` | `{row['folder']}` | {row['files']} "
                f"| {row['author']} | {row['date']} | {row['pr']} |"
            )
    else:
        lines.append("_Weli ma jiraan arday gudbiyay._")
    lines.append("")

    lines.append("## ⏳ Weli Ma Gudbin")
    lines.append("")
    if missing:
        for name in missing:
            lines.append(f"- `{name}`")
    else:
        lines.append("_Dhammaan ardayda submissions leh waa gudbiyeen final project! 🎉_")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Warbixinta waa la abuuray: {REPORT_PATH}")
    print(f"     Gudbiyay: {total_submitted} / {total_students}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
