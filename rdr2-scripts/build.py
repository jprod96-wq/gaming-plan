import json, re, sys

def kebab(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower().replace("'", '')).strip('-')

# ---------- material -> animal mapping ----------
LEG_PELT = {
    "Legendary Bear Pelt": "Legendary Bharati Grizzly Bear",
    "Legendary Beaver Pelt": 'Legendary Beaver "Malia"',
    "Legendary Ram Hide": "Legendary Bighorn Ram",
    "Legendary Boar Pelt": 'Legendary Boar "Oryx"',
    "Legendary Buck Pelt": 'Legendary Buck "Obie"',
    "Legendary Coyote Pelt": 'Legendary Coyote "Suki"',
    "Legendary Elk Pelt": 'Legendary Elk "Enyeto"',
    "Legendary Fox Pelt": 'Legendary Fox "Layla"',
    "Legendary Moose Pelt": 'Legendary Moose "Anoki"',
    "Legendary White Bison Pelt": "Legendary White Bison",
    "Legendary Wolf Pelt": 'Legendary Wolf "Hotah"',
    "Legendary Panther Pelt": "Legendary Giaguaro Panther",
    "Legendary Alligator Skin": 'Legendary Bullgator "Lacartus"',
    "Legendary Cougar Pelt": "Legendary Cougar",
    "Legendary Pronghorn Hide": 'Legendary Pronghorn "Ira"',
    "Legendary Tatanka Bison Pelt": "Legendary Tatanka Bison",
}
WORD_ANIMAL = {
    "Ram": "Bighorn Ram", "Cow": "Cow", "Bull": "Bull", "Ox": "Ox", "Goat": "Goat", "Sheep": "Sheep",
    "Pig": "Pig", "Collared Peccary Pig": "Collared Peccary", "Black Bear": "Black Bear", "Bear": "Bear",
    "Seagull": "Seagull", "Cedar Waxwing": "Waxwing", "Gila Monster": "Gila Monster", "Blue Jay": "Blue Jay",
}

def animal_for(item):
    if item in LEG_PELT:
        return LEG_PELT[item]
    m = re.match(r'(?:Perfect )?(.+?) (Pelt|Hide|Skin|Carcass|Feather|Antlers?)$', item)
    if not m:
        return None
    base = m.group(1)
    return WORD_ANIMAL.get(base, base)

def mats(spec):
    """spec: 'Item x2; Item2' -> list of material dicts"""
    out = []
    for part in [p.strip() for p in spec.split(';') if p.strip()]:
        m = re.match(r'(.+?)\s+x(\d+)$', part)
        item, qty = (m.group(1), int(m.group(2))) if m else (part, 1)
        out.append({"item": item, "qty": qty, "animal": animal_for(item)})
    return out

# ---------- PEARSON ----------
pearson = []
LWT = "Leatherworking Tools"
satchels = [
    # name, materials, unlock, fence price (epilogue)
    ("Tonics Satchel", "Perfect Deer Pelt; Perfect Buck Pelt; Perfect Elk Pelt", "Upgrade Medicine Wagon twice", 18.00, "More tonics."),
    ("Ingredients Satchel", "Perfect Deer Pelt; Perfect Badger Pelt; Perfect Squirrel Pelt", "Donate 5 carcasses to Pearson", 23.85, "More cooking/crafting ingredients."),
    ("Kit Satchel", "Perfect Deer Pelt; Perfect Elk Pelt; Perfect Panther Pelt", "None (or donate 3 valuables?)", 13.50, "More kit items."),
    ("Provisions Satchel", "Perfect Deer Pelt; Perfect Bison Pelt; Perfect Raccoon Pelt", "Upgrade Provisions Wagon twice", 23.85, "More provisions."),
    ("Materials Satchel", "Perfect Deer Pelt; Perfect Boar Pelt; Perfect Iguana Skin", "Craft 3 recipes at Scout Fire", 26.10, "More materials."),
    ("Valuables Satchel", "Perfect Deer Pelt; Perfect Beaver Pelt; Perfect Rabbit Pelt", "Donate $50 cash to camp", 22.00, "More valuables."),
    ("Legend of the East Satchel", "Perfect Deer Pelt; Perfect Cougar Pelt; Perfect Wolf Pelt", "Craft all other satchels", 150.00, "Most items to 99."),
]
for name, spec, unlock, fence, eff in satchels:
    e = {"id": kebab(name), "name": name, "category": "Satchel", "materials": mats(spec),
         "requires": f"{LWT}; {unlock}" if not unlock.startswith("None") else f"{LWT}",
         "note": f"{eff} Epilogue: buy at fence ${fence:.2f}."}
    if name == "Kit Satchel":
        e["verify"] = True
        e["note"] = ("Pearson page: no unlock needed; Satchel page: donate 3 valuables. "
                     f"Epilogue: fence ${fence:.2f}.")
    pearson.append(e)

