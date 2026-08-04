# The Spine — A Linear Plan, Year 1 to Year 70

`02-map.md` says what the territory is. `resources/` says what to read and do
in each part of it. Neither tells you what to do *this year*, or in what
order, or what has to come first so the thing after it isn't wasted effort.
That's this file.

The spine walks all 44 ledger domains, the fundamentals, one language, one
craft, and the mastery spikes across seven decades in a defensible order. It
is a **default sequence, not a contract**. Reorder it freely — but reorder it
deliberately, at an annual review, knowing which prerequisite you're skipping
and what it will cost you.

## The seventy-year frame

Seven decades, seventy years.

| Decade | Years | The work |
|--------|-------|----------|
| 1 | 1–10 | The trunk: fundamentals, and the domains everything else needs |
| 2 | 11–20 | The second spike; the branches that needed scaffolding |
| 3 | 21–30 | The applied world; the ledger completes; synthesis begins |
| 4 | 31–40 | Integration, first re-foundations, promotions |
| 5 | 41–50 | The free decade: reclaimed hours, third spike, transmission |
| 6 | 51–60 | Distillation: what survives you, put in usable form |
| 7 | 61–70 | The long view: the perspective nobody younger can have |

**The ledger completes around year 30 — with forty years left.**
That is the single most important fact about this plan, and the one most
people get wrong when they imagine a "lifetime learning plan." Covering the
map once is the *first third*. What follows is not repetition: fields you
learned in Decade 1 will have moved by Decade 4, entire domains will exist
that have no name today, and the domains that actually pull will be waiting
for promotion to real depth. Decades 4–7 are where a broad education stops
being a collection and becomes a point of view.

A note on pace. Seventy years is generous for 44 domains — deliberately. The
slack absorbs the years that go wrong: illness, a demanding program, a new
child, a move, a job that eats everything. Falling five years behind the
sequence is not failure; it's the schedule working as designed.

---

## The sequencing logic

Four rules generated this order. If you rebuild the sequence yourself, keep
them and you'll get something equally good.

**1. Fundamentals first, because they tax everything downstream.** A slow
reader pays that tax on all 44 domains. Someone who can't write pays it on
every artifact, which is the only thing that earns a checkmark. Years 1–2 are
disproportionately about the instrument rather than the territory, and that
front-loading buys back more time than it costs by roughly year 6.

**2. Prerequisite chains, honoured.** Some domains are dramatically cheaper
after another one. The real chains:

```mermaid
flowchart LR
    STAT["Statistics<br/><i>yr 1</i>"] --> PSY[Psychology]
    STAT --> ECON[Economics]
    STAT --> GEN[Genetics]
    STAT --> MED[Medicine]
    STAT --> PH[Public health]
    STAT --> FIN[Finance]

    MATH["Mathematics<br/><i>yr 2</i>"] --> PHYS["Physics<br/><i>yr 3</i>"]
    MATH --> LOGIC[Logic]
    MATH --> TCS[Theoretical CS]
    PHYS --> CHEM["Chemistry<br/><i>yr 5</i>"]
    PHYS --> ASTRO[Astronomy]
    PHYS --> ENG[Engineering ×3]
    CHEM --> MAT[Materials]
    CHEM --> EARTH[Earth science]
    CHEM --> GEN
    GEN --> MED
    MED --> PH

    EVO["Evolution<br/><i>yr 4</i>"] --> ECOL[Ecology]
    EVO --> ANTH[Anthropology]
    EVO --> PSY
    EVO --> AGRI[Agriculture]
    EVO --> GEN

    PSY --> NEURO[Neuroscience]
    CHEM --> NEURO
    NEURO --> LING[Linguistics]
    NEURO --> AI[AI]

    HIST["World history<br/><i>yr 2</i>"] --> POL[Politics]
    HIST --> LAW[Law]
    HIST --> SOC[Sociology]
    HIST --> GEO[Geography]
    HIST --> MIL[Military history]
    HIST --> MEDIA[Media]
    ECON --> FIN
    ECON --> GEO

    PROG["Programming<br/><i>fundamental</i>"] --> COMP[Computing]
    PROG --> AI

    PHIL["Philosophy<br/><i>yr 1</i>"] -.->|"informs everything"| POL
    PHIL -.-> LAW
    PHIL -.-> AI

    style STAT fill:#2d4a63,stroke:#5a8cb8,color:#fff
    style MATH fill:#2d4a63,stroke:#5a8cb8,color:#fff
    style PHIL fill:#2d4a63,stroke:#5a8cb8,color:#fff
    style HIST fill:#2d4a63,stroke:#5a8cb8,color:#fff
    style EVO fill:#2d4a63,stroke:#5a8cb8,color:#fff
```

