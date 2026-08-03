# Made & Applied

These are the fields where knowing and doing are the same act. A physics
paper can be right on paper; a bridge cannot. Every domain here has a
practice component that reading cannot substitute for, so the T2 sections
are heavier on *do this* than anywhere else in `resources/`.

---

## Engineering: energy & power systems

**The question it asks.** How do you move energy from where nature offers it
to where people want it — at scale, reliably, affordably — inside hard
thermodynamic and material limits? The grid is the largest machine ever
built and it must balance supply against demand *instantaneously*, forever,
with no meaningful storage in the middle. Everything else in the field is a
consequence of that constraint.

**Big ideas to walk away with.**
- Energy vs power (joules vs watts). Almost every public energy argument is
  a category error between these two.
- Thermodynamic ceilings: Carnot efficiency, and why heat engines throw away
  half of what you feed them no matter how clever you are.
- Energy density and power density — why liquid fuels won transport and why
  land area is the real constraint on renewables.
- Capacity factor vs nameplate capacity. A 100 MW wind farm is not 100 MW.
- The grid as a control system: frequency as the balance signal, inertia,
  reserves, contingency (N-1) planning.
- LCOE and its dishonesty — it prices energy, not reliability, and ignores
  integration and transmission cost.
- Storage as time-shifting, priced in $/kWh of capacity *and* $/kW of power;
  the two are different products.
- Orders of magnitude as a skill: kWh/day per person, TWh/yr per country.

**What outsiders get wrong.**
- They believe efficiency gains reduce total consumption. Historically they
  often raise it (Jevons).
- They argue about generation when transmission, permitting and land are the
  binding constraints.
- They treat "baseload vs intermittent" as the whole design problem. It is
  one of about six.

**T3 — Literacy (~150 hrs)**
- *Start here:* David MacKay, *Sustainable Energy — Without the Hot Air*
  (free at withouthotair.com). The door because it refuses to argue with
  adjectives — every claim is in kWh per person per day, and after it you
  cannot read energy journalism the same way.
- *Survey:* Vaclav Smil, *Energy: A Beginner's Guide* for the technical
  sweep; then Smil, *Energy and Civilization: A History* for why energy is
  the substrate under every other domain in this map.
- *Canon:* Sadi Carnot, *Reflections on the Motive Power of Fire* (1824) —
  short, foundational, readable. Then MacKay's technical chapters (the
  appendices, not the popular front half) and Smil's *Power Density* for the
  land-use argument done honestly.
- *Course:* MIT OpenCourseWare's *Introduction to Electric Power Systems*
  (James Kirtley) if you have calculus; MIT OCW's *Sustainable Energy* for
  the systems view. Grady Hillhouse's *Practical Engineering* videos are
  genuinely good for grid intuition and cost nothing.
- *Artifact:* MacKay's own exercise, done for yourself. Build an energy
  balance for your life in kWh/day — transport, heat, food, electricity,
  embodied goods — then build a supply stack for your country that adds up
  to it. Publish the arithmetic. If your columns don't balance, you don't
  have an opinion yet.

**T2 — Working depth**
- *Spine:* Glover, Overbye & Sarma, *Power System Analysis and Design* (the
  standard undergraduate text). Moran & Shapiro, *Fundamentals of
  Engineering Thermodynamics*. Fitzgerald, Kingsley & Umans, *Electric
  Machinery*. Alexandra von Meier, *Electric Power Systems: A Conceptual
  Introduction* is the clearest bridge from literacy into the real math.
  For the resources themselves: Manwell, McGowan & Rogers, *Wind Energy
  Explained*; Duffie & Beckman, *Solar Engineering of Thermal Processes*.
- *Practice:* Run the numbers, on real data, in real tools. Build a per-unit
  model of a small network and solve the power flow by hand, then check it
  in MATPOWER or PyPSA (both free). Do an economic dispatch and a unit
  commitment. Size a rooftop PV + battery system with NREL's PVWatts and
  SAM, price it, and compare against your actual utility bills for a year —
  then find out why your estimate was wrong. Instrument your own house with
  a clamp meter and a logger; you will discover your mental model of where
  your electricity goes is badly off. Read a real interconnection study.
- *Primary literature:* *IEEE Transactions on Power Systems*, *Applied
  Energy*, *Joule*, *Energy Policy*. The annual data documents are the
  field's shared reality: IEA *World Energy Outlook*, NREL *Annual
  Technology Baseline*, EIA *Annual Energy Outlook*. Landmarks: the
  US-Canada Task Force final report on the 2003 Northeast blackout; FERC and
  NERC's report on the February 2021 Texas cold-weather event; Schweppe et
  al., *Spot Pricing of Electricity* (1988), which invented modern
  electricity markets.
- *You've arrived when:* given a load profile, a resource dataset and a
  reliability target, you can size a generation-plus-storage portfolio,
  compute its cost, run the power flow to confirm it doesn't violate
  thermal or voltage limits, and defend it against a hostile reviewer on
  both cost and reliability.

**T1 — Mastery**
- *Graduate texts/monographs:* Wood, Wollenberg & Sheblé, *Power
  Generation, Operation, and Control*. Prabha Kundur, *Power System
  Stability and Control* (the reference for dynamics). Mohan, Undeland &
  Robbins, *Power Electronics: Converters, Applications, and Design*.
- *Frontier:* Grid-forming inverters and stability in low-inertia systems —
  the central open problem as synchronous machines retire. Long-duration
  storage chemistry and economics. Transmission expansion and
  interconnection-queue reform. Electrification of heat and industry.
  Market design that pays for reliability rather than energy. Follow NREL,
  Lawrence Berkeley National Lab's Electricity Markets and Policy group, and
  Jesse Jenkins' group at Princeton.
- *Contribution looks like:* a control scheme or market mechanism that gets
  adopted; a validated model that changes what planners assume; hardware
  that moves a cost curve; or standards work, which is undervalued and
  enormously consequential.