decor = [
    # name, area, materials, needs LWT
    ("Alligator Skull", "Arthur's tent", "Perfect Alligator Skin", False),
    ("Big Horn Ram Skull", "Arthur's tent", "Perfect Ram Carcass", False),
    ("Cougar Pelt Covered Chest", "Arthur's tent", "Perfect Cougar Pelt x2", True),
    ("Boar Skin Table", "Arthur's tent", "Perfect Boar Pelt", True),
    ("Ox Hide Rug", "Arthur's tent", "Perfect Ox Hide x2", False),
    ("Boar Skin Rug", "John's tent", "Perfect Boar Pelt x4", False),
    ("Pronghorn Leather Table Tops", "Camp tables", "Perfect Pronghorn Hide x2", True),
    ("Pronghorn Skull", "Chuckwagon", "Perfect Pronghorn Carcass", False),
    ("Moose Antlers", "Main campfire", "Moose Antler", False),
    ("Wolf Skull", "Main campfire", "Perfect Wolf Carcass", False),
    ("Snake Skin Banjo Head", "Main campfire", "Perfect Snake Skin x2", True),
    ("Campfire Seat Cover", "Main campfire", "Perfect Beaver Pelt; Perfect Muskrat Pelt; Perfect Fox Pelt", False),
    ("Campfire Log Seat Cover", "Main campfire", "Perfect Wolf Pelt x2", False),
    ("Lean-to Cow Hide Ground Cover", "Main campfire", "Perfect Cow Hide", False),
    ("Scout Fire Ground Covers", "Scout campfire", "Perfect Goat Hide x2", False),
    ("Elk Antlers", "Scout campfire", "Elk Antlers", False),
    ("Hanging Bones", "Scout campfire", "Buck Antlers", False),
]
for name, area, spec, lwt in decor:
    pearson.append({"id": kebab(name), "name": name, "category": "Camp", "materials": mats(spec),
                    "requires": LWT if lwt else "", "note": f"Decor: {area}."})

# ---------- TRAPPER ----------
def cat(name):
    n = name.lower()
    if "saddle" in n: return "Saddle"
    if "accessory" in n: return "Accessory"
    if "gloves" in n: return "Gloves"
    if "chaps" in n: return "Chaps"
    if "vest" in n: return "Vest"
    if any(w in n for w in ("boots", "moccasins", "fowlers")): return "Boots"
    if any(w in n for w in ("coat", "jacket", "cloak", "roper")): return "Coat"
    if any(w in n for w in ("hat", "cap", "sombrero")): return "Hat"
    return "Other"

