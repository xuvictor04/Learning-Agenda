# Formal

## Mathematics (as a domain)

**The question it asks.** Which patterns are *necessarily* true — forced into
existence by a few assumptions rather than observed in the world — and how far
can pure deduction be pushed before it runs out? A second question shadows the
first and nobody has answered it: why does a subject built with no reference
to reality keep predicting reality with absurd precision?

**Big ideas to walk away with.**
- Proof is the unit of knowledge. "Checked a million cases" and "settled
  forever" are different epistemic species.
- Abstraction as method: group, ring, field, vector space, metric, topology.
  You stop studying objects and start studying the pattern they share.
- The limit — the single idea that makes calculus, analysis, and all of
  continuous mathematics possible, and took 200 years to state correctly.
- Algebra and geometry are the same subject in two languages (Descartes'
  coordinates; Klein's Erlangen program; algebraic geometry).
- Symmetry is explanatory: Galois showed that "can this equation be solved by
  radicals?" is secretly a question about a group.
- Infinity comes in sizes, and Cantor's diagonal argument proves it in four
  lines. That argument recurs everywhere in this file.
- Pure and applied are not separable in advance. Number theory was the
  proudly useless branch until it became the basis of all encryption.

**What outsiders get wrong.**
- That mathematics is about numbers and calculation. Arithmetic is to
  mathematics what spelling is to literature.
- That it is finished. More new mathematics is published each year than in
  the whole nineteenth century.
- That speed indicates talent. Serious mathematics is done slowly, and
  research problems take years.

**T3 — Literacy (~200 hrs)**
- *Start here:* Timothy Gowers, **Mathematics: A Very Short Introduction**.
  150 small pages, and the door because it explains the *abstract method* —
  why mathematicians refuse to say what a number "really is" — which is the
  thing that locks outsiders out.
- *Survey:* Aleksandrov, Kolmogorov & Lavrent'ev, **Mathematics: Its
  Content, Methods and Meaning** (Dover, three volumes in one), the great
  panorama written by masters. If it's too dense, Courant & Robbins,
  **What Is Mathematics?** is the friendlier equivalent.
- *Canon:* Euclid, **Elements**, Book I — the definitions, postulates and
  common notions slowly, then Propositions 1–47, ending at Pythagoras. Add
  Book IX Prop. 20, the infinitude of primes: two paragraphs and perfect.
  Skip the rest of Euclid. Then G. H. Hardy, **A Mathematician's Apology**.
- *Course:* 3Blue1Brown's **Essence of Linear Algebra** and **Essence of
  Calculus** (free, ~8 hrs) for geometric intuition, then MIT OCW **18.06
  Linear Algebra** with Gilbert Strang for the real thing. The videos are
  intuition pumps, not substitutes.
- *Artifact:* Explain Cantor's diagonal argument and Galois' insight to a
  bright sixteen-year-old, in full, in 2,000 words — then use those two
  examples to argue whether mathematics is discovered or invented.

**T2 — Working depth**
- *Spine:* Daniel Velleman, **How to Prove It** (or Hammack's free **Book of
  Proof**) to learn proof-writing; Spivak, **Calculus**; Axler, **Linear
  Algebra Done Right**; Abbott, **Understanding Analysis** then Rudin,
  **Principles of Mathematical Analysis**; Dummit & Foote, **Abstract
  Algebra** (or Artin, **Algebra**); Munkres, **Topology**.
- *Practice:* Every exercise in Velleman ch. 1–3 and Abbott ch. 1–4, no
  solutions consulted, written in full sentences. All of Axler ch. 1–7. A
  third of Dummit & Foote ch. 1–4 and 7–9. Budget 1,500+ worked problems over
  two to three years: this is the job, and the reading is only setup for it.
  People stall in exactly one place — they read proofs instead of producing
  them.
- *Primary literature:* survey articles in *Notices of the AMS* and
  *Bulletin of the AMS*; research papers in *Annals of Mathematics* are not
  yet readable and that's fine. Read directly: Wigner, "The Unreasonable
  Effectiveness of Mathematics in the Natural Sciences" (1960); Thurston,
  "On Proof and Progress in Mathematics" (*Bulletin AMS*, 1994); Cantor's
  1891 diagonal paper.
- *You've arrived when:* you can take an unfamiliar theorem statement from a
  *Bulletin* survey and reconstruct a proof over a weekend — and you can read
  someone else's proof and point to the exact line where it fails.

**T1 — Mastery**
- *Graduate texts/monographs:* nobody masters "mathematics"; you master a
  subfield. By direction: Rudin, **Real and Complex Analysis** and Folland,
  **Real Analysis**; Lang, **Algebra**; Hatcher, **Algebraic Topology**
  (free); Lee, **Introduction to Smooth Manifolds**; Hartshorne, **Algebraic
  Geometry**. The **Princeton Companion to Mathematics** (ed. Gowers) keeps
  you oriented outside your corner.
- *Frontier:* the Langlands program; formalization in Lean and mathlib
  (follow Kevin Buzzard); Polymath-style collaboration. Daily feeds: arXiv
  math listings, Terence Tao's blog, MathOverflow, *Quanta Magazine*.
- *Contribution looks like:* a theorem nobody has proved, published in a
  refereed journal. Also real and undervalued: a new proof of a known
  theorem, a decisive counterexample, a formalization, or an expository
  synthesis that makes a subfield learnable.
- *Community:* AMS, MAA, SIAM; the Joint Mathematics Meetings each January;
  the ICM every four years; workshops at SLMath (formerly MSRI) and
  Oberwolfach.

## Logic & foundations

**The question it asks.** What makes an argument valid regardless of its
subject matter — and can all of mathematics be reduced to mechanical
manipulation of symbols from a fixed list of axioms? The programme to answer
"yes" ran from Frege to Hilbert and was killed by Gödel in 1931. The shape of
that failure, and what survived it, is the field.

**Big ideas to walk away with.**
- Syntax versus semantics; provability versus truth. Keeping these apart is
  the whole discipline in one habit.
- Soundness and completeness: for first-order logic, provable and true-in-
  all-models coincide (Gödel, 1929). This is the good news.
- Incompleteness: any consistent, effectively axiomatised theory strong
  enough for arithmetic has true sentences it cannot prove, and cannot prove
  its own consistency. Every hypothesis in that sentence is load-bearing.
- Sets as foundation: ZFC, the axiom of choice, cardinality, and the
  independence of the continuum hypothesis (Gödel's constructible universe
  plus Cohen's forcing).
- Computability and provability are the same subject: Church–Turing, the
  halting problem, the undecidability of the Entscheidungsproblem.
- Model theory: a theory never pins down one structure. Löwenheim–Skolem and
  nonstandard models of arithmetic are the standing proof.
- Constructive mathematics rejects excluded middle — and via the
  Curry–Howard correspondence, proofs turn out to be programs.

**What outsiders get wrong.**
- Gödel did not show mathematics is broken, that "nothing can be proven," or
  that truth is relative. Read Torkel Franzén, **Gödel's Theorem: An
  Incomplete Guide to Its Use and Abuse**, as an inoculation.
- Formal logic is not "being logical." It is the mathematical study of formal
  systems, not a rhetoric of debate; the list of informal fallacies belongs
  to a different and much shallower subject.
- "Undecidable" is always relative to a system. A sentence unprovable in one
  theory is often provable in a stronger one.

**T3 — Literacy (~150 hrs)**
- *Start here:* Nagel & Newman, **Gödel's Proof**. Roughly 100 pages, and the
  door because it actually walks the argument rather than gesturing at it.
- *Survey:* Graham Priest, **Logic: A Very Short Introduction** for the map,
  then Peter Smith's free **An Introduction to Formal Logic**
  (logicmatters.net) for the machinery — truth tables, natural deduction,
  quantifiers. Skip the machinery and nothing after it will land.
- *Canon:* Gödel's 1931 paper is brutal; take it through Smith's **An
  Introduction to Gödel's Theorems** instead. Do read Turing's 1936 **On
  Computable Numbers**, sections 1–4, with Petzold's **The Annotated Turing**
  beside it. Then Frege's preface to the **Begriffsschrift** and Russell's
  1902 letter to Frege — both in van Heijenoort's **From Frege to Gödel**,
  and together an evening's work.
- *Course:* Stanford Online's **Introduction to Logic** (Michael Genesereth)
  is decent, but plainly: no MOOC here beats reading, and Peter Smith's free
  **Beginning Mathematical Logic: A Study Guide** is a better roadmap than
  any course on offer.
- *Artifact:* State both incompleteness theorems precisely, with every
  hypothesis, then explain in 1,500 words what each hypothesis is doing and
  what the theorems do *not* imply about minds, machines, or mathematics.

**T2 — Working depth**
- *Spine:* Enderton, **A Mathematical Introduction to Logic**; Boolos,
  Burgess & Jeffrey, **Computability and Logic**; Smith, **An Introduction to
  Gödel's Theorems**; Halmos, **Naive Set Theory** then Enderton, **Elements
  of Set Theory**.
- *Practice:* Build the whole tower yourself, in order: soundness and
  completeness for propositional logic, then for first-order; compactness;
  Löwenheim–Skolem; then arithmetisation and both incompleteness theorems.
  Every exercise in Enderton ch. 1–2, most of ch. 3. Then formalise: work
  through **Software Foundations** (Pierce et al., free, in Coq) or
  **Mathematics in Lean** — 100+ hours with a proof assistant changes what
  you believe a proof is.
- *Primary literature:* *Journal of Symbolic Logic*, *Bulletin of Symbolic
  Logic*, *Notre Dame Journal of Formal Logic*. Read directly: Gödel 1931;
  Turing 1936; Tarski, "The Semantic Conception of Truth" (1944); Cohen,
  "The Independence of the Continuum Hypothesis" (*PNAS*, 1963–64).
- *You've arrived when:* you can prove the completeness theorem from scratch
  at a whiteboard, and explain to a working mathematician exactly why it does
  not contradict incompleteness.

**T1 — Mastery**
- *Graduate texts/monographs:* Kunen, **Set Theory**; Jech, **Set Theory**
  (Third Millennium ed.); Marker, **Model Theory: An Introduction** and
  Hodges, **Model Theory**; Soare, **Turing Computability**; Simpson,
  **Subsystems of Second Order Arithmetic** for reverse mathematics;
  Troelstra & van Dalen, **Constructivism in Mathematics**; Girard, Lafont &
  Taylor, **Proofs and Types** (free).
- *Frontier:* forcing, large cardinals and Woodin's work on the continuum;
  homotopy type theory and univalent foundations (the **HoTT Book** is free);
  reverse mathematics; proof assistants and the mathlib project as a
  foundational experiment running in public.
- *Contribution looks like:* an independence result; a new axiom with mapped
  consequences; classification theorems in model theory; degree-theoretic
  results in computability; or formalising a major theorem end to end.
- *Community:* the Association for Symbolic Logic (its Logic Colloquium and
  ASL meetings); the FOM mailing list; the nLab; the Lean Zulip, which is
  where a surprising amount of current foundational work happens.

## Statistics & probability

**The question it asks.** How much can you honestly claim about a world you
cannot fully observe, from a finite and noisy sample of it? Probability builds
the mathematics of chance forward from axioms; statistics runs it backwards,
from data to the process that produced the data. Everything difficult lives in
that reversal, because many processes produce the same data.

**Big ideas to walk away with.**
- Conditioning is the core operation. Sample space, random variable,
  expectation — then P(A|B), which is where almost all confusion originates.
- The law of large numbers and the central limit theorem: why the normal
  distribution is everywhere, and the conditions under which it isn't.
- Bayes' theorem, and the ruthless importance of base rates.
- The sampling distribution and the standard error. Grasping that your
  estimate is itself a random variable *is* the concept of inference.
- Frequentist versus Bayesian: whether a probability describes a long-run
  procedure or a state of belief. Both are usable; know which you're doing.
- Bias and variance, overfitting, regularisation. A model that fits your data
  perfectly has learned nothing.
- Correlation isn't causation — but randomisation, potential outcomes
  (Rubin), and causal graphs (Pearl) are how you get causation anyway.
- Multiplicity: p-hacking, garden of forking paths, publication bias, and the
  replication crisis they produced.

**What outsiders get wrong.**
- A p-value is not the probability that the hypothesis is false, nor the
  probability the result was due to chance. It is P(data this extreme | null
  true), and that is a much weaker thing.
- "Statistically significant" says nothing about whether an effect is large
  or important.
- More data fixes variance, never bias. The *Literary Digest* polled 2.4
  million people in 1936 and called the election wrong.

**T3 — Literacy (~200 hrs)**
- *Start here:* David Spiegelhalter, **The Art of Statistics**. The door
  because it teaches the reasoning through real cases and postpones formulas
  until you want them.
- *Survey:* Freedman, Pisani & Purves, **Statistics** — the great
  calculus-free text, still unmatched on what inference actually means. Then
  Blitzstein & Hwang, **Introduction to Probability** (free PDF), ch. 1–6, for
  the mechanics.
- *Canon:* R. A. Fisher, **The Design of Experiments**, ch. 2 — the lady
  tasting tea, the origin of the modern experiment, in fifteen pages. Then
  Tukey, **Exploratory Data Analysis** (browse; the spirit matters more than
  the stem-and-leaf plots) and Tufte, **The Visual Display of Quantitative
  Information**. Salsburg's **The Lady Tasting Tea** supplies the history.
- *Course:* Harvard **Stat 110** (Joe Blitzstein) — all lectures free on
  YouTube and edX, and the best probability course available anywhere at any
  price. Then Richard McElreath's **Statistical Rethinking** lectures (free,
  YouTube) for the Bayesian and causal side. Both, in that order.
- *Artifact:* Find a statistical claim in the news, get the underlying paper,
  reconstruct what was actually done, and write 2,000 words on what it does
  and does not support — sample, interval, assumptions, and how many
  comparisons were really made.

**T2 — Working depth**
- *Spine:* Casella & Berger, **Statistical Inference** (the standard first
  graduate year); Wasserman, **All of Statistics** as the fast parallel
  track; Gelman et al., **Bayesian Data Analysis** (free PDF); Gelman, Hill &
  Vehtari, **Regression and Other Stories**; Efron & Hastie, **Computer Age
  Statistical Inference** (free).
- *Practice:* Every exercise in Blitzstein ch. 1–10; Casella & Berger ch.
  1–10 — twelve months, honestly. Then compute: work the entire *Statistical
  Rethinking* problem set in Stan, PyMC, or brms, and fit, criticise and
  break at least twenty models on real messy data. Simulate everything —
  never trust a result you cannot also generate by simulation.
- *Primary literature:* *JASA*, *Annals of Statistics*, *JRSS Series B*, and
  *Statistical Science* (start here; it is written to be read). Read
  directly: Neyman & Pearson (1933); Efron, "Bootstrap Methods: Another Look
  at the Jackknife" (1979); Breiman, "Statistical Modeling: The Two Cultures"
  (2001); Ioannidis, "Why Most Published Research Findings Are False" (2005).
- *You've arrived when:* handed a raw dataset and a vague question, you can
  choose a model, state its assumptions, check them, report uncertainty
  honestly, and say clearly what the data cannot answer — and you can
  reproduce the analysis in any applied paper you read.

**T1 — Mastery**
- *Graduate texts/monographs:* Lehmann & Casella, **Theory of Point
  Estimation** and Lehmann & Romano, **Testing Statistical Hypotheses**; van
  der Vaart, **Asymptotic Statistics**; Durrett, **Probability: Theory and
  Examples** (free) or Billingsley, **Probability and Measure**, with
  Williams, **Probability with Martingales** as the humane entry to measure-
  theoretic probability; Hastie, Tibshirani & Friedman, **The Elements of
  Statistical Learning** (free); Imbens & Rubin, **Causal Inference**, and
  Pearl, **Causality**.
- *Frontier:* causal inference at scale; conformal prediction; high-
  dimensional and post-selection inference; the statistics of machine
  learning (benign overfitting, double descent); simulation-based inference.
  Follow Andrew Gelman's blog, arXiv stat.ME and math.ST, and Data Colada for
  the meta-science front.
- *Contribution looks like:* a new estimator or design with proved
  properties; methodology an applied field adopts; or an applied analysis
  decisive enough to settle a live question.
- *Community:* ASA (Joint Statistical Meetings), IMS, the Royal Statistical
  Society, ISBA for Bayesians; NeurIPS and AISTATS on the machine-learning
  boundary.

## Theoretical computer science & information theory

**The question it asks.** What can be computed at all, what can be computed
efficiently, and how much information is actually in a message? One half draws
the hard limits of mechanical procedure — Turing's undecidability, P versus
NP; the other measures information independently of meaning and derives exact
limits on compression and on transmission through noise. Both turn out to be
theories of resources: time, space, randomness, bits.

**Big ideas to walk away with.**
- Computation is substrate-independent. Turing machines, lambda calculus, and
  every other reasonable model define the same class (Church–Turing).
- Undecidability: the halting problem and Rice's theorem. Some questions have
  no algorithm, ever, at any speed.
- Complexity classes and reductions; P, NP, and NP-completeness (Cook–Levin,
  then Karp's 21 problems). P versus NP is the field's central open question.
- Diagonalisation is the one trick that keeps working: Cantor to Gödel to
  Turing to the time hierarchy theorem.
- Entropy is the true measure of information. Shannon's source coding theorem
  fixes the compression limit; his noisy-channel theorem says you can
  transmit essentially error-free right up to capacity, which nobody expected.
- Randomness as a computational resource — randomised algorithms, BPP, and
  the surprising evidence that randomness may be eliminable.
- Kolmogorov complexity: an object's information content is the length of its
  shortest description, and most strings are incompressible.
- Hardness as a building material: one-way functions, zero-knowledge proofs,
  the PCP theorem and hardness of approximation.

**What outsiders get wrong.**
- P versus NP is not about computers getting faster. It asks whether checking
  a solution is fundamentally easier than finding one.
- Shannon information is not meaning. A random string has maximum entropy and
  says nothing.
- Quantum computers do not "try all answers at once," and are not known to
  solve NP-complete problems efficiently.

**T3 — Literacy (~150 hrs)**
- *Start here:* Charles Petzold, **Code: The Hidden Language of Computer
  Hardware and Software**. It builds a working computer from flashlights and
  relays, so "computation" stops being a metaphor.
- *Survey:* Sipser, **Introduction to the Theory of Computation**, ch. 0–5
  and 7 — read ch. 3, 4 and 7 slowly and skip ch. 6 on a first pass.
  Alternatively Moore & Mertens, **The Nature of Computation**, ch. 1–6: much
  longer, far more delightful, the best expository book the field has.
- *Canon:* Turing, **On Computable Numbers** (1936), with Petzold's **The
  Annotated Turing** as the guide. Then Shannon, **A Mathematical Theory of
  Communication** (1948) — read it in full; it is one of the most readable
  landmark papers ever written, and you need only elementary probability.
- *Course:* MIT OCW **18.404J Theory of Computation** is Sipser teaching his
  own book on video — take it. For information theory, David MacKay's
  Cambridge lectures (free on YouTube) with his **Information Theory,
  Inference, and Learning Algorithms** (free PDF) are the equal of anything
  paid.
- *Artifact:* Prove the halting problem undecidable from scratch, explain
  what NP-completeness means and why 3-SAT is the hinge, then estimate the
  entropy of English text and say what that number means. 2,000 words.

**T2 — Working depth**
- *Spine:* Sipser, all of it; Arora & Barak, **Computational Complexity: A
  Modern Approach** (draft free online); Cover & Thomas, **Elements of
  Information Theory**; MacKay; and Kleinberg & Tardos, **Algorithm Design**
  or Cormen et al., **Introduction to Algorithms** for the constructive side.
- *Practice:* Every exercise in Sipser ch. 1–5 and 7 — all of them, without
  solutions. Arora & Barak ch. 1–9. Cover & Thomas ch. 2–5, 7–8. Prove
  fifteen to twenty problems NP-complete by reduction until reductions feel
  mechanical, because that fluency is the actual skill. Build four things: a
  Turing machine simulator, a DPLL/CDCL SAT solver, a Huffman plus arithmetic
  coder, and a Hamming or LDPC decoder you test against a simulated channel.
- *Primary literature:* in this field the conferences *are* the journals —
  STOC, FOCS, CCC, SODA; plus *SIAM Journal on Computing*, *Journal of the
  ACM*, and *IEEE Transactions on Information Theory*. Preprints at ECCC and
  arXiv cs.CC. Read directly: Shannon (1948); Cook, "The Complexity of
  Theorem-Proving Procedures" (1971); Karp, "Reducibility Among Combinatorial
  Problems" (1972); Goldwasser, Micali & Rackoff on zero-knowledge (1985).
- *You've arrived when:* given an unfamiliar computational problem, you can
  place it — polynomial-time algorithm, NP-hard by reduction, or undecidable
  — and defend the placement; and you can compute the capacity of a channel
  you have never seen before.

**T1 — Mastery**
- *Graduate texts/monographs:* Arora & Barak; Goldreich, **Computational
  Complexity: A Conceptual Perspective** and **Foundations of Cryptography**
  (2 vols.); Motwani & Raghavan, **Randomized Algorithms**; Vazirani,
  **Approximation Algorithms**; Csiszár & Körner, **Information Theory:
  Coding Theorems for Discrete Memoryless Systems**; Li & Vitányi, **An
  Introduction to Kolmogorov Complexity**; Nielsen & Chuang, **Quantum
  Computation and Quantum Information**.
- *Frontier:* hardness of approximation and the Unique Games Conjecture;
  geometric complexity theory; meta-complexity; quantum advantage, error
  correction, and results like MIP* = RE; lattice-based post-quantum
  cryptography. Follow ECCC, Scott Aaronson's *Shtetl-Optimized*, the
  Fortnow–Gasarch *Computational Complexity* blog, and the Simons Institute's
  free workshop videos.
- *Contribution looks like:* a better algorithm with a proved bound; a new
  lower bound (rare, and the most prized result in the field); a new
  reduction or hardness result; a code approaching capacity; a cryptographic
  primitive with a security proof.
- *Community:* ACM SIGACT and the IEEE Information Theory Society;
  STOC/FOCS/CCC/ITCS/SODA and ISIT; CRYPTO and EUROCRYPT; QIP for quantum.
  The Gödel Prize and Knuth Prize mark what the field itself values.