The five shaded nodes are the load-bearing ones: statistics, mathematics,
philosophy, world history, and evolution. Everything else in the ledger gets
cheaper after them, which is why all five land in years 1–4. Get those wrong
and the rest of the sequence costs more than it should.

**3. Alternate hard and free.** Every year pairs one prerequisite-chained
domain with one that has no prerequisites at all — literature, music, art,
religion, film. This isn't decoration. It's what makes seventy years
survivable: the free domain is the one you read on a bad week, and it keeps
the curiosity budget from being the only non-obligatory thing in your life.

**4. Some things run continuously, not in slots.** Spaced repetition, weekly
logging, the language, the craft, the spike, and the curiosity budget are
*tracks*, not domains. They appear in every year because they never stop.

This is why 43 of the ledger's 44 domains get a year and one doesn't: **"a
craft done with the hands" is a track, not a slot.** You cannot bring
embodied skill to literacy in a hundred hours and then leave it — it decays,
and it is the one domain on the map the rest cannot fake. It starts in year 3
and runs to year 30, reaching working-craftsperson level by the end. Language
works the same way for the same reason (see `resources/languages.md`), which
is why it's a three-year track from year 3 rather than a ledger entry.

---

## The load model

The agenda assumes **ten focused hours a week**, about 500 a year. A year's
allocation:

| Track | Hours/yr | Notes |
|-------|----------|-------|
| Two T3 domains | ~200 | 100 each; this is the ledger work |
| Spike (T1/T2) | ~150 | Your professional depth; more in some years |
| Fundamentals | ~50 | Heavy in years 1–2, maintenance after |
| Frontier slot | ~40 | Reconnaissance on what isn't on the map yet — `04-frontier.md` |
| Current awareness | ~100 | 2 hrs/wk across all frequencies — `05-current.md` |
| Curiosity budget | ~50 | Unplanned, off-ledger, no artifact required |

Two of those tracks are new and permanent. The **frontier slot** is 5–10% of
your hours held open, every year for seventy years, for fields that don't
exist yet — because over that span some will, and a fixed map would sleep
through them. **Current awareness** is the live layer: a map with no news
attached becomes a museum. Both are capped deliberately, because both expand
to fill whatever you give them.

Three caveats worth stating plainly.

**The trunk years run heavier than this table.** `TIMELINE.md` lists closer to
300 hours of ledger material in Decade 1, because those years carry two
domains *and* the fundamentals. Either run twelve or thirteen hours a week
through the trunk, or cut from the bottom of each year's queue — it's ordered
for exactly that. Decades 2 and 3 come back under budget as the spike takes
over.

**If you're in a demanding degree or training program, halve the ledger and
run one domain a year** — the spike comes first, always, and a professional
program *is* the spike. You'll finish the ledger around year 44 instead of
year 30, which is fine.

**A domain's hours don't have to be evenly spread**: six weeks of intensity
beats ten months of thirty-minute sessions for most literacy passes.

---

## How to read a year

Each year below gives you:

- **Ledger** — the two T3 domains, with the file to open in `resources/`
- **Why now** — the prerequisite argument, so you can judge a reorder
- **Fundamentals** — which capacity gets deliberate work
- **Modes** — the variety mandate. Minimum three modes per domain; see
  `resources/modes.md`
- **Kit** — what to buy this year; see `resources/kit.md` for the detail
- **By December** — the artifacts that must exist

---

# Decade 1 — Years 1–10: The Trunk

The mission is the trunk of the tree: the fundamentals, the formal and
physical core that half the ledger depends on, and the habits. Twenty domains
land here — the most of any decade — because these are the ones that make
later domains cheap.

## Year 1 — The instrument, and how to argue

- **Ledger:** Statistics & probability (`formal.md`) · Philosophy
  (`meaning-expression.md`)
- **Why now:** These are the two meta-domains. Statistics is how you evaluate
  every empirical claim in the other 42; philosophy is how you evaluate every
  argument. Doing them first makes everything after cheaper and makes you
  much harder to fool. Neither has prerequisites.