TRAPPER_SETS = {
 "Bear Hunter": [("Legendary Bear Head Hat",40,"Legendary Bear Pelt"),("Legendary Bear Coat",28,"Legendary Bear Pelt; Perfect Bison Pelt"),("Legendary Bear Roper",34,"Legendary Bear Pelt; Perfect Bull Hide"),("Boar Riding Gloves",15,"Perfect Boar Pelt; Perfect Rabbit Pelt x2")],
 "Trophy Buck": [("Raccoon Mountain Hat",21,"Perfect Beaver Pelt; Perfect Raccoon Pelt; Hawk Feather x2"),("Legendary Buck Vest",26,"Legendary Buck Pelt; Perfect Ram Hide"),("Legendary Fox Moccasins",40,"Legendary Fox Pelt; Perfect Elk Pelt"),("Legendary Buck & Fox Range Gloves",28,"Legendary Buck Pelt; Legendary Fox Pelt")],
 "Dreamcatcher": [("Legendary Beaver Flop Hat",22,"Legendary Beaver Pelt; Legendary Boar Pelt; Cardinal Feather"),("Legendary Bison Vest",30,"Legendary Tatanka Bison Pelt"),("Legendary Bison Batwing Chaps",32,"Legendary Tatanka Bison Pelt"),("Legendary Boar & Bison Fowlers",37,"Legendary Boar Pelt; Legendary Tatanka Bison Pelt"),("Legendary Beaver Cavalry Gloves",18,"Legendary Beaver Pelt")],
 "Beast of Prey": [("Legendary Cougar Flop Hat",19,"Legendary Cougar Pelt; Turkey Feather x2"),("Legendary Cougar & Wolf Vest",42,"Legendary Cougar Pelt; Legendary Wolf Pelt"),("Legendary Wolf Batwing Chaps",34,"Legendary Wolf Pelt; Perfect Goat Hide"),("Bull Fowler Boots",29,"Perfect Boar Pelt; Perfect Bull Hide"),("Legendary Cougar Riding Gloves",20,"Legendary Cougar Pelt; Perfect Boar Pelt")],
 "Huntsman": [("Legendary Coyote Mountain Hat",23,"Legendary Coyote Pelt; Eagle Feather x2"),("Legendary Pronghorn Coat",35,"Legendary Pronghorn Hide; Perfect Moose Pelt"),("Legendary Coyote Half Chaps",20,"Legendary Coyote Pelt; Perfect Fox Pelt x2"),("Workman's Pride Boots",28,"Perfect Cow Hide; Perfect Goat Hide"),("Legendary Pronghorn Range Gloves",17,"Legendary Pronghorn Hide; Perfect Muskrat Pelt")],
 "Death Roll": [("Legendary Alligator Gambler's Hat",22,"Legendary Alligator Skin; Perfect Snake Skin x2"),("Legendary Panther Cloak",45,"Legendary Panther Pelt"),("Legendary Alligator Vest",35,"Legendary Alligator Skin"),("Legendary Alligator Fowlers",35,"Legendary Alligator Skin"),("Legendary Panther Range Gloves",30,"Legendary Panther Pelt; Perfect Gila Monster Skin")],
 "Stalker": [("Legendary Ram Hat",17,"Legendary Ram Hide"),("Legendary Moose Hunting Jacket",24,"Legendary Moose Pelt; Perfect Wolf Pelt"),("Legendary Ram Batwing Chaps",33,"Legendary Ram Hide"),("Legendary Moose Moccasins",22,"Legendary Moose Pelt; Perfect Cow Hide"),("Legendary Ram Rifleman Gloves",12,"Legendary Ram Hide; Perfect Boar Pelt")],
 "Ghost Bison": [("Legendary White Bison Hat",45,"Legendary White Bison Pelt"),("Legendary White Bison Coat",29,"Legendary White Bison Pelt"),("Legendary Elk Half Chaps",16,"Legendary Elk Pelt; Perfect Sheep Hide"),("Legendary Elk Moccasins",30,"Legendary Elk Pelt; Perfect Goat Hide"),("Legendary Elk Range Gloves",13,"Legendary Elk Pelt")],
 "Rattler": [("Ram Sombrero",10,"Perfect Ram Hide"),("Outdoorsmen Vest",22,"Perfect Pronghorn Hide"),("Javelina Half Chaps",18,"Perfect Collared Peccary Pig Pelt; Perfect Snake Skin"),("Iguana Range Gloves",27,"Perfect Collared Peccary Pig Pelt; Perfect Iguana Skin x2")],
 "Wrangler": [("Goat Flop Hat",12,"Perfect Goat Hide; Perfect Pronghorn Hide"),("Trapper's Cloak",32,"Perfect Sheep Hide"),("No-Man's Vest",27,"Perfect Goat Hide; Perfect Panther Pelt"),("Two Toned Moccasins",15,"Perfect Buck Pelt"),("Moose Range Gloves",22,"Perfect Moose Pelt")],
 "Bronco Buster": [("Elk Flop Hat",12,"Perfect Elk Pelt"),("Coyote Scout Jacket",20,"Perfect Coyote Pelt; Perfect Ox Hide"),("Huntsman Vest",25,"Perfect Deer Pelt; Perfect Sheep Hide"),("Boar Fringed Shotgun Chaps",25,"Perfect Boar Pelt x2"),("Pigskin Rifleman Gloves",8,"Perfect Pig Hide")],
 "Marauder": [("Muskrat Cavalry Hat",15,"Perfect Muskrat Pelt; Perfect Rabbit Pelt x4"),("Principal Vest",18,"Perfect Cow Hide; Perfect Deer Pelt"),("Bull Fringed Shotgun Chaps",18,"Perfect Bull Hide"),("Snake Skin Cavalry Gloves",26,"Perfect Boar Pelt; Perfect Snake Skin")],
 "Bounty Hunter": [("Plantation Slouch Hat",15,"Perfect Bison Pelt"),("Beaver Hunting Jacket",21,"Perfect Beaver Pelt x2; Perfect Cow Hide"),("Sheepskin Vest",20,"Perfect Sheep Hide x2"),("Pronghorn Half Chaps",7,"Perfect Pronghorn Hide"),("Buck Riding Gloves",5,"Perfect Buck Pelt")],
 "Desperado": [("Beaver Drifter Hat",20,"Perfect Beaver Pelt x2"),("Wolf Coat",25,"Perfect Ram Hide; Perfect Wolf Pelt"),("Billy Vest",32,"Perfect Armadillo Skin x2; Perfect Goat Hide"),("Boar & Bull Fowler Boots",31,"Perfect Boar Pelt; Perfect Ox Hide"),("Winter Cavalry Gloves",25,"Perfect Muskrat Pelt x2; Perfect Rabbit Pelt")],
 "Night Wrangler": [("Coyote Gambler's Hat",16,"Perfect Coyote Pelt x2"),("Cougar Cutaway Coat",39,"Perfect Black Bear Pelt; Perfect Cougar Pelt x2"),("Wilderness Vest",28,"Perfect Panther Pelt; Perfect Wolf Pelt"),("Moose Half Chaps",10,"Perfect Moose Pelt"),("Badger Rifleman Gloves",10,"Perfect Badger Pelt")],
 "Mountain Man": [("Grenadier Hat",24,"Perfect Beaver Pelt; Perfect Muskrat Pelt"),("Ram Shotgun Coat",45,"Perfect Ram Hide x2"),("Country Vest",25,"Perfect Beaver Pelt; Perfect Buck Pelt"),("Elk Riding Gloves",12,"Perfect Elk Pelt")],
}
NONSET = [
 ("Badger Mountain Hat",26,"Perfect Badger Pelt"),("Beaver Mountain Hat",28,"Perfect Beaver Pelt"),("Fox Mountain Hat",30,"Perfect Fox Pelt"),
 ("Skunk Mountain Hat",23,"Perfect Skunk Pelt"),("Bear Grenadier Hat",24,"Perfect Black Bear Pelt"),("Squirrel Flat Cap",16,"Perfect Squirrel Pelt x6"),
 ("Rat Flat Cap",12,"Perfect Rat Pelt x10"),("Snake Bulldogger Cap",23,"Perfect Sheep Hide; Perfect Snake Skin"),("Iguana Big Valley Hat",14,"Perfect Cow Hide; Perfect Iguana Skin"),
 ("Gila Monster Gambler's Hat",16,"Perfect Elk Pelt; Perfect Gila Monster Skin"),("Pronghorn Flop Hat",12,"Perfect Opossum Pelt x4; Perfect Pronghorn Hide"),
 ("Deer Cavalry Hat",20,"Perfect Deer Pelt; Raven Feather x10"),("Bison Gambler's Hat",18,"Perfect Bison Pelt; Oriole Feather x4; Robin Feather x4"),
 ("Rat Infantry Hardee Hat",17,"Perfect Goat Hide; Perfect Rat Pelt x6"),
 ("Stalker Accessory",13,"Condor Feather; Loon Feather x2; Raven Feather x3"),("Scavenger Accessory",11,"Seagull Feather; Vulture Feather"),
 ("Native Accessory",10,"Pheasant Feather; Robin Feather x3; Sparrow Feather x4"),("Pilgrim Accessory",11,"Blue Jay Feather x3; Cedar Waxwing Feather x2; Turkey Feather"),
 ("Huntsman Accessory",10,"Perfect Boar Pelt; Hawk Feather; Quail Feather x2"),("Pioneer Accessory",11,"Chicken Feather x3; Duck Feather x3; Turkey Feather x3"),
 ("Rococo Accessory",15,"Cardinal Feather x2; Crow Feather x2"),("Glorious Accessory",10,"Oriole Feather; Woodpecker Feather x4"),
 ("Pursuer Accessory",13,"Eagle Feather x2; Pigeon Feather x2"),("Majestic Accessory",15,"Rooster Feather x4; Songbird Feather x2; Woodpecker Feather x2"),
 ("Homestead Accessory",10,"Chicken Feather; Goose Feather x2"),("Judicious Accessory",10,"Owl Feather; Pheasant Feather"),
 ("Rugged Wrangler Vest",23,"Perfect Pig Hide"),("Hinterland Vest",21,"Perfect Ram Hide"),("Rustic Vest",23,"Perfect Cougar Pelt"),
 ("Bear Batwing Chaps",27,"Perfect Bear Pelt"),("Ox Fringed Shotgun Chaps",15,"Perfect Ox Hide"),("Elk Fringed Shotgun Chaps",21,"Perfect Elk Pelt"),
 ("Moose Batwing Chaps",10,"Perfect Moose Pelt"),("Batwing Chaps",12,"Perfect Deer Pelt"),("Bear Fringed Shotgun Chaps",38,"Perfect Black Bear Pelt"),
 ("Sheep Batwing Chaps",35,"Perfect Sheep Hide x2"),("Muskrat Half Chaps",5,"Perfect Muskrat Pelt x2"),("Deer Pelt Half Chaps",9,"Perfect Deer Pelt"),
 ("Javelina Moccasins",33,"Perfect Collared Peccary Pig Pelt x2"),("Skunk Trapper Boots",39,"Perfect Skunk Pelt x2"),("Moccasins",17,"Perfect Buck Pelt"),
]
SADDLES = [
 ("Rattlesnake Vaquero Saddle","Perfect Snake Skin x10"),("Cougar McClelland Saddle","Perfect Cougar Pelt"),("Boar Mother Hubbard Saddle","Perfect Boar Pelt"),
 ("Alligator Ranch Cutter Saddle","Perfect Alligator Skin"),("Bear Dakota Saddle","Perfect Bear Pelt"),("Beaver Roping Saddle","Perfect Beaver Pelt"),
 ("Panther Trail Saddle","Perfect Panther Pelt"),
]
EP1 = ("Legendary Tatanka Bison Pelt","Legendary Cougar Pelt","Legendary Pronghorn Hide","Perfect Gila Monster Skin",
       "Perfect Collared Peccary Pig Pelt","Perfect Armadillo Skin","Condor Feather")
