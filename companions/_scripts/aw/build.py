"""Build companions/aw.js from parsed.json. Usage: build.py PARSED OUTJS"""
import json, re, sys

P, OUT = sys.argv[1], sys.argv[2]
d = json.load(open(P, encoding="utf-8"))

EP = {"1": "Episode 1: Nightmare", "2": "Episode 2: Taken", "3": "Episode 3: Ransom",
      "4": "Episode 4: The Truth", "5": "Episode 5: The Clicker", "6": "Episode 6: Departure"}
WORDNUM = {"One": "1", "Two": "2", "Three": "3", "Four": "4", "Five": "5", "Six": "6"}

def ep(raw):
    m = re.match(r"Episode (\w+)", raw or "")
    n = WORDNUM.get(m.group(1), m.group(1))
    return EP[n]

def fix(s):
    s = s.replace("�", "'").replace("’", "'").strip()
    s = s.rstrip(",. ")
    s = re.sub(r"^(On|In|Inside|At|Next to|Behind) the the ", r"\1 the ", s)
    s = s.replace("the the ", "the ").replace("bellow", "below").replace("caravana", "caravan")
    s = s.replace("in a dead of the hedge maze", "in a dead end of the hedge maze")
    s = s.replace("an dead end", "a dead end").replace("On the hedge maze", "In the hedge maze")
    return s

# Spoiler-safe / cleaned location overrides: (section, number) -> text
LOC = {
    ("pages", 1): "Given automatically at the start of the section",
    ("pages", 2): "Given automatically at the start of the section",
    ("pages", 30): "On the trail back to the hilltop cabin, after a phone call",
    ("pages", 41): "On a tree stump, after a phone call",
    ("pages", 44): "Down the road near the fallen trees, after the police car is thrown",
    ("pages", 58): "Bottom of the cave tunnel in the Old Silver Mine, near the flooded shaft",
    ("pages", 62): "Handed to you during a conversation in the Cauldron Lake Lodge",
    ("pages", 74): "Lying on the path leading to Walter Snyder's cabin",
    ("pages", 82): "In the cell corridor of the Bright Falls Sheriff Station",
    ("pages", 83): "In the cell corridor of the Bright Falls Sheriff Station",
    ("pages", 32): "Picnic area right of the Lovers' Peak trail, after the bridge, near the waterfall vista",
    ("thermos", 56): "Inside the gazebo in the lodge garden",
    ("thermos", 100): "Final area: shine the flashlight on the word \"thermos\" next to the sofa",
    ("chests", 11): "Inside a small dilapidated cottage, after a phone call",
    ("nsgames", 4): "On the roof of the rotating cabin (light the word \"cabin\" to make it appear)",
    ("nsgames", 7): "On the ground near a rusty ship, after climbing down the uprooted tree",
    ("pages", 33): "Behind a log at the cliff edge above the old mill, after the bear-trap path",
    ("pages", 45): "Cliff edge above the small river gorge, past the old wooden bridge near a safe haven",
    ("thermos", 11): "Behind rocks on the promontory near the generator safe haven, between camps 2 and 3",
    ("clocks", 3): "Blue armchair in the church basement, between the broken stairs and exit ladder",
    ("clocks", 5): "In the red-and-white circus tent with the word \"Boom!\", near the end of the railway",
    ("radio", 8): "Small abandoned shack by the broken bridge on the road to the Coal Mine Museum",
    ("chests", 3): "Wooden shed with a rusted pickup, behind the safe-haven shed after the second camp",
    ("cans", 4): "Picnic table by an abandoned caravan and safe haven, in the pasture left of the road back to the Visitor Center",
    ("cans", 7): "Low wall of the pergola walkway in the lodge garden, after passing under the bridge",
}

def loc(sec, n, raw):
    return LOC.get((sec, n), fix(raw))

def item(**kw):
    return {k: v for k, v in kw.items() if v not in (None, "", [])}

# 1. Manuscript pages
pages = []
for r in d["pages"]:
    n = int(r["#"]); e = ep(r["_episode"])
    tags = ["Nightmare only" if r["Difficulty"] == "Nightmare" else "All difficulties"]
    if e == EP["6"]: tags.append("Late game")
    tip = None
    if n in (1, 2, 62): tip = "Unmissable"
    if r["Difficulty"] == "Nightmare": tip = "Only appears on Nightmare difficulty"
    pages.append(item(id=f"page-{n}", name=f"Page {n}", tags=tags, episode=e,
                      location=loc("pages", n, r["Location"]), note=f"Area: {r['Section']}"))

