# Gaming Tracker: Project Notes

Personal dashboard to finish games instead of growing the backlog.
**Read this first before changing anything.**

## Files
| Path | What |
|---|---|
| `tracker.html` | The whole dashboard: data, styling and logic in one file. Opened via the Desktop shortcut "Gaming Plan" (pinned tab in the browser). |
| `covers/<id>.jpg` | Box art per game id, downloaded from Wikipedia's REST API (`/api/rest_v1/page/summary/<Page>` → `originalimage`). Some are PNGs with a .jpg name, which is fine. |
| `~/.claude/skills/add-game/SKILL.md` | Skill for adding games / changing priority. The user gives game + platform only. |

## How it works
- **Data block** at the top of the `<script>` is the only part edited routinely:
  - `GAMES`: id → title, platform, hours, steps (chapters), `approx: true` if the chapter list isn't verified.
  - `SLOTS`: Main / Epic / Handheld / Snack, each with a `queue` (the first unfinished game is the active one) and `after` (what's next when the queue empties).
  - `RULES`, `PARKED` (backlog groups incl. "Coming soon").
- **Progress lives in browser localStorage** (key `gamingTracker.v1`), not in the file: ticks, chapter edits, notes, ratings, the message box, finished/dropped dates.
  - ⚠️ **Never rename a game id.** Progress is keyed by id.
  - Same browser always. There's a Download/Restore backup button at the bottom.
- **"Copy for Claude"** button: copies a `[Gaming tracker update]` text block (requests, ratings, active games + "left off" notes). The user pastes it into Claude Code. Claude can't read localStorage, so this block is the only way ratings and notes reach Claude.

## RDR2 companion
- `rdr2.html`: Hunt list / Pearson / Trapper / Legendary / Ledger tabs. Progress in localStorage key `rdr2Companion.v1`. Linked from the tracker via `companion: "rdr2.html"` on the GAMES entry (any game can get one).
- `rdr2-data.js` (`const RDR2 = {...}`, a JS file so it loads from file://): built from the Red Dead fandom wiki **API** via curl (the API works; normal pages return 402). Raw downloads in `rdr2-raw/`, rebuild with `python -I rdr2-scripts/build.py <output>`.
- Known gaps: 13 ledger prices are only in a wiki screenshot (`cost: null`, shown as "see ledger"). 3 entries are marked `verify` (Kit Satchel unlock, two "Perfect Bear Pelt" items: black bear or grizzly?).
- With nothing starred, the Hunt list shows Pearson items only.
- Phone/tablet version is wanted later. Idea: host the page so it opens on the phone, with progress sync TBD.

## Companion engine (all other games)
- `companion.html?game=<id>` loads `companions/<id>.js` (`const COMPANION = {...}`). Built by the `game-companion` skill (schema is in the skill).
- Section types: `checklist` (star / done / materials, optional `groupBy`, `tags` → filter buttons, `shopDefault`) and `tips`. A shopping-list tab appears automatically when any item has materials.
- Progress in localStorage key `companion.<id>.v1`. The cover comes from `covers/<id>.jpg`, and the accent from tracker slot colours 1-4.
- Raw wiki downloads in `companions/_raw/<id>/`, helper scripts in `companions/_scripts/<id>/`.

## Phone + sync
- Hosted on **GitHub Pages** from the user's **personal** GitHub account (not the Siemens one). The folder is a git repo (branch `main`); `.gitignore` skips raw wiki downloads. `index.html` redirects to `tracker.html`.
- `sync.js` (loaded first in every page's `<head>`) mirrors all localStorage keys starting with `gamingTracker.` / `rdr2Companion.` / `companion.` to one **secret Gist** (`gaming-plan-sync.json`, `{updatedAt, data}`). Last save wins. It notices saves by wrapping `localStorage.setItem`, so pages need no changes.
- Each device connects once via the **☁ Sync** button with a classic GitHub token (**gist scope only**). The token stays in that browser. The first device to connect creates the gist; later devices take the cloud copy.
- **Claude can read progress directly** (no paste needed): `curl -s https://api.github.com/gists/<sync id>`. Secret gists are readable by id. The sync id is kept in `.local/` (gitignored), never in published files.
- After editing files, publish with `git add -A && git commit -m "..." && git push` (Pages updates in ~1 min).

## Decisions
- **Max 4 active games**, one per slot, each tied to a moment (TV evening / chill TV / in bed / 20 min). Friends' online games aren't tracked.
- **Ratings** are Liked / Didn't like / Hated, used to reprioritise queues (e.g. hated a game → its sequel gets parked).
- **No "last played" indicator.** The user can take a long time per chapter, so it would nag unfairly.
- **No hours-played tracking.** Manual input kills trackers.
- **Colours** are the dataviz skill reference palette, slots 1–4 (blue/orange/aqua/yellow), light and dark mode. Text is never in series colours.
- **Web search is blocked** by company policy, and fandom wikis return 402. Wikipedia's API works (used for covers).

## Change log
- 2026-10-16: Created tracker (slots, chapter checklists, shelf, backup). Added Plan section (rules, parked, "after" per slot). Deleted plan.md. Created `add-game` skill + Desktop shortcut. GTA 6 → "Coming soon" (expected Nov 19, 2026, top priority for Epic slot on release). Added covers, "Where I left off" notes, ratings, "Message to Claude" box, this file.
- 2026-10-16: `add-game` skill extended: processes pasted update blocks, rating rules, auto cover download, change log. "Drop this game" is now a visible button.
- 2026-10-16: RDR2 companion (`rdr2.html` + `rdr2-data.js`): 24 Pearson, 123 Trapper, 16 legendary, 16 ledger entries. 🤠 Companion link on the RDR2 card.
- 2026-10-16: Generic companion engine `companion.html` + `game-companion` skill (wiki data + spoiler-free tips). Card button renamed 🧭 Companion.
- 2026-10-16: RDR2 Tips tab (`rdr2-tips.js`, 13 tips, separate file so rebuilds don't overwrite it). Alan Wake companion: 106 pages, 120 thermoses/clocks/games, 26 TV & radio, 67 chests/signs/cans, 14 tips (2 verify: radio-7, tv-lodge-bonus).
- 2026-10-16: Danganronpa companion: 14 Free Time (one per classmate, on purpose: per-classmate entry counts would hint at the plot), 14 gift lists, 28 skills, 14 tips. No hidden Monokumas (DR2/V3 only). 2 verify: Observation, Run On (PSP-only Free Time unlocks?).
- 2026-10-16: Hades companion: 31 keepsakes/companions, 24 aspects (Titan Blood per level → Resources tab), 55 prophecies (2 hidden as story spoilers), 12 mirror pairs, 13 tips. Late-game character + hidden aspects anonymised.
- 2026-10-16: game-companion skill: displayed-fields list, structural spoiler checklist, Python emoji note. "Copy for Claude" now sends a `Shelf:` list (all finished/dropped games + date + rating) instead of only rated games; add-game skill reads it and refills empty slots.
- 2026-10-16: Published to GitHub Pages (https://jprod96-wq.github.io/gaming-plan/, repo jprod96-wq/gaming-plan). Gist sync live (sync.js). Desktop shortcut now opens the website. Sync id stored in .local/sync-id.
- 2026-10-16: Skills now publish automatically (git push) and add-game reads synced progress directly ("check my tracker", mode C, with .local/processed.json). Message box hint updated.
- 2026-10-16: Redesign ("console launcher"): tracker slot cards with big cover hero + blurred art, swipeable carousel with dots on phones, bottom nav (Home/Plan/Shelf/Guides/Claude, hash-based views), companions list view. PWA: manifest.webmanifest, sw.js (network-first, offline fallback, never touches GitHub API), icons/ from tools/make_icons.py. Companion pages got mobile CSS (swipe tabs). Sync button top-right on phones.
- 2026-10-16: Mobile polish from real phone screenshots: cover below hero badges, short stat labels, cards fit content, compact sync button (time in panel), companion done buttons on own line, taller message box, nicer empty shelf.
- 2026-10-16: Home banners: "Almost there" (active game with highest %, Show jumps to slot) and release-day alerts. New data lists RELEASES (date countdown in Plan; GTA 6 moved here from PARKED) and WISHLIST (want: buy|play). add-game skill: releases, wishlist lines, "bought X", companion offer when a new game becomes active (.local/processed.json companionAsked).
- 2026-10-16: Wishlist + Control Resonant, Indiana Jones (both to buy, PS5). Plan tab redesign: rule tiles, per-slot Roadmap (now → queue → after, with covers + progress), Coming soon countdown cards, wishlist cover cards, parked backlog as chips. RELEASES/WISHLIST items take an optional `id` for covers/<id>.jpg (gta6, indiana, control-resonant added).
- 2026-10-19: DMC 5 Special Edition (PS5) → parked "Short (under 15h)" (Someday), from the message box.
- 2026-10-19: Phone fix: Plan tab no longer stretches sideways (roadmap/rules/plan grids use minmax(0,…)/min(…,100%) so cover strips scroll inside their row). RDR2 Hunt list + companion shopping list sorted alphabetically (cards used to jump when a material was ticked, looking like both were removed); RDR2 "Got it" toast has Undo, "Got 1" when qty > 1.