def gate_note(ms):
    items = [m["item"] for m in ms]
    n = []
    if any(i in EP1 for i in items): n.append("Needs Epilogue (New Austin) material.")
    if "Legendary Alligator Skin" in items: n.append("Bullgator: Ch.6+.")
    if "Legendary Panther Pelt" in items: n.append("Panther: Master Hunter 9.")
    return " ".join(n)

trapper = []
def add_trapper(name, price, spec, note, cat_override=None):
    ms = mats(spec)
    e = {"id": kebab(name), "name": name, "category": cat_override or cat(name), "price": float(price),
         "materials": ms, "note": (note + " " + gate_note(ms)).strip()}
    if any(m["item"] == "Perfect Bear Pelt" for m in ms):
        e["verify"] = True
        e["note"] = (e["note"] + " Wiki says 'Perfect Bear Pelt' (black bear or grizzly unclear).").strip()
    trapper.append(e)
for setname, items in TRAPPER_SETS.items():
    for name, price, spec in items:
        add_trapper(name, price, spec, f"{setname} set.")
for name, price, spec in NONSET:
    add_trapper(name, price, spec, "")
for name, spec in SADDLES:
    add_trapper(name, 0, spec, "Free; pelt only. Trapper saddles boost speed/accel +2.")

# ---------- LEGENDARY ----------
L = lambda name, region, loc, unlock, note="": {"id": kebab(name.replace('"', '')), "name": name, "region": region,
                                               "location": loc, "unlock": unlock, "note": note}
