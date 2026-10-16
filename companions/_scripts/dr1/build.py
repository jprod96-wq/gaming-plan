import json, re, os, sys

RAW = sys.argv[1]
OUT = sys.argv[2]
students = ["Aoi Asahina", "Byakuya Togami", "Celestia Ludenberg", "Chihiro Fujisaki", "Hifumi Yamada",
            "Junko Enoshima", "Kiyotaka Ishimaru", "Kyoko Kirigiri", "Leon Kuwata", "Mondo Owada",
            "Sakura Ogami", "Sayaka Maizono", "Toko Fukawa", "Yasuhiro Hagakure"]
HG = "Hangman's Gambit"
# skill: (student, cost, effect, used in)
skills = {
    "Extraordinary Focus": ("Aoi Asahina", "2 SP", "Focus Gauge +2", "Class Trial"),
    "Ambidextrousness": ("Aoi Asahina", "4 SP", "Lock on to two statements at once", "Bullet Time Battle"),
    "Cool and Composed": ("Byakuya Togami", "2 SP", "Steadies your aim a little", "Nonstop Debate, " + HG),
    "Envious Influence": ("Byakuya Togami", "4 SP", "Influence Gauge +5", "Class Trial"),
    "Raise": ("Celestia Ludenberg", "Passive", "Triples Monocoins found in School Life; +10% Monocoins after trials", "School Life, Class Trial"),
    "Menacing Focus": ("Celestia Ludenberg", "4 SP", "Focus Gauge +5", "Class Trial"),
    "Algorithm": ("Chihiro Fujisaki", "2 SP", "Memorize statements faster", "Nonstop Debate"),
    "Cheat Code": ("Chihiro Fujisaki", "2 SP", "Timer doesn't drop when you shoot with the silencer", "Nonstop Debate"),
    "Handiwork": ("Hifumi Yamada", "4 SP", "Reload two bullets at once", "Bullet Time Battle"),
    "Delusion": ("Hifumi Yamada", "5 SP", "Influence Gauge recovers during concentration and Fever Time", "Nonstop Debate, " + HG + ", Bullet Time Battle"),
    "Trance": ("Junko Enoshima", "4 SP", "Focus Gauge recovers faster", "Nonstop Debate, " + HG + ", Bullet Time Battle"),
    "Charisma": ("Junko Enoshima", "5 SP", "More Influence Gauge recovery on correct answers", "Class Trial"),
    "Attentive Influence": ("Kiyotaka Ishimaru", "2 SP", "Influence Gauge +2", "Class Trial"),
    "Steel Patience": ("Kiyotaka Ishimaru", "3 SP", "Less Influence damage when you miss", "Nonstop Debate, " + HG + ", Bullet Time Battle, Closing Argument"),
    "Neural Liberation": ("Kyoko Kirigiri", "5 SP", "Focus Gauge drains slower during concentration and Fever Time", "Nonstop Debate, " + HG + ", Bullet Time Battle"),
    "Robot Jock": ("Leon Kuwata", "3 SP", "Faster Truth Bullet rate of fire", "Nonstop Debate, Bullet Time Battle"),
    "Kinetic Depth Perception": ("Leon Kuwata", "2 SP", "Concentration auto-targets the weak spot", "Nonstop Debate"),
    "Downshift": ("Mondo Owada", "1 SP", "Slower aim speed", "Nonstop Debate, " + HG),
    "Upshift": ("Mondo Owada", "1 SP", "Faster aim speed", "Nonstop Debate, " + HG),
    "Breathing Technique": ("Sakura Ogami", "4 SP", "Focus Gauge recovers faster", "Nonstop Debate, " + HG + ", Bullet Time Battle"),
    "Tranquility": ("Sakura Ogami", "3 SP", "Completely steadies your aim", "Nonstop Debate, " + HG),
    "Melodious Voice": ("Sayaka Maizono", "3 SP", "More damage when a statement is destroyed", "Bullet Time Battle"),
    "Vocabulary": ("Toko Fukawa", "4 SP", "Larger bullet capacity", "Bullet Time Battle"),
    "Crystal Prediction": ("Yasuhiro Hagakure", "5 SP", "Cuts an argument to three statements or fewer", "Nonstop Debate, Bullet Time Battle"),
    "Lost in Thought": ("Yasuhiro Hagakure", "3 SP", "Longer time limit for each phase", "Class Trial"),
}


