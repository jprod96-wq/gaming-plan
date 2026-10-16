import json, sys
TB = "Titan Blood"
def mats(costs): return [{"item": TB, "qty": c, "source": TB} for c in costs]

OLY = "Next boon is from this god; their boons get +10/15/20% chance to be Rare or better."
K = []
def kp(id, name, giver, effect, tags=("Keepsake",), note_extra="", requires=None, **kw):
    d = {"id": id, "name": name, "tags": list(tags), "giver": giver,
         "requires": requires or f"Give Nectar to {giver}", "note": effect + ((" " + note_extra) if note_extra else "")}
    d.update(kw); K.append(d)
kp("old-spiked-collar","Old Spiked Collar","Cerberus","+25/38/50 max Life.")
kp("myrmidon-bracer","Myrmidon Bracer","Achilles","Take 20/25/30% less damage from the front, 10% more from behind.")
kp("black-shawl","Black Shawl","Nyx","+10/15/20% damage vs undamaged foes and when striking from behind.")
kp("pierced-butterfly","Pierced Butterfly","Thanatos","+1/1.5/2% damage per Encounter cleared without taking damage.")
kp("bone-hourglass","Bone Hourglass","Charon","Well of Charon items last +4/6/8 more Encounters.")
kp("chthonic-coin-purse","Chthonic Coin Purse","Hypnos","Get 100/125/150 Obols once per escape attempt.", tip="Safe to swap out after the gold is paid.")
kp("skull-earring","Skull Earring","Megaera","+20/30/40% damage while at 35% Life or less.")
kp("distant-memory","Distant Memory","Orpheus","+10/20/30% damage to distant foes.")
kp("harpy-feather-duster","Harpy Feather Duster","Dusa","Broken urns have a 3/5/6% chance to hold healing.")
kp("lucky-tooth","Lucky Tooth","Skelly","Restore 50/75/100 Life when Life hits 0 (once per escape).", note_extra="Triggers after all Death Defiances.")
kp("thunder-signet","Thunder Signet","Zeus",OLY,tags=("Keepsake","Olympian"))
kp("conch-shell","Conch Shell","Poseidon",OLY,tags=("Keepsake","Olympian"))
kp("owl-pendant","Owl Pendant","Athena",OLY,tags=("Keepsake","Olympian"))
kp("eternal-rose","Eternal Rose","Aphrodite",OLY,tags=("Keepsake","Olympian"))
kp("blood-filled-vial","Blood-Filled Vial","Ares",OLY,tags=("Keepsake","Olympian"))
kp("adamant-arrowhead","Adamant Arrowhead","Artemis",OLY,tags=("Keepsake","Olympian"))
kp("overflowing-cup","Overflowing Cup","Dionysus",OLY,tags=("Keepsake","Olympian"))
kp("frostbitten-horn","Frostbitten Horn","Demeter",OLY,tags=("Keepsake","Olympian"))
kp("lambent-plume","Lambent Plume","Hermes","+1/1.1/1.2% dodge and move speed per quickly cleared Encounter.",tags=("Keepsake","Olympian"),
   tip="Also opens some Hermes boons without their prerequisites.")
kp("cosmic-egg","Cosmic Egg","Chaos","Enter Chaos Gates without losing Life; Chaos blessings +20/30/40% chance Rare or better.")
kp("shattered-shackle","Shattered Shackle","Sisyphus","Attack, Special and Cast deal +50/75/100% damage while not empowered by a boon.")
kp("evergreen-acorn","Evergreen Acorn","Eurydice","In each region's final encounter, take 0 damage from the first 3/4/5 hits.")
kp("broken-spearpoint","Broken Spearpoint","Patroclus","After taking damage, impervious for 1/1.25/1.5 sec (7 sec refresh).")
kp("late-game-keepsake","Late-game keepsake","Late-game character","After every 6/5/4 Encounters, a random boon gains +1 Lv.",
   tags=("Keepsake","Late game"), requires="Unlocks late in the story")
kp("sigil-of-the-dead","Sigil of the Dead","Hades","Call becomes Hades' Aid (brief Invisibility); God Gauge starts 10/20/30% full.",
   tags=("Keepsake","Late game"), requires="Unlocks late in the story (special gift)")