BRUISED = "After 'Exit Pursued by a Bruised Ego' (Ch.2)"
legendary = [
 L('Legendary Beaver "Malia"', "New Hanover", "Elysian Pool, center of Roanoke Ridge", BRUISED),
 L("Legendary Bharati Grizzly Bear", "Ambarino", "O'Creagh's Run, Grizzlies East", BRUISED, "First met in that mission. Needs 2 clues."),
 L("Legendary Bighorn Ram", "Ambarino", "Cattail Pond, Grizzlies West", BRUISED),
 L('Legendary Boar "Oryx"', "Lemoyne", "Bluewater Marsh, NE of Lagras by Kamassa River", BRUISED),
 L('Legendary Buck "Obie"', "West Elizabeth", "Center of Black Bone Forest, Big Valley", BRUISED),
 L('Legendary Coyote "Suki"', "Lemoyne", "Dewberry Creek, Scarlett Meadows", BRUISED),
 L('Legendary Elk "Enyeto"', "New Hanover", "Cumberland Forest, east of Bacchus Station", BRUISED),
 L('Legendary Fox "Layla"', "Lemoyne", "Mattock Pond, Scarlett Meadows (N of Rhodes)", BRUISED),
 L('Legendary Moose "Anoki"', "New Hanover", "Roanoke Ridge, island W of Willard's Rest", BRUISED),
 L("Legendary White Bison", "Ambarino", "North end of Lake Isabella, Grizzlies West", BRUISED),
 L('Legendary Wolf "Hotah"', "Ambarino", "Cotorra Springs, Grizzlies East", BRUISED),
 L("Legendary Giaguaro Panther", "Lemoyne", "SE of Bolger Glade, Scarlett Meadows, near coast", "Master Hunter Rank 9 done", "Killing it completes Master Hunter 10."),
 L('Legendary Bullgator "Lacartus"', "Lemoyne", "Bayou Nwa, S of Lagras, W of Lakay", "After 'That's Murfree Country' (end Ch.5)", "Fought in that mission first."),
 L("Legendary Cougar", "New Austin", "Gaptooth Ridge, N of Gaptooth Breach", "Epilogue (after 'The Wheel')"),
 L('Legendary Pronghorn "Ira"', "New Austin", "Rio Bravo, W of Del Lobo Rock", "Epilogue (after 'The Wheel')"),
 L("Legendary Tatanka Bison", "New Austin", "Hennigan's Stead, SE of MacFarlane's Ranch", "Epilogue (after 'The Wheel')"),
]

