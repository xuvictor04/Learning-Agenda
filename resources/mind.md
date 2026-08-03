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
