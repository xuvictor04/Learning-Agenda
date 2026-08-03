# Mind

## Neuroscience

**The question it asks.** How does an organ made of cells — electrical,
chemical, wet — produce perception, memory, decision, and action? The hard
part is not any one level but the *bridging*: nobody yet knows how to get
from ion channels to a thought without hand-waving somewhere in the middle.
The field is the sustained attempt to make those bridges load-bearing.

**Big ideas to walk away with.**
- The neuron doctrine (Cajal): the brain is discrete cells, not a continuous
  net — and the synapse is where the interesting computation lives.
- The action potential is a regenerative, all-or-none event with a physical
  explanation (Hodgkin–Huxley). Neural signaling is *understood*, at this level.
- Plasticity: synapses change with use (Hebb, then LTP). Learning is physical.
- Receptive fields and population codes — neurons are tuned, and information
  lives in patterns across many cells, not in single "grandmother" neurons.
- Functional specialization is real but coarse; nearly every function is
  distributed across interacting circuits.
- Neuromodulation: dopamine, serotonin, acetylcholine change the *rules* of
  processing rather than carrying the message. Dopamine signals reward
  *prediction error*, not pleasure.
- Marr's three levels — computational, algorithmic, implementational. Most
  confused neuroscience arguments are two people working at different levels.
- Development and critical periods: the wiring is built by activity, not
  only by genes.

**What outsiders get wrong.**
- fMRI is not mind-reading. BOLD is an indirect, seconds-slow proxy for
  aggregate activity in cubic-millimeter voxels holding ~a million neurons.
  "Region X lit up" is a correlation, and a coarse one.
- Neuromyths persist because they are satisfying: left-brain/right-brain,
  the 10% claim, "chemical imbalance," learning styles. None survive contact
  with the literature.
- Lesion and correlation data tell you a part is *involved*, never *how*.

**T3 — Literacy (~200 hrs)**
- *Start here:* Oliver Sacks, **The Man Who Mistook His Wife for a Hat**. The
  door because it makes the abstract concrete — each chapter is a mind broken
  in one specific way, which is precisely how the field learned what the parts
  do. You will finish it wanting the mechanism, which is the right appetite.
- *Survey:* Matthew Cobb, **The Idea of the Brain** — the whole history of
  how we've thought about brains, honest about how much is still unknown.
  Pair with V.S. Ramachandran, **Phantoms in the Brain**.
- *Canon:* Kandel et al., **Principles of Neural Science**. Do not read it
  cover to cover at this tier. Read Part I (the overview chapters), then the
  chapters on membrane potential, the action potential, and synaptic
  transmission, then one systems chapter on vision. Skip the molecular
  detail entirely for now. Add Cajal's Nobel lecture (short, free) to hear
  the founder's own voice.
- *Course:* MIT OCW **9.13 The Human Brain** (Nancy Kanwisher) — free video,
  outstanding, and unusually honest about the limits of the methods. If you
  want the cellular side too, Harvard's **Fundamentals of Neuroscience**
  (free, three parts, with browser simulations) covers what Kanwisher skips.
- *Artifact:* Write 2,000 words tracing a single act — reaching for a cup you
  see on a table — from photons to muscle contraction. Name each structure
  and the transformation it performs. Then mark, explicitly, every step where
  the textbook story is actually a hypothesis. The marks are the real test.

**T2 — Working depth**
- *Spine:* Bear, Connors & Paradiso, **Neuroscience: Exploring the Brain**
  (the teachable one) or Purves et al., **Neuroscience**; then Kandel's
  **Principles** as the reference you now use properly. For the computational
  side, Dayan & Abbott, **Theoretical Neuroscience**.
- *Practice:* Work with real recordings. The Allen Institute's Brain
  Observatory and Neuropixels datasets are open; so is OpenNeuro and the
  Human Connectome Project. Build the pipeline yourself in Python: spike
  sorting, raster plots, tuning curves, decoding a stimulus from population
  activity. Then simulate: implement Hodgkin–Huxley from the 1952 equations,
  then an integrate-and-fire network in Brian2 or NEURON. If you can get wet-
  lab access, take a sheep-brain dissection and a histology course — spatial
  intuition for the anatomy is not obtainable from diagrams.
- *Primary literature:* Neuron, Nature Neuroscience, Journal of Neuroscience,
  eLife, bioRxiv. Read directly: Hodgkin & Huxley (1952) on the squid axon;
  Hubel & Wiesel (1962) on receptive fields in cat visual cortex; O'Keefe &
  Dostrovsky (1971) on place cells; Schultz, Dayan & Montague (1997) on the
  dopamine prediction-error signal.
- *You've arrived when:* handed a raw electrophysiology dataset you have never
  seen, you can produce tuning curves and a decoder without a tutorial — and
  you can read a Neuron paper from its figures alone, then say what the
  authors' controls failed to rule out.

**T1 — Mastery**
- *Graduate texts/monographs:* Kandel, **Principles of Neural Science** (6th
  ed) as the standing reference; Dayan & Abbott, **Theoretical Neuroscience**;
  Koch, **Biophysics of Computation**; Rieke et al., **Spikes: Exploring the
  Neural Code**; Sterling & Laughlin, **Principles of Neural Design**.
