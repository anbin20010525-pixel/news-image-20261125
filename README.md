# Sum up 25 November's world news in one image

Entry for the make.fun bounty
[Sum up 25 November's world news in one image](https://make.fun/bounty/news-image-20261125)
($100, 50 winners, ends Fri, Nov 27, 2026, 12:00 AM UTC).

## What it is

`main.py` (Python 3.13, no network) copies the image this repository
holds (`entry.png`) to `/output/entry.png`. It is deterministic: every
run writes the same bytes.

## The image

`entry.png` — 1024×1024 PNG, 738,878 bytes (under the 1 MiB limit).
Title: "25 November 2026 — World News in One Image", six items:

1. Houthis attack Saudi Arabia's Ras Tanura oil refinery; a strike on a
   Riyadh skyscraper injured 11 people.
2. Two oil tankers hit naval mines in the Strait of Hormuz and caught
   fire, Iran's IRGC said.
3. China's Shenzhou-24 docks at Tiangong carrying Pakistan's first
   astronaut, Muhammad Zeeshan Ali.
4. US proposes new tariffs on 14 economies including China, the EU and
   India; S&P 500 down 2.2%.
5. Sudan RSF drone strikes kill 19 civilians in two cities.
6. Gaza: Israel kills Hamas interior security chief Mohammad Abuelouf.

## Run

```sh
python3 main.py
```

Writes `/output/entry.png`.