# 2. Thermoses + special replacements
thermos = []
for r in d["thermos"]:
    n = int(r["#"]); e = ep(r["_episode"])
    tags = ["Thermos"] + (["Late game"] if e == EP["6"] else [])
    thermos.append(item(id=f"thermos-{n}", name=f"Thermos {n}", tags=tags, episode=e,
                        location=loc("thermos", n, r["Location"]), note="Area: final area" if n == 100 else f"Area: {r['Section']}"))
for r in d["clocks"]:
    n = int(r["#"])
    it = item(id=f"clock-{n}", name=f"Alarm clock {n}", tags=["Alarm clock"], episode="The Signal",
              location=loc("clocks", n, r["Location"]), tip="Listen for ticking nearby")
    if n == 1:
        it["note"] = "Wiki: clocks occasionally fail to spawn; reload the last checkpoint"
    thermos.append(it)
for r in d["nsgames"]:
    n = int(r["#"])
    thermos.append(item(id=f"nsgame-{n}", name=f"Night Springs game {n}", tags=["Night Springs game"],
                        episode="The Writer", location=loc("nsgames", n, r["Location"]),
                        tip="Listen for a menu-style sound cue"))

# 3. TV + radio
media = []
for r in d["tv"]:
    n = int(r["#"]); e = ep(r["_episode"]); name = fix(r["Name"])
    if name.startswith("Writer in the Cabin"):
        tag, tip = "Writer in the Cabin", "TV turns on by itself"
    elif "Harry Garrett" in name:
        tag, tip = "Talk show", "Required to progress"
    else:
        tag, tip = "Night Springs", "Turn the TV on yourself"
    tags = ["TV", tag] + (["Late game"] if e == EP["6"] else [])
    media.append(item(id=f"tv-{n}", name=name, tags=tags, episode=e,
                      location=loc("tv", n, r["Location"]), tip=tip))
media.append(item(id="tv-lodge-bonus", name="Lodge bonus TV (2 Night Springs eps)", tags=["TV", "Night Springs"],
                  episode=EP["4"], location="A separate TV in the Cauldron Lake Lodge",
                  note="Remastered only; counts for Boob Tube, not Couch Potato. Exact spot not given on wiki",
                  verify=True))
for r in d["radio"]:
    n = int(r["#"]); name = fix(r["Name"])
    it = item(id=f"radio-{n}", name=name, tags=["Radio"], episode=ep(r["_episode"]),
              location=loc("radio", n, r["Location"]), tip="You don't need to hear it fully")
    if n == 7:
        it["tip"] = "Unmissable"
        it["note"] = "Wiki lists it as #7 of 11, but trivia says it does not count for the KBF-FM trophy"
        it["verify"] = True
    media.append(it)

# 4. Chests, signs, cans
misc = []
for r in d["chests"]:
    n = int(r["#"]); e = ep(r["_episode"])
    misc.append(item(id=f"chest-{n}", name=f"Chest {n}", tags=["Chest"] + (["Late game"] if e == EP["6"] else []),
                     episode=e, location=loc("chests", n, r["Location"]), note="Contains: " + fix(r["Content"]),
                     tip="Follow the light-paint arrows"))
seen7 = False
for r in d["signs"]:
    n = int(r["#"]); e = ep(r["_episode"])
    if n == 7:
        if seen7: continue
        seen7 = True
        misc.append(item(id="sign-7", name="Coal Mine Museum plaques", tags=["Sign"], episode=e,
                         location="Bright Falls Coal Mine Museum (3 plaques: tunnel, display cabinet, main building)",
                         note="The three plaques count as one sign; reading one is enough"))
        continue
    it = item(id=f"sign-{n}", name=fix(r["Name"]), tags=["Sign"] + (["Late game"] if e == EP["6"] else []),
              episode=e, location=loc("signs", n, r["Location"]))
    if n == 2: it["note"] = "Two posters count as one sign"
    misc.append(it)
for r in d["cans"]:
    n = int(r["#"]); e = ep(r["_episode"])
    misc.append(item(id=f"cans-{n}", name=f"Can pyramid {n}", tags=["Can pyramid"] + (["Late game"] if e == EP["6"] else []),
                     episode=e, location=loc("cans", n, r["Location"]), tip="Shoot it down"))