- *Frontier:* Connectomics at scale (the FlyWire whole-fly connectome; the
  MICrONS cortical volume); brain-wide recording with Neuropixels; molecular
  tools — optogenetics, expansion microscopy; and NeuroAI, where artificial
  networks are used as models of biological ones. Follow the Allen Institute,
  Janelia, and Cosyne abstracts; read Eve Marder on circuit degeneracy for a
  corrective to naive mechanism-hunting.
- *Contribution looks like:* a mechanism established in a circuit, a
  computational theory that makes a falsifiable prediction someone then tests,
  or a method that lets other labs see what they couldn't.
- *Community:* Society for Neuroscience (the field's annual mass gathering),
  Cosyne (computational), Gordon Research Conferences. The summer courses at
  Woods Hole (MBL) and Cold Spring Harbor — Methods in Computational
  Neuroscience, Neural Systems & Behavior — are the field's real initiation.

**Beyond T1 — the long shelf**

- *Branch into:* cellular and molecular neuroscience — Hille, **Ion Channels
  of Excitable Membranes**; owns how a membrane computes. Sensory systems —
  Wandell, **Foundations of Vision** (free online); owns how a stimulus
  becomes a code. Computational neuroscience — Gerstner et al., **Neuronal
  Dynamics** (free), after Dayan & Abbott; owns what the circuit is actually
  computing. Cognitive neuroscience — Gazzaniga, Ivry & Mangun, **Cognitive
  Neuroscience: The Biology of the Mind**; owns the mapping from mental
  function onto tissue, and the methods argument that comes with it.
  Developmental neurobiology — Sanes, Reh & Harris, **Development of the
  Nervous System**; owns how the wiring gets built. Neuroanatomy — Nolte,
  **The Human Brain**; owns where things are, which quietly constrains every
  story anyone tells. Behavioural endocrinology — Nelson & Kriegsfeld, **An
  Introduction to Behavioral Endocrinology**; owns how hormones set the state
  the circuits run in. Clinical neurology and neuropsychology — **Adams and
  Victor's Principles of Neurology**, with Lezak, **Neuropsychological
  Assessment**; owns what breaks and what breaking reveals. Comparative and
  evolutionary neuroscience — Striedter, **Principles of Brain Evolution**;
  owns which features are general and which are ours.
- *The long canon:* Cajal, **Recollections of My Life** and **Advice for a
  Young Investigator** — the founder, and still the best advice on research
  temperament ever written. Marr, **Vision** — a monument; read the whole
  thing eventually, not just chapter 1. Hubel, **Eye, Brain, and Vision** —
  the discoverer explaining his own discovery. Luria, **The Mind of a
  Mnemonist** and **The Man with a Shattered World** — the founding case
  studies, and models of how to write about a person. Kandel, **In Search of
  Memory** — memoir and field history at once. Finger, **Origins of
  Neuroscience** — the long view. Buzsáki, **Rhythms of the Brain** and **The
  Brain from Inside Out** — heterodox, arguing that the standard
  stimulus-response framing has the causality backwards. Sterling & Laughlin,
  **Principles of Neural Design** — design constraints as explanation.
  Sapolsky, **Behave** — sprawling, and the best bridge from cells to social
  behaviour. Damasio, **Descartes' Error** — contested, generative. Crick,
  **The Astonishing Hypothesis** — the moment consciousness became a
  respectable research target. Jonas & Kording, "Could a Neuroscientist
  Understand a Microprocessor?" (2017) — a joke that is not a joke, and the
  sharpest methodological critique the field has produced. Eve Marder's
  essays on circuit degeneracy — the permanent corrective to naive
  mechanism-hunting.
- *Re-foundation watch:* durable — the neuron doctrine, Hodgkin–Huxley
  biophysics, synaptic transmission, gross anatomy, the classical lesion
  literature, Hubel and Wiesel. Volatile — nearly everything methodological.
  The small-sample human imaging literature is largely unreliable, and
  brain-wide association studies now appear to need thousands of subjects, not
  dozens; the cell-type taxonomy is being rewritten by single-cell
  transcriptomics and will be rewritten again; connectomics is scaling by
  orders of magnitude; the amyloid hypothesis in Alzheimer's has been through
  both clinical disappointment and a fraud scandal in its supporting
  literature. Signal you have gone stale: you cite a 2005 imaging result with
  n = 12 as established; you still say dopamine is the reward chemical; you
  cannot name the current cell-type nomenclature.
- *A lifetime practice:* a standing weekly journal club, alone or with others
  — one paper, read from the figures first, with a written note on what the
  controls did not rule out. Thirty years of that is fifteen hundred papers
  and a nose you cannot get any other way. If you have the tooling, keep your
  own analysis pipeline alive and run it against each major open dataset as it
  is released.
- *Rabbit holes:* the crab stomatogastric ganglion — thirty neurons, decades
  of work, still not solved, and the best argument that "understanding a
  circuit" is harder than it sounds; place cells, grid cells, and what a
  cognitive map is; blindsight and what it means to see without seeing;
  *C. elegans*, which has had a complete connectome since 1986 and still
  cannot have its behaviour predicted from it; the rise and deflation of
  mirror neurons, as a case study in how a field overclaims.

## Psychology (cognitive, social, developmental, clinical)

**The question it asks.** What are the mechanisms that produce perception,
memory, motivation, personality, development, and disorder — and how much of
what we find in one sample of humans is true of humans? It is uniquely hard
because the instrument and the object of study are the same kind of thing,
and because its constructs (attention, self-esteem, intelligence) have to be
*invented* before they can be measured.

**Big ideas to walk away with.**
- Two-system / bounded rationality: judgment runs on heuristics that are
  usually adaptive and predictably wrong in specifiable ways.
- Attention and working memory are hard capacity limits, and much of
  cognition is architecture built around those limits.
- Reinforcement and associative learning — the oldest and most durable
  mechanistic story psychology has.
- Situationism: behavior is far more context-driven than either lay intuition
  or the actors themselves believe.
- Development is staged but not lockstep; attachment shapes later relating;
  nature and nurture is a false dichotomy — heritability is a population
  statistic, not a claim about any individual.
- Individual differences are real and measurable: g and the Big Five are
  among the most replicable findings in the whole field.
- Signal detection theory and psychophysics: the measurement backbone that
  separates sensitivity from bias.
- Clinically: the diathesis–stress framing, and that some treatments (CBT,
  exposure) have far better evidence than others.

**What outsiders get wrong.**
- The replication crisis. The Open Science Collaboration's 2015 attempt at
  100 studies reproduced roughly a third at comparable effect size. Ego
  depletion, social priming, power posing, and much of the "small intervention,
  big life outcome" literature did not survive. This is not a reason to
  dismiss the field — it is the field correcting itself, and it means you must
  read anything published before ~2013 with the sample size and the effect
  size in front of you.
- WEIRD samples: most published findings come from Western, Educated,
  Industrialized, Rich, Democratic undergraduates, generalized to *humans*.
- Freud is intellectual history, not current science; and pop psychology is
  not psychology — the gap is as wide as astrology to astronomy.

**T3 — Literacy (~180 hrs)**
- *Start here:* Daniel Kahneman, **Thinking, Fast and Slow**. The door because
  it shows, repeatedly, how a vague claim about the mind gets converted into a
  cheap decisive experiment. Read it with the replication crisis in hand: the
  priming chapter has not held up, and Kahneman said so publicly before he
  died. Watching a great book age is itself part of the literacy.
- *Survey:* Peter Gray & David Bjorklund, **Psychology** — a real textbook,
  evolutionary in framing and genuinely well written. Paul Bloom's **Psych:
  The Story of the Human Mind** is the shorter, more opinionated alternative.
- *Canon:* William James, **The Principles of Psychology** (1890). Astonishing
  and still quoted. Read five chapters and stop: "Habit," "The Stream of
  Thought," "The Consciousness of Self," "Attention," and "Will." Add
  Festinger, Riecken & Schachter's **When Prophecy Fails** for what social
  psychology looked like when it was brave.
- *Course:* Open Yale **PSYC 110, Introduction to Psychology** (Paul Bloom) —
  free at oyc.yale.edu, and among the best introductory courses in any
  subject, anywhere. Take it whole.
- *Artifact:* Pick a famous psychological finding you believed before you
  started. Write 2,000 words tracing its full evidential history: the original
  study's N and effect size, what the press said, what replication attempts
  found, and where the claim honestly stands today. Then state what you would
  need to see to change your mind again.

**T2 — Working depth**
- *Spine:* Goldstein, **Cognitive Psychology**; Gilovich, Keltner & Nisbett,
  **Social Psychology**; Siegler et al., **How Children Develop**; Barlow &
  Durand, **Abnormal Psychology**. Then the methods books that matter more
  than any of them: Field, **Discovering Statistics Using R**, and Gelman &
  Hill on regression and multilevel models.
- *Practice:* Run a study end to end, more than once. Build the task in
  jsPsych or PsychoPy, do the power analysis *first* (G*Power), preregister on
  OSF, collect on Prolific, analyze in R with mixed-effects models (lme4),
  report effect sizes with confidence intervals. Then do the harder thing:
  pick a published effect and try to replicate it exactly. Separately, code
  observational or interview data and compute inter-rater reliability — the
  qualitative skills are not optional for developmental or clinical work.
- *Primary literature:* Psychological Science, Journal of Personality and
  Social Psychology, Cognition, Psychological Review, Nature Human Behaviour,
  and Advances in Methods and Practices in Psychological Science. Read
  directly: Miller (1956) on the magical number seven; Tversky & Kahneman
  (1974) on judgment under uncertainty; Simmons, Nelson & Simonsohn (2011),
  "False-Positive Psychology" — the paper that named the disease.
- *You've arrived when:* handed any published result, you can state its
  design, N, effect size, and the three most plausible alternative
  explanations within ten minutes — and you can design, preregister, run, and
  analyze a properly powered study of your own without supervision.

**T1 — Mastery**
- *Graduate texts/monographs:* **Stevens' Handbook of Experimental Psychology
  and Cognitive Neuroscience**; the **Handbook of Social Psychology** (Fiske,
  Gilbert & Lindzey); Kruschke, **Doing Bayesian Data Analysis**; Borsboom,
  **Measuring the Mind** on the philosophy of psychological measurement — the
  book most working psychologists should read and haven't.
- *Frontier:* Computational cognitive modeling (Griffiths, Chater &
  Tenenbaum's **Bayesian Models of Cognition**); computational psychiatry;
  network theories of psychopathology; large-scale distributed replication
  (the Psychological Science Accelerator, ManyBabies); cultural evolution
  after Henrich; and the ongoing measurement-reform argument.
- *Contribution looks like:* a theory that makes point predictions rather than
  directional ones; a method or measure others adopt; a well-powered
  multi-site test that settles something.
- *Community:* Association for Psychological Science, APA, Psychonomic
  Society, Cognitive Science Society, SPSP (social), SRCD (developmental),
  ABCT (clinical), and SIPS for the reform wing.

**Beyond T1 — the long shelf**

- *Branch into:* psychophysics and perception — Goldstein, **Sensation and
  Perception**, with Gescheider, **Psychophysics**; owns the mapping from
  physical stimulus to experience, and it is the most durable part of the
  whole discipline. Memory — Baddeley, Eysenck & Anderson, **Memory**; owns
  encoding, retrieval, and distortion. Judgment and decision making — Hastie &
  Dawes, **Rational Choice in an Uncertain World**; owns departures from the
  normative model. Psychometrics and individual differences — Furr &
  Bacharach, **Psychometrics**; owns whether your construct exists at all.
  Behaviour genetics — Plomin et al., **Behavioral Genetics**; owns where
  variance comes from, and it is a minefield worth entering carefully.
  Personality — Funder, **The Personality Puzzle**; owns what is stable in a
  person across situations. Cultural and evolutionary psychology — Henrich,
  **The WEIRDest People in the World**; owns which of your findings are about
  humans. Clinical science — Barlow, **Clinical Handbook of Psychological
  Disorders**; owns what actually helps, and how you would know.
- *The long canon:* James, **The Principles of Psychology**, this time whole —
  it takes a year and repays it. Skinner, **Science and Human Behavior**
  (free from the B. F. Skinner Foundation) — the position everyone caricatures
  without reading. Neisser, **Cognitive Psychology** (1967) — the book that
  named the field. Simon, **Models of Bounded Rationality** — the alternative
  to the rational agent, from the person who built it. Gibson, **The
  Ecological Approach to Visual Perception** — heterodox, still generating
  research fifty years on. Bowlby, **Attachment and Loss** — the origin of a
  framework now everywhere and often mangled. Meehl, **Clinical versus
  Statistical Prediction** (1954) — a hundred pages that were right and were
  ignored for sixty years. Cronbach & Meehl, "Construct Validity in
  Psychological Tests" (1955) — the paper the whole measurement argument
  descends from. Ellenberger, **The Discovery of the Unconscious** — the
  definitive history of dynamic psychiatry. Gould, **The Mismeasure of Man** —
  famous polemic, itself substantially contested; read it with the critiques
  beside it, as an exercise in evaluating a beloved book. Gina Perry, **Behind
  the Shock Machine**, and Le Texier's 2019 reassessment of the Stanford
  Prison Experiment — what happens when the archives of famous studies are
  finally opened. Chambers, **The Seven Deadly Sins of Psychology**, and
  Ritchie, **Science Fictions** — the reform case, from inside. Kahneman &
  Klein (2009), "Conditions for Intuitive Expertise" — adversarial
  collaboration done properly, and a model for how to disagree.
- *Re-foundation watch:* durable — psychophysics, signal detection, the basic
  memory phenomena (serial position, spacing, retrieval practice), conditioning,
  capacity limits, the Big Five's factor structure, developmental milestones.
  Volatile — the social psychology effect catalogue, where much of the
  pre-2013 literature has already gone and more will follow; treatment
  guidelines; the diagnostic system itself, with DSM categories now contested
  by RDoC and HiTOP; anything about technology and wellbeing; and the
  measurement-reform argument, which is unfinished. Signal you have gone
  stale: you quote an effect without checking for a post-2015 replication;
  your evidence for a treatment is more than ten years old; you cannot say
  what a registered report or a multiverse analysis is.
- *A lifetime practice:* keep a provenance log. Every week, take one
  psychological claim you met in the wild, spend twenty minutes tracing it to
  its original study, and write two paragraphs on where it honestly stands.
  Ten years of that produces a calibration almost nobody has, including many
  professionals. Add one small properly-powered study of your own a year,
  however trivial the question — running them keeps you honest about how hard
  it is.
- *Rabbit holes:* the Flynn effect and its apparent reversal in some
  countries; the spacing effect and desirable difficulties, which is the one
  finding that should change how you study everything else on this map;
  Tetlock's forecasting tournaments and what distinguished the accurate
  minority; the open-label placebo literature, which should not work and
  apparently does; feral children, critical periods, and the case of Genie —
  and the ethics of studying her.

## Linguistics

**The question it asks.** What exactly do you know when you know a language —
a system you acquired as a small child, without instruction, and cannot fully
state? And what is common across all seven thousand of them? Language is at
once a mental computational system, a social marker, and a historical
artifact, and the field's deepest disagreements are about which of those is
primary.

**Big ideas to walk away with.**
- Discrete infinity: a finite inventory plus recursive combination yields
  unbounded expression. This is the property that needs explaining.
- The levels: phonetics, phonology, morphology, syntax, semantics,
  pragmatics — each with its own units and its own rules.
- Descriptive, not prescriptive. "Grammatical" means what fluent speakers
  actually produce; every stigmatized variety, including AAVE, is
  rule-governed to the same precision as any standard.
- The central live fight: poverty-of-the-stimulus and an innate Universal
  Grammar versus usage-based, construction-based learning from input.
  You should be able to argue both sides.
- Saussure's frame: the sign is arbitrary; langue versus parole; synchronic
  versus diachronic description.
- Sound change is regular, which is why the comparative method can
  reconstruct languages nobody ever wrote down.
- Typology and universals: what varies, what doesn't, and why implicational
  universals are more interesting than absolute ones.
- Variation is structured, not noise (Labov) — social factors predict
  linguistic form quantitatively.

**What outsiders get wrong.**
- Prescriptivism. "Correct grammar" is a social standard, useful and real as
  a social fact, but it is not a fact about language.
- Strong linguistic relativity — language determining thought — is dead. The
  weak version survives and is modest. And nobody has an unusual number of
  words for snow.
- Linguistics is not polyglottery. Speaking many languages is a different
  skill; many excellent linguists are monolingual, and knowing ten languages
  teaches you nothing about phonological rule ordering.

**T3 — Literacy (~150 hrs)**
- *Start here:* Guy Deutscher, **The Unfolding of Language**. The door because
  it shows grammar the way geology shows mountains — as the accumulated
  residue of ordinary erosion and laziness. You will never again think of
  grammatical structure as designed. (Pinker's **The Language Instinct** is the
  more famous entry point; read it too, but know it argues one side hard.)
- *Survey:* **Language Files** (Ohio State University Department of
  Linguistics). Exercise-driven, covers every subfield, and the problem sets
  are the point — do them, don't read past them.
- *Canon:* Saussure, **Course in General Linguistics** — read the Introduction,
  Part One on the nature of the sign, and the synchrony/diachrony material;
  the rest is skippable. Chomsky, **Syntactic Structures** is short: read
  chapters 1–5, above all the "colorless green ideas" argument, then his 1959
  review of Skinner's *Verbal Behavior*, which is the shot that started the
  cognitive revolution. Edward Sapir's **Language** (1921) is beautiful prose
  and still worth the evening. Bloomfield's **Language** (1933) is heavy —
  skip it.
- *Course:* MIT OCW **24.900 Introduction to Linguistics** — full materials
  free, and unusually good on syntax. Leiden's **Miracles of Human Language**
  (Marc van Oostendorp, Coursera) is the friendlier alternative and stronger
  on typology and fieldwork.
- *Artifact:* Transcribe three minutes of your own unscripted speech in IPA —
  actual narrow transcription, not spelling. Then write 1,500 words on what
  the transcription reveals that the orthography hides, and on what a
  five-year-old knows about your language that nobody taught them. Cite real
  child-language data (CHILDES is free) rather than reasoning from the
  armchair.

**T2 — Working depth**
- *Spine:* Ladefoged & Johnson, **A Course in Phonetics**; Hayes,
  **Introductory Phonology**; Carnie, **Syntax: A Generative Introduction**;
  Haspelmath & Sims, **Understanding Morphology**; Saeed, **Semantics**;
  Levinson, **Pragmatics**; Campbell, **Historical Linguistics**.
- *Practice:* The core drill is problem sets on languages you don't speak:
  given 40 words of data, derive the phoneme inventory, the allophonic rules
  and their ordering, and the morpheme boundaries. Do hundreds. Then get real
  data: run elicitation sessions with a native speaker of a language you
  don't know, using standard fieldwork method; annotate in ELAN; do acoustic
  analysis in Praat (vowel formants, VOT); do corpus work in COCA or CHILDES
  with actual frequency statistics. Build syntactic analyses of a
  construction and test your predictions against native-speaker judgments you
  collect systematically, not casually.
- *Primary literature:* Language (LSA), Linguistic Inquiry, Natural Language
  & Linguistic Theory, Journal of Phonetics, and Glossa (open access). Read
  directly: Greenberg (1963) on word-order universals; Labov (1963) on Martha's
  Vineyard, the paper that founded sociolinguistics; Grice (1975), "Logic and
  Conversation," which invented modern pragmatics in twenty pages.
- *You've arrived when:* handed 50 words of an unfamiliar language with
  glosses, you produce a defensible phoneme inventory, ordered phonological
  rules, and a morphological segmentation — and can say which further data
  would distinguish your analysis from the competing one.

**T1 — Mastery**
- *Graduate texts/monographs:* Adger, **Core Syntax** and Chomsky's **The
  Minimalist Program** on the generative road; Heim & Kratzer, **Semantics in
  Generative Grammar** — the standard graduate semantics text and genuinely
  hard; Prince & Smolensky, **Optimality Theory**; Croft, **Radical
  Construction Grammar** and Dixon's **Basic Linguistic Theory** for the
  typological/descriptive road; Huddleston & Pullum, **The Cambridge Grammar
  of the English Language** as reference.
- *Frontier:* Documentation of endangered languages — roughly half of the
  world's languages will not survive the century, and this work has a
  deadline. Also: quantitative typology on large databases (WALS, Grambank);
  experimental syntax and semantics; neurolinguistics of the language network;
  and large language models used as evidence in the learnability argument,
  which has reopened questions everyone thought were settled.
- *Contribution looks like:* a language described and documented that wasn't;
  a formal analysis that unifies patterns previously treated separately; a
  corpus or database others build on.
- *Community:* Linguistic Society of America and its biennial Summer
  Institute (the field's central training event); NELS and WCCFL for syntax;
  SALT for semantics; ACL if you go computational; SSILA for the Americas;
  and the Endangered Languages Documentation Programme for fieldwork funding.

**Beyond T1 — the long shelf**

- *Branch into:* phonetics and speech science — Keith Johnson, **Acoustic and
  Auditory Phonetics**; owns the physical signal and how ears carve it.
  Phonology — Kenstowicz, **Phonology in Generative Grammar**; owns sound
  patterns as mental computation. Syntax beyond one framework — Sag, Wasow &
  Bender, **Syntactic Theory** (HPSG), read against Adger; owns the
  combinatorics of sentences, and reading two frameworks is the only cure for
  mistaking a notation for a fact. Formal semantics — Heim & Kratzer, already
  named, then Portner; owns how form fixes truth conditions. Historical and
  comparative linguistics — Fortson, **Indo-European Language and Culture**;
  owns descent and change. Sociolinguistics — Labov, **Principles of
  Linguistic Change** (3 vols); owns structured variation in a community.
  Psycholinguistics and acquisition — Traxler, **Introduction to
  Psycholinguistics**, with Tomasello, **Constructing a Language**; owns
  real-time processing and how children get there. Sign language linguistics —
  Sandler & Lillo-Martin, **Sign Language and Linguistic Universals**; owns
  what modality does and does not change, and it will overturn assumptions you
  did not know you had. Computational linguistics — Jurafsky & Martin,
  **Speech and Language Processing** (free draft); owns language as something
  a machine must model.
- *The long canon:* Jespersen, **The Philosophy of Grammar** — a century old
  and still argued with. Whorf, **Language, Thought, and Reality** — read the
  primary source, since he is almost always cited through caricature.
  Hockett, "The Origin of Speech" (1960) — the design features, still the
  cleanest statement of what makes language language. Chomsky & Halle, **The
  Sound Pattern of English** — the monument phonology has spent fifty years
  responding to. Randy Allen Harris, **The Linguistics Wars** — how the field
  actually behaved during its central schism. Evans & Levinson (2009), "The
  Myth of Language Universals", with the twenty published responses — the best
  single heterodox attack and the field arguing in public. Everett, **Don't
  Sleep, There Are Snakes**, read with the published rebuttals — a contested
  challenge, and a lesson in evaluating fieldwork claims. Deutscher, **Through
  the Language Glass** — the moderate relativity case, honestly made. Labov,
  **The Social Stratification of English in New York City** — the founding
  quantitative study. Ostler, **Empires of the Word** — world history told
  through languages. Nettle & Romaine, **Vanishing Voices** — the case for
  documentation, made before it was fashionable. Crystal, **The Cambridge
  Encyclopedia of Language** — a browsing reference good for decades.
  Berlin & Kay, **Basic Color Terms** — contested for fifty years and still
  the reference point for the whole relativity debate.
- *Re-foundation watch:* durable — the descriptive levels, articulatory
  phonetics and the IPA, the comparative method, fieldwork technique, Grice,
  Labov's findings, the basic typological facts. Volatile — syntactic theory
  above all: the framework you learn at 25 may be unrecognisable at 55, and
  Minimalism has already been revised repeatedly without settling. Also
  volatile: the learnability argument, genuinely reopened by language models
  trained on child-scale input; documentation technology; and the typological
  databases, which keep growing. Signal you have gone stale: you talk about
  "the" generative framework as if it were fixed; your position on poverty of
  the stimulus has not moved since before large language models; you cannot
  name a paper from the last five years in a subfield you claim.
- *A lifetime practice:* one grammar a year. Take a reference grammar of a
  language you do not speak, work through it, and write your own ten-page
  structural sketch — inventory, morphology, alignment, word order, whatever
  is strange. Thirty of those, deliberately spread across families and areas,
  gives you an internal typology no textbook can hand you. Keep a few minutes
  of narrow IPA transcription a month alongside it, or the ear goes.
- *Rabbit holes:* the laryngeal theory — sounds predicted from
  reconstruction alone, then found in Hittite decades later, one of the
  humanities' great predictive successes; Nicaraguan Sign Language emerging
  with full grammar in a single generation of children; Ventris and the
  decipherment of Linear B, then the scripts still unread; whistled and
  drummed languages; creole genesis and the bioprogram hypothesis.

## Artificial intelligence (as a field of study, not a toolset)

**The question it asks.** What is required to build a system that perceives,
reasons, learns, and acts competently in a world it was never fully told
about? The field is unusual in having an engineering half and a philosophical
half that cannot be separated: every working system is also a claim about
what intelligence *is*, and every failure is evidence about what it isn't.

**Big ideas to walk away with.**
- Search over problem spaces — the field's first unifying idea and still its
  skeleton: state spaces, heuristics, A*, adversarial search, Monte Carlo
  tree search.
- Knowledge representation and the frame problem: saying what you know is
  harder than reasoning with it, and saying what *doesn't* change is worse.
- Agents and rationality: expected utility as the normative standard, and
  probability as the successor to logic for most real problems.
- Learning theory: why generalization from finite data is possible at all —
  bias–variance, PAC learning, no free lunch.
- Reinforcement learning: MDPs, value and policy, exploration versus
  exploitation, credit assignment.
- Sutton's "bitter lesson": general methods that scale with computation keep
  beating hand-engineered knowledge. Know why, and what it doesn't imply.
- Specification and alignment: optimizing a stated objective is not getting
  what you wanted. Goodhart's law is an engineering constraint, not a joke.
- The philosophical stack: the Turing test, the Chinese Room, symbol
  grounding, Moravec's paradox.

**What outsiders get wrong.**
- Capability is not understanding — in both directions. A benchmark score
  tells you almost nothing about what internal representation produced it,
  and interpretability lags capability badly; the people building these
  systems will say so. Equally, "it's just statistics" is a dismissal
  masquerading as an analysis: it makes no prediction and rules nothing out.
- AI is not the current crop of models. The field is seventy years old. The
  tooling has a two-year half-life; search, representation, learning theory,
  and the philosophical questions do not. Learn tools inside a project that
  needs them — never schedule a framework years ahead (principle 5). This
  section deliberately names almost no libraries.
- Benchmarks are constructed artifacts with their own failure modes —
  contamination, saturation, construct invalidity. Read one as skeptically
  as you'd read a psychology paper.

**T3 — Literacy (~250 hrs)**
- *Start here:* Melanie Mitchell, **Artificial Intelligence: A Guide for
  Thinking Humans**. The door because Mitchell is a working researcher who
  takes both the achievements and the skepticism seriously, and keeps the
  historical thread visible — you finish knowing the field has a past, which
  is what separates literacy from following the news.
- *Survey:* Russell & Norvig, **Artificial Intelligence: A Modern Approach**.
  Do not attempt it whole at this tier. Read Part I on intelligent agents and
  the search chapters, skim uncertainty and decisions, and read the closing
  philosophy-and-futures chapters properly. For history, Nils Nilsson's **The
  Quest for Artificial Intelligence** (Cambridge, 2010) is the authoritative
  account by someone who was there.
- *Canon:* Turing (1950), "Computing Machinery and Intelligence" — read the
  objections-and-replies section, not just the imitation game. The 1955
  Dartmouth proposal (McCarthy, Minsky, Rochester & Shannon), which names the
  field. Newell & Simon's 1976 Turing Award lecture, "Computer Science as
  Empirical Inquiry: Symbols and Search," for the physical symbol system
  hypothesis, then Searle (1980), "Minds, Brains, and Programs," for the best
  attack on it. Chapter 1 of Marr's **Vision** for levels-of-analysis
  discipline. Sutton's "The Bitter Lesson" (2019) is two pages — read it, then
  argue with it.
- *Course:* MIT OCW **6.034 Artificial Intelligence** — Patrick Winston's
  lectures, free on video, the best teaching of AI *as a field* rather than as
  a stack. Follow with Berkeley's **CS188, Introduction to Artificial
  Intelligence**, whose free Pacman projects are the most efficient way to
  make search, CSPs, MDPs, and reinforcement learning stick. Skip courses that
  are really product tutorials; they expire before your notes do.
- *Artifact:* Write 2,500 words answering: what would have to be true for you
  to say a system understands something? State a concrete test, then apply it
  to a chess engine, a large language model, and a honeybee. Where the test
  gives an answer you don't believe, say so and diagnose why. A literate
  answer engages Turing and Searle without merely restating either.

**T2 — Working depth**
- *Spine:* Russell & Norvig, now cover to cover. Sutton & Barto,
  **Reinforcement Learning: An Introduction** (2nd ed, free online — the best
  textbook in the field). Murphy, **Probabilistic Machine Learning: An
  Introduction**, or Bishop's **Pattern Recognition and Machine Learning**.
  Goodfellow, Bengio & Courville, **Deep Learning** (free online). And
  Shalev-Shwartz & Ben-David, **Understanding Machine Learning** (free) for
  the theory almost everyone skips and shouldn't.
- *Practice:* Implement from scratch, in a language you control: A*, minimax
  with alpha–beta pruning, a CSP solver with constraint propagation, a
  resolution theorem prover, value iteration, Q-learning, a policy gradient.
  Write backpropagation by hand in numpy before you ever call a framework —
  Karpathy's free **Neural Networks: Zero to Hero** builds to a working
  transformer this way. Then reproduce a published result and run an ablation
  on it; the ablation is where you learn whether you understood the paper or
  the abstract.
- *Primary literature:* NeurIPS, ICML, ICLR, AAAI, IJCAI; JMLR, the Artificial
  Intelligence Journal, TMLR; arXiv cs.AI, cs.LG, cs.CL. Read directly:
  Krizhevsky, Sutskever & Hinton (2012) on AlexNet; Mnih et al. (2015) on
  deep Q-networks; Silver et al. (2016) on AlphaGo; Vaswani et al. (2017),
  "Attention Is All You Need." Add Amodei et al. (2016), "Concrete Problems
  in AI Safety," for how the specification problem is actually posed.
- *You've arrived when:* given an unfamiliar paper from a top venue, you can
  state its claim, identify the baseline it must beat for that claim to mean
  anything, implement a stripped-down version that reproduces the qualitative
  result — and say which of its numbers you don't believe, and why.

**T1 — Mastery**
- *Graduate texts/monographs:* Koller & Friedman, **Probabilistic Graphical
  Models**; Murphy, **Probabilistic Machine Learning: Advanced Topics**;
  Bertsekas, **Dynamic Programming and Optimal Control**; Boyd &
  Vandenberghe, **Convex Optimization** (free); Vapnik, **The Nature of
  Statistical Learning Theory**; Pearl, **Causality** — the book that made
  causal reasoning respectable again in a field that had exiled it.
- *Frontier:* Mechanistic interpretability; scaling laws and where they break;
  reasoning and planning as open problems rather than solved ones; agents and
  tool use; learning from human feedback and alignment; the neurosymbolic
  revival; evaluation as its own science. Follow the venues directly rather
  than commentary, and deliberately read researchers who disagree — Sutton and
  Chollet want different things, and the disagreement teaches more than either
  position alone.
- *Contribution looks like:* an algorithm with a proof or a reproducible
  result; a negative result that closes off a direction; an interpretability
  finding that explains a behavior rather than describing it; a formalization
  that lets a fuzzy question be argued precisely.
- *Community:* NeurIPS, ICML, ICLR, AAAI, IJCAI, UAI, AISTATS; ACL for
  language, CVPR for vision, CoRL for robotics; FAccT and AIES for ethics and
  governance. Open review and public reproduction are the norm — joining them
  is the cheapest way in.

**Beyond T1 — the long shelf**

- *Branch into:* learning theory — Mohri, Rostamizadeh & Talwalkar,
  **Foundations of Machine Learning**; owns when generalisation is guaranteed
  rather than observed. Robotics — Thrun, Burgard & Fox, **Probabilistic
  Robotics**, with LaValle, **Planning Algorithms** (free); owns intelligence
  that has a body and cannot ignore physics. Computer vision — Szeliski,
  **Computer Vision: Algorithms and Applications** (free), with Hartley &
  Zisserman, **Multiple View Geometry**; owns recovering a world from images.
  Natural language processing — Jurafsky & Martin (free); owns meaning from
  strings. Knowledge representation — Brachman & Levesque, **Knowledge
  Representation and Reasoning**; owns what a system can be said to believe,
  and it is the branch the current era neglects most. Automated planning —
  Ghallab, Nau & Traverso, **Automated Planning and Acting**; owns getting
  from a state to a goal. Multi-agent systems — Shoham & Leyton-Brown,
  **Multiagent Systems** (free); owns intelligence among other agents.
  Cognitive architectures — Anderson, **How Can the Human Mind Occur in the
  Physical Universe?**; owns what a whole mind's control structure would look
  like. Alignment and safety — Russell, **Human Compatible**, plus the
  technical literature; owns getting what you meant rather than what you said.
  Fairness and social impact — Barocas, Hardt & Narayanan, **Fairness and
  Machine Learning** (free); owns who is affected.
- *The long canon:* Wiener, **Cybernetics** and **The Human Use of Human
  Beings** — the ancestor field, and startlingly current. Ashby, **An
  Introduction to Cybernetics** (free) — still the clearest book on
  regulation and variety. Simon, **The Sciences of the Artificial** — what a
  science of made things even is. Minsky, **The Society of Mind**, and
  Minsky & Papert, **Perceptrons** — the second for the historical fight it
  caused. Rumelhart & McClelland, **Parallel Distributed Processing** (1986) —
  where the current paradigm actually starts. Newell, **Unified Theories of
  Cognition** — the most serious attempt to build a whole mind. Dreyfus,
  **What Computers Still Can't Do** — the great critic; wrong about much,
  right about embodiment, and worth more than most supporters. Weizenbaum,
  **Computer Power and Human Reason** — moral critique from someone inside.
  Winograd & Flores, **Understanding Computers and Cognition** — a founder
  changing his mind in public. McCorduck, **Machines Who Think** — the field's
  history by someone who was in the room. Hofstadter, **Fluid Concepts and
  Creative Analogies** — analogy as the core of cognition, a road not taken.
  Brooks, "Intelligence Without Representation" (1991), and Chollet, "On the
  Measure of Intelligence" (2019) — two short heterodox papers, thirty years
  apart, both still unanswered. Bostrom, **Superintelligence**, and Christian,
  **The Alignment Problem** — dated in places, but the debate descends from
  them. Marcus & Davis, **Rebooting AI**, and O'Neil, **Weapons of Math
  Destruction** — the contrarian and critical wings, read for their strongest
  points rather than their weakest.
- *Re-foundation watch:* this is the most volatile domain in the file, and you
  should plan for that rather than resent it. Durable — search, knowledge
  representation, probability and decision theory, learning theory, the RL
  formalism, the cybernetic framing, the philosophical arguments, and the
  history. Volatile — essentially everything about whatever paradigm is
  current: architectures, training methods, capabilities, costs, benchmarks,
  the interpretability toolkit, every library. Volatile too, and less
  noticed: what the field believes its central problem is. That has flipped
  roughly every fifteen years, and it will flip more than once inside seventy.
  Whatever dominates when you are 25 is a history chapter at 55. Signal you
  have gone stale: your model of what systems can do is a demo you saw three
  years ago; you confidently describe a limitation that has been fixed; you
  cannot name what replaced the technique you learned.
- *A lifetime practice:* keep a dated capability logbook. Fix a personal
  battery of tasks you actually care about, write down beforehand how you
  expect the best available system to do, run it, record the result — every
  six months, forever. Thirty years of that is a private, uncontaminated
  evaluation record and a calibration training set for your own judgment, and
  it is worth more than any quantity of commentary. Alongside it, implement
  one classic pre-2010 algorithm a year, so the field's memory stays in your
  hands and not only in its citations.
- *Rabbit holes:* the Lighthill report and how a field talks itself into a
  winter; SHRDLU's blocks world and the precise reason it did not scale; Cyc
  and a thirty-year bet on hand-built knowledge; the multiple independent
  discoveries of backpropagation, and what priority disputes reveal about how
  fields remember; reward hacking in the wild, starting with the boat-racing
  agent that learned to spin in circles collecting points forever.