# ---------- LEDGER ----------
def LG(name, group, cost, effect, requires, note=""):
    e = {"id": kebab(name), "name": name, "group": group, "cost": cost, "effect": effect, "requires": requires}
    if note: e["note"] = note
    return e
NOPRICE = "Price not in wiki text (only a screenshot)."
ledger = [
 LG("Leatherworking Tools", "Camp", 225, "Pearson can craft satchels/some decor", "Camp ledger unlocked", "$180 with high honor."),
 LG("Dutch's Lodging", "Lodging", 220, "Encourages others to donate", "Camp ledger unlocked"),
 LG("Arthur's Lodging", "Lodging", 325, "Unlocks fast travel from camp", "Dutch's Lodging"),
 LG("Everyone's Lodging", "Lodging", None, "Raises camp morale", "Arthur's Lodging", NOPRICE),
]
for grp, who, eff in (("Medicine", "Strauss's", "More tonic/liquor types"),
                      ("Provisions", "Pearson's", "More provision types"),
                      ("Ammunition", "Arthur's", "More ammo/throwable types")):
    for i in (1, 2, 3):
        req = "Camp ledger unlocked" if i == 1 else f"{grp} Wagon {i-1}"
        ledger.append(LG(f"{grp} Wagon {i}", grp, None, eff, req, f"{who} wagon. {NOPRICE}"))