- *Community:* IEEE Power & Energy Society (the PES General Meeting is the
  field's town square), CIGRE, IEEE and IEC standards committees. Licensure
  matters here: the FE exam, then the PE with the NCEES Power depth exam.
  If you sign drawings that energize things, you need it.

**Beyond T1 — the long shelf**

- *Branch into:* Protection and relaying — Blackburn & Domin, *Protective
  Relaying* — owns the few cycles after a fault, where the field is least
  forgiving. High-voltage engineering — Kuffel, Zaengl & Kuffel, *High
  Voltage Engineering: Fundamentals* — owns insulation coordination and why
  clearances are the sizes they are. Power electronics — Erickson &
  Maksimović, *Fundamentals of Power Electronics* — owns the converter, now
  sitting between nearly every source and every load. Nuclear — Lamarsh &
  Baratta, *Introduction to Nuclear Engineering* — owns decay heat and the
  fuel cycle. Market design — Steven Stoft, *Power System Economics* — owns
  why the price is what it is. The demand side — Incropera & DeWitt,
  *Fundamentals of Heat and Mass Transfer* with the ASHRAE Handbook — owns
  the half of the problem generation people ignore. Combustion — Stephen
  Turns, *An Introduction to Combustion*.
- *The long canon:* Thomas P. Hughes, *Networks of Power*, the best history
  of how grids became grids and still the sharpest account of technological
  momentum. Jill Jonnes, *Empires of Light*, for the AC/DC fight told
  straight. Vaclav Smil, *Energy Transitions* for the pace argument and
  *Prime Movers of Globalization* for the machines that carry it. Richard
  Rhodes, *The Making of the Atomic Bomb*, then his *Energy: A Human
  History*. Daniel Yergin, *The Prize*, for oil as statecraft. Charles
  Perrow, *Normal Accidents* beside the Kemeny Commission report on Three
  Mile Island. IAEA's INSAG-7 on Chernobyl, then Serhii Plokhy's *Chernobyl*
  — one event as engineering and as a state. Meredith Angwin, *Shorting the
  Grid*: partisan, sometimes wrong, and the clearest thing written on who
  actually governs a grid. Gretchen Bakke's *The Grid* is readable and thin;
  keep the anecdotes, not the analysis. Then make event reports a standing
  habit — AEMO on the 2016 South Australia black system, Ofgem and NGESO on
  9 August 2019, and whatever comes next.
- *The project ladder:*
  1. A weekend: clamp meter and plug loggers on your own house, a real load
     profile, and a prediction of next month's bill to within 5%.
  2. A standalone PV-battery system — panel, controller, battery, load —
     sized by hand, then metered for a season until you can account for
     every missing kilowatt-hour.
  3. A logging power monitor you built, publishing a year of one-second data
     with the calibration documented.
  4. A replication: rebuild a published dispatch or capacity-expansion study
     in PyPSA or MATPOWER from public data, and find where you disagree.
  5. A bench DC-AC converter under closed-loop control, into a resistive
     load only. Grid-tying is licensed work and the mistake is lethal.
  6. A Stirling or small heat engine you machined and instrumented, whose
     measured efficiency you can place honestly against Carnot.
  7. A building retrofit — envelope, heat pump sizing, controls — with
     metered consumption across two heating seasons either side.
  8. A year of maintained contribution to an open model or dataset others
     plan with: PyPSA, the Open Energy Modelling Initiative.
  9. The decade project: a real asset — community solar, a microgrid, a
     small hydro rebuild — permitted, interconnected, commissioned, and
     metered for a year against what you promised.
- *Re-foundation watch:* thermodynamics, power flow, electromagnetics and
  energy density will be exactly as true in 2065, and so will the fact that
  demand is a human behaviour rather than a curve. What moves: storage
  chemistry and its cost curve, inverter-dominated stability (an open
  problem now, probably a solved one then), market rules, interconnection
  law, and every software tool you learn. Rebuy the cost data every five
  years and the toolchain every ten. Do not rebuy Carnot.
- *A lifetime practice:* keep MacKay's household ledger and re-run it each
  decade — it becomes a fifty-year dataset nobody else has. Maintain
  something that generates or stores. Sit on a rural co-op board, a
  municipal utility commission or a planning body, where the decisions are
  actually made by people who mostly cannot read a load-duration curve.
- *Rabbit holes:* the 1965 Northeast blackout and the founding of NERC; grid
  frequency used as a clock, and time-error correction; ferroresonance;
  Danish district heating; the TVA as an institution.

---

## Engineering: structures & the built environment

**The question it asks.** How do you get load safely into the ground using
the least material, when the consequences of being wrong are measured in
lives? Underneath the arithmetic is a design question — *choosing* the path
force will take — and above it a temporal one: buildings outlive their
designers, their uses, and often their assumptions.

**Big ideas to walk away with.**
- The load path. Every force must reach the soil by a continuous route, and
  the engineer's real job is deciding that route before calculating it.
- Stress vs strain; strength vs stiffness. A thing can be strong and
  unusably bouncy, or stiff and brittle.
- Section properties: moment of inertia and section modulus explain why
  I-beams, tubes and hollow bones all look the way they do.
- Buckling. Slender members fail by instability at loads far below crushing.
  This is the single most counterintuitive fact in the field.
- Materials have sides: concrete and masonry take compression, steel and
  cable take tension, and reinforced concrete is a marriage of the two.
- Limit states and safety factors — engineering under uncertainty, not
  under certainty.
- Redundancy and progressive collapse. A structure that fails gracefully is
  a different design from one that merely doesn't fail.
- Codes are compressed failure history. Every clause is a memorial.
- Buildings change; embodied carbon and maintenance dominate the lifetime
  ledger, not the day-one cost.

**What outsiders get wrong.**
- They think the work is arithmetic. The arithmetic is checkable; choosing
  the scheme is the judgment, and that's where careers are made.
- They confuse architects and structural engineers, then wonder why nobody
  can answer their question.
- They read codes as bureaucracy. Read the NIST report on any collapse and
  you'll never say that again.

**T3 — Literacy (~150 hrs)**
- *Start here:* J.E. Gordon, *Structures: Or Why Things Don't Fall Down*.
  The door because Gordon teaches you to *see* force in ordinary objects,
  with almost no mathematics and no condescension.
- *Survey:* Mario Salvadori, *Why Buildings Stand Up*, paired with Levy &
  Salvadori, *Why Buildings Fall Down*. Read them as a set — the second is
  the exam for the first.
- *Canon:* Vitruvius, *Ten Books on Architecture* (Book I, for the ancient
  triad of firmitas, utilitas, venustas — skip the war machines unless
  curious). Gordon, *The New Science of Strong Materials*. Henry Petroski,
  *To Engineer Is Human*, for design as a failure-driven process. David
  Billington, *The Tower and the Bridge*, for structural art as a
  discipline with its own aesthetics. Stewart Brand, *How Buildings Learn*,
  for the time dimension the textbooks omit.
- *Course:* MIT OCW 1.050 *Engineering Mechanics I* is the real thing and is
  free — statics and mechanics of materials, which is the entire foundation.
  Do the problem sets or don't bother.
- *Artifact:* Pick a structure you can physically walk to — a bridge, a
  parking garage, a market hall. Draw its load path from roof to soil.
  Estimate the loads (ASCE 7 gives you the numbers). Write 1,500 words on
  why it is shaped the way it is and what would have changed if the span
  doubled.

**T2 — Working depth**
- *Spine:* Hibbeler, *Structural Analysis* and *Mechanics of Materials*
  (or Beer & Johnston for the latter). Then the design texts: Segui, *Steel
  Design*, and McCormac & Brown, *Design of Reinforced Concrete*. The three
  documents you'll actually work from are ASCE 7 (loads), the AISC *Steel
  Construction Manual*, and ACI 318 (concrete). Own or borrow them; the
  texts teach you to read them.
- *Practice:* Hand-calculate before you ever open software, then check
  yourself in OpenSees or a student license — software that you cannot
  sanity-check by hand is a liability, and this is how engineers actually
  get hurt. Do a complete gravity load takedown on a small building, then
  add wind and seismic. Produce a calculation package another engineer could
  check without phoning you. Build physical models and load them to failure —
  balsa or spaghetti bridges, predicted capacity written down *before* the
  test — because the gap between your prediction and the break is the
  fastest feedback in the field.
- *Primary literature:* ASCE *Journal of Structural Engineering*,
  *Engineering Structures*, *Structure* magazine for practice. The
  landmarks are forensic: the NIST investigations (World Trade Center,
  Champlain Towers South) and the Hyatt Regency walkway collapse
  literature — study them as an ethics curriculum as much as a technical
  one. Add Fazlur Khan's papers on tube structures, which made the modern
  tall building possible.
- *You've arrived when:* handed architectural drawings, you can produce a
  code-compliant structural scheme with member sizes, connections and a
  checkable calculation package — and explain to the architect what her
  design costs in steel.

**T1 — Mastery**
- *Graduate texts/monographs:* Timoshenko & Gere, *Theory of Elastic
  Stability*; Timoshenko & Woinowsky-Krieger, *Theory of Plates and
  Shells*; Anil Chopra, *Dynamics of Structures* (the seismic standard);
  K.J. Bathe, *Finite Element Procedures*; Cook, Malkus, Plesha & Witt,
  *Concepts and Applications of Finite Element Analysis*.
- *Frontier:* Performance-based seismic design replacing prescriptive
  codes. Mass timber and low-carbon concrete. Embodied-carbon accounting as
  a design constraint with real teeth. Digital fabrication and
  non-repetitive geometry. Designing for climate loads that no longer match
  the historical record the codes were calibrated on. Follow PEER (Pacific
  Earthquake Engineering Research Center), NIST, and the Carbon Leadership
  Forum.
- *Contribution looks like:* experimental programs that change a code
  provision, new analysis methods that get adopted, forensic work that
  establishes why something failed, or built structures that advance the
  art.
- *Community:* ASCE/SEI, IABSE, AISC, ACI, EERI. Licensure is not optional
  in this field: FE, then PE, then the SE in jurisdictions that require it;
  CEng through the Institution of Structural Engineers in the UK.

**Beyond T1 — the long shelf**

- *Branch into:* Geotechnical engineering — Terzaghi, Peck & Mesri, *Soil
  Mechanics in Engineering Practice* — owns the half of the load path below
  grade, which is the half that surprises people. Wind engineering — Simiu &
  Scanlan, *Wind Effects on Structures* — owns everything tall. Masonry and
  limit analysis — Jacques Heyman, *The Stone Skeleton* — owns why Gothic
  vaults stand and why elastic analysis lies about them. Structural fire —
  Buchanan & Abu, *Structural Design for Fire Safety* — owns the load case
  that actually destroys buildings. Timber — the USDA Forest Products
  Laboratory's *Wood Handbook* (free) — owns the material now displacing
  concrete at mid-rise. Bridges — Chen & Duan, *Bridge Engineering Handbook*
  — owns long spans and fatigue under traffic. Building science — Straube &
  Burnett, *Building Science for Building Enclosures*, plus Ching's *Building
  Construction Illustrated* for assembly literacy.
- *The long canon:* Bill Addis, *Building: 3000 Years of Design Engineering
  and Construction* — the single best long history. Robert Mark, *Light,
  Wind, and Structure*, for medieval builders reverse-engineered with modern
  analysis. Eduardo Torroja, *Philosophy of Structures*, and Pier Luigi
  Nervi, *Aesthetics and Technology in Building* — two masters arguing that
  form is a structural act. Billington, *Robert Maillart's Bridges*, as the
  case study for the argument. David McCullough, *The Great Bridge* and *The
  Path Between the Seas*, for what building costs in lives and politics.
  Petroski, *Design Paradigms* and *To Forgive Design*, for error as a
  discipline. Heyman, *The Science of Structural Engineering*, for the
  intellectual history. Then the failure literature, forever: the NIST NCSTAR
  reports; Ronan Point (1968) and the invention of progressive-collapse
  design; Billah & Scanlan's 1991 paper correcting what physics textbooks
  say about Tacoma Narrows; the Citicorp Center retrofit. Stewart Brand and
  Jane Jacobs belong here too — buildings are used by people, and the codes
  are silent on that.
- *The project ladder:*
  1. A weekend: build a model truss or beam, write down the predicted
     failure load, then break it. The gap is the lesson.
  2. Something real and small, designed by you to code with a calculation
     package behind it — a deck, a shed, a retaining wall.
  3. A traditional timber frame, cut and raised, at a workshop. Joinery
     that resists by geometry teaches what fasteners hide.
  4. Instrument a real footbridge with accelerometers, extract the modal
     frequencies, and compare them to your hand model.
  5. The full package for a small building: gravity, wind, seismic,
     foundations, connections, drawings — then pay a licensed engineer to
     review it and take the correction.
  6. A form-found structure: a gridshell, a cable net, a thin concrete
     shell, or a Guastavino-style tile vault. You cannot compute your way
     there; you find the shape and then verify it.
  7. A forensic investigation of a real local failure or distress case,
     worked from evidence rather than from the news account.
  8. The decade project: take a building from sketch through permitting,
     construction and a year of monitored performance — or lead the repair
     of a historic structure, which is harder.
- *Re-foundation watch:* statics, mechanics of materials, buckling, soil
  behaviour and load paths are permanent, and so is the fact that people
  occupy buildings badly. What churns: the codes themselves, which revise on
  roughly six-year cycles and which you re-buy rather than re-learn;
  analysis software; low-carbon cement chemistries; mass timber's tall-
  building provisions; and the climate hazard maps, which are being
  recalibrated because the historical record the codes assumed no longer
  holds. That last one is a genuine re-foundation, not a tool update.
- *A lifetime practice:* draw the load path of every building you enter,
  for decades, in a notebook. Own and maintain a building. Serve on a code
  committee or a local board of building appeals — dull, and where the
  memorials get written. Mentor engineers through licensure.
- *Rabbit holes:* Guastavino tile vaulting; hanging-chain form-finding from
  Gaudí to Heinz Isler; the Citicorp Center quiet retrofit of 1978; Roman
  concrete and the pozzolan literature; post-tensioning failures and what
  Champlain Towers South taught about inspection.

---

## Engineering: machines, manufacturing & transport

**The question it asks.** How do you turn an intention into a mechanism that
works reliably for years — and then make a million of them at a price
someone will pay? Design and production are not two problems. The process
you'll use determines the geometry you're allowed to draw, and the volume
determines the process.

**Big ideas to walk away with.**
- Kinematics before strength: degrees of freedom, constraint, and the
  difference between a mechanism and a structure.
- Tolerances and stack-up. Nothing is a dimension; everything is a
  distribution. GD&T exists because "make it 10 mm" is meaningless.
- Exact constraint — over-constrain a part and it will bind, distort, or
  crack, and no amount of extra steel fixes it.
- Fatigue. Machines die from cycles, not from single loads. Static strength
  is the easy half.
- Friction, lubrication and wear — tribology is where machines actually
  fail in service.
- Design for manufacture: the drawing is a purchase order for a process.
- Wright's law / the learning curve: unit cost falls a predictable
  percentage per doubling of cumulative volume. This is the most powerful
  fact in manufacturing.
- The Toyota Production System: flow, pull, takt time, jidoka — and
  inventory as a *symptom* of problems, not an asset.
- Transport physics: rolling resistance, drag rising with the square of
  speed, and the Breguet range equation. These three explain most of why
  vehicles look the way they do.

**What outsiders get wrong.**
- They think manufacturing is a commodity to be outsourced. It's the hard
  part, and the knowledge lives on the floor, not in the CAD file.
- They think 3D printing displaces mass production. It displaces tooling for
  low volumes, which is a different and much smaller claim.
- They think lean means cutting headcount. Ohno's system is about exposing
  problems by removing the buffers that hide them.

**T3 — Literacy (~200 hrs, including shop time)**
- *Start here:* David Macaulay, *The Way Things Work Now*. Do not skip it
  because it looks like a children's book — it is the best mechanism-literacy
  text in print, and adults consistently learn from it.
- *Survey:* Womack, Jones & Roos, *The Machine That Changed the World* —
  the study that showed manufacturing systems, not just factories, differ by
  orders of magnitude in performance. Then Eliyahu Goldratt, *The Goal*, a
  novel about constraints that teaches more operations theory than most
  textbooks.
- *Canon:* Taiichi Ohno, *Toyota Production System*, in his own terse voice.
  Henry Petroski, *To Engineer Is Human*. Matthew Crawford, *Shop Class as
  Soulcraft*, for why this work is worth doing at all. Frederick Taylor,
  *The Principles of Scientific Management* — read it critically; it is both
  foundational and the origin of much that Ohno was reacting against.
- *Course:* MIT OCW 2.007 *Design and Manufacturing I* — the materials
  include the design process and the contest that motivates it. Supplement
  with machining channels that show real chips being cut (This Old Tony,
  NYC CNC); watching an experienced machinist think aloud is worth more per
  hour than most lectures.
- *Artifact:* Take a machine apart — a bicycle derailleur, a stapler, a hard
  drive, a cordless drill. Photograph and catalogue every part. For each
  one: its function, its material, and the process that made it (die cast?
  stamped? injection moulded? screw machine?). Then write 1,500 words on why
  each choice was made and what would change at 100x the volume.

**T2 — Working depth**
- *Spine:* Budynas & Nisbett, *Shigley's Mechanical Engineering Design* —
  the machine-design bible; work the fatigue and bearing chapters properly.
  Kalpakjian & Schmid, *Manufacturing Engineering and Technology*, for
  processes. *Machinery's Handbook* (Industrial Press) is the reference you
  buy once and keep forever.
- *Practice:* Learn parametric CAD and then *make the parts*. 3D print, then
  take a community-college machining course and cut metal on a manual lathe
  and mill — the tactile knowledge of feeds, speeds and how a part moves when
  you clamp it does not come from screens. Design an assembly with real
  tolerances and have it fit on the first try; the first time you do this it
  will feel like magic and it is just arithmetic. Do a complete gearbox
  design with bearing life and fatigue calculations. Build and instrument a
  test rig, and compare measurement to prediction. Then run a batch of 50
  identical items and measure your own yield, cycle time and scrap rate.
  Fifty is the number where manufacturing stops being a word and becomes a
  problem.
- *Primary literature:* ASME *Journal of Mechanical Design*, *Journal of
  Manufacturing Science and Engineering*, SAE technical papers. Landmarks:
  Ohno, *Toyota Production System*; Hopp & Spearman, *Factory Physics* (the
  quantitative theory of production, and the antidote to lean-as-slogan);
  Daniel Whitney, *Mechanical Assemblies*.
- *You've arrived when:* you can take a functional requirement to a released
  drawing package — dimensions, tolerances, materials, finish, process and
  a defensible cost per unit at 1,000 volume — and a vendor can quote and
  make it without calling you for clarification.

**T1 — Mastery**
- *Graduate texts/monographs:* Uicker, Pennock & Shigley, *Theory of
  Machines and Mechanisms*. Hosford & Caddell, *Metal Forming: Mechanics and
  Metallurgy*. Milton Shaw, *Metal Cutting Principles*. Douglass Blanding,
  *Exact Constraint: Machine Design Using Kinematic Principles*, and Smith &
  Chetwynd, *Foundations of Ultraprecision Mechanism Design*, for the
  precision end. Hopp & Spearman, *Factory Physics*, again — it is a
  graduate text pretending to be readable.
- *Frontier:* Qualification of additively manufactured parts for safety-
  critical use. Flexible automation that pays off at low volume. Battery and
  EV manufacturing scale-up, which is currently the world's largest applied
  manufacturing problem. Reshoring and supply-chain resilience as an
  engineering rather than political question. Follow SME, the ASME design
  conferences, and teardown analysts like Munro & Associates.
- *Contribution looks like:* a process nobody could run before, a machine
  that holds a tolerance nobody could hold, a patent that gets practiced, or
  a production system that hits a cost and quality point competitors can't.
- *Community:* ASME, SAE, SME. PE licensure (mechanical) for consulting and
  anything safety-critical. Note that the machining apprenticeship-to-
  journeyman route is a parallel and fully legitimate ladder to mastery
  here, and the two ladders respect each other more than outsiders assume.

**Beyond T1 — the long shelf**

- *Branch into:* Tribology — Stachowiak & Batchelor, *Engineering Tribology*
  — owns friction, lubrication and wear, which is how machines actually die.
  Precision engineering — Alexander Slocum, *Precision Machine Design*, and
  Wayne Moore, *Foundations of Mechanical Accuracy* — owns the question of
  how you make anything accurate using only things less accurate than it.
  Control and mechatronics — Franklin, Powell & Emami-Naeini, *Feedback
  Control of Dynamic Systems* — owns everything that has to hold a value.
  Welding metallurgy — Sindo Kou, *Welding Metallurgy* — owns the joint,
  where fatigue starts. Vehicle dynamics — Gillespie, *Fundamentals of
  Vehicle Dynamics*, then Milliken & Milliken, *Race Car Vehicle Dynamics*.
  Flight — Anderson, *Introduction to Flight*, then Raymer, *Aircraft
  Design*. Reliability — O'Connor & Kleyner, *Practical Reliability
  Engineering* — owns the arithmetic of "how long will it last", which
  almost no designer can actually do.
- *The long canon:* David Hounshell, *From the American System to Mass
  Production, 1800–1932* — how interchangeable parts were really achieved,
  and how long it took. L.T.C. Rolt, *Tools for the Job*, for the machine
  tools underneath. Robert Kanigel, *The One Best Way*, on Taylor, read
  against Ohno. Sloan, *My Years with General Motors*, and Ford, *My Life
  and Work*, as primary sources by people who were wrong in instructive
  ways. Shigeo Shingo, *A Revolution in Manufacturing: The SMED System* —
  changeover time as the hinge of everything. Ben Rich, *Skunk Works*, and
  Kelly Johnson's *Kelly*, for small-team engineering done at speed. Then
  the failure library, which is this field's real literature: Diane Vaughan,
  *The Challenger Launch Decision* — the best book on how competent
  organizations normalize deviance; Nancy Leveson, *Engineering a Safer
  World*; Sidney Dekker, *The Field Guide to Understanding 'Human Error'*;
  Perrow, *Normal Accidents*; and the 737 MAX documents — the JATR report
  and the Indonesian KNKT final report on Lion Air 610 — read as an
  engineering-management failure rather than a software one.
- *The project ladder:*
  1. A weekend: a mechanism from scratch — a Geneva drive, a Peaucellier
     linkage — printed or cut, then measured against its intended motion.
  2. Restore a machine to working spec: a hand plane, a small engine, a
     bicycle. You find out what "spec" means by having to meet one.
  3. An assembly of a dozen parts with a real tolerance stack-up, made and
     fitted first-article. Getting this right once feels like magic.
  4. Hold a tenth on a manual lathe and mill — then make five identical,
     which is a different and much harder problem.
  5. A gearbox designed with bearing life and fatigue calculations, built,
     run to failure, and compared against the prediction.
  6. A machine that makes something: a small CNC, a wire bender, a filament
     extruder. Then use it on a real job until it annoys you.
  7. A vehicle to a stated spec — an electric bike, a kart, a boat — where
     range, mass and drag were predicted before they were measured.
  8. A production run of 200–500 units with SPC, yield tracking and a
     customer who complains. This is where manufacturing becomes real.
  9. The decade project: scrape a machine tool in against a surface plate,
     or build a lathe from castings. Making a precise machine with
     imperfect tools is the field's oldest and deepest trick.
- *Re-foundation watch:* kinematics, fatigue, tribology, tolerance theory,
  Wright's law and factory physics are permanent — they were true for
  Whitworth and will be true for whatever replaces the factory. What churns:
  the CAD/CAM stack, which you will relearn perhaps five times; additive
  processes and their qualification regimes; battery and drive-unit
  manufacturing, currently the largest applied problem on earth; automation
  economics; and supply-chain geography, which is politics wearing an
  engineering hat. Relearn the toolchain. Do not relearn stress
  concentration factors.
- *A lifetime practice:* a shop with a running logbook — every job, every
  setup, every scrap part and why. Maintain your own vehicles and machines.
  Make one tool a year. Teach a machining or CAD class at a community
  college, which is where this knowledge is actually transmitted.
- *Rabbit holes:* Whitworth and the origin of standard threads; the
  three-plate method for generating a flat surface from nothing; Watt's
  parallel motion; containerization (Marc Levinson, *The Box*); the Wankel
  apex seal; the Bessemer process and why it was abandoned.

---

## Computing in practice (systems, networks, software)

**The question it asks.** How do you make a machine that does exactly what
you said do what you actually meant — at scale, while parts of it are
failing, while people keep changing the requirements, and while adversaries
probe it? The durable problems are abstraction, state, concurrency, partial
failure, and human coordination. None of them are about a language.

**Big ideas to walk away with.**
- The abstraction stack from transistor to browser — and that every layer
  leaks under load, which is why you must be able to descend.
- The memory hierarchy and latency numbers. Performance is mostly about how
  far the data has to travel.
- Concurrency vs parallelism, and why shared mutable state is the source of
  the bugs you cannot reproduce.
- The network is not reliable. Partial failure, timeouts, retries and
  idempotency are the whole discipline of distributed systems in four words.
- Consistency has a price: replication, consensus, and the tradeoffs CAP
  gestures at (and oversimplifies).
- Naming, caching, and invalidation — the recurring hard problems at every
  layer.
- Version control and reproducible builds as the substrate that makes
  collaboration possible at all.
- Brooks' essential vs accidental complexity, and that complexity — not
  compute — is the binding cost of software.
- Security as systematic assumption-checking, not a feature you add.

**What outsiders get wrong.**
- They mistake the tool churn for the field. The framework of the moment is
  a three-year artifact sitting on fifty-year ideas. Per this repo's
  principles, learn tools just-in-time inside a project; never schedule them.
- They assume programming ability equals systems ability. Writing code and
  reasoning about a system under failure are different skills, and the
  second is rarer.
- They believe adding people accelerates a late project.

**T3 — Literacy (~250 hrs)**
- *Start here:* Charles Petzold, *Code: The Hidden Language of Computer
  Hardware and Software* (2nd ed.). The door because it builds a computer
  from flashlights and relays, so "it's just electricity and logic" stops
  being a slogan and becomes something you've watched happen.
- *Survey:* Harvard **CS50** (free on edX) — still the best on-ramp to
  computing in existence. Finish it, including the final project. Do not
  watch it; do it.
- *Canon:* Fred Brooks, *The Mythical Man-Month* — read chapters 1–3, 11,
  and "No Silver Bullet"; skip the PL/I-era specifics. Kernighan & Pike,
  *The Practice of Programming*, for taste in the small. Abelson &
  Sussman, *Structure and Interpretation of Computer Programs* (free
  online) — read chapters 1 and 2; if it grips you, keep going, and if it
  doesn't, that is a legitimate outcome rather than a moral failure.
- *Course:* MIT's *The Missing Semester of Your CS Education* (free) —
  shell, git, editors, debugging, profiling. Roughly a week of work that
  removes years of friction. It is the highest-leverage free course in this
  entire file.
- *Artifact:* Build and deploy something small that strangers actually use,
  then write it up: what broke, what you measured, what you'd change.
  Separately, write 1,500 words tracing everything that happens between
  typing a URL and pixels appearing — DNS, TCP, TLS, HTTP, rendering. If you
  can do that honestly you are literate.

**T2 — Working depth**
- *Spine:* Bryant & O'Hallaron, *Computer Systems: A Programmer's
  Perspective* — the single best systems book, and the labs are the point.
  Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (free). Kurose &
  Ross, *Computer Networking: A Top-Down Approach*. Martin Kleppmann,
  *Designing Data-Intensive Applications* — the modern bridge between theory
  and what you'll build.
- *Practice:* Implement, don't read. A shell. An HTTP server from a raw
  socket. A key-value store with a write-ahead log and crash recovery. A toy
  TCP. A Raft implementation that survives a partition test. Write something
  in C, Rust or Go, profile it, and make it three times faster with
  measurements rather than guesses. Then the part most people skip: *run*
  something in production for a year — monitoring, alerts, on-call, and a
  written postmortem after every incident. Operating your own system for
  twelve months teaches things no book contains. Finally, read a large
  codebase you didn't write and land a merged patch in it.
- *Primary literature:* USENIX venues (OSDI, NSDI, ATC, SREcon), SIGCOMM,
  *ACM Queue*. Landmarks: Leslie Lamport, "Time, Clocks, and the Ordering of
  Events in a Distributed System" (1978); Ritchie & Thompson, "The UNIX
  Time-Sharing System"; Google's GFS, MapReduce and Bigtable papers and
  Amazon's Dynamo paper, read as a set; Google's *Site Reliability
  Engineering* (free online).
- *You've arrived when:* handed an unfamiliar production system that is
  misbehaving, you can diagnose it from measurements rather than hunches —
  and, given a stated load and failure budget, design a system and defend
  every tradeoff in it.

**T1 — Mastery**
- *Graduate texts/monographs:* Hennessy & Patterson, *Computer
  Architecture: A Quantitative Approach*. Herlihy & Shavit, *The Art of
  Multiprocessor Programming*. Cachin, Guerraoui & Rodrigues, *Introduction
  to Reliable and Secure Distributed Programming*. Gray & Reuter,
  *Transaction Processing: Concepts and Techniques*. Pierce, *Types and
  Programming Languages*, if you go the languages route.
- *Frontier:* Hardware/software co-design now that single-thread scaling is
  over; heterogeneous accelerators; formal verification finally reaching
  production systems; confidential computing; the systems problems created
  by machine-learning workloads. Follow the proceedings, not the vendors —
  and follow individual researchers and practitioners who publish.
- *Contribution looks like:* a paper at a systems venue, or — equally
  legitimate in this field, unlike most — a widely-adopted open-source
  system, an IETF RFC, or operational knowledge published so others stop
  relearning it.
- *Community:* ACM, USENIX, IETF, and the maintainer communities of whatever
  you depend on. There is no licensure. Your credential is your code, your
  review history, and what you've kept running.

**Beyond T1 — the long shelf**

- *Branch into:* Compilers — Appel, *Modern Compiler Implementation*, or the
  dragon book (Aho, Lam, Sethi & Ullman) — owns the gap between what you
  wrote and what runs. Databases — Bailis, Hellerstein & Stonebraker's
  *Readings in Database Systems* (the Red Book, free) and Bernstein &
  Newcomer, *Principles of Transaction Processing* — owns durability, which
  everything else assumes. Security — Ross Anderson, *Security Engineering*
  (3rd ed., free) — owns adversarial reasoning, and is the best-written
  systems book in existence. Cryptography — Boneh & Shoup, *A Graduate
  Course in Applied Cryptography* (free). Formal methods — Lamport,
  *Specifying Systems* (TLA+, free) — owns the designs you can check before
  building. Performance — Brendan Gregg, *Systems Performance* — owns the
  methodology, not the tricks. Embedded and real-time — Lee & Seshia,
  *Introduction to Embedded Systems* (free) — owns everything with a
  deadline. Type theory and language design — Harper, *Practical Foundations
  for Programming Languages*.
- *The long canon:* Knuth, *The Art of Computer Programming*, which is a
  twenty-year project and should be treated as one — a section at a time,
  forever. Peter Naur, "Programming as Theory Building" (1985), the best
  fifteen pages ever written on why software rots. Parnas, "On the Criteria
  To Be Used in Decomposing Systems into Modules" (1972). Hoare's Turing
  lecture, "The Emperor's Old Clothes". Dijkstra's EWDs, read as a
  temperament rather than a method. Lions' *Commentary on UNIX 6th Edition*
  — a whole operating system you can read in an evening. Kernighan, *UNIX:
  A History and a Memoir*. Weinberg, *The Psychology of Computer
  Programming*, still the sharpest thing on the human half. Brooks, *The
  Design of Design*. Tracy Kidder, *The Soul of a New Machine*. Michael
  Abrash's *Graphics Programming Black Book* (free) for the measurement
  mindset, obsolete in every specific and correct in every general. And the
  failure canon: Leveson & Turner's "An Investigation of the Therac-25
  Accidents" (1993), which should be read once a decade.
- *The project ladder:*
  1. A weekend: a script that removes a chore you do weekly — then keep it
     running, unbroken, for a year. That second part is the project.
  2. A published tool with docs, tests, packaging and versioning, used by
     strangers who file issues you did not anticipate.
  3. A service you operate: API, database, deploys, backups, monitoring —
     and a restore drill you actually perform, not one you documented.
  4. An interpreter, then a compiler for a small language with a real
     backend. Nystrom's *Crafting Interpreters* (free) is the on-ramp.
  5. A storage engine — LSM or B-tree — with a write-ahead log, crash
     recovery, and fault injection that you trust because it found bugs.
  6. A distributed system that survives adversarial testing: Raft or a
     replicated store against Jepsen-style partitions. MIT's 6.5840 labs
     are free and remain the standard route.
  7. A hobby OS that boots on real hardware, or a driver merged upstream
     into the Linux kernel. Both teach that hardware is not an abstraction.
  8. Maintainership: sustained ownership of something others depend on —
     the review load, the releases, the security disclosures, the saying no.
  9. The decade project: publish something original — a system with a paper
     at OSDI or NSDI, or a library people build on for ten years. In this
     field those are equally legitimate, which is unusual.
- *Re-foundation watch:* the memory hierarchy, concurrency, partial failure,
  the consensus impossibility results, complexity theory and the human
  factors of being on call at 3 a.m. are permanent. Lamport's 1978 paper
  will be correct in 2065. What churns, and churns fast: languages,
  frameworks, cloud APIs, orchestration, and the entire machine-learning
  toolchain, which has the shortest half-life of anything in this file.
  Expect to rebuild your working toolkit every five to eight years, learn it
  inside a project, and never schedule it. Two genuine re-foundations are
  visible from here: post-quantum migration, which invalidates deployed
  cryptography rather than merely dating it, and hardware heterogeneity,
  which changes the constants that architecture reasoning depends on.
- *A lifetime practice:* run something for decades — a mail server, a site,
  a home lab, a backup regime whose restores you test annually. Keep an
  incident journal and reread it. Review other people's code weekly.
  Publish operational knowledge so the next person stops relearning it.
- *Rabbit holes:* Therac-25 in full; Multics and what Unix chose not to
  inherit; the RFC process as a governance invention; Postel's law and its
  critics; leap seconds; SQLite's testing regime, which is stranger and more
  rigorous than almost any commercial equivalent.

---

## Public health & care systems

**The question it asks.** What makes *populations* healthy — as opposed to
patients — and how do you find that out when the experiment you'd want to
run is unethical, impossible, or forty years long? Then the harder half: how
do you build institutions that deliver it under scarcity, politics, and
public distrust.

**Big ideas to walk away with.**
- Population thinking, and Geoffrey Rose's prevention paradox: a large
  number of people at small risk produce more cases than the small number at
  high risk. This inverts most intuitions about where to intervene.
- Confounding, selection bias, and the machinery of causal inference from
  observational data — the field's central methodological problem.
- Incidence vs prevalence; absolute vs relative risk; number needed to
  treat. Most health reporting fails on these alone.
- Transmission dynamics: R0 and Re, herd immunity thresholds, and why
  exponential growth defeats human intuition every single time.
- Screening's hidden harms: lead-time bias, length bias, overdiagnosis. More
  detection is not more health.
- Social determinants — income, education, housing, air — dwarf clinical
  care in their effect on population outcomes.
- Health systems trade access, cost and quality against each other; every
  country has picked a point on that surface and calls it common sense.
- Surveillance infrastructure is the precondition for all of the above, and
  it is boring, underfunded, and decisive.

**What outsiders get wrong.**
- They read "risk doubled" without asking doubled from what. Twice a tiny
  number is a tiny number.
- They equate more medicine with more health, and are surprised by the
  weak correlation between spending and outcomes across rich countries.
- They think public health is a technical field. It is roughly a third
  technical, a third law and logistics, a third persuasion.

**T3 — Literacy (~150 hrs)**
- *Start here:* Steven Johnson, *The Ghost Map*. The door because it shows
  you an epidemiological argument being constructed — John Snow assembling
  evidence against the consensus — rather than telling you its conclusion.
- *Survey:* Kenneth Rothman, *Epidemiology: An Introduction*. Short, written
  by a master of the field, and it teaches the concepts rather than the
  vocabulary. Pair with Atul Gawande's essays for the delivery side.
- *Canon:* John Snow, *On the Mode of Communication of Cholera* (1855, free
  online) — read the Broad Street pump section and the South London water
  supply comparison, which is the first natural experiment. Geoffrey Rose,
  *Rose's Strategy of Preventive Medicine*, is the field's philosophical
  core in under 150 pages. John Barry, *The Great Influenza*, and Siddhartha
  Mukherjee, *The Emperor of All Maladies*, for medicine as an institution
  under pressure.
- *Course:* Johns Hopkins' *Epidemiology in Public Health Practice*
  specialization on Coursera, from the field's leading school; UNC Chapel
  Hill's *Epidemiology: The Basic Science of Public Health* is a gentler
  free alternative. Both are auditable at no cost.
- *Artifact:* Take a health claim currently in the news. Find the actual
  study behind it. Write 1,500 words on its design, its plausible
  confounders, the absolute (not relative) risk change, and whether the
  headline survives contact with the paper. Do this three times and you will
  never be fooled the same way again.

**T2 — Working depth**
- *Spine:* Rothman, Greenland & Lash, *Modern Epidemiology* — the standard.
  Hernán & Robins, *Causal Inference: What If* (free PDF), which is the
  modern methodological spine and worth the struggle. For the systems half:
  Roberts, Hsiao, Berman & Reich, *Getting Health Reform Right*, plus a
  serious statistics text for health data.
- *Practice:* Get real data and analyze it yourself in R or Python — NHANES,
  BRFSS, CDC WONDER, the Demographic and Health Surveys, the Global Burden
  of Disease results tool are all free and open. Reproduce a published
  table from raw data; the discrepancies teach you what papers omit. Build
  an SEIR model and fit it to a real outbreak's case counts, then watch how
  badly it does out of sample. Run a cost-effectiveness analysis with QALYs
  on an actual intervention. And spend time inside a real program or clinic,
  because the gap between the protocol and what happens at the front desk is
  where public health actually lives or dies.
- *Primary literature:* *The Lancet*, *NEJM*, *American Journal of
  Epidemiology*, *Health Affairs*, and the CDC's *MMWR* — read *MMWR*
  weekly, it's how the field talks in real time. Landmarks: Doll & Hill's
  British Doctors Study on smoking; the Framingham Heart Study papers;
  Michael Marmot's Whitehall studies on status and mortality.
- *You've arrived when:* given a raw surveillance dataset and a policy
  question, you can specify a study design, defend it against the
  confounding a reviewer will raise, run the analysis, quantify the
  uncertainty honestly, and write it so a decision-maker who hates
  statistics can act on it.

**T1 — Mastery**
- *Graduate texts/monographs:* *Modern Epidemiology* (Rothman, Greenland &
  Lash) and *Causal Inference: What If* (Hernán & Robins) at full depth.
  Anderson & May, *Infectious Diseases of Humans: Dynamics and Control*, and
  Keeling & Rohani, *Modeling Infectious Diseases in Humans and Animals*,
  for the modeling track. Fitzmaurice, Laird & Ware, *Applied Longitudinal
  Analysis*. Neumann et al., *Cost-Effectiveness in Health and Medicine*,
  for the economic evaluation track.
- *Frontier:* Causal inference from routinely-collected electronic health
  records; genomic and wastewater surveillance; pandemic preparedness
  governance after 2020; measuring health equity in ways that survive
  scrutiny; health-system strengthening in low- and middle-income
  countries. Follow IHME, the WHO, and Miguel Hernán's group.
- *Contribution looks like:* an original study that changes practice, a
  method that others adopt, or an intervention you evaluated rigorously and
  then scaled.
- *Community:* American Public Health Association, Society for Epidemiologic
  Research, International Epidemiological Association. Credentials: the MPH
  is the field's entry ticket, the CPH exam certifies it, and state or local
  health-department practice is where most of the real work happens.

**Beyond T1 — the long shelf**

- *Branch into:* Survival analysis — Kleinbaum & Klein, *Survival Analysis:
  A Self-Learning Text* — owns time-to-event, which is most of clinical
  epidemiology. Health economics — Drummond et al., *Methods for the
  Economic Evaluation of Health Care Programmes* — owns the question of what
  a year of life is worth, which someone is answering whether or not you
  like it. Demography — Preston, Heuveline & Guillot, *Demography* — owns
  the denominators everything else divides by. Environmental and
  occupational health — Frumkin (ed.), *Environmental Health: From Global to
  Local* — owns exposure, the field's hardest measurement problem. Public
  health law — Lawrence Gostin, *Public Health Law* — owns the powers, and
  is a third of practice. Infectious disease modelling — Vynnycky & White,
  *An Introduction to Infectious Disease Modelling*, as the working bridge
  to Keeling & Rohani. Quality and safety — the IOM reports *To Err Is
  Human* and *Crossing the Quality Chasm*, which founded a whole discipline.
  Global health delivery — the World Bank's *Disease Control Priorities*
  (free) and Farmer et al., *Reimagining Global Health*.
- *The long canon:* Archie Cochrane, *Effectiveness and Efficiency* (1972) —
  seventy pages that created evidence-based medicine. Austin Bradford Hill,
  "The Environment and Disease: Association or Causation?" (1965), the most
  cited nine pages in the field. Paul Starr, *The Social Transformation of
  American Medicine*, for why the US system is shaped as it is. Thomas
  McKeown, *The Role of Medicine*, read together with Simon Szreter's
  rebuttal — the argument about whether medicine or plumbing did the work.
  Frank Snowden, *Epidemics and Society*. Michael Marmot, *The Health Gap*.
  Randy Shilts, *And the Band Played On*, and Laurie Garrett, *The Coming
  Plague*, for institutional failure in real time. James Jones, *Bad Blood*,
  on Tuskegee, and Skloot's *The Immortal Life of Henrietta Lacks* — read
  both as the ethics curriculum, not as reading. Ioannidis, "Why Most
  Published Research Findings Are False" (2005). Ben Goldacre, *Bad
  Pharma*. Case & Deaton, *Deaths of Despair*. Mona Hanna-Attisha, *What the
  Eyes Don't See*, for what it costs to be right about Flint. Wilkinson &
  Pickett's *The Spirit Level* is worth reading and is genuinely contested —
  read the critiques alongside it.
- *The project ladder:*
  1. A weekend: reproduce a published figure from NHANES or BRFSS microdata
     and publish the code. Your number will differ. Find out why.
  2. A surveillance dashboard from an open feed, maintained for a year, with
     the data-quality problems documented rather than smoothed away.
  3. Six months inside a real program — a clinic, a vaccination drive, a
     needle exchange, a food bank. Nothing else teaches the front desk.
  4. A survey you designed and ran: sampling frame, instrument, ethics
     review where applicable, and an honest non-response analysis.
  5. A cost-effectiveness model of a real local intervention, with
     sensitivity analysis, delivered to the people who could act on it.
  6. An outbreak investigation, done properly — case definition, line list,
     epidemic curve, hypothesis, control measure. If you are not employed to
     do this, health departments take volunteers and CSTE runs training.
  7. A pre-registered analysis of an existing cohort, published, including
     the parts that did not work.
  8. The decade project: design, run and evaluate an intervention with a
     real comparison group — then publish the null result if it is null,
     which is the actual test of whether you belong to this field.
  9. Serve on a board of health, an IRB, or a county advisory body.
- *Re-foundation watch:* confounding, selection bias, the prevention
  paradox, transmission dynamics and the dominance of social determinants
  are permanent, and so is the fact that implementation is decided by
  persuasion and law rather than by evidence. What churns: statistical
  software; specific data platforms; sequencing and wastewater methods,
  which are becoming infrastructure; disease-specific therapeutics; and the
  guideline of the moment. One real re-foundation is already underway —
  causal inference moved from Rothman-era stratification to potential
  outcomes and DAGs within one career, and something will displace that
  too. Learn the reasoning, not the estimator.
- *A lifetime practice:* read *MMWR* weekly for forty years — it is the
  field talking to itself, and the accumulated pattern recognition is
  unbuyable. Curate one indicator or dataset personally. Serve locally.
  Teach statistics to clinicians. Keep a file of your own wrong forecasts,
  dated, and reread it during the next emergency.
- *Rabbit holes:* how badly Snow was actually received, and by whom; salt
  iodization as the highest-return intervention nobody discusses; the 1976
  swine flu campaign and its aftermath; the design compromises inside the
  Framingham cohort; Semmelweis as a failure of communication rather than
  of evidence.

---

## Business, management & entrepreneurship

**The question it asks.** Why does an organization sometimes produce more
value than the sum of the people in it — and why do most attempts fail?
Underneath that: how does coordination happen under uncertainty, who
captures the value created, and how does a firm know whether it is actually
working before the cash runs out?

**Big ideas to walk away with.**
- Why firms exist at all (Coase): because using the market has transaction
  costs, and the boundary of the firm sits where those costs cross.
- Cash flow is not profit, and profit is not the residual you think — the
  real residual is after opportunity cost of capital.
- Unit economics: CAC, LTV, gross margin, contribution margin, payback
  period. A business that doesn't work per unit doesn't work at volume.
- Competitive advantage is structural, not effortful. Porter's five forces
  and the "moat" framing are two vocabularies for the same question: what
  stops someone from copying you?
- Demand is discovered, not decided. The gap between an idea and a market is
  where nearly all startups die.
- Principal-agent problems: incentives quietly rewrite strategy, and what
  you measure is what you will get instead of what you wanted.
- Capital allocation is the CEO's actual job, and most are bad at it.
- Organizations are information-processing systems that slow down as they
  grow; Grove's managerial leverage is the response.
- Survival dominates optimization. You cannot compound if you're dead.

**What outsiders get wrong.**
- They mistake business books for evidence. Most are survivor-biased
  storytelling — *Good to Great* is the standing example, its companies
  having subsequently underperformed. Read them as hypothesis generators.
- They think startups are about ideas. They are about distribution and
  timing, and ideas are cheap.
- They use revenue and profit interchangeably, which is how people lose
  money enthusiastically.

**T3 — Literacy (~150 hrs)**
- *Start here:* Josh Kaufman, *The Personal MBA*. The door because it maps
  the whole territory honestly in one volume, and tells you where the real
  books are.
- *Survey:* Benjamin Graham, *The Interpretation of Financial Statements*
  (short, old, still correct) or Berman & Knight, *Financial Intelligence*.
  You cannot claim literacy in business without being able to read a balance
  sheet, and this is the cheapest way to fix that.
- *Canon:* Peter Drucker, *The Effective Executive* and *The Practice of
  Management*. Andy Grove, *High Output Management* — the best book ever
  written on managing. Michael Porter, *Competitive Strategy* (chapters
  1–3 carry the argument). Ronald Coase, "The Nature of the Firm" (1937) —
  twenty pages that explain the existence of your employer.
- *Course:* Y Combinator's *Startup School* and the Stanford *How to Start a
  Startup* lecture series (both free). The Paul Graham, Sam Altman and
  Brian Chesky lectures are the load-bearing ones; several others are
  filler. Read Paul Graham's essays alongside.
- *Artifact:* Pull a real company's annual report (10-K in the US). Build a
  one-page model of how it makes money — where revenue enters, what it costs
  to serve, where the cash actually goes. Then write 1,500 words on where
  its advantage is structural and what would kill it in five years.

**T2 — Working depth**
- *Spine:* Brealey, Myers & Allen, *Principles of Corporate Finance*.
  Stephen Penman, *Financial Statement Analysis and Security Valuation*.
  Cachon & Terwiesch, *Matching Supply with Demand*, for operations. Kotler
  & Keller, *Marketing Management*, for the demand side. Richard Rumelt,
  *Good Strategy Bad Strategy* — the rare strategy book with actual content.
- *Practice:* Put real money at risk, even a small amount. Sell something to
  a stranger who has no reason to be kind to you. Build a full linked
  three-statement model — income statement, balance sheet, cash flow — for a
  real business, forecast it a year out, then go back and check it against
  what happened; the error analysis is the education. Do thirty customer
  interviews before building anything (Rob Fitzpatrick's *The Mom Test*
  tells you how to ask without generating flattery). Manage people, or if
  you can't yet, own a project with a budget, a deadline and consequences.
  Read your own P&L monthly until the numbers have faces.
- *Primary literature:* *Harvard Business Review* selectively — Levitt's
  "Marketing Myopia", Christensen's "Disruptive Technologies", Kotter's
  "Leading Change". *Strategic Management Journal* for the scholarship.
  Annual reports and the Berkshire Hathaway shareholder letters as a
  long-form course in capital allocation. Landmarks: Clayton Christensen,
  *The Innovator's Dilemma*; Drucker, *Innovation and Entrepreneurship*.
- *You've arrived when:* handed a business you've never seen, you can read
  its financials, state its unit economics and structural advantage, and say
  what you'd do in the first ninety days — and, separately, you have shipped
  a product to paying customers and know your own numbers cold.

**T1 — Mastery**
- *Graduate texts/monographs:* Milgrom & Roberts, *Economics, Organization
  and Management* — the rigorous spine under everything above. Robert Grant,
  *Contemporary Strategy Analysis*. Aswath Damodaran, *Investment
  Valuation*. Edith Penrose, *The Theory of the Growth of the Firm*. Nelson
  & Winter, *An Evolutionary Theory of Economic Change*.
- *Frontier:* Platform and network economics; how AI is redrawing firm
  boundaries and the labor inside them; the migration of company formation
  into private capital markets; productivity dispersion between firms in the
  same industry, which is larger than almost anyone expects. Follow NBER
  working papers on firms and productivity, and Damodaran's public datasets.
- *Contribution looks like:* this domain forks at T1, and you should choose
  deliberately. The scholarly route means papers in *SMJ* or *AMJ* and
  probably a PhD. The operator route means building an enterprise that
  survives a decade, or a capital allocation record that beats the index
  over a full cycle. These are different games with different feedback
  loops; people who blur them do neither well.
- *Community:* Academy of Management for the scholarly side; industry
  associations, YC/Techstars networks and board seats for the operator side.
  The MBA is optional and expensive — the CPA and CFA are the credentialed
  sub-paths that actually gate work.

**Beyond T1 — the long shelf**

- *Branch into:* Accounting proper — Kieso, Weygandt & Warfield,
  *Intermediate Accounting* — owns the language, and skipping it is why most
  self-taught business people stall permanently. Valuation — Koller,
  Goedhart & Wessels, *Valuation* — owns what a stream of cash is worth.
  Supply chain — Chopra & Meindl, *Supply Chain Management* — owns the
  physical business under the financial one. Pricing — Nagle & Müller, *The
  Strategy and Tactics of Pricing* — owns the most under-managed variable in
  any company. Negotiation — Howard Raiffa, *The Art and Science of
  Negotiation*, for the rigorous version, with Fisher & Ury for the field
  guide. Organizational design and culture — Edgar Schein, *Organizational
  Culture and Leadership*. Sales — Neil Rackham, *SPIN Selling*, which is
  unusual in being based on observed data. Venture and private capital —
  Gompers & Lerner, *The Venture Capital Cycle*, with Feld & Mendelson's
  *Venture Deals* for the mechanics of a term sheet.
- *The long canon:* Alfred Chandler, *Strategy and Structure* and *The
  Visible Hand* — the deep history of why firms look the way they do.
  William Thorndike, *The Outsiders*, on capital allocation as the actual
  job. Ron Chernow, *Titan* and *The House of Morgan*. Kindleberger & Aliber,
  *Manias, Panics, and Crashes*, which will explain every bubble you live
  through. Then the failure library, which is where the real education is:
  Roger Lowenstein, *When Genius Failed*; McLean & Elkind, *The Smartest
  Guys in the Room*; Carreyrou, *Bad Blood*; Burrough & Helyar, *Barbarians
  at the Gate*; Finkelstein, *Why Smart Executives Fail*. Marc Levinson,
  *The Box*, for how a container reorganized the world economy. Cialdini,
  *Influence*, read as defence. Drucker's *Managing Oneself*, twenty pages,
  reread every five years. Founder memoirs are the weakest genre here —
  Knight's *Shoe Dog* is honest, most of the rest are retrofitted.
- *The project ladder:*
  1. A weekend: sell ten things to strangers and record the unit economics
     honestly, including your own time at a real rate.
  2. A side business to its first $1,000 of revenue — priced, delivered,
     invoiced, collected. Collection is the part nobody warns you about.
  3. A three-statement model of a public company, forecast a year out, then
     scored against what happened. The error analysis is the course.
  4. Own a P&L that is not yours: treasurer of a nonprofit, a team budget,
     a project with a real number attached.
  5. Hire someone, manage them, and if it comes to it, fire them. Write the
     spec, run the interviews, own the outcome. This is the step people
     avoid for a decade and it is the one that changes them.
  6. A business to $100k revenue with a repeatable acquisition channel and
     a written process another person can run without you.
  7. Put outside money at risk, or take it — a private deal, a loan, a
     round — and live with the governance that follows.
  8. A board seat with fiduciary duty. Nonprofit boards are real, available,
     and teach the same thing.
  9. The decade project: build an enterprise that survives ten years and one
     downturn, then hand it to a successor — or run a portfolio through a
     full cycle with a dated written thesis on every position, scored.
- *Re-foundation watch:* double-entry accounting, cash conversion, Coase's
  transaction-cost logic, incentives, distribution as the binding
  constraint, and the primacy of survival are permanent — they were true
  for the Medici. What churns: acquisition channels, which have a five-year
  half-life and swallow whole careers; tax and securities regimes; valuation
  multiples; the funding environment; and every piece of software you run
  the business on. The one likely re-foundation is AI moving the boundary
  between what a firm does inside itself and what it buys — which is a huge
  practical change and leaves Coase's question exactly as posed.
- *A lifetime practice:* a decision journal with dated predictions and the
  reasoning, reviewed annually — it is the only defence against remembering
  yourself as having been right. Read one annual report a month for
  decades. Close your own books monthly. Mentor founders, and sit on one
  board at a time.
- *Rabbit holes:* Pacioli and the invention of double-entry; the East India
  Company as a corporate form; the Lincoln Electric incentive system, which
  should not work and does; the conglomerate era and its unwinding; the
  Japanese *shinise* — firms that have lasted three hundred years, and what
  they did instead of growing.

---

## Military history & strategy

**The question it asks.** How does organized violence translate — or, far
more often, fail to translate — into political outcomes? Strategy is the art
of relating means to ends against an opponent who is also thinking and also
adapting. Military history is the empirical record of how badly that usually
goes, and it is the closest thing the field has to a laboratory.

**Big ideas to walk away with.**
- War as a continuation of policy by other means, and Clausewitz's trinity:
  passion, chance, and reason — mapping loosely to people, army, government.
- Friction and the fog of war. The gap between the plan and the execution is
  not a failure of planning; it is the medium.
- Logistics governs. Amateurs talk tactics; the professionals count trucks,
  fuel and calories, and the count decides.
- The decisive-battle illusion. Most wars are won by attrition, exhaustion
  and finance, and the tactical genius of the loser is a recurring pattern
  (Germany, 1914–45, is the standing case).
- Attrition vs maneuver as competing theories, and the fact that operational
  brilliance cannot rescue a bad strategy.
- Deterrence has its own logic — Schelling's threat that leaves something to
  chance, commitment, signaling, and the stability of mutual vulnerability.
- Civil-military relations: who controls the instrument, and what happens
  when the answer is unclear.
- Insurgency and counterinsurgency: the center of gravity is political, and
  military superiority can be strategically irrelevant.
- Technology changes the tactical problem far more often than it changes the
  strategic one.

**What outsiders get wrong.**
- They read Sun Tzu as a business manual. It is an argument about statecraft
  and the costs of war, and the aphorisms are not instructions.
- They believe the better weapon wins. Check the record; it is a weak
  predictor.
- They count battles won as evidence of a war being won. Nolan's book exists
  to dismantle exactly this.

**T3 — Literacy (~200 hrs)**
- *Start here:* Cathal Nolan, *The Allure of Battle*. The door because it
  attacks the illusion you almost certainly hold — that wars are decided by
  great battles — and once that's gone, everything else in the field reads
  differently.
- *Survey:* Michael Howard, *War in European History* — short, dense,
  superb. John Keegan, *A History of Warfare*, for the wider anthropological
  sweep, and Keegan's *The Face of Battle* for what combat is actually like
  at eye level.
- *Canon:* Thucydides, *History of the Peloponnesian War* — read Pericles'
  funeral oration, the Corcyra passages on civil war, the Melian Dialogue,
  and the Sicilian Expedition; you can skip much of the campaign narrative
  on a first pass. Clausewitz, *On War* (Howard & Paret translation) — read
  Book One Chapter One, then Book Eight, and leave the rest until you have a
  reason. Sun Tzu, *The Art of War* (Griffith or Sawyer translation) — ninety
  minutes, read once, don't build a philosophy on it.
- *Course:* Be honest with yourself: no free open course is worth
  structuring this domain around. The reading is the course. If you want
  lectures, the U.S. Army War College's *Parameters* and the *Naval War
  College Review* are free and are where practitioners argue. Dan Carlin's
  *Hardcore History* is immersion, not analysis — enjoy it, don't cite it.
- *Artifact:* Pick one campaign. Reconstruct the decision problem as the
  commander actually faced it — the information he had, when he had it, the
  constraints he could not change. Then write 2,000 words on whether the
  standard verdict on him is fair. Hindsight is the field's occupational
  disease and this exercise is the cure.

**T2 — Working depth**
- *Spine:* Peter Paret (ed.), *Makers of Modern Strategy*, and the 2023
  edition edited by Hal Brands — read both, they disagree usefully. Lawrence
  Freedman, *Strategy: A History*. Martin van Creveld, *Supplying War*,
  which will permanently change what you notice. Murray & Millett, *A War to
  Be Won*, for the operational level of the Second World War done properly.
- *Practice:* The practice here is analytic and it is real work. Write
  operational analyses and submit them somewhere with editors. Walk terrain
  — a staff ride on any battlefield you can reach teaches what maps hide.
  Play serious wargames, the professional or serious-hobby kind, where
  friction and imperfect information are modeled; the feeling of deciding
  without enough information is not obtainable from books. Red-team a real
  decision for someone. Above all, work from primary sources — orders, war
  diaries, after-action reports, logistics returns — rather than from
  narrative histories, which have already done the interpreting for you.
- *Primary literature:* *Journal of Strategic Studies*, *International
  Security*, *War in History*, *Parameters* and the *Naval War College
  Review* (both free), *War on the Rocks* for current practice. Landmarks:
  Alfred Thayer Mahan, *The Influence of Sea Power upon History*; Thomas
  Schelling, *The Strategy of Conflict* and *Arms and Influence*; Roberta
  Wohlstetter, *Pearl Harbor: Warning and Decision*, the founding text of
  intelligence-failure analysis.
- *You've arrived when:* you can take a campaign you have never studied,
  work from the primary orders and the logistics data, and produce an
  assessment a specialist finds defensible — including a clear statement of
  what evidence would change your mind.

**T1 — Mastery**
- *Graduate texts/monographs:* Barry Posen, *The Sources of Military
  Doctrine*. Stephen Biddle, *Military Power: Explaining Victory and Defeat
  in Modern Battle*. Jack Snyder, *The Ideology of the Offensive*. Robert
  Jervis, *Perception and Misperception in International Politics*. Hew
  Strachan's work on Clausewitz and on the First World War.
- *Frontier:* Drones and precision at mass; the return of large-scale
  attrition warfare that doctrine had written off; nuclear multipolarity;
  AI in command and control; and, historiographically, the turn away from
  operational narrative toward logistics, economy, and society. Follow the
  IISS (*The Military Balance*, *Survival*), RAND, CSIS, and the war
  colleges' journals.
- *Contribution looks like:* archival work that overturns an accepted
  account, or strategic analysis that changes doctrine. Both are rare and
  both take a decade.
- *Community:* Society for Military History, IISS, the security studies
  section of the International Studies Association, the war colleges. No
  licensure. The credential is published work — and, for practitioners,
  service.

**Beyond T1 — the long shelf**

- *Branch into:* Maritime strategy — Julian Corbett, *Some Principles of
  Maritime Strategy* — owns the argument Mahan got half right, and is the
  better book. Air power — Tami Davis Biddle, *Rhetoric and Reality in Air
  Warfare* — owns the gap between what air forces promised and delivered;
  read Douhet first to see what was promised. Nuclear strategy — Freedman,
  *The Evolution of Nuclear Strategy*, with Brodie's *Strategy in the
  Missile Age* — owns the only domain where the theory was built before the
  evidence. Intelligence — Michael Herman, *Intelligence Power in Peace and
  War*, and Richard Betts, *Enemies of Intelligence*. Irregular war —
  Galula, *Counterinsurgency Warfare*, and Mao, *On Guerrilla Warfare*,
  read as opposing halves of one manual. Civil-military relations —
  Huntington, *The Soldier and the State*, against Eliot Cohen's *Supreme
  Command*. Military operations research and simulation — Philip Sabin,
  *Simulating War*, plus Lanchester's equations and the literature on why
  they fit the data poorly.
- *The long canon:* Hans Delbrück, *History of the Art of War* — four
  volumes, and the founding of source-critical military history. Jomini,
  *The Art of War*, as the road not taken from Clausewitz. Ardant du Picq,
  *Battle Studies*, on what men actually do under fire. Liddell Hart,
  *Strategy*, read with suspicion — he shaped the field and bent evidence to
  do it. S.L.A. Marshall's *Men Against Fire* is famous, influential, and
  methodologically discredited; read it to understand how a bad statistic
  survives fifty years. Adam Tooze, *The Wages of Destruction*, and Richard
  Overy, *Why the Allies Won* — economies deciding wars. Gerhard Weinberg,
  *A World at Arms*. Christopher Clark, *The Sleepwalkers*, on how decisions
  for war are actually made. Graham Allison, *Essence of Decision* — three
  models of the same crisis, and the best methodological training in this
  file. Alistair Horne, *A Savage War of Peace*; Neil Sheehan, *A Bright
  Shining Lie*; H.R. McMaster, *Dereliction of Duty*. Michael Howard, *The
  Franco-Prussian War*. John Lynn, *Battle: A History of Combat and
  Culture*, against Keegan and Hanson both.
- *The project ladder:*
  1. A weekend: reconstruct the order of battle for one day of one action
     from primary sources, and notice how much the narrative histories
     silently invented.
  2. Design and play a wargame of a small engagement, then write down what
     your model got wrong. Designing one teaches more than playing fifty.
  3. Plan and lead a staff ride for other people on terrain you can reach.
     Explaining a decision while standing where it was made is the test.
  4. An archival project: work a collection of war diaries or unit records
     and produce something the published record does not contain.
  5. A logistics reconstruction — compute a campaign's actual requirement
     in tons and calories per day, and compare it to what moved.
  6. A published article in *Parameters*, the *Naval War College Review*,
     *War in History* or *War on the Rocks*, through real editing.
  7. Red-team a live decision for an organization, under stakes, where
     being wrong costs someone something.
  8. An edited or translated primary source made available to others — a
     dull, enormous contribution that outlasts most monographs.
  9. The decade project: an archival monograph on a campaign or an
     institution that overturns an accepted account. This is ten years and
     it is the only thing the field ultimately counts.
- *Re-foundation watch:* the trinity, friction, the primacy of logistics,
  the political nature of victory, small-unit psychology and deterrence
  logic are permanent. What churns: force structures, current doctrine,
  order-of-battle data, and the technology assessment of the moment —
  drones at mass, hypersonics, AI in command and control — which will read
  as period pieces. So will most "lessons" from the most recent war; they
  almost always are. There is also a re-foundation specific to this domain:
  archives open on thirty-year rules and declassification schedules, so the
  standard account of any war you live through will be rewritten twice.
  Plan to reread the standard history of anything twenty years after you
  first read it, and expect to be embarrassed.
- *A lifetime practice:* one campaign a year, studied from primary sources,
  with a written assessment you keep. A commonplace book of sourced
  quotations. A wargaming group that meets. Terrain walked deliberately —
  a battlefield a year is forty battlefields.
- *Rabbit holes:* the Prussian general staff's invention of the staff ride;
  Blackett's operational research circus in the Battle of the Atlantic; the
  Dreadnought race as a budget problem; the logistics of the 1918 Ludendorff
  offensives; the 1973 Sinai argument about tanks and anti-tank missiles,
  which is being had again right now with different nouns.

---

## Design (industrial, graphic, interaction)

**The question it asks.** How do you shape an object, an image, or a system
so that a person who will never meet you can understand it, use it, and want
it — and how do you find out whether you succeeded *before* you commit to
production? Design is the discipline of making intent legible in form, under
constraints you didn't choose.

**Big ideas to walk away with.**
- Norman's vocabulary: affordances, signifiers, mapping, feedback,
  constraints. Learn these five words properly and you will see badly
  designed objects everywhere for the rest of your life.
- The conceptual model — the user's mental model versus the system's — and
  the gulfs of execution and evaluation between them.
- Prototype, test, revise. Design is empirical; opinions are hypotheses.
  Nielsen's finding that about five users surface most usability problems is
  the reason cheap testing works.
- Typography as the interface to text: hierarchy, measure, leading,
  contrast. Most "bad design" is bad typography.
- Grid and composition as instruments for directing attention, not as
  decoration.
- Constraints generate designs. Material, cost, process, and accessibility
  are the brief, not obstacles to it.
- Accessibility is a requirement, not a retrofit — and designing for the
  edge usually improves the middle.
- Taste is trained. You acquire it by copying masters and submitting to
  critique, the way musicians and painters always have.

**What outsiders get wrong.**
- They think design is decoration applied at the end. It's the decisions
  made at the beginning, which is why it's cheap to change then and ruinous
  later.
- They confuse "I like it" with "it works." These are separately testable.
- They think "design thinking" workshops are design. That's a facilitation
  method, and a thin one; it does not substitute for craft.

**T3 — Literacy (~150 hrs)**
- *Start here:* Don Norman, *The Design of Everyday Things* (revised
  edition). The door because it hands you a vocabulary for frustrations you
  have had all your life and blamed yourself for.
- *Survey:* Lidwell, Holden & Butler, *Universal Principles of Design* — a
  browsable index of the field's concepts, good for finding out what you
  don't know exists.
- *Canon:* Christopher Alexander, *The Timeless Way of Building* (read the
  first hundred pages) and *A Pattern Language* (dip, don't read cover to
  cover). Josef Müller-Brockmann, *Grid Systems in Graphic Design*. Robert
  Bringhurst, *The Elements of Typographic Style*. Edward Tufte, *The Visual
  Display of Quantitative Information*. Dieter Rams' ten principles are one
  page — read them today.
- *Course:* Matthew Butterick's *Practical Typography* (free online) is
  excellent, opinionated, and will improve every document you produce within
  a week. The Nielsen Norman Group's free articles are the working reference
  for usability. The paid design-thinking certificate courses are, for the
  most part, not worth the money.
- *Artifact:* Redesign one real thing that annoys you — a government form, a
  wayfinding sign, a remote control, an app screen. State a hypothesis about
  why the original fails. Produce before-and-after. Then test it on five
  real people and report what they did, not what they said. The test is
  what separates this from doodling.

**T2 — Working depth**
- *Spine:* Cooper, Reimann, Cronin & Noessel, *About Face: The Essentials of
  Interaction Design*. Ellen Lupton, *Thinking with Type*. Bill Buxton,
  *Sketching User Experiences*. For the industrial and product side, Ulrich
  & Eppinger, *Product Design and Development*. Steve Krug's *Rocket
  Surgery Made Easy* tells you exactly how to run usability tests on almost
  no budget — read it and then actually do it.
- *Practice:* Make constantly and submit to critique; unreviewed work
  plateaus. Draw daily — sketching is this field's handwriting and everyone
  who is good at it does it badly at first. Copy master work deliberately:
  rebuild a Swiss-school poster from scratch, reset a book page in a real
  typeface, reverse-engineer an interface you admire down to its spacing.
  Build physical prototypes in card, foam and print — the object teaches
  things the render conceals. Run real usability sessions with strangers and
  watch yourself want to explain; don't. Then ship, where outcomes are
  measured rather than admired.
- *Primary literature:* ACM CHI proceedings for the research side, *Design
  Issues* and *Design Studies* for the scholarship, NN/g reports and *Eye*
  magazine for practice. Landmarks: Herbert Simon, *The Sciences of the
  Artificial* (design as the science of how things ought to be); Christopher
  Alexander, *Notes on the Synthesis of Form*; Victor Papanek, *Design for
  the Real World*, which poses the ethical question the field still ducks.
- *You've arrived when:* you can take an ambiguous brief through research,
  concept, prototype, testing and production — and defend every decision
  with a reason that is not taste — with a portfolio a hiring designer takes
  seriously on sight.

**T1 — Mastery**
- *Graduate texts/monographs:* Simon, *The Sciences of the Artificial*.
  Alexander, *Notes on the Synthesis of Form*. Nigel Cross, *Designerly Ways
  of Knowing* and *Design Thinking*. Donald Schön, *The Reflective
  Practitioner*. Klaus Krippendorff, *The Semantic Turn*.
- *Frontier:* Interfaces mediated by AI, where the system's behavior is
  probabilistic and the old feedback model breaks. Service and systems
  design. Circular design and material accountability. The field's
  reckoning with attention capture and dark patterns, which is an ethics
  problem it created. Follow NN/g, the research groups at CMU HCII, Delft
  and the RCA, and practitioners who publish their process rather than only
  their results.
- *Contribution looks like:* work that becomes a reference — a produced
  product, an identity system in daily use, a pattern others adopt — or
  research at CHI and in *Design Studies*.
- *Community:* AIGA (graphic), IDSA (industrial), ACM SIGCHI (interaction),
  the Type Directors Club. No licensure except where design touches
  architecture or safety-critical equipment. The portfolio and the produced
  work are the entire credential, which is liberating and merciless.

**Beyond T1 — the long shelf**

- *Branch into:* Type design — Walter Tracy, *Letters of Credit*, and Karen
  Cheng, *Designing Type* — owns the letterform itself, and is the deepest
  well in graphic design. Information design — Tufte's *Envisioning
  Information* and *Visual Explanations*, with Jacques Bertin's *Semiology
  of Graphics* underneath them — owns encoding quantity as position and
  mark. Materials and process for product work — Ashby & Johnson,
  *Materials and Design* — owns why the object feels the way it does. Human
  factors — Wickens et al., *An Introduction to Human Factors Engineering*,
  with Dreyfuss's *The Measure of Man and Woman* — owns the body, and is
  where design touches safety. Service and systems design — Polaine, Løvlie
  & Reason, *Service Design*. Accessibility — the W3C WCAG documents
  themselves, plus Kat Holmes, *Mismatch*. Design history and criticism —
  Adrian Forty, *Objects of Desire*, and Banham, *Theory and Design in the
  First Machine Age*. Environmental and urban legibility — Kevin Lynch,
  *The Image of the City*, and Jan Gehl, *Life Between Buildings*.
- *The long canon:* Bruno Munari, *Design as Art* — playful, short, and
  wiser than it looks. Jan Tschichold, *The New Typography* and then *The
  Form of the Book*, which is the same man recanting; read them in that
  order, it is an education in dogma and its cost. Emil Ruder,
  *Typographie*, and Armin Hofmann, *Graphic Design Manual*, for the Swiss
  argument in its own words. Paul Rand, *Thoughts on Design*. Massimo
  Vignelli, *The Vignelli Canon* (free). Henry Dreyfuss, *Designing for
  People*, and Loewy's *Never Leave Well Enough Alone*, as the two American
  temperaments. Sophie Lovell, *Dieter Rams: As Little Design as Possible*.
  Jef Raskin, *The Humane Interface*, and Alan Cooper, *The Inmates Are
  Running the Asylum*. Lupton & Miller, *Design Writing Research*. Then the
  failure literature, which this field neglects and shouldn't: the Therac-25
  papers as an interface failure, the Three Mile Island control room, the
  2018 Hawaii false missile alert, and the 737 MAX documents on what
  happens when the human is the last undesigned component.
- *The project ladder:*
  1. A weekend, repeated monthly for a year: redesign one real thing — a
     form, a sign, a label — and test it on five people. Twelve of these
     beats any course.
  2. A complete identity for a real client: mark, type system, applications,
     and a guidelines document someone else can follow without you.
  3. A printed object made under production constraint — a letterpressed
     poster series, a bound book. Ink and paper refuse to be undone.
  4. A physical product to a manufacturable prototype: CAD, DFM, a real
     quote from a real vendor, and a conversation about tooling.
  5. A shipped software product's end-to-end interaction design, with
     measured outcomes and at least one iteration after launch.
  6. A wayfinding system installed in a real building or campus, then
     observed in use — you will find out you were wrong somewhere.
  7. A design system others build on, documented and governed, maintained
     for years. Maintenance is the part that separates this from a portfolio.
  8. Teach a studio course and run critiques. Articulating why something
     fails is a different skill from fixing it, and it improves the fixing.
  9. The decade project: a released text typeface with a full character set
     across weights — three to five years of work, and the field's classic
     long haul — or a produced object or public identity still in daily use
     ten years on.
- *Re-foundation watch:* perception, Gestalt grouping, the optical rules of
  typography, anthropometry, the empirical test loop and the practice of
  critique are permanent. A Müller-Brockmann grid works exactly as well
  today as in 1961. What churns: the tool, which has gone Illustrator to
  Sketch to Figma inside one career and will move again; platform interface
  guidelines; and visual fashion, which cycles on roughly a decade. The one
  real re-foundation in view is interfaces whose behaviour is probabilistic
  rather than specified — feedback, mapping and the conceptual model all
  need rebuilding for systems that answer differently each time, and nobody
  has done it yet. That is a genuine opening, not a tool update.
- *A lifetime practice:* a daily sketchbook kept for decades — the single
  habit that most separates designers who improve from designers who
  plateau. A standing critique group. A personal archive of collected
  artifacts: tickets, packaging, signage, forms. Redesign one public thing a
  year and send it, unsolicited, to whoever owns it.
- *Rabbit holes:* Otto and Marie Neurath's Isotype project; the Vignelli and
  Noorda *New York City Transit Authority Graphics Standards Manual*; Harry
  Beck and the London Underground diagram; Muriel Cooper's Visible Language
  Workshop at MIT; the HfG Ulm and its quarrel with the Bauhaus inheritance.

---

## A craft done with the hands

**The question it asks.** Can you make the material do what you intend? Not
describe how, not specify it for someone else — do it, with your hands,
repeatably. This is the one domain in the whole map that cannot be faked by
reading, and that is precisely why it belongs here: it is a standing check
on the difference between knowing about a thing and being able to do it.

**Big ideas to walk away with.**
- Skill is not knowledge. You will understand the technique long before your
  hands can execute it, and that gap closes only with repetition.
- Maintaining the tool is the first skill, in every craft. Sharpening,
  tuning, cleaning, calibrating. Beginners blame themselves for what a dull
  edge or an untuned instrument caused.
- The material has opinions. Wood moves with humidity, clay remembers how
  you handled it, dough responds to temperature, solder wants to be clean.
  Fighting the material always loses.
- Repetition beats variety: make one thing twenty times, not twenty things
  once. This is the single most common beginner error.
- Speed comes from economy of motion, not hurry — and it arrives last.
- Feedback must be immediate and physical. The joint gaps or it doesn't.
- Embodied skill transfers by demonstration and correction. An in-person
  teacher for even a few sessions is worth months of video.

**What outsiders get wrong.**
- They think buying better tools substitutes for practice. It does not,
  though genuinely bad tools do hold you back — the fix is few, good tools.
- They treat craft as leisure and therefore optional. It's the calibration
  instrument for everything else in this repo.
- They start with an ambitious project and abandon it. Start with a small
  finished thing.

**Pick one.** Depth in one craft beats sampling five.
- *Cooking:* Samin Nosrat, *Salt Fat Acid Heat*, then J. Kenji López-Alt,
  *The Food Lab*. Later, Harold McGee's *On Food and Cooking* for the
  science.
- *Woodworking:* Christopher Schwarz, *The Anarchist's Tool Chest*, for what
  to buy and why; Paul Sellers' free video courses for hand-tool technique;
  R. Bruce Hoadley, *Understanding Wood*, for the material.
- *Ceramics:* Bernard Leach, *A Potter's Book*, is the canon; a wheel class
  is non-negotiable. Later, John Britt on glazes.
- *Electronics:* Charles Platt, *Make: Electronics* (build every circuit),
  then Horowitz & Hill, *The Art of Electronics*.
- *Gardening:* Edward C. Smith, *The Vegetable Gardener's Bible*; Eliot
  Coleman, *The New Organic Grower*, when you get serious.
- *An instrument:* a teacher, weekly, plus Gerald Klickstein's *The
  Musician's Way* for how to practice rather than merely repeat.

**T3 — Literacy (~200 hrs): make a first competent object**
- *Start here:* the tool. Learn to sharpen, tune, calibrate or maintain
  before you learn to make. Learn the safety rules cold, from a person, if
  the craft has ways to injure you.
- *Survey:* the one book above for your chosen craft — read it once, then
  keep it beside the bench, not on a shelf.
- *Canon:* watch a master work, at length, in person if at all possible. A
  demonstration you can walk around teaches what no camera angle does.
- *Course:* take an in-person class. This is the tier where the money is
  best spent, because a teacher corrects errors you cannot see yourself.
- *Artifact:* **the object.** Not an essay about the object. A dovetailed
  box whose joints close. A bowl thrown, trimmed, glazed and fired. A meal
  for six, on the table, hot, at the time you said. A circuit that works on
  a board and not just a breadboard. A harvest you ate. A piece performed
  from memory in front of people. The standard is not "good for a beginner."
  The standard is that a stranger would call it good.

**T2 — Working depth: fluency in the material and the tools**
- *Spine:* the material science of your medium — moisture content and wood
  movement; clay body and glaze fit; emulsion and the Maillard reaction;
  impedance and grounding; soil biology; the physics of your instrument.
  This is where the second, harder book belongs.
- *Practice:* stop following recipes and start diagnosing. Why did the joint
  gap, the glaze craze, the sauce break, the oscillator refuse to start, the
  seedlings bolt? Work to a spec someone else set and a deadline you didn't
  choose — a commission, a dinner for paying guests, a repair someone
  depends on. Track your time and material cost per piece. Sell or give away
  work to people who will judge it. Teach a beginner, which will expose
  every gap in what you think you know.
- *Primary literature:* the craft's own periodicals and guild publications —
  *Fine Woodworking*, *Ceramics Monthly*, *Cook's Illustrated*,
  *Nuts and Volts*, and the standard repertoire lists for instruments. Also
  the historical exemplars: study the work of acknowledged masters in your
  craft directly, in museums or collections.
- *You've arrived when:* you can make something you have never made before
  by reasoning from the material and the tools, without a set of
  instructions, and it comes out right the first or second time.

**T1 — Mastery: the level of a working craftsperson**
- *Graduate texts/monographs:* by this tier the references are technical
  manuals, historical treatises and other makers' work rather than books —
  in most crafts the deep knowledge was never written down, which is why
  apprenticeship persists.
- *Frontier:* your own hand. At this level you develop a recognizable style,
  make your own tools, jigs, glazes, recipes or arrangements, and can hold
  quality *and* speed simultaneously — which is the actual difference
  between an accomplished amateur and a professional.
- *Contribution looks like:* an original design, technique, recipe or
  interpretation that others adopt; restoration or repair work that
  preserves something; and above all teaching — crafts survive by
  transmission, and taking an apprentice is the highest contribution
  available.
- *Community:* guilds and societies (the Furniture Society, the American
  Craft Council, NCECA for ceramics, local guilds for nearly everything),
  juried shows and competitions, the local makerspace, farmers' markets,
  gigs, and apprenticeship in both directions. There is no licensure and no
  degree. The work in your hands is the entire argument.
