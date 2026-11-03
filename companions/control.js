const COMPANION = {
 "id": "control",
 "title": "Control",
 "source": "control.fandom.com (Control Wiki, MediaWiki API)",
 "accent": 1,
 "sections": [
  {
   "id": "side",
   "label": "🧭 Side missions",
   "type": "checklist",
   "doneLabel": "Completed",
   "hint": "30 optional missions incl. free Expedition and DLC; reward lines show Ability Points and mods.",
   "groupBy": "area",
   "items": [
    {
     "id": "what-a-mess-burn-the-trash",
     "name": "What a Mess: Burn the Trash",
     "area": "Maintenance",
     "tags": [
      "Maintenance"
     ],
     "location": "Furnace Chamber; take the clipboard on the wall near Ahti",
     "requires": "Meet Ahti (early story, Directorial Override)",
     "note": "Reward: 2 Ability Points, a weapon mod. Dispose of 6 toxic waste barrels in the Furnace."
    },
    {
     "id": "what-a-mess-clear-the-clog",
     "name": "What a Mess: Clear the Clog",
     "area": "Maintenance",
     "tags": [
      "Maintenance"
     ],
     "location": "Janitor's Office corkboard (bottom right), then the Pump Station",
     "requires": "Unlocked once the Research-sector story mission has started (Old Boys' Club)",
     "note": "Reward: 3 Ability Points, Common Pierce Aimed Fire Boost."
    },
    {
     "id": "what-a-mess-talk-to-the-plants",
     "name": "What a Mess: Talk to the Plants",
     "area": "Maintenance",
     "tags": [
      "Maintenance",
      "Research"
     ],
     "location": "Janitor's Office, then Central Research",
     "requires": "Unlocked after a mid-story mission has started",
     "note": "Reward: 2 Ability Points, Uncommon personal mod."
    },
    {
     "id": "what-a-mess-even-more-mold",
     "name": "What a Mess: Even More Mold",
     "area": "Maintenance",
     "tags": [
      "Maintenance",
      "Late game"
     ],
     "location": "NCS Coolant Pumps; pick up the task from the Janitor's Office pinboard",
     "requires": "Unlocked after a late-story mission",
     "note": "Reward: 2 Ability Points, Uncommon Energy Renewal. Wiki infobox also hints Mold Removal may be required.",
     "verify": true
    },
    {
     "id": "what-a-mess-take-a-break",
     "name": "What a Mess: Take a Break",
     "area": "Maintenance",
     "tags": [
      "Maintenance",
      "Late game"
     ],
     "location": "Janitor's Office",
     "requires": "Finish What a Mess: Even More Mold, then return to the office",
     "note": "Reward: 4 Ability Points, Uncommon Headshot Boost, Janitor's Assistant."
    },
    {
     "id": "a-good-defense",
     "name": "A Good Defense",
     "area": "Maintenance",
     "tags": [
      "Maintenance"
     ],
     "location": "Field Training obstacle course",
     "requires": "Starts when you pick up Home Safe Tests or enter Field Training",
     "note": "Reward: new ability (Shield), 2 Ability Points, Common Weapon Armor Damage."
    },
    {
     "id": "a-merry-chase",
     "name": "A Merry Chase",
     "area": "Maintenance",
     "tags": [
      "Maintenance"
     ],
     "location": "Break room opposite the Janitor's Office",
     "requires": "Starts when you pick up Arish: Escaped OoP or approach the break room",
     "note": "Reward: new ability (Evade), 2 Ability Points, Common Health Recovery."
    },
    {
     "id": "old-friends",
     "name": "Old Friends",
     "area": "Maintenance",
     "tags": [
      "Maintenance"
     ],
     "location": "Talk to Simon Arish at Central Executive",
     "requires": "Available after your first visit to the Panopticon",
     "note": "Reward: 2 Ability Points, Uncommon Shield Reload Efficiency. Wiki is unsure of the exact trigger.",
     "verify": true
    },
    {
     "id": "a-captive-audience",
     "name": "A Captive Audience",
     "area": "Research",
     "tags": [
      "Research"
     ],
     "location": "Hypnosis Lab",
     "requires": "Starts when you pick up Astralnauts Information or enter the Hypnosis Lab",
     "note": "Reward: new ability (Seize), 3 Ability Points, Common Low Health Boost."
    },
    {
     "id": "old-growth",
     "name": "Old Growth",
     "area": "Research",
     "tags": [
      "Research"
     ],
     "location": "Talk to Emily Pope in Executive, or Raya Underhill in Underhill's Lab",
     "requires": "After the Threshold story mission",
     "note": "Reward: 4 Ability Points, Prime Health Recovery. Leads to Mold Removal."
    },
    {
     "id": "mold-removal",
     "name": "Mold Removal",
     "area": "Research",
     "tags": [
      "Research"
     ],
     "location": "Underhill's Lab, then Parapsychology, Ritual Division and Central Research",
     "requires": "Finish Old Growth first",
     "note": "Reward: 2 Ability Points, Rare Consecutive Kills Boost."
    },
    {
     "id": "self-reflection",
     "name": "Self-Reflection",
     "area": "Research",
     "tags": [
      "Research"
     ],
     "location": "Synchronicity Lab, Clearance Level 6 room",
     "requires": "Starts when you pick up Mirror Supplement or enter that room",
     "note": "Reward: 4 Ability Points, Rare Shield Boost."
    },
    {
     "id": "dr-tokui-guided-imagery",
     "name": "Dr. Tokui's Guided Imagery Experience",
     "area": "Research",
     "tags": [
      "Research"
     ],
     "location": "Extrasensory Lab: find the Dr. Tokui Tapes next to Isolation Pod #4",
     "requires": "Access to the Research Sector",
     "note": "Reward: Astral Dive Outfit, Prime Energy Recovery. Was PlayStation-only, now in the Ultimate Edition."
    },
    {
     "id": "a-matter-of-time",
     "name": "A Matter of Time",
     "area": "Containment",
     "tags": [
      "Containment"
     ],
     "location": "Kevin Horowitz by the shelter in the Logistics lobby",
     "requires": "Access to the Containment Sector",
     "note": "Reward: 2 Ability Points, Common Reload Efficiency. Leads to The Enemy Within."
    },
    {
     "id": "the-enemy-within",
     "name": "The Enemy Within",
     "area": "Containment",
     "tags": [
      "Containment"
     ],
     "location": "Sealed Threshold Hall",
     "requires": "Finish A Matter of Time first",
     "note": "Reward: 3 Ability Points, Uncommon Shield Efficiency."
    },
    {
     "id": "fridge-duty",
     "name": "Fridge Duty",
     "area": "Containment",
     "tags": [
      "Containment"
     ],
     "location": "Panopticon, Floor 4 Unit 15 (you hear a call for help)",
     "requires": "Pass the unit during a mid-story mission",
     "note": "Reward: 3 Ability Points, Rare Headshot Boost. Leads to Langston's Runaways."
    },
    {
     "id": "langstons-runaways",
     "name": "Langston's Runaways",
     "area": "Containment",
     "tags": [
      "Containment",
      "Executive",
      "Research"
     ],
     "location": "Report back to Langston at the Panopticon entrance",
     "requires": "Finish Fridge Duty and tell the Panopticon Supervisor",
     "note": "Reward: 5 Ability Points, Rare Energy Recovery, Rare Accuracy Boost. Contain 7 Altered Items (see next tab)."
    },
    {
     "id": "what-a-mess-clear-the-mold",
     "name": "What a Mess: Clear the Mold",
     "area": "Containment",
     "tags": [
      "Containment"
     ],
     "location": "Medical Wing",
     "requires": "Unlocked after a mid-story mission",
     "note": "Reward: 3 Ability Points, Uncommon Ammo Refund."
    },
    {
     "id": "mr-tommasi",
     "name": "Mr. Tommasi",
     "area": "Containment",
     "tags": [
      "Containment",
      "Executive",
      "Late game"
     ],
     "location": "Talk to Emily Pope in the Board Room; then Turntable and Sterling AWE",
     "requires": "Unlocked after a late-story mission",
     "note": "Reward: 3 Ability Points, Rare Levitation Ammo Efficiency."
    },
    {
     "id": "put-a-record-on",
     "name": "Put a Record On",
     "area": "Expedition",
     "tags": [
      "Expedition"
     ],
     "location": "Central Executive: pick up the Jukebox Token on the crate",
     "requires": "Appears after a mid-story mission",
     "note": "Free-update Expedition. Reward: Jukebox, Jukebox Token. Replayable via the Jukebox."
    },
    {
     "id": "found-footage",
     "name": "Found Footage",
     "area": "The Foundation",
     "tags": [
      "DLC"
     ],
     "location": "Foundation cave system: cavern with a Chasm entry, up high",
     "requires": "Both new abilities from the Foundation story",
     "note": "Reward: 3 Ability Points, Rare Melee Source Gain, VHS Tape Procedures."
    },
    {
     "id": "swift-platform",
     "name": "Jesse Faden starring in \"Swift Platform\"",
     "area": "The Foundation",
     "tags": [
      "DLC"
     ],
     "location": "Transit Access in the Collapsed Department",
     "requires": "Try to re-contain the ActionMaxx Camera on its platform once it has moved",
     "note": "Reward: 3 Ability Points, Rare Elemental Source Gain, Movie Camera Procedures."
    },
    {
     "id": "popes-collection",
     "name": "Pope's Collection",
     "area": "The Foundation",
     "tags": [
      "DLC"
     ],
     "location": "Talk to Pope at the Crossroads (Warehouse area)",
     "requires": "Complete any 1 ritual in the Foundation story and own any ID card",
     "note": "Reward: 3 Ability Points, Rare Concussed Source Gain."
    },
    {
     "id": "another-fine-mess-burn-the-dark",
     "name": "Another Fine Mess: Burn the Dark",
     "area": "AWE",
     "tags": [
      "DLC"
     ],
     "location": "Ahti's pinboard in the Operations Center (Investigations)",
     "requires": "Investigations Sector open; same board offers the other two Fine Messes",
     "note": "Reward: Shaded Facet. Optional bonus objective."
    },
    {
     "id": "another-fine-mess-clear-the-mold",
     "name": "Another Fine Mess: Clear the Mold",
     "area": "AWE",
     "tags": [
      "DLC"
     ],
     "location": "Ahti's pinboard in the Operations Center (Investigations)",
     "requires": "Investigations Sector open",
     "note": "Reward: Rare Shooter Dodge Efficiency. Optional bonus objective."
    },
    {
     "id": "another-fine-mess-nourish-the-plants",
     "name": "Another Fine Mess: Nourish the Plants",
     "area": "AWE",
     "tags": [
      "DLC"
     ],
     "location": "Ahti's pinboard in the Operations Center (Investigations)",
     "requires": "Investigations Sector open",
     "note": "Reward: a Prime mod (wiki page is sparse on details). Doing all three Fine Messes gives a unique Pierce mod.",
     "verify": true
    },
    {
     "id": "dead-in-its-tracks",
     "name": "Dead in its Tracks",
     "area": "AWE",
     "tags": [
      "DLC"
     ],
     "location": "Eagle Limited AWE (Investigations)",
     "requires": "Starts automatically from AWE story progress in that area",
     "note": "Reward: Shaded Facet, unique mod One-Way Track, Train Car Procedures."
    },
    {
     "id": "gerbil-took-the-top-head",
     "name": "Gerbil Took the Top Head",
     "area": "AWE",
     "tags": [
      "DLC"
     ],
     "location": "Fra Mauro AWE and Sector Head Office (Investigations)",
     "requires": "Starts automatically from AWE story progress in that area",
     "note": "Reward: Shaded Facet, unique mod Thin Space."
    },
    {
     "id": "return-to-sender",
     "name": "Return to Sender",
     "area": "AWE",
     "tags": [
      "DLC"
     ],
     "location": "Shifted Offices, Operations Center, Abandoned Offices, Observation Deck",
     "requires": "Starts when you pick up the Chain Letter collectible",
     "note": "Reward: Shaded Facet, unique mod Spam Mail."
    },
    {
     "id": "shum",
     "name": "SHÜM",
     "area": "AWE",
     "tags": [
      "DLC"
     ],
     "location": "Active Investigations, Arcade Mode",
     "requires": "Starts from AWE story progress in the Active Investigations area",
     "note": "Reward: Shaded Facet, Arcade Cabinets Supplement."
    }
   ]
  },
  {
   "id": "mods",
   "label": "🔫 Mods & weapon forms",
   "type": "checklist",
   "doneLabel": "Unlocked",
   "hint": "Service Weapon forms, upgrades and the special mods you can only get once.",
   "groupBy": "kind",
   "items": [
    {
     "id": "form-grip",
     "name": "Grip",
     "kind": "Weapon form",
     "tags": [
      "Weapon form"
     ],
     "location": "Default form from the start",
     "tip": "Accurate single shots; fine for most fights."
    },
    {
     "id": "form-shatter",
     "name": "Shatter",
     "kind": "Weapon form",
     "tags": [
      "Weapon form"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Becomes buildable after the Directorial Override briefing and a cleansed Control Point",
     "note": "Cost: 5,000 Source, 8 Undefined Reading, 4 House Memory. Shotgun-style.",
     "tip": "Strong at close range."
    },
    {
     "id": "form-spin",
     "name": "Spin",
     "kind": "Weapon form",
     "tags": [
      "Weapon form"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Buildable during Directorial Override once Maintenance Sector access is gained",
     "note": "Cost: 15,000 Source, 12 Ritual Impulse, 8 Threshold Remnant. Rapid fire.",
     "tip": "Good for medium range."
    },
    {
     "id": "form-pierce",
     "name": "Pierce",
     "kind": "Weapon form",
     "tags": [
      "Weapon form"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Buildable during Old Boys' Club once Research Sector access is gained",
     "note": "Cost: 24,000 Source, 12 Intrusive Pattern, 8 Astral Blip. Hits through walls and cover.",
     "tip": "Charged single shots; accuracy matters."
    },
    {
     "id": "form-charge",
     "name": "Charge",
     "kind": "Weapon form",
     "tags": [
      "Weapon form"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Buildable mid-story once Containment Sector access is gained and Remote Thought is collected",
     "note": "Cost: 25,000 Source, 10 Remote Thought, 3 Astral Blip, 2 Corrupted Sample. Up to 3 charged explosive rounds."
    },
    {
     "id": "upgrade-grip",
     "name": "Upgrade Grip (Lv2, Lv3)",
     "kind": "Form upgrade",
     "tags": [
      "Upgrade"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Required materials collected",
     "note": "Lv2: 10,000 Source. Lv3: 20,000 Source. Each level adds a mod slot and base damage."
    },
    {
     "id": "upgrade-shatter",
     "name": "Upgrade Shatter (Lv2, Lv3)",
     "kind": "Form upgrade",
     "tags": [
      "Upgrade"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Required materials collected",
     "note": "Lv2: 25,000 Source. Lv3: 20,000 Source."
    },
    {
     "id": "upgrade-spin",
     "name": "Upgrade Spin (Lv2, Lv3)",
     "kind": "Form upgrade",
     "tags": [
      "Upgrade"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Required materials collected",
     "note": "Lv2: 20,000 Source. Lv3: 25,000 Source."
    },
    {
     "id": "upgrade-pierce",
     "name": "Upgrade Pierce (Lv2, Lv3)",
     "kind": "Form upgrade",
     "tags": [
      "Upgrade"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Required materials collected",
     "note": "Lv2: 24,000 Source. Lv3: 36,000 Source."
    },
    {
     "id": "upgrade-charge",
     "name": "Upgrade Charge (Lv2, Lv3)",
     "kind": "Form upgrade",
     "tags": [
      "Upgrade"
     ],
     "location": "Control Point > Astral Constructs",
     "requires": "Required materials collected",
     "note": "Lv2: 30,000 Source. Lv3: 45,000 Source."
    },
    {
     "id": "mod-eternal-fire",
     "name": "Eternal Fire (Grip)",
     "kind": "Unique mod",
     "tags": [
      "Unique mod"
     ],
     "location": "Maintenance Sector, Furnace",
     "requires": "Dispose of 6 items in the Furnace",
     "note": "Unique, once per game. Wiki Mods page says 6 TV sets; the Burn the Trash page says 6 barrels. Check in game.",
     "verify": true
    },
    {
     "id": "mod-spam-mail",
     "name": "Spam Mail (Spin)",
     "kind": "Unique mod",
     "tags": [
      "Unique mod",
      "DLC"
     ],
     "location": "AWE side mission",
     "requires": "Complete Return to Sender",
     "note": "Unique. Needs AWE / Ultimate Edition."
    },
    {
     "id": "mod-one-way-track",
     "name": "One-Way Track (Shatter)",
     "kind": "Unique mod",
     "tags": [
      "Unique mod",
      "DLC"
     ],
     "location": "AWE side mission",
     "requires": "Complete Dead in its Tracks",
     "note": "Unique. Needs AWE / Ultimate Edition."
    },
    {
     "id": "mod-custodial-readiness",
     "name": "Custodial Readiness (Pierce)",
     "kind": "Unique mod",
     "tags": [
      "Unique mod",
      "DLC"
     ],
     "location": "Investigations Sector, Ahti's pinboard",
     "requires": "Complete all 3 Another Fine Mess missions",
     "note": "Unique. Needs AWE / Ultimate Edition."
    },
    {
     "id": "mod-thin-space",
     "name": "Thin Space (Charge)",
     "kind": "Unique mod",
     "tags": [
      "Unique mod",
      "DLC"
     ],
     "location": "AWE side mission",
     "requires": "Complete Gerbil Took the Top Head",
     "note": "Unique. Needs AWE / Ultimate Edition."
    },
    {
     "id": "mod-aerobics",
     "name": "Aerobics (personal mod)",
     "kind": "Unique mod",
     "tags": [
      "Unique mod",
      "DLC"
     ],
     "location": "Hidden spot in the Shifted Passage (Investigations)",
     "requires": "Solve the puzzle at the hidden location",
     "note": "Unique personal mod (health on Evade). Wiki gives no exact steps.",
     "verify": true
    },
    {
     "id": "mod-astral-reload-efficiency",
     "name": "Astral Reload Efficiency",
     "kind": "PlayStation bonus",
     "tags": [
      "PlayStation"
     ],
     "location": "Loadout from a new game's start",
     "note": "PlayStation-version Rare weapon mod, same effect as Reload Efficiency. Source: old pre-order FAQ.",
     "verify": true
    },
    {
     "id": "mod-astral-health-boost",
     "name": "Astral Health Boost",
     "kind": "PlayStation bonus",
     "tags": [
      "PlayStation"
     ],
     "location": "Loadout from a new game's start",
     "note": "PlayStation-version Rare personal mod, same effect as Health Boost. Source: old pre-order FAQ.",
     "verify": true
    }
   ]
  },
  {
   "id": "altered",
   "label": "🗿 Altered Items & Bounties",
   "type": "checklist",
   "doneLabel": "Done",
   "hint": "Altered Items to contain, Bureau Alert spots and Board Countermeasures.",
   "groupBy": "kind",
   "items": [
    {
     "id": "ai-paper-lantern",
     "name": "Japanese Paper Lantern",
     "kind": "Altered Item",
     "tags": [
      "Containment",
      "Altered Item"
     ],
     "location": "Sealed Threshold Hall (Containment)",
     "requires": "Langston's Runaways active",
     "note": "Cleanse and contain. First batch of 4."
    },
    {
     "id": "ai-traffic-light",
     "name": "Traffic Light",
     "kind": "Altered Item",
     "tags": [
      "Containment",
      "Altered Item"
     ],
     "location": "Panopticon (Containment)",
     "requires": "Langston's Runaways active",
     "note": "Cleanse and contain. First batch of 4."
    },
    {
     "id": "ai-hand-chair",
     "name": "Hand Chair",
     "kind": "Altered Item",
     "tags": [
      "Containment",
      "Altered Item"
     ],
     "location": "Medical Wing (Containment)",
     "requires": "Langston's Runaways active",
     "note": "Cleanse and contain. First batch of 4."
    },
    {
     "id": "ai-moving-letters",
     "name": "Moving Letters",
     "kind": "Altered Item",
     "tags": [
      "Executive",
      "Altered Item"
     ],
     "location": "Dead Letters (Executive)",
     "requires": "Langston's Runaways active",
     "note": "Cleanse and contain. Then report back to Langston."
    },
    {
     "id": "ai-flamingo",
     "name": "Flamingo",
     "kind": "Altered Item",
     "tags": [
      "Containment",
      "Altered Item"
     ],
     "location": "Sealed Threshold Corridor (Containment)",
     "requires": "After reporting back to Langston",
     "note": "Cleanse and contain. Second batch of 3."
    },
    {
     "id": "ai-mannequin",
     "name": "Mannequin",
     "kind": "Altered Item",
     "tags": [
      "Containment",
      "Altered Item"
     ],
     "location": "Prime Candidate Program (Containment)",
     "requires": "After reporting back to Langston",
     "note": "Cleanse and contain. Second batch of 3."
    },
    {
     "id": "ai-rubber-duck",
     "name": "Rubber Duck",
     "kind": "Altered Item",
     "tags": [
      "Research",
      "Altered Item"
     ],
     "location": "Protective Studies (Research)",
     "requires": "After reporting back to Langston",
     "note": "Cleanse and contain. Then report back to Langston."
    },
    {
     "id": "board-countermeasures",
     "name": "Board Countermeasures",
     "kind": "Bounty",
     "tags": [
      "Bounty"
     ],
     "location": "Any Control Point",
     "requires": "After the Unknown Caller story mission; up to 3 active at once",
     "note": "Repeatable. Rewards include mods, even for forms or abilities you don't own yet."
    },
    {
     "id": "alert-first",
     "name": "Complete 1 Bureau Alert",
     "kind": "Bureau Alert",
     "tags": [
      "Bureau Alert",
      "Milestone"
     ],
     "location": "Random alert notification; follow the objective marker",
     "requires": "After the Directorial Override story mission",
     "note": "Trophy: First On the Scene. Reward: 3 Uncommon materials, plus a Jukebox Token once the Jukebox is unlocked."
    },
    {
     "id": "alert-five",
     "name": "Complete 5 Bureau Alerts",
     "kind": "Bureau Alert",
     "tags": [
      "Bureau Alert",
      "Milestone"
     ],
     "location": "Random alert notification",
     "requires": "After the Directorial Override story mission",
     "note": "Trophy: Crisis Management. Repeatable; 20 min timer; failing has no penalty."
    },
    {
     "id": "alert-executive",
     "name": "Alerts: Executive",
     "kind": "Bureau Alert",
     "tags": [
      "Bureau Alert",
      "Executive"
     ],
     "location": "Nodes: Communications Department. Targets: Pneumatics. Protection: Mail Room",
     "note": "Nearest Control Points: Dead Letters / Mail Room."
    },
    {
     "id": "alert-maintenance",
     "name": "Alerts: Maintenance",
     "kind": "Bureau Alert",
     "tags": [
      "Bureau Alert",
      "Maintenance"
     ],
     "location": "Nodes: NSC Power Plant. Targets: NSC Energy Converters. Protection: Black Rock Quarry",
     "note": "Quarry protection alert only unlocks after a late-story mission."
    },
    {
     "id": "alert-research",
     "name": "Alerts: Research",
     "kind": "Bureau Alert",
     "tags": [
      "Bureau Alert",
      "Research"
     ],
     "location": "Nodes: Central Research. Targets: Ritual Division. Protection: Parapsychology",
     "note": "Central Research Control Point sits on a balcony; Parapsychology entrance avoids Levitate."
    },
    {
     "id": "alert-containment",
     "name": "Alerts: Containment",
     "kind": "Bureau Alert",
     "tags": [
      "Bureau Alert",
      "Containment"
     ],
     "location": "Nodes: Transit Corridor North. Targets: Panopticon. Protection: Ordinary Town Model",
     "note": "Use the Transit Corridor / Upper Panopticon / Ordinary AWE Control Points."
    },
    {
     "id": "alert-investigations",
     "name": "Alerts: Investigations",
     "kind": "Bureau Alert",
     "tags": [
      "Bureau Alert",
      "DLC"
     ],
     "location": "Nodes: AWE Loading Bay. Targets: AWE Transit Bay. Protection: Eagle Limited AWE",
     "requires": "Only after the AWE story is finished",
     "note": "Needs AWE / Ultimate Edition."
    },
    {
     "id": "alert-foundation",
     "name": "Alerts: Foundation",
     "kind": "Bureau Alert",
     "tags": [
      "Bureau Alert",
      "DLC"
     ],
     "location": "Targets: Warehouse. Protection: Collapsed Department (Fractured Cavern)",
     "requires": "Only after the Foundation story is finished",
     "note": "Needs The Foundation / Ultimate Edition. Wiki lists no Hiss Nodes alert here."
    }
   ]
  },
  {
   "id": "collectibles",
   "label": "📁 Collectibles",
   "type": "checklist",
   "doneLabel": "Found",
   "hint": "412 exist; tracked by category and trophy milestone, not one by one.",
   "groupBy": "group",
   "items": [
    {
     "id": "milestone-40",
     "name": "Collect 40 collectibles",
     "group": "Milestone",
     "tags": [
      "Milestone"
     ],
     "note": "Trophy: Strange Collection. 412 exist in total (287 base, 57 Foundation, 67 AWE, 1 extra)."
    },
    {
     "id": "milestone-80",
     "name": "Collect 80 collectibles",
     "group": "Milestone",
     "tags": [
      "Milestone"
     ],
     "note": "Trophy: Record Keeper."
    },
    {
     "id": "milestone-120",
     "name": "Collect 120 collectibles",
     "group": "Milestone",
     "tags": [
      "Milestone"
     ],
     "note": "Trophy: Bureau Archivist."
    },
    {
     "id": "milestone-foundation",
     "name": "All Foundation collectibles",
     "group": "Milestone",
     "tags": [
      "Milestone",
      "DLC"
     ],
     "note": "Trophy: Subterranean Research. 57 collectibles in The Foundation."
    },
    {
     "id": "milestone-awe",
     "name": "80% of Investigations collectibles",
     "group": "Milestone",
     "tags": [
      "Milestone",
      "DLC"
     ],
     "note": "Trophy: In-depth Investigations. AWE has 67 collectibles."
    },
    {
     "id": "milestone-cp-5",
     "name": "Cleanse 5 Control Points",
     "group": "Milestone",
     "tags": [
      "Milestone"
     ],
     "note": "Trophy: Ritualistic Thinking."
    },
    {
     "id": "milestone-cp-10",
     "name": "Cleanse 10 Control Points",
     "group": "Milestone",
     "tags": [
      "Milestone"
     ],
     "note": "Trophy: Ritual Intuition."
    },
    {
     "id": "milestone-cp-25",
     "name": "Cleanse 25 Control Points",
     "group": "Milestone",
     "tags": [
      "Milestone"
     ],
     "note": "Trophy: Discerning the Pattern."
    },
    {
     "id": "rr-hiss-research",
     "name": "Hiss Research",
     "group": "Research & Records",
     "tags": [
      "Research & Records"
     ],
     "note": "19 items."
    },
    {
     "id": "rr-reports",
     "name": "Reports",
     "group": "Research & Records",
     "tags": [
      "Research & Records"
     ],
     "note": "48 items."
    },
    {
     "id": "rr-research",
     "name": "Research",
     "group": "Research & Records",
     "tags": [
      "Research & Records"
     ],
     "note": "51 items."
    },
    {
     "id": "rr-astral-research",
     "name": "Astral Research",
     "group": "Research & Records",
     "tags": [
      "Research & Records",
      "DLC"
     ],
     "note": "3 items. All from The Foundation."
    },
    {
     "id": "cf-objects-of-power",
     "name": "Case Files: Objects of Power",
     "group": "Case Files",
     "tags": [
      "Case Files"
     ],
     "note": "10 items."
    },
    {
     "id": "cf-altered-world-events",
     "name": "Case Files: Altered World Events",
     "group": "Case Files",
     "tags": [
      "Case Files"
     ],
     "note": "24 items. Summary + Supplement pairs."
    },
    {
     "id": "cf-altered-items",
     "name": "Case Files: Altered Items",
     "group": "Case Files",
     "tags": [
      "Case Files"
     ],
     "note": "51 items. Procedures + Supplement files."
    },
    {
     "id": "co-official",
     "name": "Correspondence: Official",
     "group": "Correspondence",
     "tags": [
      "Correspondence"
     ],
     "note": "37 items."
    },
    {
     "id": "co-non-official",
     "name": "Correspondence: Non-official",
     "group": "Correspondence",
     "tags": [
      "Correspondence"
     ],
     "note": "36 items. One was once PlayStation-only; now in the Ultimate Edition."
    },
    {
     "id": "co-dead-letters",
     "name": "Correspondence: Dead Letters",
     "group": "Correspondence",
     "tags": [
      "Correspondence"
     ],
     "note": "17 items."
    },
    {
     "id": "mm-interviews",
     "name": "Multimedia: Interviews",
     "group": "Multimedia",
     "tags": [
      "Multimedia"
     ],
     "note": "9 items."
    },
    {
     "id": "mm-darling",
     "name": "Multimedia: Darling Presentations",
     "group": "Multimedia",
     "tags": [
      "Multimedia"
     ],
     "note": "21 items."
    },
    {
     "id": "mm-fbc-recordings",
     "name": "Multimedia: FBC Recordings",
     "group": "Multimedia",
     "tags": [
      "Multimedia"
     ],
     "note": "23 items."
    },
    {
     "id": "mm-america-overnight",
     "name": "Multimedia: America Overnight",
     "group": "Multimedia",
     "tags": [
      "Multimedia"
     ],
     "note": "6 items."
    },
    {
     "id": "mm-threshold-kids",
     "name": "Multimedia: Threshold Kids",
     "group": "Multimedia",
     "tags": [
      "Multimedia"
     ],
     "note": "7 items."
    },
    {
     "id": "mm-music",
     "name": "Multimedia: Music",
     "group": "Multimedia",
     "tags": [
      "Multimedia"
     ],
     "note": "5 items."
    },
    {
     "id": "mm-ash-tapes",
     "name": "Multimedia: Ash Tapes",
     "group": "Multimedia",
     "tags": [
      "Multimedia",
      "DLC"
     ],
     "note": "8 items. All from The Foundation."
    },
    {
     "id": "hl-hotline",
     "name": "Hotline recordings",
     "group": "Hotline",
     "tags": [
      "Hotline"
     ],
     "note": "36 items. Includes sets that are Foundation-only (5) and AWE-only (6)."
    }
   ]
  },
  {
   "id": "tips",
   "label": "💡 Tips",
   "type": "tips",
   "hint": "Spoiler-free",
   "items": [
    {
     "title": "Keep Loadout space free",
     "text": "Mods handed out by talking to someone are lost if your Loadout is full. Deconstruct spares before turning in missions.",
     "tag": "Economy"
    },
    {
     "title": "Deconstruct spare mods",
     "text": "Deconstructing gives Source: 50 (Common) up to 2,000 (Infinite); a unique mod gives 10,000 but is gone for that playthrough.",
     "tag": "Economy"
    },
    {
     "title": "Rarity is not everything",
     "text": "Mod stat ranges overlap between rarities, so an Uncommon roll can beat a Prime one. Compare the numbers.",
     "tag": "Economy"
    },
    {
     "title": "Constructing mods is a gamble",
     "text": "Constructed mods are random; you only pick Weapon or Personal and the rarity. Refreshing costs Source, so treat it as low priority.",
     "tag": "Economy"
    },
    {
     "title": "Build forms early",
     "text": "Mods only drop for forms and abilities you already own, so unlocking a form sooner widens what you can find.",
     "tag": "Progression"
    },
    {
     "title": "Collect materials first",
     "text": "A form's build option only shows once you have found at least one of each required material.",
     "tag": "Progression"
    },
    {
     "title": "Ability Points open mod slots",
     "text": "You start with one Personal Mod slot; upgrading abilities unlocks two more. Form upgrades add weapon mod slots.",
     "tag": "Progression"
    },
    {
     "title": "Swap Personal Mods per fight",
     "text": "Personal Mods boost things like Shield strength, recovery speed or lower Energy cost. Re-equip from the Loadout when your plan changes.",
     "tag": "Combat"
    },
    {
     "title": "Pierce needs aim",
     "text": "Pierce shoots through walls and cover, but its charge and cooldown make missed shots costly.",
     "tag": "Combat"
    },
    {
     "title": "Shatter and Spin scale with mods",
     "text": "Shatter mods add projectiles or tighten spread; Spin mods raise fire rate and grouping.",
     "tag": "Combat"
    },
    {
     "title": "Use Control Points as hubs",
     "text": "Control Points are where you fast travel and build Astral Constructs. Cleansing them also counts toward trophies.",
     "tag": "Exploration"
    },
    {
     "title": "Bureau Alerts are optional",
     "text": "You get 20 minutes; failing costs nothing. Rewards are 3 Uncommon materials, plus a Jukebox Token once it is unlocked.",
     "tag": "Exploration"
    },
    {
     "title": "Careful in Personnel Protection",
     "text": "Explosives and launched objects can hurt the agents you protect. Only one needs to survive.",
     "tag": "Combat"
    },
    {
     "title": "Board Countermeasures help mods",
     "text": "Their rewards can include mods for forms or abilities you do not own yet. Up to 3 can be active.",
     "tag": "Economy"
    }
   ]
  }
 ]
};