- **Fundamentals:** The big three, and this is the year for them — writing,
  reading, and SRS discipline. Adler's *How to Read a Book* in month one;
  Williams' *Style* worked with its exercises; Anki started on day one and
  never stopped.
- **Modes:** Stat 110's free lectures (Blitzstein) as a scheduled class with
  the problem sets actually done. Philosophy through the primary texts, not
  summaries — the Socratic dialogues are sixty pages. A reading group or one
  reader who owes you honesty.
- **Kit:** Almost nothing, deliberately. A library card, a notebook system,
  and Anki. Under $50. The year-1 restraint is the point — gear bought before
  the habit exists is gear that goes unused.
- **By December:** Two literacy artifacts published. Forty-plus weeks of
  weekly public writing. An unbroken SRS streak. A self-rating against the
  fundamentals table in `02-map.md`, done honestly.

## Year 2 — The universal solvent

- **Ledger:** Mathematics (`formal.md`) · World history, part 1 of 2
  (`human-social.md`)
- **Why now:** Mathematics gates physics, chemistry, economics, and the
  entire formal cluster — it is the single highest-leverage domain on the
  map. World history is the timeline every social and humanities domain plugs
  into later; starting it now means politics, law, and sociology all arrive
  with somewhere to attach. History is the one domain given two years,
  because `resources/human-social.md` is right that no single book does it.
- **Fundamentals:** Math and statistics to working level. Programming begins
  — automate one real annoyance in your own life, which is the whole on-ramp.
- **Modes:** 3Blue1Brown for intuition, then Strang's linear algebra for the
  real thing. The Big History Project for deep time. A natural history museum
  visit with a specific question in hand.
- **Kit:** A whiteboard and a proof notebook. Under $100.
- **By December:** A mathematics artifact. History part 1 notes. A working
  script you wrote that saves you real time.

## Year 3 — Physical law, and the first art

- **Ledger:** Physics (`physical.md`) · Literature (`meaning-expression.md`)
- **Why now:** Physics needs year 2's mathematics and is itself the gate to
  chemistry, astronomy, materials, and all three engineerings. Literature is
  the alternation rule's first real test: a domain with no prerequisites, no
  math, and a completely different rhythm, deliberately placed against the
  hardest year so far.
- **Continuous tracks begin:** **Your language** starts now and runs three
  years to B2 — see `resources/languages.md` for why "fluent" is a
  meaningless target and CEFR isn't. **Your craft** starts now too, and never
  ends.
- **Modes:** The Feynman Lectures, free online, read by the chapters
  `resources/physical.md` names rather than cover to cover. Susskind's
  *Theoretical Minimum* lectures. A tutor for the language from month one —
  conversation is the feedback loop and there's no substitute.
- **Kit:** 10×50 binoculars (they'll serve astronomy in year 10 and birding
  forever), and the craft's starting tools. Whichever instrument or tool you
  chose, buy the cheap version and use it until its limits genuinely annoy
  you.
- **By December:** A physics artifact. A literature artifact. CEFR A2 in the
  language. One finished object from the craft, however bad.

## Year 4 — The living world

- **Ledger:** Evolutionary & molecular biology (`living.md`) · Music
  (`meaning-expression.md`)
- **Why now:** Evolution is the organizing idea of the entire living cluster
   — ecology, genetics, medicine, anthropology, and half of psychology all
  assume it. Nothing in biology makes sense without it, so it comes first.
- **Modes:** Stearns' Open Yale lectures. A microscope on your own kitchen
  scrapings — pond water, yeast, your own cheek cells. A local natural
  history society. For music: an instrument in your hands, not a book about
  music.
- **Kit:** A real compound microscope, bought used from university surplus if
  you can — the difference between a toy and a usable scope with achromatic
  objectives is the difference between the mode working and not. An
  instrument and a metronome.
- **By December:** A biology artifact tracing one adaptation end to end. A
  music artifact. Language at B1.

## Year 5 — Matter and mind

- **Ledger:** Chemistry (`physical.md`) · Psychology (`mind.md`)
- **Why now:** Chemistry needs year 3's physics and gates genetics, medicine,
  and materials. Psychology needs year 1's statistics — without it you cannot
  read the field's literature honestly, and the replication crisis makes that
  a live problem rather than an academic one.