def kebab(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def first(s):
    return s.split()[0]


# ---- Free Time
ft = []
for st in students:
    for k, v in skills.items():
        if v[0] != st:
            continue
        ft.append({"id": kebab(first(st) + "-" + k), "name": f"{st}: {k}", "tags": ["Skill"], "student": st,
                   "note": f"Free Time unlocks {k} ({v[1]}): {v[2]}."})
    ft.append({"id": kebab(first(st) + "-all-events"), "name": f"{st}: all events seen", "tags": ["Report card"],
               "student": st, "tip": "Report card complete = every event with this classmate seen."})

# ---- Gifts (parsed from raw wiki pages)
UNIVERSAL = {"Hope's Peak Ring", "The Funplane"}


def clean(lst):
    out = []
    for x in lst.split(','):
        x = x.replace('�', ' ').replace('\xa0', ' ')
        x = re.sub(r'^\s*\d+\.\s*', '', x).strip()
        x = x.replace("Prince Shotoku's Guide", "Prince Shotoku's Globe").replace("T-shirt", "T-Shirt")
        x = re.sub(r'<[^>]*>|\[\[|\]\]|\{\{|\}\}', '', x)
        if x:
            out.append(x)
    return out


gifts = []
for st in students:
    t = open(os.path.join(RAW, "fte_" + st.replace(' ', '_') + ".txt"), encoding='utf-8').read()
    lv = clean(re.search(r"'''Loves:'''\s*\n\|[^|]*\|(.*)", t).group(1))
    lk = [x for x in clean(re.search(r"'''Likes:'''\s*\n\|[^|]*\|(.*)", t).group(1)) if x not in UNIVERSAL]
    more = ""
    if len(lk) > 8:
        more = f" (+{len(lk) - 8} more)"
        lk = lk[:8]
    gifts.append({"id": kebab(first(st) + "-gifts"), "name": st, "student": st,
                  "note": "Loves: " + ", ".join(lv), "tip": "Likes: " + ", ".join(lk) + more})

# ---- Skills
sk = []
for k in sorted(skills):
    st, cost, eff, when = skills[k]
    tags = ["Free Time"] + [w.strip() for w in when.split(',')]
    tags = list(dict.fromkeys(tags))
    sk.append({"id": kebab(k), "name": f"{k} ({cost})", "tags": tags, "requires": f"Free Time with {st}",
               "note": eff + "."})
sk.append({"id": "trigger-happy", "name": "Trigger Happy (3 SP)", "tags": ["Free Time", "Nonstop Debate", "Bullet Time Battle"],
           "requires": "Free Time (unlocks later in the story)", "note": "Shorter delay between Truth Bullet shots."})
for k, eff in (("Observation", "Mark objects you can investigate in School Life (R button)."),
               ("Run On", "Hold Circle to move faster in School Life.")):
    sk.append({"id": kebab(k), "name": f"{k} (no cost)", "tags": ["Default", "School Life"],
               "requires": "Unlocked from the start",
               "note": eff + " Wiki: a Free Time unlock on the original PSP only; later versions start with it.",
               "verify": True})

tips = [
    {"title": "Spread your Free Time", "text": "Spread Free Time across classmates early: you can't always come back later.", "tag": "Free Time"},
    {"title": "Free Time builds your skills", "text": "Free Time events unlock skills and earn Skill Points (SP). Equip skills before a trial; their total cost can't exceed your SP.", "tag": "Free Time"},
    {"title": "Safe gifts for anyone", "text": "Hope's Peak Ring and The Funplane are liked by every classmate. Save rarer items for whoever loves them.", "tag": "Gifts"},
    {"title": "Sad face = no event", "text": "A classmate with a sad face icon won't start a Free Time event, though you can still give them gifts.", "tag": "Free Time"},
    {"title": "Hunt for Monocoins", "text": "Examine objects during School Life: many hide Monocoins, and the spots change every chapter.", "tag": "Monocoins"},
    {"title": "Get Raise from Celestia", "text": "Celestia's Free Time unlocks Raise, a free passive that triples Monocoins found in School Life and adds 10% after trials.", "tag": "Monocoins"},
    {"title": "Trials pay out too", "text": "After each trial you get 1 Monocoin per 10 points of your grade.", "tag": "Monocoins"},
    {"title": "MonoMono Machine", "text": "Spend Monocoins at the MonoMono Machine in the school store for random presents. Check the Gifts tab before handing them out.", "tag": "MonoMono"},
    {"title": "Nonstop Debate", "text": "Shoot White Noise to gain time, but hitting it while aiming at a weak point costs time. Later debates let you absorb statements as new Truth Bullets.", "tag": "Class trial"},
    {"title": "Hangman's Gambit", "text": "Shoot the floating letters to spell the key word. Wrong letters cost Influence, so don't rush.", "tag": "Class trial"},
    {"title": "Bullet Time Battle", "text": "It's a rhythm game: staying on the beat locks on and reloads. When the gauge is empty, fire the right Truth Bullet to finish.", "tag": "Class trial"},
    {"title": "Closing Argument", "text": "Rebuild the case as a comic. Not every panel in the pool belongs, so walk through the timeline before placing.", "tag": "Class trial"},
    {"title": "Tune the difficulty", "text": "Action and Logic difficulty are set separately. Lower Action if the minigames frustrate you, without making the mystery easier.", "tag": "General"},
    {"title": "Bonus School Mode", "text": "Clearing the story unlocks School Mode, a bonus mode with extra time to bond with classmates.", "tag": "General"},
]

C = {"id": "dr1", "title": "Danganronpa: Trigger Happy Havoc", "source": "danganronpa.fandom.com", "accent": 3, "sections": [
    {"id": "freetime", "label": "💬 Free Time", "type": "checklist", "doneLabel": "Seen",
     "hint": "Skills and report cards earned by spending Free Time with classmates.", "groupBy": "student", "items": ft},
    {"id": "gifts", "label": "🎁 Gift favorites", "type": "checklist", "doneLabel": "Given",
     "hint": "Loved and liked MonoMono presents (Ring and Funplane suit everyone).", "items": gifts},
    {"id": "skills", "label": "🧠 Skills", "type": "checklist", "doneLabel": "Unlocked",
     "hint": "Equip before trials; cost in SP.", "items": sk},
    {"id": "tips", "label": "💡 Tips", "type": "tips", "hint": "Spoiler-free", "items": tips}]}

for s in C["sections"]:
    if s["type"] == "checklist":
        ids = [i["id"] for i in s["items"]]
        assert len(ids) == len(set(ids)), s["id"]
        tags = {t for i in s["items"] for t in i.get("tags", [])}
        print(s["id"], len(ids), "items, tags:", len(tags))
    else:
        print(s["id"], len(s["items"]))
open(OUT, "w", encoding="utf-8").write("const COMPANION = " + json.dumps(C, ensure_ascii=False, indent=1) + ";\n")