def cp(id,name,giver,effect,extra=""):
    K.append({"id":id,"name":name,"tags":["Companion"],"giver":giver,
              "requires":f"Ambrosia to {giver} after earning their favor","note":effect+(" "+extra if extra else "")})
cp("companion-battie","Companion Battie","Megaera","Summon deals 2500 damage near the closest foe, then down the line.","Not usable vs the Furies.")
cp("companion-mort","Companion Mort","Thanatos","Summon deals 3500 damage in front of you after a short delay.","Not usable in Thanatos' encounters.")
cp("companion-rib","Companion Rib","Skelly","Summon a 250-Life decoy that foes attack until it breaks.","Not usable vs Charon.")
cp("companion-shady","Companion Shady","Sisyphus","Summon deals 1000 area damage and drops Life, Darkness and Obols.")
cp("companion-fidi","Companion Fidi","Dusa","Summon joins you for 30 sec, firing shots that petrify foes (70 dmg).")
cp("companion-antos","Companion Antos","Achilles","Summon deals 1500 damage to 2 foes in turn.")

A = []
W = {"blade":"Stygius (Blade)","spear":"Varatha (Spear)","shield":"Aegis (Shield)","bow":"Coronacht (Bow)","fists":"Malphon (Fists)","rail":"Exagryph (Rail)"}
DEF = "Default aspect; each level costs Titan Blood"
UNL = "Spend Titan Blood at the weapon"
def asp(id,w,name,effect,costs,req,tags=None,**kw):
    d={"id":id,"name":name,"weapon":W[w],"requires":req,"materials":mats(costs),
       "note":effect+" Per level: "+"/".join(map(str,costs))+f" (total {sum(costs)})."}
    if tags: d["tags"]=tags
    d.update(kw); A.append(d)
Z=[1]*5; S2=[1,2,3,4,5]; S3=[2,2,3,4,5]; H=[3]*5
HREQ="Secret: revealed through a conversation after story progress and 5 Titan Blood spent on this weapon"
asp("blade-zagreus","blade","Aspect of Zagreus","+3-15% Attack and move speed.",Z,DEF,["Default"])
asp("blade-nemesis","blade","Aspect of Nemesis","For 3 sec after your Special, Attack can crit (15-30% chance).",S2,UNL)
asp("blade-poseidon","blade","Aspect of Poseidon","Special dislodges Cast ammo from foes; +10-50% Cast damage.",S3,UNL)
asp("blade-hidden","blade","Hidden aspect","Alternate moveset with a slowing defensive aura; +50 max Life.",H,HREQ,["Late game"])
asp("spear-zagreus","spear","Aspect of Zagreus","+10-25% Special damage, range and speed.",Z,DEF,["Default"])
asp("spear-achilles","spear","Aspect of Achilles","After Special, dash to the spear (Raging Rush); next 4 Attacks/Casts +50-150%.",S2,UNL)
asp("spear-hades","spear","Aspect of Hades","Spin Attack becomes Punishing Sweep: foes take +30-150% Attack/Special dmg for 10 sec.",S3,UNL)
asp("spear-hidden","spear","Hidden aspect","Alternate moveset; reduced Life total and healing.",H,
    "Secret: needs story progress and 5 non-default aspects unlocked",["Late game"],
    tip="Reveal this one first; the other hidden aspects need it.")