- **Modes:** Chemistry is the least autodidact-friendly domain on the map
  because you cannot fake a lab. Take the community college lab course; it's
  cheap and it's the honest route. Psychology through Bloom's Open Yale
  course plus running a classic experiment on yourself.
- **Kit:** Lab course fees rather than home equipment. Home chemistry has
  real safety and legal constraints — the legitimate hobby routes are in
  `resources/kit.md`.
- **By December:** Two artifacts. Language at B1+. The craft's second object,
  visibly better than the first.

## Year 6 — Incentives and images

- **Ledger:** Economics (`human-social.md`) · Visual art & architecture
  (`meaning-expression.md`)
- **Why now:** Economics needs statistics (year 1) and history (year 2) —
  it's incoherent without both. Art needs nothing, which is exactly why it's
  here.
- **Modes:** CORE Econ's *The Economy*, free and better than most paid
  courses. FRED and Our World in Data for a real dataset — an afternoon with
  actual series teaches what ten chapters don't. For art: standing in front
  of real paintings, because scale does not survive reproduction.
- **Kit:** A museum membership, which pays for itself in two visits and
  changes how you use a museum — repeatedly and briefly, rather than once and
  exhaustively.
- **By December:** Two artifacts. Language at B2 — the level that changes
  your life. Sixty percent of the fundamentals table at "strong."

## Year 7 — Brains and belief

- **Ledger:** Neuroscience (`mind.md`) · World religions & mythology
  (`meaning-expression.md`)
- **Why now:** Neuroscience needs biology (year 4), chemistry (year 5), and
  psychology (year 5) — attempted earlier it's memorization. Religion pairs
  with it deliberately: the two most different accounts of the human interior
  you will meet, read in the same year, is a genuinely useful collision.
- **Modes:** Kanwisher's MIT lectures, free. A brain specimen at a museum or
  a university open day. For religion: primary texts, and attending services
  or ceremonies of two traditions not your own, observed as a scholar would.
- **Kit:** Nothing significant. Bank it for year 10.
- **By December:** Two artifacts. Language maintenance, not acquisition.

## Year 8 — Inheritance and power

- **Ledger:** Genetics (`living.md`) · Political science (`human-social.md`)
- **Why now:** Genetics needs evolution (4), chemistry (5), and statistics
  (1) — it's the most prerequisite-dense domain in the living cluster.
  Political science needs history (2) and philosophy (1).
- **Modes:** Real sequence data — pull from GenBank, build a tree, learn what
  a bootstrap value does and doesn't mean. For politics: attend a local
  council meeting, then read the minutes. The gap between the two is the
  domain's actual subject.
- **Kit:** Nothing new.
- **By December:** Two artifacts. **Mid-decade decision point:** which
  domains so far pulled hardest? Those are your second-spike candidates.

## Year 9 — Machines and peoples

- **Ledger:** Computing in practice (`made-applied.md`) · Anthropology &
  archaeology (`human-social.md`)
- **Why now:** Computing lands after seven years of programming as a
  fundamental, so you arrive with real problems rather than tutorials.
  Anthropology needs evolution (4) and history (2).
- **Modes:** CS50 if you want the structure, but the better route by now is
  building something you need. MIT's *Missing Semester* for the tools nobody
  teaches. For anthropology: a field school, or a dig season — volunteer
  archaeology genuinely takes amateurs.
- **Kit:** A soldering iron (temperature-controlled — the fixed-temperature
  one is a false economy), a multimeter, a microcontroller starter kit. Under
  $200 and it opens the whole made-and-applied cluster.
- **By December:** Two artifacts. Something you built that another person
  uses.

## Year 10 — The sky, the screen, and the audit

- **Ledger:** Cosmology & astronomy (`physical.md`) · Theater, film &
  narrative media (`meaning-expression.md`)
- **Why now:** Astronomy needs physics (3) and mathematics (2). It's placed
  last in the decade because it's the best possible payoff for the discipline
  that got you here — and because the binoculars from year 3 have been
  waiting.
- **Modes:** SDSS SkyServer for real data. An astronomy club, which is the
  most welcoming amateur community in existence and will let you look through
  telescopes worth more than your car. An observatory or planetarium visit.
- **Kit:** **The year-10 purchase: a Dobsonian reflector.** Aperture matters
  more than magnification, and this is the one big-ticket item the decade has
  earned. (Never point any telescope at the sun without a proper solar
  filter.)
- **By December:** Two artifacts. **The ten-year audit:** twenty domains
  checked, the fundamentals table honest, and the second spike chosen — see
  `phases/decade-1-foundations.md`.