order = {"Chest": 0, "Sign": 1, "Can pyramid": 2}
epi = list(EP.values())
misc.sort(key=lambda x: (epi.index(x["episode"]), order[x["tags"][0]]))
media.sort(key=lambda x: (epi.index(x["episode"]), 0 if "TV" in x["tags"] else 1))
ext = ["The Signal", "The Writer"]
thermos.sort(key=lambda x: (epi + ext).index(x["episode"]))

tips = [
    {"title": "Burn, then shoot", "text": "Taken are shielded by darkness. Hold the flashlight on them (boost it to speed this up) until the halo shrinks and the shield breaks, then shoot.", "tag": "Combat"},
    {"title": "Dodge at the last moment", "text": "Dodge just as an enemy swings to dodge; well-timed dodges trigger a slow-motion camera. Dodging is often better than backing away.", "tag": "Combat"},
    {"title": "Flashbangs for crowds", "text": "A flashbang destroys every Taken in its large blast radius instantly. Throw it just before you get surrounded.", "tag": "Combat"},
    {"title": "Flares buy space", "text": "Holding or dropping a flare keeps Taken back and drains their shields. It is your best tool against possessed objects and for escaping a mob.", "tag": "Combat"},
    {"title": "Flare gun = panic button", "text": "The flare gun instantly kills Taken in its blast. Save it for big groups or tough enemies; chests often refill it.", "tag": "Resources"},
    {"title": "Let batteries recharge", "text": "Your flashlight slowly recharges when not boosted. Swap in a fresh battery only when you need full power mid-fight.", "tag": "Resources"},
    {"title": "Run for the light", "text": "Streetlights are safe havens: standing in one heals you, clears nearby Taken and usually acts as a checkpoint. Sometimes sprinting to the next one beats fighting.", "tag": "Survival"},
    {"title": "Follow the yellow paint", "text": "Shine your flashlight around to reveal light-sensitive arrows and torch symbols. They lead to supply chests just off the main path.", "tag": "Collectibles"},
    {"title": "Turn on every TV and radio", "text": "Night Springs TVs and radios only count if you interact with them, so check sheds, cabins and huts as you go.", "tag": "Collectibles"},
    {"title": "Use episode select", "text": "Missed something? Replay any episode from the menu to mop up collectibles; collectibles you already found stay counted.", "tag": "Collectibles"},
    {"title": "Listen for the specials' collectibles", "text": "Alarm clocks (The Signal) tick and Night Springs games (The Writer) play a sound cue when you are close.", "tag": "Collectibles"},
    {"title": "Words in the specials", "text": "In The Signal and The Writer, shining the flashlight on floating words makes them real - including ammo, flares and handy objects.", "tag": "Specials"},
    {"title": "Nightmare unlocks extra pages", "text": "15 manuscript pages only appear on Nightmare difficulty, which unlocks after you finish the game once. Use episode select to hunt them.", "tag": "Nightmare"},
    {"title": "Nightmare needs patience", "text": "On Nightmare, Taken take more light and bullets. Fight near light sources, keep flashbangs for groups and don't waste flare gun shots.", "tag": "Nightmare"},
]

COMPANION = {
    "id": "aw", "title": "Alan Wake Remastered", "source": "alanwake.fandom.com", "accent": 1,
    "sections": [
        {"id": "pages", "label": "📄 Manuscript pages", "type": "checklist", "doneLabel": "Found",
         "hint": "106 pages (15 Nightmare only). Specials have no pages", "groupBy": "episode", "items": pages},
        {"id": "thermos", "label": "☕ Thermoses & clocks", "type": "checklist", "doneLabel": "Found",
         "hint": "100 thermoses; The Signal uses alarm clocks, The Writer Night Springs games", "groupBy": "episode", "items": thermos},
        {"id": "media", "label": "📺 TV & radio shows", "type": "checklist", "doneLabel": "Watched / heard",
         "hint": "Interact with TVs and radios to collect them. None in the specials", "groupBy": "episode", "items": media},
        {"id": "misc", "label": "🧰 Chests, signs & cans", "type": "checklist", "doneLabel": "Found",
         "hint": "30 chests, 25 signs, 12 can pyramids", "groupBy": "episode", "items": misc},
        {"id": "tips", "label": "💡 Tips", "type": "tips", "hint": "Spoiler-free", "items": tips},
    ],
}

js = "const COMPANION = " + json.dumps(COMPANION, ensure_ascii=False, indent=2) + ";\n"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(js)
for s in COMPANION["sections"]:
    print(s["id"], len(s["items"]))