asp("shield-zagreus","shield","Aspect of Zagreus","+3-15 Attack and Dash-Strike damage.",Z,DEF,["Default"])
asp("shield-chaos","shield","Aspect of Chaos","After Bull Rush, next Special throws +1-5 extra shields.",S2,UNL)
asp("shield-zeus","shield","Aspect of Zeus","Special becomes Blitz Disc (8-30 dmg per hit), recalled on command.",S3,UNL)
asp("shield-hidden","shield","Hidden aspect","Alternate moveset; Cast empowers Bull Rush; you take +10% damage.",H,HREQ,["Late game"])
asp("bow-zagreus","bow","Aspect of Zagreus","+3-15% critical Attack chance.",Z,DEF,["Default"])
asp("bow-chiron","bow","Aspect of Chiron","Special homes in on the foe last hit by your Attack (4-8 shots).",S2,UNL)
asp("bow-hera","bow","Aspect of Hera","Cast ammo loads into your next Attack; ammo drops faster (10s to 5s).",S3,UNL)
asp("bow-hidden","bow","Hidden aspect","Alternate moveset that can inflict Shared Suffering (30-60% of Attack for 7 sec).",H,HREQ,["Late game"])
asp("fists-zagreus","fists","Aspect of Zagreus","+5-15% dodge chance.",Z,DEF,["Default"])
asp("fists-talos","fists","Aspect of Talos","Special becomes Magnetic Cutter; +10-50% Attack/Cast for 6 sec after.",S2,UNL)
asp("fists-demeter","fists","Aspect of Demeter","After 12 strikes, next Special hits +1-5 more times.",S3,UNL)
asp("fists-hidden","fists","Hidden aspect","Alternate moveset; Dash-Upper can Maim foes (100-400 dmg).",H,HREQ,["Late game"])
asp("rail-zagreus","rail","Aspect of Zagreus","+4-12 max ammo.",Z,DEF,["Default"])
asp("rail-eris","rail","Aspect of Eris","After standing in your Special's blast, +15-75% damage for 4 sec.",S2,UNL)
asp("rail-hestia","rail","Aspect of Hestia","After a manual Reload, next shot is empowered (50-150 base dmg).",S3,UNL)
asp("rail-hidden","rail","Hidden aspect","Alternate moveset that launches volatile blasts.",H,HREQ,["Late game"])

P = []
def pr(id,name,req,reward,tags,**kw):
    d={"id":id,"name":name,"tags":tags,"requires":req,"note":"Reward: "+reward}; d.update(kw); P.append(d)
SP="Hidden: story spoiler"
pr("story-prophecy-1","Story prophecy",SP,"20 Ambrosia",["Late game"])
pr("story-prophecy-2","Story prophecy",SP,"5 Diamonds",["Late game"])
pr("is-there-no-escape","Is There No Escape?","Escape the Underworld once","1000 Darkness",["Progress"])
pr("distant-relatives","Distant Relatives","Meet 7 Olympians","3 Nectar",["Characters"])
pr("chthonic-colleagues","Chthonic Colleagues","Meet the 9 rulers of the Underworld","10 Chthonic Keys",["Characters"])
pr("night-and-darkness","Night and Darkness","Help Nyx (6 Nectar, then a Contractor work order)","4 Ambrosia",["Side quest"])
pr("the-reluctant-musician","The Reluctant Musician","Release Orpheus via a Contractor work order","80 Gemstones",["Side quest"])
pr("musician-and-muse","Musician and Muse","Reunite Orpheus and Eurydice (Nectar + work order)","2 Ambrosia",["Side quest"])
pr("end-to-torment","End To Torment","Pardon Sisyphus (Nectar + work order)","4 Ambrosia",["Side quest"])
pr("divided-by-death","Divided by Death","Reunite Achilles and Patroclus (Nectar + work order)","4 Ambrosia",["Side quest"])
pr("eternal-rest","Eternal Rest","Slay Skelly with Stygius in a max-level Aspect of Zagreus","6 Diamonds",["Weapons"])
pr("a-place-of-revelry","A Place of Revelry","Renovate the Lounge for Dusa (cleaning, detailing, rug + 10 items)","4 Diamonds",["House"])
pr("amusing-chaos","Amusing Chaos","Defeat the final boss with the Cosmic Egg equipped","3 Diamonds",["Combat"])
pr("sea-gods-spite","Sea-God's Spite","Beat Theseus with 'Extreme Measures' active, then see Poseidon","3 Ambrosia",["Combat"])
pr("war-gods-bloodlust","War-God's Bloodlust","Slay 10,000 foes, then see Ares","2 Titan Blood",["Combat"])
pr("a-friendly-wager","A Friendly Wager","Defeat Charon twice in a row (any runs)","5 Titan Blood",["Combat"])
for gid,name,god,n in [("goddess-of-wisdom","Goddess of Wisdom","Athena",11),("god-of-the-heavens","God of the Heavens","Zeus",13),
    ("god-of-the-sea","God of the Sea","Poseidon",13),("goddess-of-love","Goddess of Love","Aphrodite",13),("god-of-war","God of War","Ares",13),
    ("goddess-of-the-hunt","Goddess of the Hunt","Artemis",12),("god-of-wine","God of Wine","Dionysus",12),("god-of-swiftness","God of Swiftness","Hermes",13),
    ("goddess-of-seasons","Goddess of Seasons","Demeter",11)]:
    pr(gid,name,f"Earn all {n} listed boons of {god}","150 Gemstones",["Boons"])