---

# Decade 2 — Years 11–20: The Second Spike and the Branches

Twelve to fourteen domains, at a deliberately slower ledger pace, because the
second spike is now taking real hours and the mastery work in
`phases/decade-2-mastery.md` is the decade's actual mission. The domains here
are the ones that needed a decade of scaffolding underneath them.

## Years 11–12 — Foundations of form

- **Ledger:** Logic & foundations · Theoretical computer science &
  information theory · Rhetoric & writing
- **Why now:** Logic and theoretical CS are the same subject wearing two
  hats, and both need a decade of mathematical maturity to land as anything
  but symbol-pushing. Rhetoric arrives now because you've been writing weekly
  for ten years — you have something to refine rather than something to
  start.
- **Modes:** Lean and mathlib for formalization, which turns logic from a
  reading subject into a doing subject. A serious writing workshop with real
  feedback, which beats any course.
- **Kit:** Nothing. These are pencil-and-screen domains.
- **Continuous:** Second spike at T2. Craft approaching material fluency.

## Years 13–14 — Language, intelligence, society

- **Ledger:** Linguistics · Artificial intelligence · Sociology
- **Why now:** Linguistics and AI both need neuroscience (7) and psychology
  (5); AI additionally needs the mathematics and the programming. Sociology
  needs history and statistics. Note that AI here means the *field* — search,
  representation, learning theory, the philosophical questions — not the
  tooling, which has a two-year half-life and is learned inside projects.
- **Modes:** Build a model from scratch, badly, before reading about better
  ones. Transcribe and analyze an hour of real recorded speech for
  linguistics — the gap between what people think they say and what they say
  is the field's front door.
- **Kit:** A decent microphone and recorder for linguistic fieldwork.

## Years 15–16 — Systems that sustain

- **Ledger:** Ecology · Earth science & climate · Law & legal systems
- **Why now:** Ecology needs evolution (4) and statistics (1). Earth science
  needs chemistry (5) and physics (3). Law needs history (2) and philosophy
  (1) — and it's the domain where the licensing wall is real, so the ledger
  pass is literacy and nothing more.
- **Modes:** Citizen science with genuine scientific value — eBird,
  iNaturalist, Zooniverse. A local mycological or botanical society. Read
  actual court opinions rather than books about them.
- **Kit:** A home weather station, regional field guides, a plant press, a
  hand lens. Under $250 and it converts two domains from reading to fieldwork.

## Years 17–18 — Bodies and money

- **Ledger:** Medicine & physiology · Materials science · Finance & markets
- **Why now:** Medicine needs biology, chemistry, genetics, and statistics —
  it is the most prerequisite-dense domain on the whole map, which is why
  it's this late. Materials needs chemistry and physics. Finance needs
  economics (6) and statistics (1).
- **Modes:** For medicine, the honest amateur routes are EMT certification or
  hospital and hospice volunteering — both genuinely open to anyone, and both
  teach what no textbook does. Shiller's Yale course for finance, free.
- **Kit:** A metallography setup for materials is cheaper than it sounds and
  genuinely doable at home.

## Years 19–20 — Place, learning, and the audit

- **Ledger:** Geography & geopolitics · Education
- **Why now:** Geography integrates history, politics, economics, and earth
  science — it's best late, when it has all four to integrate. Education
  arrives now because you're twenty years into an experiment in it, and
  because Decade 3's stewardship work needs it.
- **Modes:** Travel as actual field equipment. Teach a real class at a
  library or makerspace.
- **By year 20:** The **twenty-year audit** in
  `phases/decade-2-mastery.md`. Roughly 34 domains checked. Second spike at
  or near T1. A legible body of work.

---

# Decade 3 — Years 21–30: The Applied World and Synthesis

The remaining domains are deliberately concentrated in the made-and-applied
cluster, and that's a design choice: after two decades of largely textual
learning, the third act is where you build things. It also carries the
synthesis, stewardship, and reinvention tracks from
`phases/decade-3-synthesis.md`.

## Years 21–23 — Engineering, three ways

- **Ledger:** Engineering: energy & power systems · Engineering: structures &
  the built environment · Engineering: machines, manufacturing & transport
- **Why now:** All three need physics (3), mathematics (2), and materials
  (17–18). Taken together in a block, they teach the same habit of mind three
  times, which is why they're adjacent rather than scattered.
