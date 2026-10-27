"""Plot number of listed papers per year, stacked by technical direction and by modality.

Parses README.md and writes img/papers_by_year.png. Re-run after updating the list:
    python scripts/plot_paper_stats.py
"""
import re
from collections import Counter, OrderedDict
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
OUT = ROOT / "img" / "papers_by_year.png"

SECTIONS = OrderedDict([
    ("## 🏗️ Pretraining Biosignal Foundation Models from Scratch", "Pretraining from scratch"),
    ("## 🔄 Adapting Time Series Foundation Models to Biosignals", "Adapting TSFMs"),
    ("## 🤖 Leveraging Large Language Models for Biosignal Analysis", "Leveraging LLMs"),
])

MODALITIES = ["ECG", "EEG / MEG", "PPG", "IMU", "EMG", "Health metrics", "Multimodal", "Other / unspecified"]
COLORS = {  # categorical palette, fixed order; "Other" is neutral
    "ECG": "#2a78d6", "EEG / MEG": "#eb6834", "PPG": "#1baf7a", "IMU": "#eda100",
    "EMG": "#e87ba4", "Health metrics": "#008300", "Multimodal": "#6250d6", "Other / unspecified": "#a3a29b",
    "Pretraining from scratch": "#2a78d6", "Adapting TSFMs": "#eb6834", "Leveraging LLMs": "#1baf7a",
}

BADGE_MAP = {
    "ECG": "ECG", "EEG": "EEG / MEG", "MEG": "EEG / MEG", "iEEG": "EEG / MEG", "EOG": "EEG / MEG",
    "PPG": "PPG", "IMU": "IMU", "EMG": "EMG", "Health--metrics": "Health metrics",
}
KEYWORDS = [  # used when an entry has no modality badge (TSFM / LLM sections)
    ("ECG", r"\bECG|electrocardio|cardiac|heart"),
    ("EEG / MEG", r"\bEEG|\bMEG|brain|neural signal|electroenceph"),
    ("PPG", r"\bPPG|photoplethysmo"),
    ("IMU", r"\bIMU|accelerometer|activity|motion|trajector|smart ring"),
    ("EMG", r"\bEMG"),
    ("Health metrics", r"wearable|personal health|health insight|health prediction|health time series|glucose"),
]

entry_re = re.compile(r"^- \*\*\[([^\]]+?),\s*(\d{4})[^\]]*\]\*\*\s*(.+)$")
badge_re = re.compile(r"img\.shields\.io/badge/([A-Za-z\-]+?)-[a-z]+\"")


def modality(text):
    found = {BADGE_MAP[b] for b in badge_re.findall(text) if b in BADGE_MAP}
    other_badge = any(b not in BADGE_MAP for b in badge_re.findall(text))
    if not found and not other_badge:
        plain = re.sub(r"<[^>]+>|\[\[.*?\]\]\(.*?\)", " ", text)
        found = {m for m, pat in KEYWORDS if re.search(pat, plain, re.I)}
        if "sleep" in plain.lower() and not found:
            found = {"Multimodal"}
    if len(found) > 1 or (found and other_badge):
        # wearable health metrics + the signal they come from still count as one wearable modality
        return "Multimodal"
    return found.pop() if found else "Other / unspecified"


def parse():
    papers, seen, section = [], set(), None
    for line in README.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = SECTIONS.get(line.strip())
            continue
        m = entry_re.match(line)
        if not (section and m):
            continue
        title = re.split(r"<img|\[\[", m.group(3))[0].strip().rstrip("*").lower()
        if title in seen:  # same paper listed in two directions: keep the first
            continue
        seen.add(title)
        papers.append({"year": int(m.group(2)), "direction": section, "modality": modality(line)})
    return papers


def stacked(ax, papers, key, cats, title):
    years = list(range(min(p["year"] for p in papers), max(p["year"] for p in papers) + 1))
    counts = {c: Counter(p["year"] for p in papers if p[key] == c) for c in cats}
    bottom = [0] * len(years)
    for c in cats:
        vals = [counts[c][y] for y in years]
        if not any(vals):
            continue
        ax.bar(years, vals, bottom=bottom, width=0.6, color=COLORS[c], label=c,
               edgecolor="white", linewidth=2)
        bottom = [b + v for b, v in zip(bottom, vals)]
    for y, total in zip(years, bottom):
        ax.text(y, total + max(bottom) * 0.015, str(total), ha="center", va="bottom",
                fontsize=10, color="#3d3d3a")
    ax.set_title(title, loc="left", fontsize=12, color="#1f1f1d", pad=10)
    ax.set_xticks(years)
    ax.set_xlabel("Year")
    ax.legend(frameon=False, fontsize=9, loc="upper center", bbox_to_anchor=(0.5, -0.16),
              ncol=min(4, len(cats)), handlelength=1.2, columnspacing=1.2)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#c3c2b7")
    ax.tick_params(colors="#5c5b55")
    ax.yaxis.grid(True, color="#ebeae6", linewidth=0.8)
    ax.set_axisbelow(True)


def main():
    papers = parse()
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), sharey=True, facecolor="white")
    stacked(axes[0], papers, "direction", list(SECTIONS.values()), "By technical direction")
    stacked(axes[1], papers, "modality", MODALITIES, "By modality")
    axes[0].set_ylabel("Number of papers")
    fig.tight_layout()
    fig.savefig(OUT, dpi=200, facecolor="white")
    print(f"{len(papers)} papers -> {OUT.relative_to(ROOT)}")
    for k in ("direction", "modality"):
        print(k, Counter(p[k] for p in papers))


if __name__ == "__main__":
    main()