pr("power-without-equal","Power Without Equal","Earn the 10 Legendary boons","1000 Gemstones",["Boons"])
pr("divine-pairings","Divine Pairings","Earn all 28 Duo boons","15 Ambrosia",["Boons"])
pr("primordial-boons","Primordial Boons","Earn all 12 Chaos blessings","30 Chthonic Keys",["Boons"])
pr("primordial-banes","Primordial Banes","Suffer all 13 Chaos curses","30 Chthonic Keys",["Boons"])
pr("infernal-arms","Infernal Arms","Acquire all 6 Infernal Arms","60 Gemstones",["Weapons"])
for wid,name,w,ex in [("the-stygian-blade","The Stygian Blade","Stygius","Greater Consecration"),("the-heart-seeking-bow","The Heart-Seeking Bow","Coronacht","Repulse Shot"),
    ("the-shield-of-chaos","The Shield of Chaos","Aegis","Unyielding Defense"),("the-eternal-spear","The Eternal Spear","Varatha","Winged Serpent"),
    ("the-twin-fists","The Twin Fists","Malphon","Rending Claws")]:
    pr(wid,name,f"Get every Daedalus upgrade for {w} except {ex}","200 Gemstones",["Weapons"])
pr("the-adamant-rail","The Adamant Rail","Get every Daedalus upgrade for Exagryph except hidden-aspect-only ones","200 Gemstones",["Weapons"])
for hid,name,w in [("the-holy-liege","The Holy Liege","Stygius"),("the-fated-saint-of-war","The Fated Saint of War","Varatha"),
    ("the-preservers-avatar","The Preserver's Avatar","Coronacht"),("the-dragons-rival","The Dragon's Rival","Aegis"),
    ("the-god-like-king","The God-like King","Malphon"),("the-dawn-bringer","The Dawn Bringer","Exagryph")]:
    pr(hid,name,f"Get past Cerberus in the Temple of Styx using {w}'s hidden aspect","2 Ambrosia",["Weapons","Late game"])
pr("master-of-arms","Master of Arms","Escape with each of the 6 weapons","10 Titan Blood",["Progress"])
pr("a-violent-past","A Violent Past","Unlock all weapon aspects (hidden ones excluded)","6 Diamonds",["Weapons"])
pr("harsh-conditions","Harsh Conditions","Escape under each of the 15 Pact conditions (across runs)","15 Titan Blood",["Progress"])
pr("slashed-benefits","Slashed Benefits","Slay foes with each of the 11 'Benefits Package' perks","450 Gemstones",["Combat"])
pr("wanton-ransacking","Wanton Ransacking","Slay each of the 12 mini-boss Wardens","3 Titan Blood",["Combat"])
pr("a-simple-job","A Simple Job","Order 30 House Contractor renovations","4 Diamonds",["House"])
pr("chthonic-knowledge","Chthonic Knowledge","Reveal 70 Codex sections","40 Gemstones",["House"])
pr("customer-loyalty","Customer Loyalty","Buy each of the 26 Well of Charon items","150 Gemstones",["House"])
pr("dark-reflections","Dark Reflections","Escape with each Mirror talent active (across runs)","8 Titan Blood",["Progress"])
pr("close-at-heart","Close at Heart","Equip each keepsake once (the 2 late-game ones excluded)","2 Ambrosia",["Characters"],
   tip="Equipping in the courtyard counts; leave the cabinet after each swap.")
pr("denizens-of-the-deep","Denizens of the Deep","Catch 25 fish incl. a very rare one, then see Poseidon","250 Gemstones",["House"])
pr("the-gift-of-song","The Gift of Song","Practice the Lyre in your room, then report to Orpheus","2 Ambrosia",["House"])
pr("the-useless-trinket","The Useless Trinket","Defeat the final boss with at least 8 Heat","5 Diamonds",["Progress"])