- **Modes:** Run real numbers on real data — MATPOWER and PyPSA are free.
  Instrument your own house and discover your mental model of where your
  electricity goes is badly off. Factory and industrial heritage tours.
- **Kit:** The workshop, properly. Hand tools over power tools, a sharpening
  setup first because sharpening is the actual first skill, a bench and vise.
  Safety equipment is not optional — eye protection, hearing protection, dust
  control, a fire extinguisher.

## Years 24–26 — Systems of people

- **Ledger:** Public health & care systems · Business, management &
  entrepreneurship · Media & communication
- **Why now:** Public health needs medicine (17–18) and statistics.
  Business and media both benefit from everything, and both are domains where
  two decades of accumulated judgment makes the reading land differently.
- **Modes:** These are practitioner fields — interview people who do them.
  Run something small and real rather than reading about running things.

## Years 27–30 — The last of the ledger, and the synthesis

- **Ledger:** Military history & strategy · Design · Agriculture & food
  systems
- **Why now:** They're last because nothing depends on them, not because they
  matter least. Agriculture is a fine domain to end on — it closes the loop
  from year 4's biology to the food on your table, and it's the most
  physical, seasonal, patient subject on the map.
- **Kit:** A garden, soil test kits, and time. The slowest feedback loop of
  anything here, and worth it.
- **The three tracks:** Synthesis (the cross-field work only your combination
  enables), stewardship (transferring what you know to people and
  institutions), and optionally reinvention — a third spike chosen with zero
  career justification allowed, on pull alone.
- **By year 30:** All 44 domains checked. One major synthesis work. The craft
  at working-craftsperson level. The year-30 review written, and a sketch of
  what years 31–40 are for.

---

# The Second Half — Years 31–70

The ledger is done and you are fifty. Forty years remain — more time than the
whole plan so far has used.

The instinct at this point is to assume the learning is over and only the
using is left. That instinct is wrong, and the rest of this file exists to
say why. Four kinds of work fill the second half, and none of them are
available to someone who hasn't done the first:

**Re-foundation.** A field you brought to literacy at 25 has moved by 55.
Instrument-driven and computational fields move fastest — biology, astronomy,
linguistics, medicine, anything that got a new way of measuring. Every domain
needs a refresh roughly every 15–20 years, and the signal that one is overdue
is simple: you can no longer follow a current talk in a field you once knew.
Being taught the new version by someone who learned it long after you did
is the normal experience, not a humiliation. See `04-frontier.md`.

**Promotion.** Forty-four literacy passes tell you something no amount of
planning could: which domains actually pull. The second half is where a
handful of them go to working depth or mastery. This is a narrowing move —
saying no to thirty-nine domains in order to say yes to five.

**The frontier.** Fields will exist in Decade 5 with no name today. The
slot has been running at 5–10% since year 1 precisely so that you notice them
and can join rather than watch.

**Transmission.** Synthesis, teaching, institutions, successors. Unshared
mastery doesn't compound — it retires.

Because these are less schedulable than a literacy pass, the decades below
are lighter on year-by-year prescription and heavier on the shape of the
work. The detailed treatment is in `phases/`.

---

# Decade 4 — Years 31–40: Integration

**The move:** stop collecting, start connecting. This is typically peak
professional authority, and the decade where a completed ledger plus two
mature spikes finally produces work nobody else could do.

- **Re-foundations:** the first systematic pass. Pick the 5–8 domains that
  have moved most since you learned them and redo the literacy pass on
  current material.
- **Promotions:** 3–5 domains from T3 to T2 across the decade, chosen on
  demonstrated pull rather than on plan.
- **The signature work:** cross-field synthesis. The problems you've been
  noticing since Decade 2 that need your specific combination.
- **Institutions:** begin building the thing that teaches after you — a
  course, a curriculum, a team, a standard, an open resource.
- **Maintenance becomes curriculum:** exercise, sleep, hearing and vision
  correction, social engagement. These stop being background and become
  scheduled, because they protect the instrument everything else runs on.
- **Kit:** peak earning meets deferred wants. The big durable goods —
  a serious telescope, a full workshop, a real instrument, a kiln or lathe —
  are justifiable now on cost-per-year-of-use. The trap is buying capability
  instead of exercising it (`resources/kit.md`).

## Decade 5 — Years 41–50: The Free Decade