ledger += [
 LG("Horse Station", "Horse Station", None, "Swap/retrieve horse or saddle at camp", "Camp ledger unlocked", NOPRICE),
 LG("Chicken Coop", "Provisions", None, "Pearson's stew refills Dead Eye core", "Camp ledger unlocked", NOPRICE),
 LG("Camp Boat", "Camp", None, "Canoe at camp for waterways", "Chapter 3 or 4 only", NOPRICE),
]
for e in ledger:
    if e["requires"] == "Camp ledger unlocked":
        e["requires"] = "Camp ledger (Ch.2-4)"

# ---------- ANIMALS ----------
HINTS = {
 "Deer": "Everywhere except New Austin",
 "Buck": "Most common in Scarlett Meadows, Cumberland Forest",
 "Elk": "SW Tall Trees to NE Roanoke Ridge; not Lemoyne/New Austin",
 "Badger": "W of Kamassa River, NE of Aurora Basin, N of Bacchus Station",
 "Squirrel": "Everywhere",
 "Panther": "Old Harry Fen, Lagras, Stillwater Creek",
 "Bison": "Great Plains, The Heartlands, Heartland Overflow",
 "Raccoon": "Everywhere except Cholla Springs, Rio Bravo, Gaptooth Ridge",
 "Boar": "Big Valley, Bolger Glade, Bluewater Marsh",
 "Iguana": "Flat Iron Lake big island, Cholla Springs, San Luis River",
 "Beaver": "Owanjila, N of Lake Isabella, Kamassa River W of Van Horn",
 "Rabbit": "Almost everywhere",
 "Cougar": "Various spots in New Austin, New Hanover, West Elizabeth",
 "Wolf": "Aurora Basin, Hanging Dog Ranch",
 "Alligator": "Swamps of Bayou Nwa, Lemoyne",
 "Bighorn Ram": "Mountains: Big Valley, Grizzlies, Cumberland Forest, Tall Trees",
 "Ox": "Ranches: Carmody Dell, Guthrie Farm, Emerald Ranch",
 "Pronghorn": "West/SW; N Black Bone Forest, Flatneck Station",
 "Moose": "Aurora Basin, Cairn Lake, Strawberry, Willard's Rest",
 "Snake": "Big Valley roads, W of Rhodes, Lemoyne swamps, New Austin",
 "Muskrat": "Most waterways; most in Bluewater Marsh",
 "Fox": "Everywhere except Gaptooth Ridge",
 "Cow": "Ranches: Carmody Dell, Emerald Ranch, Hill Haven Ranch",
 "Goat": "Larned Sod, Emerald Ranch",
 "Bull": "Ranches: Carmody Dell, Emerald Ranch, Hill Haven Ranch",
 "Sheep": "Valentine, Emerald Ranch",
 "Pig": "Valentine, Flatneck Station",
 "Black Bear": "E of Aurora Basin, along Little Creek River",
 "Bear": "Ambiguous on wiki. Black bear: E Aurora Basin; grizzly: Grizzlies, Tall Trees",
 "Coyote": "Everywhere except Grizzlies West",
 "Skunk": "Everywhere except Cholla Springs",
 "Rat": "Everywhere, more in the east",
 "Opossum": "South-central: Big Valley, Scarlett Meadows, Riggs Station",
 "Collared Peccary": "Cholla Springs, Rio Bravo, Gaptooth Ridge (Epilogue)",
 "Armadillo": "New Austin only: Cholla Springs, Armadillo (Epilogue)",
 "Gila Monster": "New Austin only: NW of Armadillo, Lake Don Julio (Epilogue)",
 "Hawk": "Everywhere",
 "Cardinal": "Everywhere except New Austin",
 "Turkey": "Mainly northern and central regions",
 "Eagle": "Most areas; not Great Plains, Hennigan's Stead, Bayou Nwa",
 "Raven": "Tanner's Reach, Eris Field",
 "Oriole": "Lone Mule Stead",
 "Robin": "Everywhere except Grizzlies West",
 "Condor": "New Austin (Epilogue)",
 "Loon": "Flat Iron Lake, Owanjila, Upper Montana River",
 "Seagull": "Saint Denis, Flat Iron Lake, Van Horn",
 "Vulture": "Armadillo",
 "Pheasant": "Carmody Dell, Valentine",
 "Sparrow": "Everywhere except Gaptooth Ridge, Cholla Springs, Rio Bravo",
 "Blue Jay": "Central map; most in The Heartlands",
 "Waxwing": "Benedict Point, Riggs Station",
 "Quail": "West Elizabeth, New Austin",
 "Chicken": "Settlements",
 "Duck": "Most areas; not Grizzlies West or New Austin",
 "Goose": "Emerald Ranch",
 "Crow": "Everywhere",
 "Woodpecker": "Most areas; not New Austin or Great Plains",
 "Pigeon": "Bard's Crossing, Annesburg, Saint Denis",
 "Rooster": "Select ranches",
 "Songbird": "Almost everywhere; most in Roanoke Valley",
 "Owl": "Aurora Basin",
}
leg_by_name = {l["name"]: l for l in legendary}
used = []
for sec in (pearson, trapper):
    for e in sec:
        for m in e["materials"]:
            if m["animal"] and m["animal"] not in used:
                used.append(m["animal"])
animals = {}
missing = []
for a in sorted(used):
    if a in leg_by_name:
        l = leg_by_name[a]; animals[a] = f"{l['location']} ({l['region']})"
    elif a in HINTS:
        animals[a] = HINTS[a]
    else:
        missing.append(a)
if missing:
    sys.exit("Missing hints: %s" % missing)

# ---------- checks ----------
for nm, sec in (("pearson", pearson), ("trapper", trapper), ("legendary", legendary), ("ledger", ledger)):
    ids = [e["id"] for e in sec]
    assert len(ids) == len(set(ids)), (nm, [i for i in ids if ids.count(i) > 1])
assert len(legendary) == 16

data = {"pearson": pearson, "trapper": trapper, "legendary": legendary, "ledger": ledger, "animals": animals}
js = "const RDR2 = " + json.dumps(data, indent=1, ensure_ascii=False) + ";\n"
open(sys.argv[1], "w", encoding="utf-8").write(js)
print({k: len(v) for k, v in data.items()})
print("verify:", [(s, e["id"]) for s in ("pearson", "trapper", "ledger") for e in data[s] if e.get("verify")])