M = []
def mp(id,name,red,green,unlock,tags,tip=None):
    d={"id":id,"name":name,"tags":tags,"requires":unlock,"note":f"Red: {red} Green: {green}"}
    if tip: d["tip"]=tip
    M.append(d)
ST="Available from start"
mp("presence","Shadow Presence / Fiery Presence","+10% Attack/Special dmg from behind per rank (max 5, 100 Darkness).",
   "+15% Attack/Special dmg vs undamaged foes per rank (max 5, 100 Darkness).",ST,["Start"])
mp("vitality","Chthonic Vitality / Dark Regeneration","Heal 1 Life per rank on leaving a chamber (max 3, 70 Darkness).",
   "Darkness picked up heals 30% of its value per rank (max 2, 90 Darkness).",ST,["Start"],tip="Dark Regeneration benefits from Dark Thirst.")
mp("defiance","Death Defiance / Stubborn Defiance","Revive at 50% Life once per rank (max 3, 1,530 Darkness).",
   "Revive at 30% Life once per chamber (max 1, 600 Darkness).",ST,["Start"])
mp("reflex","Greater Reflex / Ruthless Reflex","+1 chained Dash (max 1, 50 Darkness).",
   "Dash just before a hit: +50% dmg and dodge for 2 sec (max 1, 75 Darkness).",ST,["Start"])
mp("blood","Boiling Blood / Abyssal Blood","+10% Attack/Special dmg per rank vs foes with Cast ammo in them (max 5, 250 Darkness).",
   "-6% foe speed and damage per rank while they hold Cast ammo (max 5, 300 Darkness).","Tier unlock: 5 Chthonic Keys",["5 Keys"],
   tip="Some Cast boons (e.g. Demeter's beam) don't lodge ammo, so they skip this bonus.")
mp("soul","Infernal Soul / Stygian Soul","+1 Cast ammo per rank (max 2, 100 Darkness).",
   "Cast ammo regenerates instead of dropping; 1 sec faster per rank (max 2, 180 Darkness).","Tier unlock: 5 Chthonic Keys",["5 Keys"])
mp("pockets","Deep Pockets / Golden Touch","+10 Obols at the start of each escape per rank (max 10, 525 Darkness).",
   "+5% of your Obols per rank when clearing a region (max 3, 270 Darkness).","Tier unlock: 10 Chthonic Keys",["10 Keys"])
mp("skin","Thick Skin / High Confidence","+5 max Life per rank (max 10, 625 Darkness).",
   "+5% damage per rank at 80% Life or more (max 5, 750 Darkness).","Tier unlock: 10 Chthonic Keys",["10 Keys"])
mp("status","Privileged Status / Family Favorite","+20% dmg per rank vs foes with 2+ status curses (max 2, 550 Darkness).",
   "+2.5% dmg per rank for each Olympian whose boons you have (max 2, 200 Darkness).","Tier unlock: 20 Chthonic Keys",["20 Keys"])
mp("favor","Olympian Favor / Dark Foresight","+1% chance per rank for Rare boons (max 40, 2,000 Darkness).",
   "+2% chance per rank for gold-laurel rewards (max 10, 1,500 Darkness).","Tier unlock: 20 Chthonic Keys",["20 Keys"])
mp("pride","Gods' Pride / Gods' Legacy","+1% chance per rank for Epic boons (max 20, 2,000 Darkness).",
   "+1% chance per rank for Legendary or Duo boons (max 10, 2,500 Darkness).","Tier unlock: 30 Chthonic Keys",["30 Keys"])
mp("fated","Fated Authority / Fated Persuasion","+1 die per rank to reroll the next chamber's reward (max 8, 11,000 Darkness).",
   "+1 die per rank to reroll boon and Well of Charon choices (max 4, 10,000 Darkness).","Tier unlock: 30 Chthonic Keys",["30 Keys"],
   tip="Rerolling a Well after buying something restocks it.")