**The move:** obligations loosen and learning hours roughly double. For
someone who kept the habits for forty years, this can be the most productive
learning decade of a life — a vast SRS vault, syntopical reading, a network,
taste, and now time.

- **The third spike,** chosen on pull alone with zero career justification
  permitted. Beginner-hood here is a practice, not a humiliation, and it is
  where genuinely new work often comes from.
- **Transmission at scale:** the book-length synthesis, specific named
  successors, the institution.
- **Formal re-entry** is a real and underused option — a degree, a
  fellowship, a residency. Many institutions actively want older students.
- **Second re-foundation pass,** with reverse-mentoring now essential:
  seniority insulates you from the new unless you build against it.

## Decade 6 — Years 51–60: Distillation

**The move:** the corpus is large and unsorted. The work is editing, not
accumulating — deciding what of fifty years is worth passing on and putting
it in a form that survives you.

- **The summative work:** the book, the curriculum, the archive made legible
  to a stranger. A thousand scattered pieces distilled into one usable thing
  is the greater contribution.
- **Hard learning as health infrastructure.** Novelty and difficulty are the
  active ingredient — a new language, a new instrument, a new craft beats
  reviewing what you already know.
- **Adapt the method, don't lower the ambition.** Audio as a first-class
  mode, larger type, shorter and more frequent sessions, more spaced review,
  hearing aids early rather than late. The SRS vault built over five decades
  is now doing exactly what it was designed for.
- **The frontier slot still runs.** A frozen model is the characteristic
  failure of this decade, and the slot is the countermeasure.

## Decade 7 — Years 61–70: The Long View

**The move:** you hold something no younger person can — the shape of how
knowledge actually changed across seventy years, which confident consensus
collapsed, and what turned out to matter.

- **Capture the view:** memoir, oral history, recorded conversations,
  annotated bibliographies of a life's reading, letters to successors.
- **Re-read the canon.** The books you read in Decade 1 are a different
  experience now, and reading them again with seventy years of context is
  worth doing deliberately.
- **Hand things over concretely:** books, tools, instruments, notes, and
  collections placed with named people or institutions while you can still
  explain them.
- **Honest about capacity:** scale sessions to energy, favour depth in fewer
  domains, keep the practices that protect engagement. The plan's success was
  never measured by completing every checkbox.

**Year 70 is not a finish line.** A plan written in year 1 and still running
in year 70 has already succeeded. Write the next sketch anyway.

---

## Reordering rules

The sequence is a default. Break it deliberately, under these rules:

1. **Never skip a prerequisite silently.** If you want astronomy in year 3,
   fine — but know you're reading it without the physics, and that you're
   getting a story rather than an understanding. Write the trade in your
   annual review.
2. **Pull a domain forward when life offers it.** A dig season, a class
   nearby, a friend who'll teach you, a trip to a place — opportunity beats
   sequence every time. The order exists to serve you, not the reverse.
3. **Keep the alternation.** Whatever you reorder, don't stack two hard
   prerequisite-chained domains in the same year unless the year is otherwise
   empty. That's the rule most likely to save the whole project.
4. **A domain that won't start after two attempts is telling you something.**
   Move it to a later decade and pick up its neighbour. Twice-deferred is
   information; four-times-deferred means it belongs in the anti-goals.
5. **The spike always wins.** In any year where the professional work and the
   ledger conflict, the ledger yields. A polymath with no spike is an
   audience member.

## What the spine does not schedule

Deliberately absent, and it should stay that way:

- **The curiosity budget.** Ten to twenty percent of your hours, unplanned,
  off-ledger, no artifact required. If it ever hits zero, the agenda is
  dying — that's the canary.
- **Tools and products.** Nothing with a version number appears in a
  seventy-year plan (`01-principles.md`, principle 5). Tools are learned
  just-in-time, inside projects. The frontier slot exists to catch the rare
  case where something that looks like a tool is actually a new field —
  `04-frontier.md` is how you tell the difference.
- **What fills the frontier slot.** The slot is scheduled; its contents
  cannot be. Naming in 2026 what you'll study in 2056 is precisely the error
  the slot is designed to prevent.
- **Your life.** Seventy years contains illness, moves, jobs, people, and
  losses. The spine assumes interruption; the weekly log exists to make
  restarting cheap. Any lapsed track restarts at the next weekly log, at half
  size if necessary. A plan that only works in good years isn't a plan, it's
  a wish.