T = [
 {"title":"Buy Death Defiance first","text":"Extra lives from the Mirror are the biggest early boost. Fill Death Defiance before spreading Darkness elsewhere.","tag":"Mirror"},
 {"title":"Respec the Mirror freely","text":"Once unlocked, a full Darkness refund costs just 1 Chthonic Key, so try different talents for each weapon or Heat level.","tag":"Mirror"},
 {"title":"Spend Keys on weapons and Mirror tiers","text":"All six weapons cost 24 Chthonic Keys in total and the Mirror tiers 65. Try each weapon early to find favourites.","tag":"Resources"},
 {"title":"Gemstones: Contractor first","text":"Buy the Fated List (20 Gems) and the Tartarus Fountain Chamber early. The regional Keepsake Collection (10 Gems) lets you swap keepsakes after bosses.","tag":"Resources"},
 {"title":"Give everyone one Nectar","text":"Each first Nectar gift unlocks a keepsake. Keepsakes rank up after 25 and 50 encounters equipped, so rotate them.","tag":"Resources"},
 {"title":"Steer your build with keepsakes","text":"Olympian keepsakes guarantee the next boon is from that god. Pick one whose Attack or Special boon suits your weapon.","tag":"Boons"},
 {"title":"Lock in a damage boon early","text":"An Attack or Special boon early on carries the run. Then add defence (Dash or Call) and spend Poms on your main damage boon.","tag":"Boons"},
 {"title":"Dash through danger","text":"Dashing makes you briefly invulnerable. Dashing through attacks beats running from them, and Dash-Strikes keep the pressure on.","tag":"Combat"},
 {"title":"Use companions every run","text":"Companions can be summoned once per encounter. Upgrading one with Ambrosia adds more uses per escape.","tag":"Combat"},
 {"title":"Check the Fated List often","text":"Many prophecies finish on their own. Boon collections pay 150 Gems each, and some prophecies pay Titan Blood or Ambrosia.","tag":"Progress"},
 {"title":"Pact of Punishment","text":"After your first escape, add Heat for one-time bounties per weapon (Titan Blood up to 20 Heat). Raise Heat in small steps.","tag":"Progress"},
 {"title":"God Mode is fine","text":"God Mode (Settings) gives 20% damage resistance, rising 2% per death up to 80%. Progress and rewards work as normal.","tag":"Settings"},
 {"title":"Hidden aspects come later","text":"Each weapon has a secret aspect revealed through story progress. Don't worry about missing it early.","tag":"Weapons"},
]

C = {"id":"hades","title":"Hades","source":"hades.fandom.com","accent":4,"shoppingLabel":"🎯 Resources",
  "sources":{TB:"Bosses (first clears + Heat bounties per weapon), Fated List, Wretched Broker"},
  "sections":[
   {"id":"keepsakes","label":"🎁 Keepsakes","type":"checklist","doneLabel":"Got",
    "hint":"First Nectar gift = keepsake; Ambrosia after a favor = companion. Ranks up at 25/50 encounters.","items":K},
   {"id":"aspects","label":"⚔️ Weapon aspects","type":"checklist","doneLabel":"Unlocked","shopDefault":True,
    "hint":"Aspects appear once the Rail is unlocked and you own Titan Blood. Tick each level's cost as you pay it.","groupBy":"weapon","items":A},
   {"id":"prophecies","label":"📜 Fated List","type":"checklist","doneLabel":"Fulfilled",
    "hint":"Buy the Fated List from the House Contractor (20 Gems). Story entries are hidden.","items":P},
   {"id":"mirror","label":"🪞 Mirror of Night","type":"checklist","doneLabel":"Maxed",
    "hint":"Ranks cost Darkness; tiers unlock with Chthonic Keys. The green side unlocks via Nyx after 300 Darkness.","items":M},
   {"id":"tips","label":"💡 Tips","type":"tips","hint":"Spoiler-free","items":T}]}

out = "const COMPANION = " + json.dumps(C, ensure_ascii=False, indent=1) + ";\n"
with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write(out)
for s in C["sections"]:
    ids = [i.get("id", i.get("title")) for i in s["items"]]
    tags = {t for i in s["items"] for t in i.get("tags", [])} | ({i["tag"] for i in s["items"]} if s["type"] == "tips" else set())
    print(s["id"], len(s["items"]), "dupes:", len(ids) - len(set(ids)), "tags:", len(tags))
