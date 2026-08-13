# Catalogue

Every subject with a genuinely good free university course behind it,
organised by division and level. Roughly 400 courses.

**This is the menu.** `TRANSCRIPT.md` is the suggested order through it.
Strike out whatever you don't want — filtering down is the point.

## How to read an entry

- **Institution and instructor** are given. **Course codes appear only where
  they were verified**; where a code is missing, the course exists but the
  number wasn't confirmed. Search by title and instructor.
- **Hours are approximate** and estimate total work, not video runtime.
- Each division ends with **the spine** — the handful to actually do, in
  order — and **overlaps resolved**, naming the pick where several courses
  teach the same thing.

## Four things that decide whether something is a course

1. **Lecture video is not a course.** Without problem sets and feedback it's
   a documentary. Every entry says which it is.
2. **On MIT OCW, only `SC` and `RES` designated courses carry full free
   assessment.** The rest give materials without the loop.
3. **Open Yale is frozen at 2011.** Fine for philosophy and literature; a
   real problem for anything empirical.
4. **Audit access on Coursera and edX keeps narrowing.** Re-verify anything
   there before planning around it.

## What can't be got this way

Wet lab, cadaveric anatomy, clinical exposure, studio practice under
critique, and supervised fieldwork. Each division says so where it applies
and names the substitutes that exist — community bio labs, community college
lab courses, EMT-Basic, master naturalist programmes, local studio classes.

---

# Formal — Mathematics, Statistics, Computer Science

Everything here is free to access without payment. Where a course lives on
Coursera or edX, "audit" means you can watch every lecture and read every
handout without paying — you lose graded submissions and the certificate,
nothing else. Where a course lives on a university's own web server
(Berkeley, CMU, MIT PDOS, Stanford course pages), you get the whole thing
including assignments, and often the autograder too.

**Hours are approximate throughout.** They estimate total time to actually
do the course — lectures plus problem sets plus the staring-at-the-wall
that real mathematics requires — not video runtime. A 3:1 or 4:1 ratio of
work-to-video is normal and the estimates assume it. Treat them as
order-of-magnitude.

One distinction matters more than any other in this document, so it is
flagged in every Notes cell: **whether a course ships assignments.** A
lecture series with no problems is a documentary. It can be a superb
documentary, and several below are, but you will not learn mathematics or
programming by watching. The catalogue marks each entry as *full course*
(video + assignments + solutions), *materials only* (notes, psets, exams,
no video), *video + psets* (no solutions), or *video only*.

---

## Division I — Mathematics

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Precalculus / Algebra 2 / Trigonometry | Khan Academy | Sal Khan and staff | 60–100 | Not a university course and does not pretend to be. It is the right tool for exactly one job: closing specific gaps before calculus. Mastery-based exercise engine with hints; the videos are the weaker half. Do not "take" it linearly — take the unit tests, find the holes, patch those. |
| 18.01SC Single Variable Calculus | MIT OCW | David Jerison (lectures), Christine Breiner, David Jordan, Joel Lewis (recitations) | 120–150 | Full course. The "SC" (Scholar) editions are OCW's best product: every lecture paired with a recitation video that works a problem, plus psets *with solutions* and exams with solutions. Jerison is unhurried and geometric. If you do one calculus course, this. |
| 18.02SC Multivariable Calculus | MIT OCW | Denis Auroux (lectures), Breiner/Jordan/Lewis (recitations) | 120–150 | Full course, same Scholar format. Auroux is the better lecturer of the two — his treatment of the gradient, and the sequence on Green's and Stokes' theorems near the end, are the clearest exposition of vector calculus available free anywhere. Lectures 18–24 are worth watching even if you learned multivariable elsewhere. |
| 18.03SC Differential Equations | MIT OCW | Arthur Mattuck, Haynes Miller, Jeremy Orloff, John Lewis | 100–130 | Full course. Mattuck's lectures are the draw — he is a genuinely great classroom teacher and the course includes "Mathlets," small interactive applets that make the phase-plane material land. The Laplace transform and the linear-systems/phase-portrait sections are the strongest. |
| 18.06 Linear Algebra | MIT OCW | Gilbert Strang | 70–100 | Full course: 34 lectures, psets, exams, all with solutions. The most famous free math course in the world and it deserves it. Strang teaches column space and the four fundamental subspaces as the spine of the subject rather than as a late chapter. Lectures 1–11 (elimination through the four subspaces) are the part that reorganizes your head. |
| Essence of Linear Algebra | 3Blue1Brown | Grant Sanderson | 3–5 | Video only, zero exercises. Not a course — a visual prior. Watch the whole thing in one sitting *before* Strang, then never think about it again. The determinant-as-area-scaling and change-of-basis episodes do in eight minutes what a semester often fails to do. |
| Essence of Calculus | 3Blue1Brown | Grant Sanderson | 3–4 | Video only. Same role as above, relative to 18.01. The episode deriving the chain rule and the one on Taylor series are the two that matter. |
| 6.042J / 18.062J Mathematics for Computer Science | MIT OCW | Albert R. Meyer (Spring 2015); Tom Leighton and Marten van Dijk (Fall 2010) | 120–150 | Full course, both versions have video, psets, and solutions, plus an excellent free textbook. This is the discrete math *and* proof-writing course — induction, graphs, counting, and a serious probability unit at the end. Fall 2010 (Leighton) is the warmer lecturer; Spring 2015 (Meyer) is tighter and the notes are more polished. Either is fine; do not do both. |
| Introduction to Mathematical Thinking | Stanford (Coursera, audit) | Keith Devlin | 30–50 | Audit free. Narrow and unusual: it teaches you to read and write a mathematical proof and almost nothing else. Ten weeks on quantifiers, implication, and proof structure. Worth it if 6.042J's proofs feel like they arrive from nowhere. Skip if they don't. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 18.100A Real Analysis | MIT OCW | Casey Rodriguez | 130–160 | Full course with video, psets, exams. 18.100**A** is the gentler track — more emphasis on getting comfortable with epsilon-delta, less on abstraction. This is the right first analysis course for someone self-teaching. A newer 18.100B (Spring 2025, Tobias Colding) also has video and is the more abstract, metric-space-first track — take that one *second*, or instead if you're confident. |
| Math 131 Real Analysis I | Harvey Mudd College | Francis Su | 40–60 (video) | Video only from the college's side, but the course page hosts the syllabus and homework schedule keyed to Rudin. Su is the best explainer of analysis on the internet — his lecture on the construction of the reals and his repeated insistence on *why* a definition is shaped the way it is are the reason to watch. Use as a companion to 18.100A, not a replacement, because the graded scaffolding isn't there. |
| Math E-222 Abstract Algebra | Harvard Extension School | Benedict Gross | 60–90 | Video only (35 lectures), but it follows Artin's *Algebra* chapter by chapter, so pair it with the MIT 18.701 psets below and you have a real course. Gross is a working algebraist teaching with visible affection for the material. The lectures on symmetry groups and the orthogonal group are the standouts. |
| 18.701 Algebra I | MIT OCW | Michael Artin | 130–160 | Materials only — no video. Psets, a diagnostic, exams, keyed to Artin's own textbook. Artin's course is famously hard and famously good. Combine with Gross's E-222 videos above: Gross lectures the book, Artin sets the problems. That pairing is the single best free abstract algebra setup that exists. |
| 18.600 Probability and Random Variables | MIT OCW | Scott Sheffield | 100–130 | Full course: 38 video lectures, psets, exams, solutions. Calculus-based probability done by a probabilist. More mathematically serious than the engineering-flavored 6.041; the sections on the central limit theorem and on the exponential/Poisson relationship are excellent. |
| 18.781 Theory of Numbers | MIT OCW | — | 80–110 | Materials only, no video. Elementary number theory with no algebra prerequisite: primes, congruences, quadratic reciprocity, continued fractions, partitions. Good psets. Listed without an instructor name because I am not confident enough in the attribution to print one. |
| 18.901 Introduction to Topology | MIT OCW | — | 80–110 | Materials only. Point-set topology — metric spaces, compactness, connectedness, the standard machinery. It's the prerequisite that unlocks algebraic topology and much of analysis. Unglamorous, no video, but the assignments are the real thing. Instructor deliberately omitted for the same reason as above. |
| 18.065 Matrix Methods in Data Analysis, Signal Processing, and Machine Learning | MIT OCW | Gilbert Strang | 60–90 | Full course with video and assignments. This is Strang's *second* linear algebra course and it is the bridge from 18.06 to machine learning — SVD, low-rank approximation, least squares, the optimization chapters. The SVD lectures are the best free treatment of the SVD anywhere, and worth extracting even if you take nothing else. |
| 18.335J Introduction to Numerical Methods | MIT OCW | Steven G. Johnson | 80–120 | Materials only on OCW (notes, psets), but the live GitHub repo mitmath/18335 carries current notebooks. Numerical linear algebra done properly: conditioning, stability, floating point, QR/SVD, iterative methods. Assignments are in Julia. Assumes 18.06 cold. |
| 18.05 Introduction to Probability and Statistics | MIT OCW | Jeremy Orloff, Jonathan Bloom | 60–90 | Materials only — reading questions, class slides, studio problems, psets, all with solutions. No video. Listed here rather than in Statistics because it is the cleanest short bridge from calculus into both frequentist and Bayesian inference, and it is unusually well written for a no-video course. |
| Design and Analysis of Algorithms | NPTEL / Chennai Mathematical Institute | Madhavan Mukund | 40–60 | Video plus weekly assignments during a live run; archived runs keep the videos and slides. Mukund is exceptionally clear and the course is a legitimate alternative to MIT 6.006 for anyone who finds Demaine's pace punishing. Included in the math division because it doubles as a discrete-structures course. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 18.102 Introduction to Functional Analysis | MIT OCW | Casey Rodriguez (Spring 2021); Richard Melrose (Spring 2009) | 100–130 | Spring 2021 has video; Spring 2009 has Melrose's own lecture notes and psets *with solutions*. Take both halves: Melrose's notes are the better text, Rodriguez the better lecture. Banach and Hilbert spaces, Hahn-Banach, spectral theorem. Requires real analysis, non-negotiably. |
| 18.905 Algebraic Topology I | MIT OCW | Haynes Miller | 120–160 | Materials only — no video. What you get is a livetexed set of notes from Miller's course, and they are outstanding: singular homology, CW complexes, homological algebra, cohomology, Poincaré duality. A companion 18.906 (Algebraic Topology II) exists with its own notes. Graduate level; assumes 18.901 and 18.701. |
| 18.S097 Applied Category Theory | MIT OCW | Brendan Fong, David I. Spivak | 30–50 | Full course with video, problem sets, and a free textbook (*Seven Sketches in Compositionality*). This is the real answer to "is there a free category theory course" — an actual MIT course, not a lecture series. It approaches the subject through applications (databases, resource theories, signal flow graphs) rather than through algebraic topology, which makes it far more accessible than a standard treatment. Chapter 3, on databases as categories, is the one to take even if you abandon the rest. |
| Graduate algebra lecture series (Galois theory, commutative algebra, group theory, algebraic geometry, number theory) | UC Berkeley, via YouTube | Richard Borcherds | 20–40 each | Video only, no assignments. Borcherds is a Fields medalist recording graduate courses at his desk, and the result is unlike anything else free: dense, opinionated, occasionally showing his working. Use with a textbook that supplies problems. The Galois theory series is the best entry point. |
| Introduction to Logic | Stanford Online | Michael Genesereth | 30–50 | Full course, and unusually for logic it has *automated exercises* — the Fitch proof checker grades your natural-deduction proofs, which is exactly the feedback loop the subject needs. Propositional and relational logic, resolution, Herbrand. This is the mathematical-logic entry that actually functions as a course; most alternatives are books. |
| 18.404J / 6.840J Theory of Computation | MIT OCW | Michael Sipser | 100–130 | Full course: 26 video lectures, psets, exams. Listed in both divisions. Sipser teaching Sipser's own textbook, and the undecidability and reduction lectures are the clearest presentation of the material in existence. This is where the mathematics division and the CS division actually meet. |

### The spine — Mathematics

If you do only a handful, do these, in this order:

1. **MIT 18.01SC** — single variable calculus, Jerison. Everything downstream
   assumes it.
2. **MIT 18.06** — linear algebra, Strang. Watch 3Blue1Brown's *Essence of
   Linear Algebra* first as a five-hour prelude.
3. **MIT 6.042J** — mathematics for computer science. This is where you
   learn to write a proof, and it is a better proof course than most
   "intro to proofs" courses because the proofs are about things.
4. **MIT 18.02SC** — multivariable calculus, Auroux.
5. **MIT 18.100A** — real analysis, Rodriguez, with Francis Su's Harvey Mudd
   lectures playing alongside. This is the course that converts you from
   someone who computes into someone who proves.
6. **MIT 18.600** — probability, Sheffield. The gateway to the entire
   statistics division.

Differential equations (18.03SC) is the obvious omission. It is a fine
course; it is just less load-bearing than the six above unless you are
headed into physics or engineering.

### Overlaps resolved — Mathematics

**Linear algebra: Strang (18.06) over Khan Academy and over 3Blue1Brown.**
Khan loses because it teaches matrix manipulation as a set of procedures —
you finish able to row-reduce and unable to say what a subspace is.
3Blue1Brown loses as a *course* because it has no exercises at all; it is a
brilliant intuition pump and a useless assessment. Strang wins because his
lectures build the geometric intuition that his problem sets then test,
which is the combination neither competitor has. Use 3Blue1Brown as a
warm-up, not a substitute.

**Real analysis: MIT 18.100A over 18.100B, with Francis Su alongside.**
18.100B is the more abstract track and is better mathematics; it is worse
pedagogy for someone with no instructor to ask. 100A gets you to the same
place with fewer opportunities to silently lose the thread. Su loses as a
primary because Harvey Mudd only released video — no graded structure — but
he beats both MIT lecturers on explanation, so run him in parallel.

**Abstract algebra: Gross's E-222 videos plus Artin's 18.701 psets, over
either alone.** E-222 alone is video-only, so you would watch 35 lectures
and prove nothing. 18.701 alone is materials-only, so you'd face Artin's
problems with only Artin's book. They are the same textbook and they slot
together perfectly. This is the strongest argument in the whole catalogue
for combining two courses rather than picking one.

**Probability: 18.600 (Sheffield) over 6.041 (Tsitsiklis) over 18.05.**
Sheffield wins for a mathematics track because the treatment is
measure-theory-adjacent and the problems are harder. Tsitsiklis wins if you
want probability *for engineering and inference* — see the statistics
division, where I pick him. 18.05 loses to both on depth but wins on speed
and is the right choice if probability is a means, not an end.

**Calculus: MIT 18.01SC/18.02SC over Khan Academy.** Not close. Khan is
remedial support; MIT is a course. The one thing Khan does better is drill
volume, so use it if you need reps on integration technique.

**Discrete math: MIT 6.042J over NPTEL's discrete offerings.** 6.042J has
the better textbook (free, and genuinely excellent), the better problem
sets, and solutions. NPTEL's version is fine and has a live-cohort rhythm
some people need, but the materials are thinner.

---

## Division II — Statistics and Data Science

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Probability & Statistics — Open & Free | CMU Open Learning Initiative | OLI course team | 40–60 | Full course in the OLI sense: interactive, embedded formative exercises with immediate feedback, simulations, and a mastery model. No lectures at all — it is a textbook that argues with you. Four units, algebra prerequisite only. The best pure-beginner statistics resource free online, and better than most first-year lecture courses because the feedback is instant. |
| Statistical Reasoning — Open & Free | CMU OLI | OLI course team | 30–50 | Same platform, lighter probability. Choose this over the above only if you want inference fast and don't care about the probability machinery. Most people should take Probability & Statistics instead. |
| Causal and Statistical Reasoning | CMU OLI | Richard Scheines and colleagues | 20–30 | 16 modules, 60–90 minutes each, interactive. Not a statistics course — a course on how causal claims fail. Confounding, Simpson's paradox, experimental versus observational evidence, reading a study critically. Unusually valuable early, because it inoculates you before you learn any technique. |
| Data 8: Foundations of Data Science | UC Berkeley | Ani Adhikari, John DeNero, David Wagner | 60–90 | Full course, entirely public at data8.org: free textbook, Jupyter notebooks, labs, homework. Teaches inference through *simulation* — bootstrap and permutation tests before formulas — which is the single best pedagogical decision in introductory statistics this decade. Python, no calculus needed. |
| 18.05 Introduction to Probability and Statistics | MIT OCW | Jeremy Orloff, Jonathan Bloom | 60–90 | Materials only, no video, but everything has solutions. Notable for treating Bayesian and frequentist inference side by side from the start rather than teaching one and apologizing for the other later. The Bayesian updating sections are the best short introduction to the topic in the catalogue. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Stat 110: Probability | Harvard | Joe Blitzstein | 100–130 | Full course, and the delivery is unusual: 34 lecture videos on YouTube, plus strategic practice problems, psets, and *solutions* on the public course site, plus a free textbook. Blitzstein is the best probability lecturer alive on video. His treatment of conditioning ("conditioning is the soul of statistics") and the story-proof technique change how you approach every subsequent problem. Take this over every other probability course if you are headed to statistics rather than to pure math. |
| 6.041SC Probabilistic Systems Analysis and Applied Probability | MIT OCW | John Tsitsiklis | 100–130 | Full Scholar-format course: lectures, recitations, tutorials, psets, solutions. Tsitsiklis is rigorous and structured where Blitzstein is intuitive and playful. The Markov chain and Bayesian inference units are stronger here than in Stat 110. Genuinely a coin flip between the two; see Overlaps below. |
| 18.650 Statistics for Applications | MIT OCW | Philippe Rigollet | 80–110 | Full course with 24 video lectures and psets. This is *mathematical* statistics — maximum likelihood, the delta method, hypothesis testing derived rather than tabulated, method of moments, generalized linear models. The step up from "how to run a t-test" to "why the t-test is that shape." Requires 18.600-level probability. |
| Statistical Learning with R (and the Python edition) | Stanford Online | Trevor Hastie, Robert Tibshirani | 50–70 | Free, with the textbook (*An Introduction to Statistical Learning*) free as a PDF and labs in every chapter. Regression, classification, cross-validation, the bootstrap, regularization, trees, SVMs. The authors invented half of what they are teaching. The cross-validation and bootstrap lectures are the ones to steal — most people get resampling wrong for years and these fix it in ninety minutes. |
| Applied Regression / Design of Experiments (STAT 462, STAT 503 and the wider online catalogue) | Penn State | Penn State online stat faculty | 40–60 each | Fully open courseware at online.stat.psu.edu — complete lesson text, worked examples, datasets, and exercises, free without registration. Not glamorous, no video, and rarely recommended, which is a mistake: it is the most complete free treatment of regression diagnostics and classical experimental design (blocking, factorial designs, fractional factorials) anywhere. Use as a reference you work through, not a course you binge. |
| Improving Your Statistical Inferences | Eindhoven University of Technology (Coursera, audit) | Daniël Lakens | 30–40 | Audit free; assignments are downloadable R/jamovi worksheets so auditing loses very little. What p-values actually mean, why you cannot interpret a non-significant result as no effect, power, equivalence testing, optional stopping, preregistration. This is the replication-crisis course and it repairs damage that a conventional stats sequence causes. |
| HarvardX Data Science series (PH125.1x–PH125.9x) | Harvard (edX, audit) | Rafael Irizarry | 120–160 total | Nine courses: R basics, visualization, probability, inference, productivity tools, wrangling, linear regression, machine learning, capstone. Audit free; the free textbook (*Introduction to Data Science*) covers the same ground. Irizarry is a working biostatistician and the wrangling and visualization courses are the practical ones. The machine learning course is the weakest link — use Hastie/Tibshirani instead for that. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Statistical Rethinking | Max Planck Institute for Evolutionary Anthropology | Richard McElreath | 100–140 | Full course and completely free by design — lecture videos, slides, weekly homework *and solutions*, all in a public GitHub repo, refreshed most years. A Bayesian course that is really a course on scientific inference: causal DAGs first, then priors, then multilevel models. The lectures on multilevel models and on why you should draw your causal assumptions before touching data are the best in the catalogue on either topic. The textbook is paid; the course works without it, though it works better with it. |
| Introduction to Causal Inference | Independent (Brady Neal, Mila) | Brady Neal | 30–50 | Full lecture series with a free course book and homework, at bradyneal.com. Potential outcomes and graphical models taught together rather than as rival churches, which is rare. Covers identification, backdoor/frontdoor adjustment, instrumental variables, do-calculus. The clearest available bridge between Pearl's framework and the applied-econometrics framework. |
| Causal Diagrams: Draw Your Assumptions Before Your Conclusions | HarvardX (edX, audit) | Miguel Hernán | 15–25 | Audit free. Short, and narrower than Neal's course — it is about DAGs specifically: confounding, selection bias, measurement bias, all rendered as graph structures. Pairs with Hernán and Robins's *Causal Inference: What If*, which the authors give away as a PDF. Take this before Neal if graphs are new to you. |
| Bayesian Statistics (specialization) | Duke / UC Santa Cruz (Coursera, audit) | Duke and UCSC statistics faculty | 40–70 | Audit free. Conventional Bayesian sequence — conjugate priors, MCMC, Bayesian regression, model comparison. Listed for completeness and because some people want the standard treatment. It is competent and it is not McElreath. If you have done Statistical Rethinking you can skip this entirely. |
| 18.065 Matrix Methods in Data Analysis, Signal Processing, and Machine Learning | MIT OCW | Gilbert Strang | 60–90 | Cross-listed from Mathematics. The linear algebra underneath every regression, PCA, and neural network you will meet. Take it after regression rather than before, when you have something to attach it to. |

### The spine — Statistics

1. **CMU OLI Probability & Statistics** — or skip it if you already have
   calculus and a taste for rigor, and start at step 2.
2. **Harvard Stat 110** (Blitzstein) — probability, properly.
3. **Berkeley Data 8** — inference by simulation, in Python. Cheap in
   hours, disproportionate in payoff.
4. **MIT 18.650** (Rigollet) — mathematical statistics. This is the one
   that makes you able to read a methods section.
5. **Stanford Statistical Learning** (Hastie and Tibshirani) — regression
   and prediction from the people who built it.
6. **Statistical Rethinking** (McElreath) — Bayesian methods and causal
   thinking, which is where the field's centre of gravity actually is.

### Overlaps resolved — Statistics

**Probability: Blitzstein's Stat 110 over Tsitsiklis's 6.041, narrowly.**
Both are complete, both have solutions, both are excellent. Blitzstein wins
on teaching — he builds transferable *tactics* (conditioning, symmetry,
story proofs, indicator random variables) rather than a catalogue of
distributions, and those tactics keep paying out. Tsitsiklis wins on
structure and on Markov chains, and if you are engineering-minded he is the
better fit. Sheffield's 18.600 loses to both for a statistics track and
beats both for a pure mathematics track. Do not do two of these.

**Bayesian methods: McElreath's Statistical Rethinking over the Duke
Coursera specialization.** Duke teaches you Bayes' rule with priors
attached. McElreath teaches you why the model is the scientific claim, puts
causal diagrams before likelihoods, and gives you multilevel models — which
is the actual reason to be Bayesian. Duke loses because it is a competent
rendition of a standard syllabus and this subject has moved.

**Causal inference: Neal over Hernán's edX course, but take Hernán first.**
Neal's is the fuller course — more identification strategies, more
estimation, homework. Hernán's is 20 hours and is about DAGs alone. The
sequencing matters more than the ranking: Hernán makes graphs intuitive,
then Neal can build on them. McElreath's course also teaches causal
diagrams and does it well, so if you take Statistical Rethinking you can
compress this whole area to Neal alone.

**Machine learning as statistics: Hastie and Tibshirani over Irizarry's
PH125.8x.** Both cover the same territory. Hastie and Tibshirani wrote the
canonical text, teach the theory behind the methods, and give you labs in
R and Python. Irizarry's ML module is the thinnest part of an otherwise
strong series and treats the algorithms as a toolbox.

**Regression: Penn State's open courseware over any video course.** Nobody
recommends this and everybody should. Video regression courses spend their
time on the mechanics of fitting; Penn State's material spends it on
diagnostics, transformations, multicollinearity, and what to do when the
assumptions fail — which is the entire job.

---

## Division III — Computer Science

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| CS50x: Introduction to Computer Science | Harvard (edX / cs50.harvard.edu) | David J. Malan | 100–150 | Full course, free including the autograded problem sets — CS50 puts everything on its own site as well as edX. Starts in C, ends in Python and SQL, and the C weeks are the reason to take it: you learn pointers and manual memory before you learn a language that hides them. Famously theatrical; the production values are not the point, the problem sets are. Week 4 (memory) and Week 5 (data structures) are the load-bearing ones. |
| CS61A: Structure and Interpretation of Computer Programs | UC Berkeley | John DeNero | 120–160 | Full course, entirely public at cs61a.org: videos, autograded labs, homework, and the four large projects (Hog, Cats, Ants, Scheme). Descended from the legendary MIT 6.001. Teaches recursion, higher-order functions, and interpreters — you finish by writing a Scheme interpreter in Python, which is the moment programming stops being mysterious. Harder and deeper than CS50. |
| 6.0001 / 6.0002 Introduction to Computer Science and Programming in Python | MIT OCW | Eric Grimson, John Guttag, Ana Bell | 60–90 | Full course with video, psets, solutions. Shorter and drier than CS50 or CS61A. Its distinctive value is 6.0002, the second half — a genuinely good short introduction to computational modeling, simulation, and optimization that most intro sequences never reach. |
| Nand2Tetris (The Elements of Computing Systems) | Hebrew University of Jerusalem / nand2tetris.org | Noam Nisan, Shimon Schocken | 80–120 | Full course, free at nand2tetris.org, with all software tools and project specs; also on Coursera as two auditable courses. You build a computer from NAND gates up through an assembler, VM, compiler and OS. Nothing else in this catalogue collapses so many abstraction layers into one narrative. Part I (hardware) is the more revelatory half. |
| The Missing Semester of Your CS Education | MIT | Anish Athalye, Jon Gjengset, José Javier González Ortiz | 12–20 | Full course, short, free at missing.csail.mit.edu, with exercises. Shell, scripting, editors, version control internals, debugging, profiling. Covers the tooling every course assumes you already know and none of them teach. Do this in week one, not week fifty. The git internals lecture is the single most useful hour on this list. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| CS61B: Data Structures | UC Berkeley | Josh Hug | 130–170 | Full course. Public site with lectures, labs, and large projects; the Spring 2021 edition is the most recent one with a fully public autograder, so use that one specifically. Java. Hug's course is better than MIT 6.006 as a *first* data structures course because you implement everything — you build the hash table, you build the balanced tree — instead of analyzing it. The Project 2 (data structure implementation) and the disjoint-sets material are highlights. |
| 6.006 Introduction to Algorithms | MIT OCW | Erik Demaine, Jason Ku, Justin Solomon | 120–150 | Full course, Spring 2020: video lectures, recitations, psets, solutions. Algorithm design and analysis rather than implementation. Rigorous and fast. Take after CS61B, not instead of it. |
| 6.046J Design and Analysis of Algorithms | MIT OCW | Erik Demaine, Srini Devadas, Nancy Lynch | 120–150 | Full course, Spring 2015, with video, psets, and solutions. The second algorithms course: divide and conquer, randomization, amortized analysis, network flow, NP-completeness, approximation. Demaine's lectures on amortized analysis and on NP-hardness reductions are the ones to keep. |
| Algorithms, Part I and Part II | Princeton (Coursera, audit) | Robert Sedgewick, Kevin Wayne | 80–110 | Audit free. Java, with the best visualizations of any algorithms course and superb autograded assignments (the Percolation and Seam Carving assignments are famous for good reason). Weaker on proof and complexity theory than MIT; stronger on the practical performance characteristics of real data structures. |
| Algorithms Specialization | Stanford (Coursera, audit); also on YouTube | Tim Roughgarden | 60–90 | Audit free, and Roughgarden has posted the lecture videos publicly and written the accompanying *Algorithms Illuminated* books. The most articulate algorithms lecturer of the three options here. His treatment of the master method and of randomized selection is unusually clean. Thinner on assignments than Princeton's. |
| 15-213 Introduction to Computer Systems | Carnegie Mellon | Randal Bryant, David O'Hallaron | 130–170 | Full course in effect: lectures, slides, and — critically — the lab assignments (Data Lab, Bomb Lab, Attack Lab, Cache Lab, Malloc Lab, Shell Lab, Proxy Lab) are publicly available, with self-study versions. The best systems course in existence, free or paid. Bomb Lab and Malloc Lab alone will teach you more about how a machine works than a year of lectures. If you take one CS course from this catalogue, consider making it this one. |
| CS61C: Great Ideas in Computer Architecture | UC Berkeley | Berkeley EECS faculty (rotating) | 100–130 | Public course site with lectures, labs, and projects. C, RISC-V assembly, pipelining, caches, parallelism. Overlaps heavily with 15-213 — see Overlaps. Its RISC-V treatment is more modern than CMU's x86-64. |
| 6.004 Computation Structures | MIT OCW | Chris Terman and colleagues | 100–130 | Materials with video for several editions. Bottom-up digital design: transistors, combinational logic, processors, pipelining. Complements 15-213, which comes at the machine top-down from the C programmer's side. Take one direction or the other, not both, unless hardware is the goal. |
| 18.404J / 6.840J Theory of Computation | MIT OCW | Michael Sipser | 100–130 | Full course, Fall 2020: 26 videos, psets, exams. Automata, context-free languages, decidability, reducibility, complexity, NP-completeness. Sipser teaching his own textbook. The undecidability lectures are the best explanation of the halting problem and of diagonalization available anywhere, free or paid. |
| CS162: Operating Systems and Systems Programming | UC Berkeley | John Kubiatowicz | 120–160 | Public course site plus full lecture video on YouTube. Concurrency, scheduling, virtual memory, file systems, distributed systems primer. The projects (built on the Pintos-derived PintOS/ChocOS lineage) are demanding. Kubiatowicz is a strong, structured lecturer. |
| 6.1810 (formerly 6.828) Operating System Engineering | MIT PDOS | Frans Kaashoek, Robert Morris and colleagues | 120–160 | Full course, entirely public at pdos.csail.mit.edu, including the labs and the xv6 source and the free xv6 book. You implement system calls, page tables, a copy-on-write fork, a thread scheduler, and a file system in a real (tiny) Unix kernel. Harder than CS162 and more rewarding. The page-table lab is where virtual memory finally becomes concrete. |
| CS144: Introduction to Computer Networking | Stanford | Nick McKeown, Philip Levis | 100–140 | Course materials and the lab sequence are public. The labs are the entire reason to take it: you implement a working TCP in C++, layer by layer, ending with a stack that talks to the real internet. No other free networking course makes you build the thing. Lecture video availability has moved around over the years; the labs have stayed public. |
| CS186: Introduction to Database Systems | UC Berkeley | Berkeley EECS faculty | 90–120 | Public course site (cs186berkeley.net) with lectures, notes, and the multi-part Java projects — B+ trees, joins, query optimization, concurrency. The implementation projects distinguish it from lecture-only database courses. |
| 15-445/645 Intro to Database Systems | Carnegie Mellon | Andy Pavlo | 100–140 | Full course and deliberately open: all lectures on YouTube, slides and notes on the course site, homework and the BusTub project code on GitHub. Pavlo is the most entertaining lecturer in systems and the course is genuinely current — it teaches how modern storage engines are actually built. Take this for depth, CS186 for a gentler ramp. |
| Programming Languages, Parts A/B/C | University of Washington (Coursera, audit) | Dan Grossman | 60–90 | Audit free. ML, Racket, and Ruby, chosen to isolate static-versus-dynamic typing and functional-versus-object-oriented decomposition as *ideas* rather than as tribal affiliations. The section contrasting functional decomposition with OO decomposition — the "expression problem" material in Part B — is worth the whole course. |
| Compilers | Stanford Online | Alex Aiken | 80–120 | Free. Lexing, parsing, semantic analysis, code generation, optimization, with an optional but substantial compiler-construction project for the COOL language. The standard free compilers course and still the best-organized one for a first pass. |
| CS188: Introduction to Artificial Intelligence | UC Berkeley | Dan Klein, Pieter Abbeel (classic video set); rotating faculty for current editions | 100–140 | Full course: the Pacman projects are public and autograded, and the classic Klein/Abbeel lecture set remains freely available. Search, adversarial search, CSPs, MDPs, reinforcement learning, Bayes nets. The Pacman assignments are the best-designed programming projects in AI education. The MDP and reinforcement learning lectures stand alone. |
| CS229: Machine Learning | Stanford | Andrew Ng (2018 video set), Anand Avati and others | 100–140 | Lecture video plus the course's celebrated lecture notes and problem sets, all public. This is the *real* CS229, not the softened Coursera version — it derives things, and it assumes linear algebra, multivariable calculus, and probability. The notes on generalized linear models and on the bias-variance decomposition are reference material you will return to. |
| Practical Deep Learning for Coders | fast.ai | Jeremy Howard | 60–90 | Full course, free, with notebooks and a free book. Top-down: you fine-tune a working image classifier in lesson one and learn the underlying mathematics later. Divisive by design. It is the fastest route to doing something real and a poor route to understanding backpropagation. Pair with Karpathy, below. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 6.5840 (formerly 6.824) Distributed Systems | MIT PDOS | Robert Morris and colleagues | 120–160 | Full course, entirely public: lecture videos, the paper reading list, and the four Go labs (MapReduce, Raft, a fault-tolerant key-value store, a sharded store). Implementing Raft from the paper is the single hardest and most valuable assignment in this catalogue. The lecture on the Raft paper, and the one on consistency models, are excellent even standalone. Requires real systems programming fluency first. |
| 6.851 Advanced Data Structures | MIT OCW | Erik Demaine | 60–90 | Video plus psets. Persistence, retroactivity, geometric structures, succinct structures, cache-oblivious algorithms. Beautiful, specialized, and genuinely graduate level. The cache-oblivious lectures are the ones with the widest practical relevance. |
| CS 6120: Advanced Compilers (self-guided edition) | Cornell | Adrian Sampson | 60–100 | Full course, explicitly built for self-study: a linear timeline of lessons with videos, written notes, papers, and implementation tasks in a purpose-built IR (Bril) and in LLVM. Data flow, SSA, loop optimization, JIT, garbage collection, and a lot of paper reading. The best free graduate compilers course, and the self-guided framing is not an afterthought — it is designed for you. |
| CS231n: Deep Learning for Computer Vision | Stanford | Fei-Fei Li, Justin Johnson, Serena Yeung and successors | 80–120 | The 2017 lecture videos, the course notes at cs231n.github.io, and the assignments are public. The notes are better than the lectures and are among the best technical writing in machine learning. The assignment where you implement backpropagation for a multi-layer network by hand, in NumPy, is the one that matters. Later editions are more current on architectures; the fundamentals sections have aged well. |
| EECS 498-007 / 598-005: Deep Learning for Computer Vision | University of Michigan | Justin Johnson | 80–120 | Public lecture videos and assignments. Effectively the successor to CS231n taught by one of its architects, and more current. If you can only do one of the two, this is the more modern course; CS231n has the better written notes. |
| CS224n: Natural Language Processing with Deep Learning | Stanford | Christopher Manning | 80–120 | Lecture videos and assignments public. The pre-transformer half is now historical, and that is fine — the word vector and attention lectures explain *why* the architecture arrived, which reading a transformer tutorial will not give you. Assignments involve real implementation in PyTorch. |
| Neural Networks: Zero to Hero | Independent (Andrej Karpathy) | Andrej Karpathy | 25–40 | Video with accompanying notebooks and exercises; not a university course, and included anyway because nothing free matches it. Karpathy builds backpropagation from scratch, then a language model, then a GPT, live, in Python, explaining every line. The "micrograd" lecture is the clearest explanation of automatic differentiation that exists. Take it after fast.ai or after CS229. |
| Deep Learning (DS-GA 1008) | New York University | Yann LeCun, Alfredo Canziani | 80–110 | Public lecture videos, notes, and practica in PyTorch. LeCun lectures the theory and history; Canziani runs the code sessions. More theoretically grounded than fast.ai, more accessible than a pure research course. The energy-based models material is unavailable elsewhere in this form. |
| Introduction to Machine Learning | NPTEL / IIT Madras | Balaraman Ravindran | 40–60 | Video plus weekly assignments; archived runs retain videos and slides. A mathematically motivated survey — a legitimate free alternative to CS229 for someone who wants the derivations delivered more slowly. |
| Deep Learning | NPTEL / IIT Madras | Mitesh Khapra | 40–60 | Video plus assignments. Notably careful on the historical progression — perceptrons through backpropagation through modern architectures — with the mathematics written out fully rather than gestured at. Good complement to a top-down course like fast.ai. |
| 15-462/662 Computer Graphics | Carnegie Mellon | Keenan Crane | 80–120 | Full course: lecture videos on YouTube, course website with exams and exercises, and the coding assignments (the Scotty3D renderer/mesh-editor sequence) on GitHub. Crane is a geometry processing researcher and the course reflects it — the lectures on geometric representations and on the rendering equation are exceptional. The best free graphics course. |
| 6.837 Computer Graphics | MIT OCW | Wojciech Matusik and colleagues | 80–110 | Materials with assignments. Older and more traditional than CMU's. Take it only if you want a second pass or if CMU's C++ assignments defeat you. |
| Understanding Cryptography | Ruhr University Bochum | Christof Paar | 40–60 | Video only, but 20+ full lectures accompanying a textbook with problems. Paar teaches cryptography as engineering — block ciphers, AES internals, RSA, Diffie-Hellman, elliptic curves — with unusual clarity about implementation and attack. The AES lectures are the best free explanation of that cipher. |
| Cryptography I | Stanford (Coursera, audit) | Dan Boneh | 40–60 | Audit free, with programming exercises. Boneh is rigorous where Paar is practical: semantic security, provable security reductions, authenticated encryption, key exchange. Boneh's own Stanford CS255 course page carries additional notes and assignments. Take Paar first if you want intuition, Boneh first if you want proofs. |
| 6.858 Computer Systems Security | MIT OCW | Nickolai Zeldovich, James Mickens | 80–110 | Video lectures plus labs and a paper reading list. Systems security rather than cryptography: buffer overflows, privilege separation, web security, sandboxing, side channels. Mickens's guest lectures are notoriously funny and also substantive. Requires 15-213-level systems knowledge. |
| 6.031 Software Construction | MIT | Max Goldman, Rob Miller | 60–90 | Public course site with readings, exercises, and problem sets. Specifications, invariants, abstraction functions, testing, immutability, concurrency safety. The most rigorous free treatment of *software design* as opposed to programming. Most self-taught programmers never encounter this material and it shows in their code. |
| CS50's Introduction to Artificial Intelligence with Python | Harvard (edX / cs50.harvard.edu) | Brian Yu | 40–60 | Full course with autograded projects. Much lighter than CS188 — search, knowledge representation, a little probability, a little ML — but the projects are well built and it is a reasonable ramp if CS188's mathematics is premature. |

### The spine — Computer Science

1. **CS50x** or **Berkeley CS61A** — pick one, not both. CS50 if you want
   breadth and momentum; CS61A if you want depth and can tolerate a
   steeper start.
2. **Berkeley CS61B** (Hug) — data structures, implemented rather than
   admired.
3. **CMU 15-213** (Bryant and O'Hallaron) — computer systems. This is the
   course that separates people who can program from people who know what
   the machine is doing.
4. **MIT 6.006** — algorithms, analyzed.
5. **MIT 6.1810** — operating system engineering. Or **CS144** if you'd
   rather build a network stack than a kernel; both are the same kind of
   experience.
6. **MIT 18.404J** (Sipser) — theory of computation, for the part of the
   field that isn't engineering.

Then specialize: CS188 and CS229 for AI, CMU 15-445 for databases, CMU
15-462 for graphics, MIT 6.5840 for distributed systems.

### Overlaps resolved — Computer Science

**Intro programming: CS61A over CS50x for a mathematics-and-CS degree
plan.** CS50 is the better-produced course and the better on-ramp for
someone unsure they like programming; it wins on motivation. CS61A wins on
what you can do afterward — building a Scheme interpreter forces you to
understand evaluation, environments, and recursion at a level CS50 never
asks for. If you are committed to the degree, start at CS61A and use CS50's
C weeks as a supplement for pointers and memory. MIT 6.0001 loses to both:
it is competent and it is nobody's favorite.

**Systems: CMU 15-213 over Berkeley CS61C.** They cover largely the same
ground. 15-213 wins on the labs, and it is not close — Bomb Lab, Attack
Lab, Cache Lab and Malloc Lab are the best-designed assignments in
undergraduate computer science, and CMU has kept the self-study versions
public for two decades. CS61C's advantage is RISC-V instead of x86-64,
which is cleaner to learn; take CS61C if the assembly is the point, take
15-213 if the systems understanding is. MIT 6.004 approaches from the
hardware side instead and is a genuine alternative only if you want to
build a processor.

**Algorithms: CS61B then 6.006, over Princeton or Roughgarden alone.**
Berkeley's CS61B makes you implement; MIT's 6.006 makes you prove bounds.
That sequence beats any single course. Princeton (Sedgewick) loses as the
core because it under-teaches complexity theory and NP-completeness —
though its assignments are superb and worth raiding. Roughgarden loses on
assignment quality despite having the best lectures of the four; use his
videos as a second explanation whenever 6.006 loses you.

**Operating systems: MIT 6.1810 over Berkeley CS162.** CS162 is the more
complete *survey* and Kubiatowicz lectures well. 6.1810 wins because xv6 is
small enough to read entirely and real enough that implementing copy-on-write
fork or a page-table walk is the actual thing, not a simulation. Take CS162's
lectures alongside 6.1810's labs if you want both.

**Databases: CMU 15-445 (Pavlo) over Berkeley CS186.** Both have
implementation projects. Pavlo wins because the course tracks how modern
systems are really built — storage engines, MVCC, modern query execution —
and because CMU has made a deliberate policy of open-sourcing the entire
apparatus. CS186 is the gentler entry and its B+ tree project is excellent;
take it first if 15-445 assumes too much.

**Machine learning: Stanford CS229 over Andrew Ng's Coursera "Machine
Learning."** The Coursera course is the most-taken course in the world and
it is a simplification — it avoids the derivations, and people finish it
able to call a library and unable to say why regularization works. CS229 is
the same instructor teaching the real version. fast.ai loses as a *first*
theoretical course and wins outright as a first *practical* one; they are
answering different questions and taking both, in either order, is
reasonable.

**Deep learning: Karpathy's Zero to Hero plus Michigan EECS 498, over
CS231n alone.** CS231n's written notes remain the best of any of them and
should be read regardless. But Johnson's Michigan course is CS231n brought
up to date by one of its own creators, and Karpathy's series does the one
thing no lecture course does — builds the whole apparatus from nothing,
live, with no library between you and the gradient.

**Cryptography: Paar and Boneh are not substitutes.** Paar teaches you what
the algorithms do and how they break in practice; Boneh teaches you what
"secure" means formally and how to prove it. Most people need Paar. Anyone
going near security research needs Boneh. Neither replaces MIT 6.858, which
is about systems security and shares almost no content with either.

**Compilers: Aiken's Stanford course first, Cornell CS 6120 second.**
Aiken's is the classic full-stack build-a-compiler course and is the right
first pass. Sampson's CS 6120 assumes you have already built one and moves
to optimization, SSA, and research papers — and its self-guided edition is
better structured for solo work than almost anything else in this
catalogue.

---

## Notes on what is missing and why

**Open Yale Courses** is listed among the intended sources but contributes
nothing to these three divisions. Its catalogue is strong in physics,
economics, and the humanities — Shankar's *Fundamentals of Physics* and
Polak's *Game Theory* (ECON 159) are both excellent and both free with full
problem sets — but Yale released no mathematics, statistics, or computer
science course. Polak's game theory course is worth knowing about if
decision theory ever becomes relevant.

**Coursera and edX auditing** works for every course marked "audit" above,
but the terms shift. When a course's assignments are the point (Princeton
Algorithms, Nand2Tetris, Dan Boneh's programming exercises), check whether
they are still reachable before committing — several courses have moved
graded work behind the paywall over the last few years while leaving
lectures open, and a few have moved the other way.

**Graduate mathematics is thin and this is not fixable.** The catalogue
gives you real analysis, algebra, topology, functional analysis, and
category theory, but past that the free material becomes lecture notes
without problems, or lecture series without notes. Borcherds's YouTube
channel is the best partial answer. Beyond it you are into textbooks, and
textbooks are a different document.

---

# Physical Sciences

Every course below is free to access without payment. Hour estimates are
rough throughout — treat them as "how big is this" signals, not schedules.
A 12-week university course with problem sets realistically costs 100–150
hours if you actually do the problems; the numbers here assume you do.

Two distinctions matter more than anything else in this catalogue:

**Full course versus lecture videos.** MIT OpenCourseWare usually gives you
the syllabus, lecture notes, problem sets, *and solutions*. That last item
is what makes self-study possible. Open Yale gives you polished video plus
transcripts, and problem sets for some courses but not all. Susskind's
Theoretical Minimum gives you video and nothing else. YouTube lecture
archives give you video and nothing else. A course with solutions is worth
roughly three courses without them.

**Watching versus doing.** You cannot learn physics or chemistry by
watching. The single most common failure mode in self-directed physical
science study is completing thirty hours of video and retaining nothing,
because no problem was ever attempted under the discomfort of not knowing
the answer. Choose fewer courses and do the psets.

---

## 1. Physics

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 8.01SC Classical Mechanics (Fall 2016) | MIT OCW | Peter Dourmashkin, Deepto Chakrabarty | 150 | The "SC" means Scholar — built deliberately for independent learners. Roughly 220 short instructional videos rather than 50-minute lectures, plus problem sets with solutions and concept questions. Pedagogically the most complete free mechanics course in existence. Less charismatic than Lewin, far more usable. |
| PHYS 200 Fundamentals of Physics I | Open Yale | Ramamurti Shankar | 60 | Newtonian mechanics, special relativity, thermodynamics, waves, in 24 lectures. Shankar is a genuinely great explainer and moves at pace — he covers special relativity properly in an intro course, which almost nobody does. Problem sets and exams with solutions are posted. Weaker on rotational dynamics than 8.01SC. |
| 8.02 Physics II: Electricity and Magnetism (Spring 2019) | MIT OCW | Robert Redwine, Peter Dourmashkin, Michelle Tomasik, Krishna Rajagopal, Analia Barrantes | 150 | Full materials: lecture videos, psets, solutions, exams. The modern replacement for Lewin's 8.02. Uses the TEAL studio-physics approach with heavy visualization of fields. |
| PHYS 201 Fundamentals of Physics II | Open Yale | Ramamurti Shankar | 60 | E&M, optics, and a surprisingly good four-lecture run at quantum mechanics at the end. The Lecture 18–21 quantum sequence is worth watching on its own even if you take E&M elsewhere — it is the clearest "why does any of this follow" account at intro level. |
| 8.03SC Physics III: Vibrations and Waves (Fall 2016) | MIT OCW | Yen-Jie Lee | 120 | Full course with psets and solutions. Waves and optics are the most under-taught topic in self-study curricula and the most load-bearing later — Fourier analysis, normal modes, and dispersion all show up again in quantum mechanics. Do not skip this. Lee's demonstrations are excellent. |
| RES.8-005 Vibrations and Waves Problem Solving (Fall 2012) | MIT OCW | — | 15 | Not a course — a supplement of worked problem videos. Pair it with 8.03SC when you get stuck. |
| The Feynman Lectures on Physics, Vols. I–III | Caltech | Richard Feynman | 100+ | Free and complete in HTML at feynmanlectures.caltech.edu, beautifully typeset with working equations. Read it, do not study from it. It is the best physics prose ever written and a terrible first course — no problems worth the name, no scaffolding, and it famously lost its original undergraduate audience. Vol. I chs. 1–7, the two chapters on the principle of least action (Vol. II ch. 19) and the rotating-disk/entropy material are worth reading at any stage of your education. |
| Walter Lewin's 8.01 / 8.02 / 8.03 lectures | MIT (formerly) | Walter Lewin | 100 | Handle honestly: MIT removed these from OCW and edX in December 2014 after finding Lewin had sexually harassed an online learner, and stripped his emeritus title. They were not withdrawn for quality. They remain findable — Internet Archive holds full copies, and mirrored YouTube channels carry 8.01, 8.02 and 8.03. What you get is video only; the psets and solutions went with the takedown. The demonstrations (the pendulum-and-his-own-neck, the capacitor discharge, the rainbow lecture in 8.03) are unmatched. Reasonable people decline to use them. If you do use them, use 8.01SC's problem sets alongside, because Lewin alone will teach you nothing you can be tested on. |
| Quantum Mechanics and Application | NPTEL / IIT Delhi | Ajoy Ghatak | 60 | Video-only, but Ghatak is a careful, unhurried lecturer and this is a legitimate alternate route into QM for someone whose calculus is shaky. NPTEL courses generally offer assignments only during live runs; archived versions are video plus notes. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 8.033 Relativity | MIT OCW | — | 100 | Materials-only: notes, psets, solutions, no video. Proper special relativity with four-vectors, plus a real introduction to the tensor machinery. This is the standard bridge between intro physics and 8.962. |
| Special Relativity and Classical Field Theory | Stanford (Theoretical Minimum) | Leonard Susskind | 25 | Video only, no assignments, no solutions. Susskind gets to Lagrangian field theory and the field-theoretic derivation of Maxwell in ten lectures, which no undergraduate course does. Take this *after* 8.033, not instead of it — it will make you feel you understand relativity while leaving you unable to compute anything. |
| 8.223 Classical Mechanics II | MIT OCW | — | 60 | Lagrangian and Hamiltonian mechanics, canonical transformations, Poisson brackets. A short IAP-length subject. Materials only. |
| Classical Mechanics (Theoretical Minimum) | Stanford | Leonard Susskind | 25 | Video only. The best free *motivation* for why anyone would replace F=ma with an action principle. Susskind's treatment of symmetry and conservation laws (Noether) is the standout — worth watching even if you learn the mechanics itself from 8.223. |
| 8.044 Statistical Physics I | MIT OCW | — | 120 | Undergraduate thermo and stat mech with full psets and solutions. Materials only, no video. This is the course most self-learners skip and most regret skipping — thermodynamics is where physical intuition is built, and it is a prerequisite in spirit for chemistry, condensed matter, and astrophysics alike. |
| 8.04 Quantum Physics I (Spring 2013) | MIT OCW | Barton Zwiebach | 150 | Complete video lecture set plus notes, psets, solutions and exams. Wave mechanics done properly: the experimental basis, Schrödinger in 1D, then 3D. Zwiebach is unusually careful about *what is being assumed* at each step. This is the best free first course in quantum mechanics, full stop. |
| 8.05 Quantum Physics II (Fall 2013) | MIT OCW | Barton Zwiebach | 150 | The formalism course — state spaces, operators, angular momentum, spin, addition of angular momentum. These lectures and notes became Zwiebach's *Mastering Quantum Mechanics* textbook. Full materials. |
| 8.05x Mastering Quantum Mechanics | MITx Online | Barton Zwiebach | 150 | The same content as 8.05, delivered as an interactive MITx course with auto-graded problems. Nearly everything except the proctored exams is free. If you want *feedback* rather than a solutions PDF you can peek at, take this version instead of the OCW one. |
| 18.S191 Introduction to Computational Thinking (Fall 2020) | MIT OCW | Alan Edelman, Grant Sanderson, David P. Sanders | 60 | Julia-based, with live Pluto notebooks at computationalthinking.mit.edu. Covers image processing, particle dynamics, ray tracing, epidemic modelling and a genuine climate-model unit. Not a traditional computational-physics course, but the only free one with this production quality, and Sanderson's visual explanations are the reason to take it. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 8.06 Quantum Physics III / 8.06x Applications of Quantum Mechanics | MIT OCW / MITx Online | Barton Zwiebach | 150 | Perturbation theory, variational method, WKB, scattering, identical particles. Completes the undergraduate quantum sequence. The MITx version has graded problems. |
| 8.333 Statistical Mechanics I: Statistical Mechanics of Particles (Fall 2013) | MIT OCW | Mehran Kardar | 150 | 26 video lectures plus psets and solutions. Kardar is the strongest lecturer on this list after Zwiebach. The kinetic-theory sequence — the derivation of the Boltzmann equation and the H-theorem, roughly lectures 8–11 — is the clearest treatment available anywhere free, and worth taking alone. |
| 8.334 Statistical Mechanics II: Statistical Physics of Fields (Spring 2014) | MIT OCW | Mehran Kardar | 150 | Critical phenomena, scaling, the renormalization group. Video plus full materials. Graduate level and genuinely hard. The RG lectures are the single best free introduction to the idea that reshaped twentieth-century physics. |
| 8.962 General Relativity (Spring 2020) | MIT OCW | Scott Hughes | 150 | 23 video lectures, notes, psets. Hughes teaches GR as a working physicist rather than a differential geometer — the gravitational-radiation lectures (16 and 17) reflect his own LIGO-adjacent expertise and are outstanding. Requires 8.033-level comfort with tensors. |
| General Relativity (Theoretical Minimum) | Stanford | Leonard Susskind | 25 | Video only. Much gentler entry than 8.962 and gets you to the Schwarzschild solution and black-hole horizons. Good preparation, insufficient as a course. |
| 8.701 Introduction to Nuclear and Particle Physics (Fall 2020) | MIT OCW | Markus Klute | 100 | About 67 short videos organized by chapter, plus notes and problems. Unusually good on the *experimental* side — accelerators, detectors, how the Standard Model was actually established rather than merely stated. The neutrino-physics chapter is the best free treatment of that subject. |
| Particle Physics 1–3 (Standard Model, Supersymmetry, String Theory) | Stanford (Theoretical Minimum) | Leonard Susskind | 60 | Video only. Idiosyncratic and personal — Susskind explaining what he thinks matters. Not a substitute for 8.701, but the Standard Model quarter is a good conceptual overlay on top of it. |
| 8.231 Physics of Solids I (Fall 2006) | MIT OCW | Xiao-Gang Wen | 100 | Materials only — no video. Notes, readings, psets. Wen's perspective is more theoretical than the standard Ashcroft-and-Mermin route. |
| The Oxford Solid State Basics | University of Oxford Podcasts | Steven H. Simon | 40 | 21 recorded lectures from 2014, tracking Simon's textbook of the same name chapter by chapter. Video only, but Simon's book is the best modern undergraduate solid-state text and problem sets from it circulate widely. Take this over 8.231 for a first pass — Simon builds physical pictures where Wen builds formalism. |
| 8.323 Relativistic Quantum Field Theory I (Spring 2023) | MIT OCW | — | 150 | Materials only — readings, problem sets, no video. Canonical quantization, scalar and spinor fields. Rigorous and current. |
| Quantum Field Theory (Part III lectures) | University of Cambridge | David Tong | 60 | Video lectures plus what are probably the most-read free lecture notes in physics, at damtp.cam.ac.uk/user/tong. Tong also has excellent free notes and videos on the Quantum Hall Effect, statistical field theory, string theory and general relativity. His notes are better than most textbooks you would pay for. Videos are lecture-only; the notes contain exercises. |
| Physics 253: Quantum Field Theory (1975–76) | Harvard | Sidney Coleman | 60 | Black-and-white video recordings, free from the Harvard physics department and on YouTube, with typeset notes on arXiv (1110.5013). Fifty years old and still the reference performance — Coleman's lectures on renormalization and on symmetry breaking are why physicists still talk about him. Video and notes only. Take Tong first for the modern framing, then Coleman for depth. |
| Lectures on the Geometric Anatomy of Theoretical Physics | FAU Erlangen–Nürnberg | Frederic Schuller | 60 | Video only, on YouTube, with community-typeset notes. Builds the mathematical language — topology, manifolds, bundles, connections — from logic and set theory upward. Uncompromising and slow. If you have hit a wall where GR or gauge theory feels like symbol-pushing, this is the fix. Not a physics course; a prerequisites course. |

### The spine — Physics

1. **8.01SC Classical Mechanics** (MIT) — do the problem sets.
2. **8.02 Physics II: E&M** (MIT, Spring 2019) — or PHYS 201 if you want
   Shankar's pace; take the psets from MIT either way.
3. **8.03SC Vibrations and Waves** (MIT) — the underrated hinge of the
   whole curriculum.
4. **8.044 Statistical Physics I** (MIT) — no video, do it anyway.
5. **8.04 Quantum Physics I** (MIT, Zwiebach) — then 8.05 if you continue.
6. **8.333 Statistical Mechanics I** (MIT, Kardar) — the first genuinely
   graduate-level thing you should attempt.

Everything past that is specialization. GR (8.962), QFT (Tong then
Coleman), and solid state (Simon) are three separate doors; pick one.

### Overlaps resolved — Physics

**Intro mechanics: 8.01SC vs. PHYS 200 vs. Lewin.** Pick 8.01SC. It was
designed for people exactly in your position and it has graded-quality
problem sets with solutions. Shankar's PHYS 200 loses on assessment
support and on rotational mechanics, though it wins on relativity and on
sheer watchability — a reasonable move is 8.01SC as the spine with
Shankar's lectures 12–14 (relativity) bolted on. Lewin loses because the
supporting materials no longer exist alongside the videos, quite apart
from the ethical question.

**Intro E&M: 8.02 (2019) vs. PHYS 201 vs. Lewin's 8.02.** 8.02 Spring 2019
wins on completeness. Lewin's E&M lectures are the most beloved videos in
the genre and the demonstrations really are better; treat them as an
optional supplement rather than a course.

**Quantum: 8.04/8.05 vs. Susskind's Quantum Mechanics vs. NPTEL.**
Zwiebach wins decisively — it is the only option with videos, notes,
problems, and solutions all present, and his exposition is more careful
than anyone else's on this list. Susskind's QM course is a good *preview*
and useless as a course. Ghatak's NPTEL course is a fallback if Zwiebach's
mathematical level is too steep on first contact.

**Stat mech: 8.044 vs. 8.333 vs. Susskind's Statistical Mechanics.**
These are three different levels, not competitors — 8.044 is
undergraduate, 8.333 is graduate, Susskind is conceptual overview. Do
8.044 then 8.333. Skip Susskind's unless you want the narrative first.

**GR: 8.962 vs. Susskind vs. Tong's notes.** 8.962 is the actual course.
Susskind is the on-ramp. Tong's GR notes are the best free written
reference and pair well with Hughes's videos.

**QFT: 8.323 vs. Tong vs. Coleman.** Tong wins as your primary, because
notes plus video plus exercises beat any one of the three alone. 8.323
loses only because it has no video. Coleman is not a first course; it is
the thing you watch after you already know QFT and want to understand it.

**Solid state: 8.231 vs. Simon (Oxford).** Simon wins for a first course —
better pedagogy, better accompanying book, video available. 8.231 wins if
you want problem sets with an MIT-graduate flavor and Wen's more abstract
angle.

---

## 2. Chemistry

**Read this before the tables.** Chemistry is the least self-teachable
subject in this catalogue, and the reason is the laboratory. Roughly a
third of an accredited chemistry degree is bench work, and none of it can
be replicated at home: you cannot run a column, take an NMR, titrate to a
real endpoint, or develop the hand skills that separate a chemist from
someone who has read about chemistry. Any credential-seeking path will
eventually require in-person lab, typically at a community college.

What *can* be learned fully from free materials: general chemistry
principles, all of organic reaction theory and mechanism, physical
chemistry, inorganic and group theory, and computational chemistry.

What can be partially substituted:
- **Lab technique** — MIT's 5.310 has video demonstrations of every
  technique. Watching is not doing, but it prevents you being lost when
  you do reach a bench.
- **Spectroscopic interpretation** — genuinely learnable from home. NMR,
  IR and mass-spec problem sets are just puzzles on paper, and free
  problem banks are abundant. This is the highest-return lab-adjacent
  skill you can self-teach.
- **Synthesis planning** — retrosynthesis is pure paper work.
- **Quantitative analysis** — the calculations transfer; the pipetting
  does not.
- **Computational chemistry** — fully self-teachable, and free software
  (Psi4, ORCA for academic use, Avogadro, RDKit) makes it the one branch
  where a home learner can do real original work.

What cannot be substituted at all: qualitative and quantitative wet
analysis, synthetic organic technique, instrumental operation, and the
safety judgment that only comes from a supervised bench.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 5.111SC Principles of Chemical Science (Fall 2014) | MIT OCW | Catherine Drennan | 150 | Scholar version — designed for independent study. Atomic and molecular structure, thermodynamics, acid-base and redox equilibria, kinetics, catalysis. Videos, notes, exams, practice problems with solutions. Drennan is a superb lecturer and the course is strongly biological in its examples, which suits anyone heading toward biochemistry. The default free general chemistry course. |
| 5.111 Principles of Chemical Science (Fall 2008) | MIT OCW | — | 150 | The earlier video-lecture version. Still up. Use the SC version instead unless you specifically want the older lecture style. |
| 3.091SC Introduction to Solid State Chemistry (Fall 2010) | MIT (Materials Science) | Donald Sadoway | 150 | Scholar version, full materials. Sadoway is a legendary lecturer — this course has probably converted more people to materials science than any other single artifact. Teaches general chemistry from the standpoint that electronic structure explains the material world, which is a genuinely different and more satisfying framing than 5.111's. Also listed under Materials Science below. |
| 3.091 Introduction to Solid-State Chemistry (Fall 2018) | MIT | Jeffrey Grossman | 150 | The modern re-recording with lecture videos. Content overlaps Sadoway's heavily. Grossman is good; Sadoway is better. Take the 2010 SC version for the lectures and the 2018 version for updated problems. |
| CHEM 125a Freshman Organic Chemistry I | Open Yale | J. Michael McBride | 60 | Video plus transcripts and problem sets. Unlike any other organic course you will find: McBride teaches organic chemistry *historically*, starting from how anyone first knew molecules had shapes, working through van 't Hoff and the X-ray evidence. The first eight lectures on the history of structural theory are worth taking even if you learn your actual organic chemistry from MIT. Slow-paced and idiosyncratic; not efficient exam prep. |
| CHEM 125b Freshman Organic Chemistry II | Open Yale | J. Michael McBride | 60 | Continuation, into reactions and mechanism. Same virtues and same inefficiency. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 5.12 Organic Chemistry I (Spring 2005) | MIT OCW | Kimberly Berkowski, Sarah O'Connor | 120 | Lecture handouts, problem sets, exams and solutions — **no video**. Standard MIT sophomore organic: structure, stereochemistry, substitution and elimination, then carbonyls. Complete enough to learn from if you can work from notes. Pair with McBride's Yale videos for the lecture experience. |
| 5.60 Thermodynamics & Kinetics (Spring 2008) | MIT OCW | Moungi Bawendi, Keith A. Nelson | 120 | Full video lecture set plus notes, psets and solutions. This is the physical chemistry course most people should take first — thermo before quantum. Bawendi later won a Nobel for quantum dots; the lecturing here is workmanlike rather than dazzling, but the materials are complete and the problems are good. |
| 5.61 Physical Chemistry (Fall 2017) | MIT OCW | Robert Field | 150 | Video lectures plus full materials. The quantum half of p-chem: wave nature of the electron, particle in a box, harmonic oscillator, angular momentum, hydrogen atom, perturbation theory, spectroscopy. Field is a spectroscopist and the spectroscopy sections reflect that — they are the best part of the course. Substantially overlaps MIT 8.04 but framed for chemists, i.e. aimed at molecules rather than at foundations. |
| 5.310 Laboratory Chemistry (Fall 2019) | MIT OCW | — | 40 | The closest free substitute for lab experience. Video demonstrations of the standard techniques plus the written experiment protocols. You will not learn to do these things by watching. You will learn what they are, what can go wrong, and what the data looks like — which is worth real hours before you ever pay for bench time. |
| 5.07SC Biological Chemistry I (Fall 2013) | MIT OCW | John Essigmann, Bogdan Fedeles | 120 | Scholar version. Protein structure, catalysis, cofactor chemistry, then metabolism — glycolysis, gluconeogenesis, fatty acid metabolism, pentose phosphate, Krebs, oxidative phosphorylation. Includes a "Lexicon of Biochemical Reactions" resource that organizes metabolism by *reaction type* rather than by pathway; that framing is unusually clarifying and is the standout feature of the course. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 5.04 Principles of Inorganic Chemistry II (Fall 2008) | MIT OCW | — | 120 | Materials only — lecture notes, problem sets, practice problems, exams. Systematic chemical group theory, then ligand field theory and the electronic, vibrational and magnetic spectroscopy of transition metal complexes. Group theory for chemists is hard to find free at this quality; this is the best option. No video. |
| Introductory Quantum Chemistry | NPTEL / IISc Bangalore | K. L. Sebastian | 50 | Video course. Postulates, particle in a box, tunnelling, harmonic oscillator, hydrogen atom, angular momentum, chemical bonding. A gentler on-ramp to 5.61 if MIT's pace is punishing. Video plus notes; assignments generally only during live runs. |
| Quantum Chemistry of Atoms and Molecules | NPTEL / IIT Bombay | — | 50 | Second NPTEL option at similar level. Take one, not both. |
| 3.320 Atomistic Computer Modeling of Materials (SMA 5107, Spring 2005) | MIT OCW | Gerbrand Ceder, Nicola Marzari | 100 | The best free computational course spanning chemistry and materials. Classical potentials through density functional theory and pseudopotentials; then Monte Carlo, molecular dynamics, free energies and phase transitions, coarse-graining. Includes labs. Dated in its software specifics — the *methods* are entirely current, the tooling is not. Do the theory here, run it in modern Psi4 or Quantum ESPRESSO. |

**Not courses, but the two free resources you will actually live in:**
LibreTexts Chemistry (chem.libretexts.org) is a full open textbook library
covering general, organic, physical, inorganic, analytical and biological
chemistry with worked problems — it is the free replacement for the $300
textbooks these courses assume you own. For analytical chemistry
specifically, there is no strong free *video* course anywhere; LibreTexts'
analytical volumes plus 5.310's protocols are the honest best available.

### The spine — Chemistry

1. **5.111SC Principles of Chemical Science** (MIT, Drennan) — or 3.091SC
   if the materials framing appeals more.
2. **5.12 Organic Chemistry I** (MIT) — with McBride's Yale lectures as
   the video track.
3. **5.60 Thermodynamics & Kinetics** (MIT) — thermo before quantum.
4. **5.61 Physical Chemistry** (MIT, Field) — the quantum half.
5. **5.07SC Biological Chemistry I** (MIT) — if you are heading toward
   life sciences; **5.04 Inorganic** if toward materials or catalysis.
6. **5.310 Laboratory Chemistry** (MIT) — watch it early, not last, so you
   know what the theory is describing.

### Overlaps resolved — Chemistry

**General chemistry: 5.111SC vs. 3.091SC.** Genuinely close. 5.111 is
biological in emphasis and is the right choice if biochemistry or medicine
is downstream. 3.091 is structural and materials-oriented, and Sadoway is
the better lecturer by a clear margin. If you have time for only one and
no strong direction, take 3.091SC — you will finish it, which is the
property that matters most.

**Organic: MIT 5.12 vs. Yale CHEM 125a/b.** Split the difference. MIT has
the problem sets and solutions and the conventional coverage you would be
examined on; Yale has the lectures and a far more interesting intellectual
frame. Use MIT as the spine and McBride as the narration. Taking Yale
alone will leave you with a beautiful understanding of why chemists
believe in molecular structure and an inability to predict a reaction
product.

**Physical chemistry quantum: 5.61 vs. MIT 8.04.** Different audiences.
8.04 is deeper on foundations and formalism; 5.61 is aimed at molecules,
bonding and spectroscopy. A chemist takes 5.61. A physicist takes 8.04.
Taking both is not wasteful but 8.04 first makes 5.61 feel remedial.

**Computational: 3.320 vs. the NPTEL quantum chemistry courses.** 3.320 is
about simulating materials and includes real methodology; the NPTEL
courses are about the quantum mechanics of molecules and stop before
computation. They are complements, not competitors — but if you only do
one, 3.320 is the one that produces a skill.

---

## 3. Astronomy and Cosmology

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| ASTR 160 Frontiers and Controversies in Astrophysics (Spring 2007) | Open Yale | Charles Bailyn | 50 | Video plus transcripts, problem sets and exams with solutions. Three topics only — exoplanets, black holes, dark energy — rather than a survey. Bailyn does something rare: he teaches what is *not* known and why, and derives real results with real algebra. Slightly dated on exoplanets (pre-Kepler in the main lectures, though OCW added later "Update" lectures covering Kepler and structure growth). Still the best free intro astronomy course. |
| The Science of the Solar System | Caltech (Coursera) | Mike Brown | 50 | Entirely free — the whole course, not a crippled audit track. Four units: water on Mars, giant planet interiors, small bodies, and life in the solar system. Brown discovered Eris and got Pluto demoted, and the course carries the authority of someone arguing about the actual open questions. The best free planetary science course by a wide margin. |
| 8.282J Introduction to Astronomy (Spring 2006) | MIT OCW | Saul Rappaport | 100 | Materials only — no video. Quantitative intro to the solar system, stars, ISM, galaxy and universe. Problem sets and exams with solutions. Take this if you want the numbers rather than the narrative; take ASTR 160 if you want to be interested. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 8.284 Modern Astrophysics (Spring 2006) | MIT OCW | Paul Schechter | 120 | Materials only. Applies Newtonian, statistical and quantum mechanics to main-sequence stars, white dwarfs, neutron stars, black holes, pulsars, supernovae, the ISM, and galaxies. Problem sets with solutions. This is the real undergraduate astrophysics course — it assumes you have done 8.01–8.04 and it uses all of it. |
| 8.286 The Early Universe (Fall 2013) | MIT OCW | Alan Guth | 120 | Video lectures plus slides, problem sets and solutions. Guth invented inflation; this is him teaching cosmology from the ground up, with the first half tracing the big-bang theory from 1915 to 1980 and the second covering the particle-physics era. Requires only intro physics and calculus, which makes it the most accessible serious cosmology course anywhere. The two opening lectures on inflation and the multiverse are a standalone pleasure. |
| Cosmology (Theoretical Minimum) | Stanford | Leonard Susskind | 25 | Video only. Fast, conceptual, no problems. Good as a preview of 8.286 or as a recap after. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 8.901 Astrophysics I (Spring 2006) | MIT OCW | Deepto Chakrabarty | 150 | Graduate stellar astrophysics — structure, evolution, and onward to galactic dynamics and dark matter. Materials only: readings, problem sets. No video. Hard, and dependent on having done 8.284 or equivalent. |
| Super-Earths and Life | HarvardX (edX) | Dimitar Sasselov | 30 | Audit track free. Astrobiology from the exoplanet side — habitability, biosignatures, what "Earth-like" actually means. Lighter than everything else in this section; good breadth, thin on quantitative work. Availability on edX rotates; check the archive if it is not currently running. |

### The spine — Astronomy and Cosmology

1. **ASTR 160** (Yale, Bailyn) — the hook, and more rigorous than it looks.
2. **The Science of the Solar System** (Caltech, Brown) — planetary
   science, and free in full.
3. **8.284 Modern Astrophysics** (MIT, Schechter) — the real course. Needs
   physics through quantum first.
4. **8.286 The Early Universe** (MIT, Guth) — cosmology from the person
   who wrote a chapter of it.
5. **8.901 Astrophysics I** (MIT) — only if you are going further.

### Overlaps resolved — Astronomy

**Intro: ASTR 160 vs. 8.282J.** Bailyn wins for a first pass — video,
transcripts, and a course structured around live controversies rather than
a survey. 8.282J wins if you want quantitative problem sets and are
comfortable working from notes with no lecturer. Doing both is redundant;
if you are strong enough to enjoy 8.282J you should go straight to 8.284.

**Cosmology: 8.286 vs. Susskind's Cosmology.** Guth wins on every axis
except time — full materials, problem sets, solutions, and the author of
inflation teaching inflation. Susskind's is a 25-hour appetizer.

**Planetary science: Brown's Coursera course vs. anything at MIT.** Brown
wins outright. MIT's planetary offerings on OCW are materials-only and
scattered across Course 12; Brown's is a complete, free, well-produced
course by a working planetary scientist. There is no real competition here.

---

## 4. Earth and Environmental Science

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| GG 140 The Atmosphere, the Ocean, and Environmental Change (Fall 2011) | Open Yale | Ronald B. Smith | 60 | 36 video lectures with transcripts, problem sets and three exams plus a final, all with solutions. Clouds, rain, severe storms, the ozone layer, air pollution, ocean currents, El Niño, paleoclimate, global warming, energy and water resources. The most complete free earth-systems course in existence and the natural first course in this whole division. Smith is unspectacular as a lecturer and utterly reliable as a teacher. |
| 12.001 Introduction to Geology (Fall 2013) | MIT OCW | — | 100 | Materials only — no video. Lecture notes, lab exercises, and the materials from a weekend field trip. Minerals and rock ID, plate tectonics, geologic mapping, erosion by rivers and glaciers, origin of continents, history of life. The lab exercises are the valuable part and several can be done with a hand lens and rock samples you buy for very little. Geology is the one earth science where fieldwork substitutes cheaply — go outside. |
| 12.003 Atmosphere, Ocean and Climate Dynamics (Fall 2008) | MIT OCW | — | 100 | Materials only. The fluid-dynamics foundation under GG 140: rotation, stratification, geostrophic balance, the general circulation. Includes lab demonstration materials using rotating tanks. More physical and more demanding than the Yale course. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 12.340 Global Warming Science (Spring 2012) | MIT OCW | Kerry Emanuel, Sara Seager, Daniel Cziczo, David McGee | 100 | Materials only — lecture notes and assignments. The physics and chemistry of climate change with no policy content and no hand-waving: radiative transfer, feedbacks, paleoclimate records, model construction and model limits. Emanuel is the leading authority on hurricane climatology and the course reflects that seriousness. A version was also produced as 12.340x for MITx; the OCW materials are the freely durable ones. |
| 12.808 Introduction to Observational Physical Oceanography (Fall 2004) | MIT OCW | — | 100 | Materials only. Physical properties of seawater, measurement methods, wind-driven circulation, abyssal circulation, boundary processes. Old but the physics has not changed. The measurement-methods sections are the distinctive content — most climate courses skip how anyone actually knows the ocean's temperature. |
| 1.018J Ecology I: The Earth System | MIT OCW | — | 100 | Materials only. Ecology treated as biogeochemistry — energy flow, nutrient cycling, the Earth as coupled system — rather than as natural history. The right ecology course for someone coming from a physical-science direction. |
| Energy Within Environmental Constraints | HarvardX (edX) | Michael Aziz | 40 | Audit track free with limited access to graded material. Quantitative treatment of energy systems: what each source can actually deliver, at what cost, with what emissions. Aziz teaches you to do the back-of-envelope calculations yourself rather than to hold opinions. The best free course on energy as a physical rather than political problem. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 22.081J Introduction to Sustainable Energy (Fall 2010) | MIT OCW | — | 100 | Materials only — lectures and readings, plus assignments. Assesses current and potential energy systems end to end: resources, extraction, conversion, end use. More engineering-flavored than the Harvard course and heavier on nuclear (it is taught out of Nuclear Science and Engineering). Take it after the Harvard course, not instead. |
| Climate Physics and Chemistry (MIT Course 12 graduate offering) | MIT OCW | — | 100 | Graduate-level climate. Materials only. Listed here without a course code because MIT's climate offerings have been renumbered over time and I am not confident enough in the number to give it — search OCW's Earth, Atmospheric and Planetary Sciences listing by title. |
| OpenLearn Earth science units | The Open University | various | 5–20 each | Not full university courses — free standalone units of 5 to 20 hours on plate tectonics, oceanography, volcanoes, and Earth history, with self-assessment. The OU's writing for distance learners is the best in the world and these fill gaps that MIT's materials-only pages leave open. Use them as targeted supplements. |

### The spine — Earth and Environmental Science

1. **GG 140** (Yale, Smith) — the complete introduction, with video and
   solutions.
2. **12.001 Introduction to Geology** (MIT) — and go outside with the lab
   exercises.
3. **12.003 Atmosphere, Ocean and Climate Dynamics** (MIT) — the physics
   under the first course.
4. **12.340 Global Warming Science** (MIT) — climate done as science.
5. **Energy Within Environmental Constraints** (HarvardX, Aziz) — the
   applied end.

### Overlaps resolved — Earth Science

**Climate: GG 140 vs. 12.003 vs. 12.340.** Not really competitors — they
form a ladder. GG 140 is descriptive and complete with video; 12.003 adds
the geophysical fluid dynamics; 12.340 adds the radiative physics and the
modelling. Take them in that order. If you take only one, take GG 140,
because it is the only one with a lecturer and solutions.

**Oceanography: 12.808 vs. GG 140's ocean lectures.** GG 140 covers ocean
circulation adequately for a generalist. Take 12.808 only if oceanography
is a target rather than a topic — it is materials-only, dated, and
demanding.

**Energy: HarvardX vs. 22.081J.** Aziz's course wins for a first pass —
better structured, better pedagogy, and it teaches a transferable habit of
quantitative estimation. 22.081J wins on technical depth and on nuclear
and conversion technologies. The audit-track limitation on the Harvard
course is a real cost; the MIT course gives you everything permanently.

---

## 5. Materials Science and Engineering

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 3.091SC Introduction to Solid State Chemistry (Fall 2010) | MIT OCW | Donald Sadoway | 150 | Cross-listed from Chemistry above and the correct entry point to this division. Scholar version with full video, notes, psets and solutions. Sadoway's thesis — that electronic structure explains the material world — is what makes this cohere where general chemistry courses feel like a list. The lectures on bonding, on crystal structure, and the glass and polymer lectures near the end are the best free introduction to why materials behave as they do. |
| 3.091 Introduction to Solid-State Chemistry (Fall 2018) | MIT OCW | Jeffrey Grossman | 150 | The modern re-recording with its own video set and updated problems. Use the 2018 problems with the 2010 lectures. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 3.012 Fundamentals of Materials Science | MIT OCW | — | 120 | Materials only. Thermodynamics, structure and bonding for materials — the theoretical core of the MIT materials curriculum. MIT recommends taking it alongside 3.014 (the laboratory subject). No video; problem sets present. |
| 3.032 Mechanical Behavior of Materials (Fall 2007) | MIT OCW | — | 120 | Materials only — notes, psets, exams, and the laboratory write-ups. Continuum description of properties down to the atomistic mechanisms behind them: elastic and plastic deformation, creep, fracture, across crystalline and amorphous metals, ceramics and biopolymers. This is where materials selection actually lives — the trade-offs Ashby charts summarize are derived here. |
| The Oxford Solid State Basics | University of Oxford Podcasts | Steven H. Simon | 40 | Cross-listed from Physics. 21 lectures on crystal structure, reciprocal space, free electrons, band theory, phonons and magnetism, tracking Simon's textbook. The solid-state physics half of a materials education, and the best free treatment of it. |
| 8.231 Physics of Solids I (Fall 2006) | MIT OCW | Xiao-Gang Wen | 100 | Cross-listed from Physics. Materials only. The more theoretical route through the same territory. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 3.320 Atomistic Computer Modeling of Materials (SMA 5107, Spring 2005) | MIT OCW | Gerbrand Ceder, Nicola Marzari | 100 | Cross-listed from Chemistry. Classical potentials through DFT and pseudopotentials, then Monte Carlo, molecular dynamics, free energies, phase transitions and coarse-graining. Includes labs. Software specifics are twenty years old; the methodology is not. The single highest-return advanced course in this division for a self-learner, because the output is a skill you can demonstrate. |
| DoITPoMS teaching and learning packages | University of Cambridge | various | 2–8 each | Not courses — dozens of free interactive modules (doitpoms.ac.uk) on crystallography, dislocations, phase diagrams, composites, corrosion, and more, plus a micrograph library and an interactive Miller-index tool. Cambridge built these as supplements to their own materials degree. The phase-diagram and dislocation modules do more for intuition in two hours than most lecture courses do in ten. Use them constantly alongside 3.012 and 3.032. |
| Nanotechnology / nanoscience courses | NPTEL (various IITs) | various | 40–60 each | NPTEL's materials and nanotechnology catalogue is large and uneven — quality varies sharply by instructor, so sample two or three lectures before committing. Video plus notes; assignments generally only during live runs. This is the main free option for nanomaterials specifically, because MIT's nanomaterials offerings on OCW are materials-only and assume the full 3.012/3.032 sequence. |

### The spine — Materials Science

1. **3.091SC Introduction to Solid State Chemistry** (MIT, Sadoway).
2. **3.012 Fundamentals of Materials Science** (MIT) — thermodynamics and
   structure, with DoITPoMS modules alongside for the phase diagrams.
3. **3.032 Mechanical Behavior of Materials** (MIT) — where selection
   trade-offs come from.
4. **The Oxford Solid State Basics** (Oxford, Simon) — the physics half.
5. **3.320 Atomistic Computer Modeling** (MIT, Ceder and Marzari) — the
   part that becomes a portfolio.

### Overlaps resolved — Materials Science

**Intro: 3.091SC (2010) vs. 3.091 (2018).** Same subject, two recordings.
Sadoway is the better lecturer and the reason people remember this course;
Grossman's version has fresher problems and examples. Watch 2010, work
2018.

**Solid state: Simon (Oxford) vs. 8.231 (MIT).** Simon for a first pass —
lectures exist, the accompanying book is excellent, the pedagogy is
deliberate. 8.231 if you want the more formal theoretical treatment and
are content working from notes alone.

**Materials selection.** There is no good free course. The subject is
dominated by Ashby's method and the Granta/CES software, both commercial.
The honest substitute is 3.032 for the underlying property trade-offs plus
the DoITPoMS modules — you will understand *why* the Ashby charts have the
shapes they do, without having the tool that draws them. Do not let anyone
sell you a free "materials selection course"; check what it actually
teaches first.

**Nanomaterials.** Weakest area in this catalogue. NPTEL is the main free
option and it is uneven. MIT's nanomaterials subjects on OCW exist but are
materials-only and assume the full MIT sequence. Expect to assemble this
one from review papers rather than from a course.

---

## Cross-division notes

**What this catalogue cannot give you.** No laboratory work in chemistry,
no observing time in astronomy, no field mapping in geology beyond what you
can do locally, and no credential. Every course here is genuinely free;
none of them is accredited on the free track. If credit is the goal, the
realistic path is to use these to prepare for credit-by-examination
(CLEP, DSST) and community-college lab sections, not to expect the
courses themselves to count.

**Where the free ecosystem is strongest:** physics, overwhelmingly. MIT's
physics department has published more complete, more usable free material
than any other science department anywhere, and Zwiebach and Kardar in
particular are better than what most students get in person.

**Where it is weakest:** analytical chemistry (no strong free video course
exists), materials selection (dominated by commercial software),
nanomaterials, and anything requiring a bench or an instrument.

**A note on "audit" courses.** Coursera and edX audit tracks vary from
generous (Mike Brown's solar system course is free in full, deliberately)
to nearly useless (graded assignments paywalled, access expiring after a
few weeks). Check what the audit track actually includes before building a
plan around one. OCW and Open Yale have no such problem — the materials
are permanently and completely free, which is why they dominate this list.

---

# Life Sciences and Mind

Everything below is free to access without payment. Where a course lives on
Coursera or edX, "free" means the audit track: you get the lectures and
usually the readings, and you lose graded assignments, the certificate, and
sometimes the quizzes. That distinction is called out course by course,
because for a self-directed degree the assignments are the part that
actually teaches you.

Hours are approximate throughout — they represent a serious pass with the
problem sets, not a video skim. Treat them as within about 30 percent.

Three structural facts worth knowing before you start:

MIT OpenCourseWare is the only source here that reliably gives you the full
package — lectures, problem sets, solutions, and exams with keys. The "SC"
and "RES" designations mean the course was deliberately rebuilt for
independent study. Prefer those.

Open Yale Courses stopped adding content around 2011 and the site is now
static. The courses that exist are excellent and the videos still work, but
nothing new is coming, and some material has aged.

Johns Hopkins Bloomberg School retired its OpenCourseWare site at the end of
2021. The public health material that used to live there is now split
between Coursera audit tracks and Internet Archive captures. The Coursera
route is the live one and it is genuinely deep.

---

## 1. Biology

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 7.01SC Fundamentals of Biology | MIT OCW | Lander, Weinberg, Sive, Walker, Jacks, Chisholm, Mischke | 120 | The reference implementation of a free intro bio course. Video lectures (pulled from the 2004 7.012 recordings), problem sets with full solutions, exams with keys, and study-guide framing built for solo learners. Eric Lander's genetics and molecular biology block is the best lecturing in the subject anywhere, free or paid — he builds Mendel to molecules without a gap. Bob Weinberg's cancer lectures near the end are the other standout and are worth watching even if you take a different intro course. Video is 2004-vintage and looks it. |
| 7.016 Introductory Biology | MIT OCW | Barbara Imperiali, Adam Martin, Diviya Ray | 90 | The modern MIT intro. Sharper video, tighter recitations, contemporary problem sets. Imperiali on protein structure, enzyme mechanism, and metabolism is unusually lucid — clearer than 7.01SC on that specific block. Full problem sets and exams included. Slightly less biochemistry-light than 7.01SC and more molecular from the start. |
| Introduction to Biology — The Secret of Life (7.00x) | MITx / edX | Eric Lander | 100 | Lander's course rebuilt as a MOOC with embedded interactive problems. Audit access gives the videos and most in-video questions; graded problem sets sit behind the paid track. Take this if you want Lander with modern production; take 7.01SC if you want the assignments for free. |
| E&EB 122 Principles of Evolution, Ecology and Behavior | Open Yale | Stephen C. Stearns | 40 | Recorded 2009. Thirty-six 50-minute lectures, full transcripts, syllabus, and problem sets. Stearns is one of the great living lecturers in evolutionary biology and this is the single best free evolution course in existence. Lectures 11 (life history evolution) and 17 (key events in evolution) are worth watching on their own even if you never touch the rest. No graded feedback — the real course required a 15-20 page paper you cannot submit. |
| Biology and High School Biology libraries | Khan Academy | staff | 50 | Not a university course and should not be a spine. Use it to patch specific gaps — Punnett squares, glycolysis steps, membrane transport — when an MIT problem set exposes something you never learned. Exercises are auto-graded and free. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| RES.7-006 / 7.03x Genetics | MIT OCW | Michael Hemann, Peter Reddien, Mary Ellen Wiltrout | 90 | The MITx genetics sequence archived on OCW in three parts. Full videos plus problem sets and solutions. Genetics is a subject you learn by grinding crosses and complementation tests, and this is one of very few free courses that gives you enough of them. |
| 7.03 Genetics (Fall 2004) | MIT OCW | Chris Kaiser, David Page | 30 | No video — lecture notes, problem sets, and exams only. Include it anyway: the Kaiser/Page problem sets are the hardest and best-constructed genetics problems available free. Use them as extra reps on top of 7.03x. |
| RES.7-007 / 7.06x Cell Biology | MIT OCW | Rebecca Lamason, Iain Cheeseman, Sebastian Lourido | 90 | Multi-part MITx cell biology archived on OCW with videos and assessments. Cheeseman on the cytoskeleton and mitosis is the section to keep. Genuinely current — this is not a 2005 recording. |
| RES.7-008 / 7.28x Molecular Biology | MIT OCW | Stephen P. Bell, Tania A. Baker | 100 | Three-part sequence covering replication, transcription, transposition, recombination, and repair, with problem sets. Bell on DNA replication is exceptional — he built much of the field's understanding of origin licensing and teaches it as a detective story. The mechanistic depth here is a real step up from any intro course. |
| 5.07SC Biological Chemistry I | MIT OCW | John Essigmann, JoAnne Stubbe, Bogdan Fedeles | 90 | MIT's biochemistry for independent study: video lectures, problem sets with worked solutions, and problem-solving videos. Stubbe is a legendary enzymologist and the enzyme catalysis sessions reflect it. This is a real biochemistry course, not "biochem for biologists" — expect to need organic chemistry mechanism fluency and to go get it if you don't have it. |
| Fundamentals of Immunology (4-course specialization) | Rice University / Coursera | Alma Moon Novotny | 60 | Innate immunity and B cells; complement, MHC, T cells, cytokines; inflammation, tolerance, autoimmunity; pathogens and cancer. Auditable. This is the most complete free immunology sequence available, and immunology is otherwise a hole in the free landscape. Novotny is thorough rather than charismatic. Quizzes are behind the paywall; the lecture coverage is the value. |
| Bacteria and Chronic Infections | University of Copenhagen / Coursera | Copenhagen faculty | 15 | Auditable. Biofilms, acute versus chronic infection, cystic fibrosis and wound infection as case studies. Narrow, but there is no good free general microbiology course from a major university, and this is the most substantive microbiology teaching you can get free. Treat it as a supplement to the microbial content inside 7.01SC and 7.016. |
| Antimicrobial Resistance — Theory and Methods | Technical University of Denmark / Coursera | DTU faculty | 15 | Auditable. Resistance mechanisms plus actual lab methods (disk diffusion, agar dilution, susceptibility testing). Included because it shows you what wet-lab microbiology work looks like, which matters if you are deciding whether to pursue lab access. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 7.91J Foundations of Computational and Systems Biology | MIT OCW | Christopher Burge, David Gifford, Ernest Fraenkel | 70 | Sequence alignment, hidden Markov models, RNA-seq, protein structure, regulatory networks. Full video lectures plus problem sets with solutions — the psets involve real computation, which makes this one of the highest-value OCW listings in biology. Burge's lectures on sequence motifs and alignment are the strongest section. Requires programming comfort; Python is enough. |
| Systems Biology (2018 lecture series) | Weizmann Institute | Uri Alon | 30 | Recorded lectures plus exercises and notes on Alon's lab site. Network motifs, feed-forward loops, robustness, fold-change detection. Alon essentially created this way of thinking about biological circuits and teaches it with unusual clarity about what the math is for. Not a packaged MOOC — you assemble it from the playlist and the course page. Pair with his textbook if you can find it. |
| 7.22 Developmental Biology | MIT OCW | MIT Biology faculty | 30 | Materials only — no video. Reading lists, problem sets, and paper-discussion structure for a literature-based course. Developmental biology is badly served by free video; this at least gives you a defensible reading path through the primary literature. Honest assessment: harder to self-teach than anything else in this division. |
| Bioinformatics Specialization (6 courses) | UC San Diego / Coursera | Pavel Pevzner, Phillip Compeau | 120 | Auditable. Algorithmic bioinformatics taught as computer science — genome assembly, sequence comparison, phylogeny, clustering. The companion Rosalind problem platform is entirely free and gives you the graded practice the audit track withholds, which makes this the rare Coursera listing that loses almost nothing without payment. Pevzner is opinionated and rigorous. |
| Genomic Data Science Specialization | Johns Hopkins / Coursera | Salzberg, Leek, Langmead, Hansen, Taylor, Pertea, Florea | 100 | Auditable. Sequencing technologies, command-line tools, Bioconductor, statistics for genomics. More applied and less algorithmic than the UCSD sequence. Langmead's alignment material and Salzberg's assembly material are the best parts. Weaker if you have no R or Python. |
| Fundamentals of Biotechnology / Cell Biology / Cellular and Molecular Immunology | NPTEL (IIT) | IIT faculty (varies by course) | 40 each | Free video plus assignment PDFs; certification exam is the only paid part. Quality varies sharply by instructor. Worth checking when you need a topic no Western OCW covers, but do not build a spine on NPTEL — the production and pacing are inconsistent and some courses are read-off-slides. |

**The spine**

1. 7.01SC Fundamentals of Biology — the whole foundation, with problem sets
2. E&EB 122 with Stearns — evolution as the frame everything else hangs on
3. 5.07SC Biological Chemistry I — the chemistry you cannot skip and later
   courses will assume
4. RES.7-006 Genetics — the reasoning skill that transfers furthest
5. RES.7-008 Molecular Biology with Bell and Baker — mechanism at depth
6. 7.91J Computational and Systems Biology — where modern biology is done

Add 7.06x Cell Biology between 4 and 5 if you want the standard four-course
core rather than the compressed version.

**Overlaps resolved**

7.01SC versus 7.016 versus 7.00x. All three are MIT intro biology and
overlap almost completely. Take 7.01SC: it is the only one with the full
independent-study apparatus free. 7.016 wins on production and on the
biochemistry block specifically — watch Imperiali's enzyme lectures from
7.016 and do 7.01SC's problem sets. 7.00x loses because its assignments are
paywalled and its lectures are the same Lander content.

7.03 (2004) versus RES.7-006 (7.03x). Take 7.03x for the videos. Keep the
2004 problem sets. They are complements, not competitors.

Crash Course Biology and similar YouTube series versus any of the above.
Skip them at this level. They are calibrated for high school review and will
give you a false sense of coverage.

Bioinformatics: UCSD versus Johns Hopkins. Take UCSD if you want to
understand why the algorithms work — and because Rosalind makes the free
version nearly complete. Take Hopkins if you want to run real pipelines on
real data next month. Hopkins loses on conceptual depth; UCSD loses on
practical tooling.

Immunology: Rice is the only real option. Nothing to resolve, which is
itself a finding — immunology is the weakest-covered core subject in free
university biology.

---

## 2. Neuroscience

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Fundamentals of Neuroscience, Parts 1–3 (MCB80x) | HarvardX / edX | David Cox | 60 | Part 1 electrical properties of the neuron, Part 2 neurons and networks, Part 3 the brain. The best-designed neuroscience teaching object on the internet — custom interactive simulations where you clamp a membrane and watch an action potential form, plus DIY experiment segments. Auditable. Part 1 in particular does something no lecture can: it makes the Hodgkin-Huxley picture intuitive by letting you break it. Take Part 1 even if you take nothing else here. |
| 9.13 The Human Brain | MIT OCW | Nancy Kanwisher | 45 | Cognitive neuroscience organized around functional specificity: face areas, place areas, language, number, theory of mind. Kanwisher discovered several of the regions she teaches and the course is partly the story of how. Video lectures plus written assignments and lecture notes; lectures 3, 14, 17, 19, 22, and 25 were not recorded, so there are real gaps. The fMRI methodology lectures early on are the most transferable content in the course. |
| Understanding the Brain: The Neurobiology of Everyday Life | University of Chicago / Coursera | Peggy Mason | 40 | Auditable. Neuroanatomy and neural systems taught through everyday phenomena. Mason is the most engaging lecturer in free neuroscience and the neuroanatomy coverage is unusually good for an intro course — she makes you learn the actual pathways. Weekly quizzes and the final project are behind the paywall. |
| 9.01 Introduction to Neuroscience | MIT OCW | Martha Constantine-Paton | 30 | Lecture notes, recitation handouts, and exams — no video. Include it for the recitation problems and exams, which give you self-testing that MCB80x and 9.13 do not. Do not try to learn from it cold. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Medical Neuroscience | Duke / Coursera | Leonard E. White | 120 | Auditable. The most complete free neuroscience course that exists — full first-year medical school neuroscience, neuroanatomy through neurophysiology through clinical correlation, with brain-specimen dissection video and an atlas. Enormous: 12+ weeks at real intensity. White's neuroanatomy laboratory videos are the single best free resource for learning actual brain structure. Quizzes are paywalled; the lectures and the lab videos are not. |
| Synapses, Neurons and Brains | Hebrew University of Jerusalem / Coursera | Idan Segev | 30 | Auditable. Cellular and computational neuroscience from one of the people who built the field's modeling tools. Segev connects dendritic biophysics to what networks compute better than anyone teaching free. Idiosyncratic pacing and heavy Israeli-accented delivery that some find hard; the content justifies the effort. |
| Human Behavioral Biology | Stanford | Robert Sapolsky | 40 | Twenty-five roughly 90-minute lectures, complete and free on YouTube. Straddles neuroscience, endocrinology, ethology, genetics, and psychiatry. Sapolsky is the best classroom lecturer in this catalogue by a distance. No assignments, no readings enforced, no problem sets — this is lecture-video-only and you should treat it as a way of thinking rather than a credential-equivalent course. The lectures on the limbic system, on stress and neural degeneration, and on schizophrenia are individually worth more than most complete courses. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 9.40 Introduction to Neural Computation | MIT OCW | Michale Fee, Daniel Zysman | 80 | Full video lectures, complete lecture notes, problem sets with solutions, and exams with study guides. Quantitative neuroscience done properly — integrate-and-fire models, receptive fields, convolution, PCA, spectral analysis, decision theory. This is the most rigorous free neuroscience course available and the one that will make you employable in a computational lab. Requires linear algebra and basic differential equations; get them first. |
| Computational Neuroscience | University of Washington / Coursera | Rajesh P. N. Rao, Adrienne Fairhall | 40 | Auditable. Neural encoding and decoding, information theory, network models, plasticity and learning. Gentler on-ramp than 9.40 and stronger on information-theoretic framing. Fairhall's segments on neural coding are the highlight. Programming exercises exist in the paid track but the concepts survive auditing. |
| 9.14 Brain Structure and Its Origins | MIT OCW | Gerald E. Schneider | 40 | Materials-based: extensive lecture notes, readings, and assignments on comparative and developmental neuroanatomy. Unusual angle — it teaches brain structure through evolutionary history rather than as a memorization list, which makes the anatomy stick. No video. |
| RES.9-004 Nancy's Brain Talks | MIT OCW | Nancy Kanwisher | 10 | Short standalone video modules on brain structure and on specific cognitive neuroscience methods. Not a course. Genuinely useful as a fast, accurate reference when you hit a term you don't know. |

**The spine**

1. MCB80x Parts 1–3 — mechanism from the ground up, with simulations
2. Medical Neuroscience with Leonard White — the anatomy and systems body
   of knowledge, and the lab videos
3. 9.13 The Human Brain with Kanwisher — cognitive neuroscience and how
   claims about the brain get made or fail
4. Sapolsky's Human Behavioral Biology — integration across levels
5. 9.40 Introduction to Neural Computation — the quantitative core

Add Segev's Synapses, Neurons and Brains between 1 and 2 if the biophysics
in MCB80x left you wanting more.

**Overlaps resolved**

MCB80x versus 9.01 versus Mason's Chicago course, all covering intro
neuroscience. Take MCB80x — the interactive simulations teach membrane
biophysics in a way lectures structurally cannot. Mason wins on
neuroanatomy specifically and on sheer watchability; take her anatomy weeks
as a supplement. 9.01 loses as a primary text (no video) but wins as a
source of exam questions.

Medical Neuroscience versus 9.13. They barely overlap despite both being
called neuroscience: White teaches structure and systems, Kanwisher teaches
cognition and methodology. Do both. If forced to choose one, White, because
you can acquire cognitive neuroscience from reading and you cannot acquire
neuroanatomy that way.

9.40 versus UW Computational Neuroscience. Take 9.40 — it has real problem
sets, free, with solutions, which is the entire point of a computational
course. UW wins only on approachability and on information theory framing.
Do UW first if 9.40's first problem set breaks you.

Sapolsky is overrated as a *course* and underrated as an *education*. He is
not teaching you to do neuroscience and there is nothing to submit. Watch
all 25 lectures; do not count it toward a curriculum's technical content.

---

## 3. Psychology

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| PSYC 110 Introduction to Psychology | Open Yale | Paul Bloom | 35 | Recorded 2007. Twenty lectures, transcripts, syllabus, and reading list. Bloom is a superb lecturer and the course is organized around genuinely interesting questions rather than textbook chapters. Its age shows in one important way: it predates the replication crisis, and several findings presented confidently — especially in the social psychology lectures — have since failed to replicate. Watch it, then read about the replication crisis before you believe it. The lectures on language and on development are the least dated and the best. |
| 9.00SC Introduction to Psychology | MIT OCW | John Gabrieli | 60 | Full independent-study build: video lectures, a free online textbook, multiple choice and short answer questions with keys, discussion material, and complete exams with solutions. Less charismatic than Bloom, more rigorous, and much better on the neural basis of psychological phenomena — Gabrieli is a cognitive neuroscientist and it shows. If you want one intro psych course with assessments, this is it. |
| Introduction to Psychology | Yale / Coursera | Paul Bloom | 20 | Auditable. Bloom's material rebuilt as a shorter MOOC. Redundant with PSYC 110 and thinner. Take it only if you want a fast pass with modern production. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Human Behavioral Biology | Stanford | Robert Sapolsky | 40 | Listed under neuroscience but belongs equally here — it is the best available treatment of the biological substrate of behavior, aggression, sexuality, and psychiatric disorder. The lectures on individual differences and on schizophrenia and on depression are the strongest behavioral-biology teaching free anywhere. Lecture-video-only. |
| Social Psychology | Wesleyan / Coursera | Scott Plous | 25 | Auditable. Decision making, persuasion, conformity, group behavior, attraction. Plous built the Social Psychology Network and the course is unusually well constructed, with real activities rather than passive video. Same caveat as Bloom: it leans on classic studies, several of which are contested. Plous is more candid about this than most. |
| The Science of Well-Being | Yale / Coursera | Laurie Santos | 20 | Auditable, and the videos are also on YouTube free. Four million enrollments, which makes it the most famous psychology MOOC ever. Honest assessment: it is a good course that is overrated as *psychology*. It is largely applied positive psychology with behavior-change exercises, and much of the literature it draws on is in the least-replicable corner of the field. Take it for the self-experiments; do not count it as your social or cognitive psychology. |
| Psychological First Aid | Johns Hopkins / Coursera | George Everly | 8 | Auditable. Practical crisis-response framework (RAPID model). Not academic psychology. Included because it is short, credible, and directly useful if you volunteer in any health or crisis setting — which is one of the few ways to get real clinical exposure without enrollment. |
| PSYC 123 The Psychology, Biology and Politics of Food | Open Yale | Kelly D. Brownell | 25 | Recorded lectures, transcripts, readings. Eating behavior, obesity, food policy, and the industry's role. Sits between psychology, public health, and food systems, and is one of the few courses that connects individual behavior to policy honestly. Brownell was a central figure in this policy fight and does not pretend neutrality. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 9.13 The Human Brain | MIT OCW | Nancy Kanwisher | 45 | Doubles as the cognitive psychology course. Better than any standalone free cognitive psych offering because it forces you to reason about evidence — how you would establish that a brain region does one thing and not another. Written assignments included. |
| 9.40 Introduction to Neural Computation | MIT OCW | Michale Fee | 80 | Doubles as the quantitative methods course for anyone heading toward cognitive science. |
| Research Methods / Statistics | — | — | — | Honest gap. There is no single strong free university course in psychology research methods. Build it from three pieces: the Johns Hopkins Biostatistics in Public Health sequence below for inference; Introduction to Systematic Review and Meta-Analysis (also Hopkins) for evidence synthesis; and any credible open treatment of the replication crisis, p-hacking, and preregistration. Doing this deliberately matters more in psychology than in any other field on this list. |

**The spine**

1. 9.00SC Introduction to Psychology with Gabrieli — with the assessments
2. PSYC 110 with Bloom — watched second, as enrichment, with the
   replication caveat held in mind
3. Sapolsky's Human Behavioral Biology — the biological substrate
4. Social Psychology with Plous — the social level, critically read
5. 9.13 The Human Brain with Kanwisher — cognition and methodology
6. The methods stack assembled from the Hopkins biostatistics and
   systematic review courses

**Overlaps resolved**

Bloom's PSYC 110 versus Gabrieli's 9.00SC versus Bloom's Coursera version.
Take 9.00SC as your spine because it is the only one with a full free
assessment apparatus and because Gabrieli's neuroscience grounding ages
better. Take PSYC 110 for the lecturing. Drop the Coursera version entirely
— it is strictly dominated by PSYC 110.

Social psychology: Plous versus the social lectures inside Bloom or
Gabrieli. Plous, clearly — a dedicated course with activities beats three
survey lectures.

The Science of Well-Being versus a real course on emotion or personality.
There is no strong free university course in personality psychology, which
is why Santos's course fills the slot by default. Recognize that as a gap
rather than a solution.

Clinical and abnormal psychology is the weakest area in the entire free
landscape. Sapolsky's psychiatric lectures and Gabrieli's psychopathology
lectures are the best you will do. Nobody has published a good free
abnormal psychology course from a major university. Do not pretend
otherwise.

---

## 4. Medicine and Health Sciences

This is where the free material is deepest — public health and epidemiology
in particular are better served free than almost any subject in any
division of any catalogue. Johns Hopkins alone accounts for a near-complete
MPH core.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Anatomy Specialization (4 courses) | University of Michigan / Coursera | Kelli Sullivan, Glenn Fox, B. Kathleen Alsup | 60 | Auditable. Musculoskeletal and integumentary; cardiovascular, respiratory, urinary; nervous system and senses; gastrointestinal, reproductive, endocrine. Systems-based with a large multimedia library including cadaver imagery. The most complete free human anatomy teaching available. You still cannot dissect anything, which is the actual limitation. |
| Introductory Human Physiology | Duke / Coursera | Emma Jakoi, Jennifer Carbrey | 30 | Auditable. Nine organ systems, integrated whole-organism function. Clean, dense, no padding. Jakoi and Carbrey teach the regulatory logic — set points, feedback, integration — rather than lists of facts, which is exactly what makes physiology learnable. The best free physiology course. |
| Khan Academy Health and Medicine, and the MCAT collection | Khan Academy | staff, with AAMC | 80 | Not a university course. Built with the AAMC and the Robert Wood Johnson Foundation, roughly 1,100 videos and 3,000 practice questions across biology, biochemistry, physiology, psychology, and sociology. The practice questions are the value — free, graded, and calibrated to a real professional exam. The best free self-testing instrument in this entire division. Use it to check yourself, not to learn from cold. |
| Stanford Introduction to Food and Health | Stanford / Coursera | Maya Adam | 12 | Auditable. Nutrition fundamentals with a practical cooking component. Short and unpretentious. Adam is a Stanford School of Medicine lecturer and keeps it evidence-anchored. |

### Core — Epidemiology and Biostatistics

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Epidemiology: The Basic Science of Public Health | UNC Chapel Hill / Coursera | Karin Yeatts and colleagues | 15 | Auditable. Study designs, measures of association, causal inference basics, bias and confounding, worked through cardiovascular and infectious disease cases. The right first epidemiology course: short, concrete, and it teaches you to read a study rather than to recite definitions. |
| Epidemiology in Public Health Practice (5-course specialization) | Johns Hopkins / Coursera | Aruna Chandran, Keri Althoff, Justin Lessler | 90 | Auditable. The serious sequence — essential epidemiologic tools, data and health indicators, surveillance, outbreaks and epidemics, and a capstone. Lessler's outbreak and epidemic modeling material is the standout and is the best free treatment of transmission dynamics for non-modelers. This is genuinely close to an MPH epidemiology core. Graded work is paywalled but the lecture and reading coverage is complete. |
| Biostatistics in Public Health (4-course specialization) | Johns Hopkins / Coursera | John McGready | 60 | Auditable. Summary statistics, hypothesis testing, simple regression, multiple regression. McGready is a decorated teacher and the sequence is deliberately software-free — you learn what the procedures mean before you learn to run them. That is a real strength for a first pass and a real limitation afterward; plan to learn R separately. |
| Introduction to Systematic Review and Meta-Analysis | Johns Hopkins / Coursera | Hopkins evidence synthesis faculty | 15 | Auditable. Six modules: question formulation, eligibility criteria, search, data extraction, risk-of-bias assessment, meta-analysis. Cochrane itself points learners at this course. It is the single most useful short course in this catalogue for anyone who wants to evaluate scientific claims rather than produce them. |
| Understanding Clinical Research: Behind the Statistics | University of Cape Town / Coursera | Juan Klopper | 12 | Auditable. How to read the statistics section of a clinical paper — what the tests mean, when they are misused, what the numbers can and cannot support. Pairs precisely with the systematic review course. Klopper is a surgeon and teaches from what actually goes wrong in published work. |

### Core — Public and Global Health

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Health and Society | HarvardX / edX | Harvard Chan School faculty | 20 | Auditable. Social determinants of health — income, race, occupation, neighborhood — and how they get into the body. Solid grounding in the part of health that has nothing to do with clinical care, which is most of it. |
| Improving Global Health: Focusing on Quality and Safety | HarvardX / edX | Ashish Jha | 25 | Auditable. Healthcare quality measurement and improvement in resource-limited settings. Jha is one of the more credible voices in health systems and the course is unusually specific about measurement rather than aspiration. |
| Essentials of Global Health | Yale / Coursera | Richard Skolnik | 30 | Auditable. Burden of disease, health systems, key conditions by region, cost-effectiveness of interventions. Skolnik spent a career at the World Bank and writes the standard textbook. Comprehensive and slightly dry. The cost-effectiveness sections are the ones that change how you think. |
| The Challenges of Global Health | Duke / Coursera | Duke Global Health Institute faculty | 15 | Auditable. Shorter and more case-driven than Skolnik. Take it if Essentials is too much survey. |
| Health Policy sequence | Various / Coursera and edX | varies | 20 | The weakest area of the four. Free health policy teaching is fragmented, US-centric, and dated quickly by legislation. Prefer the health systems content inside the global health courses above over any standalone free policy course. |

### Advanced and Specialized

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| HST courses in Health Sciences and Technology | MIT OCW | Harvard-MIT HST faculty | varies | A large set of graduate medical-science listings — HST.035 Principle and Practice of Human Pathology, HST.121 Gastroenterology, HST.021 Musculoskeletal Pathophysiology, HST.542J Quantitative Physiology, among others. Almost all are materials-only: syllabi, lecture notes, readings, occasional problem sets, no video. They are the best free window into how medical pathophysiology is actually taught, and they are unusable as standalone courses. Mine them, do not enroll in them. |
| Cancer Biology Specialization | Johns Hopkins / Coursera | Hopkins oncology faculty | 30 | Auditable. Includes Understanding Cancer Metastasis. Solid mechanistic oncology at a level between introductory biology and the primary literature. Weinberg's cancer lectures in 7.01SC are better for fundamentals; this is better for clinical framing. |
| Vital Signs: Understanding What the Body Is Telling Us | University of Pennsylvania / Coursera | Penn Nursing and Medicine faculty | 15 | Auditable. Body temperature, pulse, respiration, blood pressure — physiology, measurement technique, and clinical meaning. Rare among free courses in that it teaches a physical skill you can actually practice on yourself and consenting friends. |
| Drug Development | UC San Diego / Coursera | Skaggs School of Pharmacy faculty | 15 | Auditable. Preclinical through regulatory approval. The best free approximation of pharmacology available, which is a low bar — pharmacology proper is essentially absent from the free landscape and requires a professional program. |
| Nutrition and Health sequences | Wageningen University / edX | Wageningen faculty | 30 | Auditable. More biochemically serious than most nutrition MOOCs. Take these over the popular consumer-facing nutrition courses if you want the physiology rather than the advice. |

**The spine**

1. Introductory Human Physiology (Duke) — the regulatory logic first
2. Anatomy Specialization (Michigan) — structure, alongside physiology
3. Epidemiology: The Basic Science of Public Health (UNC) — the on-ramp
4. Biostatistics in Public Health (Johns Hopkins, all four) — inference
5. Epidemiology in Public Health Practice (Johns Hopkins, all five) — the
   real thing
6. Introduction to Systematic Review and Meta-Analysis (Johns Hopkins) —
   how to judge what you read

Essentials of Global Health slots in after 5 if you want the policy and
systems layer.

**Overlaps resolved**

UNC Epidemiology versus the Hopkins Epidemiology specialization. They are
sequential, not competing. UNC is 15 hours and teaches you the vocabulary
and the study designs. Hopkins is 90 hours and teaches you the practice.
Do UNC first; it makes Hopkins much easier.

Biostatistics: Hopkins versus any generic statistics MOOC. Hopkins, because
it is taught entirely in the idiom of health data — the examples are
cohorts and trials, not coin flips — and because McGready is a better
teacher than the field average by a wide margin. Its weakness is the
deliberate absence of software; fix that separately rather than by choosing
a different course.

Global health: Skolnik at Yale versus Duke versus Jha at Harvard. Skolnik
for comprehensiveness, Jha for quality measurement, Duke for cases. If you
do one, Skolnik. Duke loses on depth; Jha is narrow by design and should be
read as a specialist add-on rather than an intro.

Anatomy: Michigan versus the anatomy inside Duke's Medical Neuroscience.
Michigan for whole-body systems anatomy. White's Duke course for the brain
specifically — his neuroanatomy lab videos are better than Michigan's
nervous system module and it is not close.

Khan Academy MCAT versus a real course. Never a substitute. Always a good
self-test. The distinction matters: its questions will tell you honestly
whether the course you just finished stuck.

---

## 5. Agriculture and Food Systems

Thinner than the other divisions, and much of what exists is
policy-and-sustainability framing rather than technical agronomy. These are
the ones that are genuinely worth time.

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Sustainable Food Security: The Value of Systems Thinking | Wageningen University / edX | Wageningen faculty | 20 | Auditable. Wageningen is the leading agricultural university in the world and it shows — this is the conceptual entry point to their food security series, and it takes systems thinking seriously rather than using it as a slogan. |
| Sustainable Food Security: Crop Production | Wageningen University / edX | Wageningen faculty | 25 | Auditable. Production ecology, yield gaps, agro-ecological drivers of production system diversity. The most technically substantive free agriculture course available. If you take one course in this division, this one. |
| Sustainable Food Security: Food Access | Wageningen University / edX | Wageningen faculty | 20 | Auditable. The distribution and entitlement side — why food insecurity persists amid adequate global production. Completes the Wageningen series. |
| Feeding the World | University of Pennsylvania / Coursera | Penn faculty | 15 | Auditable. Heavily focused on livestock production — dairy, swine, beef, poultry — with their life cycles, constraints, and societal controversies. Narrower than the title implies, and better for that. The most concrete free treatment of animal agriculture. |
| PSYC 123 The Psychology, Biology and Politics of Food | Open Yale | Kelly D. Brownell | 25 | Cross-listed from psychology. The demand side and the policy fight, from someone who was in it. |
| NPTEL agricultural and food technology courses | NPTEL (IIT and agricultural universities) | varies | 40 each | Free video plus assignments. Coverage of soil science, post-harvest technology, and food processing that Western platforms simply do not offer. Quality is uneven and the pedagogical style is lecture-and-slides. Worth searching when you need a specific technical topic. |

**The spine**

1. Sustainable Food Security: The Value of Systems Thinking (Wageningen)
2. Sustainable Food Security: Crop Production (Wageningen)
3. Sustainable Food Security: Food Access (Wageningen)
4. Feeding the World (Penn) — the animal agriculture half

That is the honest whole of it. Four courses is not a division of a degree,
and you should treat agriculture as a minor concentration built on top of
the biology spine rather than as a field you can cover free.

**Overlaps resolved**

Wageningen versus Penn. They barely overlap — Wageningen is crops and
systems, Penn is livestock. Do both.

Wageningen versus the many "sustainable food" MOOCs from business schools
and NGOs. Take Wageningen. The others are advocacy with a syllabus.

---

## What You Cannot Get This Way

Being clear about this is more useful than pretending otherwise.

**Wet lab technique.** Pipetting, sterile technique, gel electrophoresis,
PCR, cell culture, cloning, microscopy, dissection. No amount of video
substitutes. Nobody will hire you into a lab, or admit you to a graduate
program in experimental biology, on coursework alone. The legitimate
substitutes, in rough order of accessibility: a community biology lab
(Genspace in New York, Counter Culture Labs in Oakland, BioCurious in the
Bay Area, and roughly forty others worldwide — most run hands-on classes
for modest fees and some offer memberships); volunteering or working as an
undergraduate research assistant or lab washer at any nearby university,
which is far more obtainable than people assume and is how most biologists
actually started; a community college laboratory course, which is cheap
rather than free but is the most direct route to documented technique.

**Cadaveric anatomy.** Michigan's specialization and White's dissection
videos are the best available and they are still watching. The substitutes
are a community college anatomy and physiology sequence with a lab, or a
university anatomy course as a non-degree student.

**Clinical exposure.** Patient contact, physical examination, clinical
reasoning under uncertainty. Free courses cannot approach this. The real
routes: EMT-Basic certification, which typically runs 120 to 200 hours at a
community college or fire academy, is the single highest-value credential a
self-directed student can obtain in this space — it is legitimate, it puts
you in direct patient contact, and it is employable. Beyond that: certified
nursing assistant training, hospital volunteering, hospice volunteering,
crisis line work (which pairs well with the Hopkins Psychological First Aid
course), and medical scribing, which requires little training and puts you
inside clinical documentation.

**Clinical and counseling psychology practice.** Supervised clinical hours
are licensure-gated by statute in every jurisdiction. Nothing here moves
you toward it. Peer support and crisis line volunteering are the honest
entry points.

**Pharmacology at professional depth.** Genuinely absent from the free
landscape. The Drug Development course above is an orientation, not a
substitute.

**Field ecology.** Species identification, survey methods, sampling design.
Stearns teaches the theory beautifully and cannot teach you to run a
transect. Substitutes: local naturalist and master naturalist programs,
Audubon and land trust volunteer surveys, and community science projects
that provide real protocol training.

**Statistical computing.** Every biostatistics course above deliberately
omits software. You will need R. Learn it separately and deliberately, or
the epidemiology sequence will leave you able to interpret analyses you
cannot perform.

---

# Social Sciences and Professions

A catalogue of free, openly available university courses covering economics,
political science, sociology, anthropology and archaeology, law, business,
education, and geography and urban studies. Everything here is genuinely
free to use — either open courseware with no login, or a MOOC whose audit
track costs nothing. Certificates cost money; the learning does not.

**All hour estimates are approximate.** They assume you do the readings and
attempt the problem sets, not just watch. A "40 hrs" course is roughly a
semester at a brisk self-directed pace, not a semester of a real student's
time.

**Two things to check before committing to anything below.** First, whether
a course is *lecture-video-only* (you watch, there is nothing to submit) or
a *full course* (problem sets, exams, and — critically — solutions). Open
Yale is almost entirely the first kind with exams attached but no grading.
MIT OCW is usually the second, often without video. Coursera and edX audit
tracks vary: some lock graded assignments behind the paywall, leaving you
with videos and reading lists. Second, whether the site is still live —
several excellent MOOCs from 2013–2016 have been archived or pulled.

**On contested subjects.** Economics, political science, and sociology all
contain live disputes where the free-course landscape is lopsided. Where
that is true I say so and name work from more than one direction. That is
not false balance; it is the difference between learning a field and
learning one department's house style.

---

## 1. Economics

Economics has the richest free offering of any social science by a wide
margin. You can genuinely reach the level of a strong undergraduate major
without paying anything. The gap is economic history, where free material
is thin and scattered.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| The Economy 2.0: Microeconomics | CORE Econ (core-econ.org) | CORE team (Bowles, Carlin, and ~20 others) | 100 | The single best free intro sequence in existence, and it is not close. Full interactive textbook, embedded quizzes, real datasets, no paywall, no login required for the text. Builds from inequality, institutions, and strategic interaction *first*, then derives supply and demand late — the reverse of the standard course. If you have never seen economics, start here rather than with a lecture course. No video lectures, which is its one real weakness. |
| The Economy 2.0: Macroeconomics | CORE Econ | CORE team | 90 | Continues the above. Unemployment, inflation, monetary and fiscal policy, financial crises, and climate, all with data. Unit 17 (the Great Depression, golden age, and financial crisis) is the best free treatment of 20th-century macro history anywhere and is worth reading even if you use a different macro course. |
| Principles of Economics: Microeconomics | Marginal Revolution University | Tyler Cowen, Alex Tabarrok | 25 | Short, sharply-made videos with practice questions. Pedagogically excellent and unusually good at intuition. Written from an explicitly market-oriented, price-theory perspective — which is a real perspective worth learning, but pair it with CORE rather than treating either as neutral. Best single videos: the price-ceilings and price-floors sequence, and "The Tragedy of the Commons." |
| Principles of Economics: Macroeconomics | Marginal Revolution University | Tyler Cowen, Alex Tabarrok | 25 | Same format. The "Money and Inflation" and "Business Fluctuations" sequences are the strongest. Weaker on financial-crisis macro than CORE. |
| 14.01 Principles of Microeconomics | MIT OCW | Jonathan Gruber | 120 | The full-fat version: complete lecture video (Fall 2023 offering, also an older 14.01SC "Scholar" version built for self-study), problem sets, solutions, exams, exam solutions. Gruber is a genuinely great lecturer — dry, fast, relentlessly example-driven. This is the course to do if you want to be able to *solve* problems, not just follow arguments. The 14.01SC version has recitation videos and solution walkthroughs, which matters when you are alone. |
| 14.02 Principles of Macroeconomics | MIT OCW | MIT Economics (varies by offering) | 100 | Full lecture notes, problem sets with solutions, and exams. Most offerings have no video, so this is a reading-and-problems course. Rigorous, IS-LM-and-onward, conventional. Take it after CORE macro if you want the formal apparatus; skip it if you don't. |
| Principles of Economics | NPTEL / IIT Madras | Sabuj Kumar Mandal | 40 | Video lectures plus weekly assignments; free, exam optional and paid. Competent and complete but not distinctive. Worth knowing about as a fallback and for examples drawn from the Indian economy, a useful corrective to the all-American case base of everything above. CORE also publishes a less mathematical variant, *Economy, Society, and Public Policy*, if calculus is a barrier right now. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| ECON 159 Game Theory | Open Yale | Ben Polak | 40 | The best undergraduate game theory course available free, and one of the best lecture courses ever recorded in any subject. Full video, transcripts, problem sets, and exams — Open Yale posts these but nobody grades them. Polak teaches by running games live on the class, which survives translation to video better than you would expect. **Take lectures 1–3 even if you take nothing else here**: the strict-dominance and iterated-deletion material with the numbers game is a permanent upgrade to how you think. Lecture 19 on subgame perfection and the "ultimatum bargaining" sessions are the other standouts. |
| 14.12 Economic Applications of Game Theory | MIT OCW | Muhamet Yildiz | 90 | The formal counterpart to Polak. Recent offerings have full lecture video plus problem sets and solutions. Harder, more proof-oriented, less charming. Do this *after* ECON 159 if you want to actually use game theory in later work; the repeated-games and folk-theorem lectures are the payoff. |
| ECON 252 Financial Markets | Open Yale | Robert Shiller | 35 | Lecture-video-only in practice, with problem sets and exams posted. Shiller is a Nobelist writing while the 2008 crisis was still smoking (the 2011 offering is the one to take — it is substantially rewritten post-crisis). Not a technical course; it is an institutional and behavioral tour of what financial markets are actually for. **The guest lectures are the reason to be here** — David Swensen on institutional portfolio management, Carl Icahn on activist investing, and Maurice "Hank" Greenberg on insurance are each worth an afternoon on their own. The lectures on insurance and on behavioral finance are the strongest of Shiller's own. |
| ECON 251 Financial Theory | Open Yale | John Geanakoplos | 45 | The technical complement to ECON 252, and much less famous than it deserves. General equilibrium applied to finance: collateral, leverage, the leverage cycle. Geanakoplos called the mechanics of the 2008 crisis early and this course shows you why. Harder than Shiller — requires comfort with algebra and expectations. Take Shiller for the world, Geanakoplos for the machinery. |
| 14.32 Econometrics | MIT OCW | Joshua Angrist | 100 | Problem sets, data files, exams, and solutions; no video. Angrist's course is the modern causal-inference approach — regression as a tool for answering questions about the world, instrumental variables, natural experiments — rather than a tour of estimator properties. Materials are terse; use with the MRU course below or with *Mostly Harmless Econometrics*. |
| Mastering Econometrics | Marginal Revolution University | Joshua Angrist | 15 | Free video series, same author, same worldview, vastly more approachable. Covers randomized trials, regression, instrumental variables, regression discontinuity, and differences-in-differences with worked real studies. **If you take one thing from this whole catalogue, consider this**: it is the cheapest possible route to being able to read empirical social science critically. Pair with 14.32 for the problem sets it lacks. |
| 14.310x Data Analysis for Social Scientists | MITx (edX / MITx Online) | Esther Duflo, Sara Fisher Ellison | 100 | Free to audit. Probability, statistics, regression, and causal inference taught for social scientists, with R. Fully built for online delivery — this is not a recorded classroom, it is a designed course with exercises. The best free bridge between "I understand economics arguments" and "I can run and criticize an empirical study." |
| 14.41 Public Finance and Public Policy | MIT OCW | Jonathan Gruber | 90 | Recent offering has full lecture video plus problem sets, solutions, and exams. Taxation, social insurance, health care, Social Security, education, externalities — applied microeconomics on the questions people actually argue about. Gruber has policy commitments and does not hide them, but the analytical framework he teaches is standard and portable. The social insurance and tax incidence lectures are the core. |
| A Beginner's Guide to Irrational Behavior | Duke (Coursera) | Dan Ariely | 20 | Auditable. The most-watched free behavioral economics course. Entertaining and a good on-ramp. Two cautions: some of the specific studies discussed have replicated poorly, and Ariely's own research record has been publicly questioned. Take it for the *questions* it raises about the rational-agent model, not as a reference for particular findings. Cross-check anything you plan to rely on. |
| The Economics of Money and Banking | Columbia / Barnard (Coursera) | Perry Mehrling | 40 | Auditable. Idiosyncratic, difficult, and one of the most valuable free courses in economics. Mehrling teaches money as a hierarchy of balance sheets and payment promises rather than as a stock of stuff, which is how the plumbing actually works. **The lectures on the money view versus the economics view, and the sequence on the shadow banking system, are worth taking on their own.** Almost no assignments; this is video plus readings. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 14.73 The Challenge of World Poverty | MIT OCW | Abhijit Banerjee, Esther Duflo | 60 | Full lecture video, notes, assignments, and exams. Two Nobelists teaching the randomized-trial approach to poverty — education, health, microfinance, savings, corruption — one policy question at a time. **Lecture 3, "Social Experiments: Why and How?", is the single best short explanation of why randomization solves the problems it solves.** The best undergraduate development course, free or paid. |
| Foundations of Development Policy | MITx (edX / MITx Online) | Abhijit Banerjee, Esther Duflo | 90 | Free to audit. The structured online version of 14.73 with a full assessment track. Take this instead of 14.73 if you want exercises; take 14.73 if you want the live lecture experience. MITx's *Challenges of Global Poverty* is a third variant of the same material. |
| Political Economy and Economic Development | MITx | Benjamin Olken, Abhijit Banerjee | 90 | Free to audit. Institutions, corruption, clientelism, state capacity, conflict — the political side of why poor countries stay poor. Fills the gap that pure-RCT development courses leave. |
| Development Economics | Marginal Revolution University | Tyler Cowen, Alex Tabarrok | 20 | Free video. Growth theory, geography, institutions, trade. Broader and more macro than the MIT material, which is almost entirely micro and experimental. Useful as a deliberate counterweight — the "big institutions and growth" tradition versus the "small credible experiments" tradition is one of the genuine live disputes in the field, and you should hear both sides argued by their advocates. |
| Using Big Data to Solve Economic and Social Problems | Harvard (Opportunity Insights) | Raj Chetty | 30 | Lecture videos and slides posted publicly by Opportunity Insights, along with data and code. Intergenerational mobility, neighborhoods, education, race, health. This is the best free treatment of inequality as an empirical subject, and the mobility-by-neighborhood material is genuinely striking. Video plus materials; no graded work. |
| Great Economists: Classical Economics and its Forerunners | Marginal Revolution University | Tyler Cowen | 15 | Free video. Smith, Malthus, Ricardo, Mill, Marx, and the mercantilists, taken seriously as thinkers rather than as steps toward the present. The closest thing to a free history-of-economic-thought course. |

**The spine — Economics**

1. CORE, *The Economy 2.0: Microeconomics* — build the worldview first.
2. MIT 14.01 with Gruber — build the technique.
3. Open Yale ECON 159, Polak — game theory, the highest-leverage tool.
4. MRU *Mastering Econometrics*, then MIT 14.32 for the problem sets.
5. CORE macro, or MIT 14.02 if you want the formal version.
6. One applied capstone: 14.41 *Public Finance* if you lean policy,
   14.73 *World Poverty* if you lean development, ECON 252 *Financial
   Markets* if you lean finance.

**Overlaps resolved — Economics**

- *Intro micro:* CORE over MRU over Khan-style alternatives, as the primary
  text; MIT 14.01 as the problem-solving course alongside it. MRU loses as
  a sole intro because it is short and carries a definite ideological
  slant; CORE loses on video and on drill, which 14.01 supplies.
- *Game theory:* Polak over Yildiz. Yildiz is more rigorous but assumes
  more and teaches less well, so he is the second course, not the first.
  Stanford/UBC's Coursera *Game Theory* (Jackson, Leyton-Brown, Shoham) is
  a legitimate third pass with better mechanism design, but too compressed
  to start with.
- *Econometrics:* Angrist's MRU series over everything for a first pass;
  14.310x over 14.32 if you want an actual graded structure. 14.32 alone
  loses because it has no lectures.
- *Finance:* Shiller for institutions and behavior, Geanakoplos for theory.
  They are complements, not substitutes — do not pick one and think you
  have covered finance. MIT 15.401 (below, under Business) is the
  corporate-finance-toolkit version and is a third distinct thing.
- *Economic history:* genuinely thin. Nothing free is a proper course.
  CORE's historical units, PLSC 270 below, and MRU's *Great Economists*
  are the best available substitutes — treat this as a gap to fill with
  books, not courses.

---

## 2. Political Science

Strong at the political-philosophy end — three of the best lecture courses
ever filmed are here and all are free. Weaker on quantitative methods and
on comparative politics, where the free options are lecture slides without
lectures.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| PLSC 114 Introduction to Political Philosophy | Open Yale | Steven B. Smith | 40 | Full video, transcripts, reading list, exams. Socrates through Tocqueville, taught as a live argument about how to live rather than a survey. Smith is a superb close reader. **The lectures on Machiavelli's *Prince* (especially the "new modes and orders" lecture) and the two on Hobbes are the ones to take even if you take nothing else** — they permanently change how you read political rhetoric. Lecture-video-only in effect; no feedback. |
| Justice | Harvard (justiceharvard.org, also edX) | Michael J. Sandel | 25 | Twelve filmed episodes, free, plus reading lists and discussion guides at justiceharvard.org. The most watched university lecture course in the world, and it earns it. Utilitarianism, libertarianism, Kant, Rawls, Aristotle, argued against student objections in a packed hall. **Episode 1 ("The Moral Side of Murder") is the best single hour of introductory philosophy on film.** Sandel is a communitarian and argues for it in the final episodes; he is fair to opponents but he is not neutral, and you should read Nozick and Rawls directly rather than only through him. |
| PLSC 118 The Moral Foundations of Politics | Open Yale | Ian Shapiro | 35 | Full video, transcripts, midterm and final posted. Asks one question — what makes a government legitimate — and runs it through utilitarianism, Marxism, social contract theory, the anti-Enlightenment, and democratic theory. More systematic than Smith and more argumentative than Sandel; Shapiro takes positions and defends them. The Marxism lectures are unusually fair-minded, and the closing democratic-theory lectures are the payoff. |
| 17.20 Introduction to the American Political Process | MIT OCW | MIT Political Science | 50 | Complete lecture slides, readings, assignments, and exams; no video in the recent offerings. Institutions, elections, parties, media, public opinion, with a political-science-as-empirical-discipline framing rather than a civics framing. Solid and unromantic. Its weakness for a self-learner is that slides without lectures leave gaps. |
| American Government: Constitutional Foundations | HarvardX (edX) | Thomas E. Patterson | 20 | Free to audit; part of a four-course sequence (the others cover citizen participation, institutions, and policy). Actual designed online course with video and assessments, not a filmed classroom. Use this *with* MIT 17.20 — Patterson supplies the lectures 17.20 lacks, 17.20 supplies the rigor and readings Patterson lacks. |
| 17.50 Introduction to Comparative Politics | MIT OCW | MIT Political Science | 50 | Lecture slides, readings, recitation materials, assignments, exams. Why democracy emerges and survives; institutions and development; country cases. Slides-only, which hurts. It is nonetheless the best free comparative politics course, which tells you something about the state of the field's open offerings. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 17.42 Causes and Prevention of War | MIT OCW | Stephen Van Evera | 45 | Extraordinarily good lecture notes — Van Evera's are effectively transcripts, dense and argumentative, and better than most books on the subject. Readings, assignments, exams included; no video. Covers misperception, military doctrine, nationalism, religion, and the great-power cases. **The World War I lecture sequence (lectures 12–14) is the best short explanation of 1914 you will find in course form**, and the Peloponnesian War lecture is a superb piece of applied theory. |
| 17.40 American Foreign Policy: Past, Present, and Future | MIT OCW | MIT Political Science | 45 | Same house style: heavy lecture notes, readings, exams, no video. WWI and WWII, the Cold War, the Cuban missile crisis, Korea, Indochina, Iraq 2003, the war on terror. Consistently willing to render judgments and defend them, which makes it more useful than a neutral survey and means you should read the critics too. |
| Power and Politics in Today's World | Yale (public lecture series) | Ian Shapiro | 25 | A full Yale lecture course posted publicly as video. Covers the post-Cold War order, the decline of trade unions and mainstream parties, populism, inequality, and the crisis of democracy. Video only — no problem sets. More contemporary than anything else here; also more contestable, since it is one scholar's synthesis of very recent events. |
| 11.002J Making Public Policy | MIT OCW | MIT Urban Studies and Planning | 40 | Readings, assignments, and lecture materials on how policy actually gets made — agenda setting, interest groups, implementation, evaluation. Complements the economics-flavored policy courses (14.41) with the political-process side that economics courses systematically omit. |
| PLSC 270 Capitalism: Success, Crisis, and Reform | Open Yale | Douglas W. Rae | 40 | Full video, transcripts, reading list. Political economy taught through an evolutionary lens — firms as organisms, markets as selection environments. Smith, Marx, Malthus, Schumpeter, the joint-stock corporation, the role of the state in guaranteeing property and contract. **Lecture 16 on Braudel's "bell jar" and the lectures on the rise of the joint stock corporation are the standouts.** The best free bridge between political science and economics, and unusually even-handed about capitalism's merits and failures. |
| Model Thinking | Michigan (Coursera) | Scott E. Page | 25 | Auditable. Not a political science course strictly, but the best free training in the formal models that political science and sociology run on — Schelling segregation, tipping points, collective action, Markov processes, diffusion, Condorcet and voting rules. Videos plus quizzes. Take it early; it makes everything else sharper. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Central Challenges of American National Security, Strategy, and the Press | HarvardX (edX) | Graham Allison, David Sanger | 25 | Free to audit. Case-method treatment of nuclear crises, cyber conflict, and the intersection with journalism, taught by the author of *Essence of Decision* and the *New York Times*'s national security correspondent. Establishment-perspective by construction; read realist and restraint-school critics alongside it. |
| 14.15J / 6.207J Networks | MIT OCW | Daron Acemoglu, Asu Ozdaglar | 60 | Lecture notes, problem sets, and solutions. Graph theory, network games, contagion, learning and herding, social influence. Mathematically demanding but the payoff for understanding diffusion of information, protest cascades, and financial contagion is large. Pairs with Easley and Kleinberg's *Networks, Crowds, and Markets*, whose full text is free online. |

**The spine — Political Science**

1. Sandel's *Justice* — the fastest possible on-ramp.
2. Open Yale PLSC 114, Smith — the canon, read closely.
3. Open Yale PLSC 118, Shapiro — the canon, argued about.
4. MIT 17.20 plus HarvardX *Constitutional Foundations* together — the
   American institutions requirement, one supplying what the other lacks.
5. MIT 17.42, Van Evera — international relations, and the best writing
   in the division.
6. Open Yale PLSC 270, Rae — political economy capstone.

**Overlaps resolved — Political Science**

- *Political philosophy:* all three of Sandel, Smith, and Shapiro are worth
  doing, and they genuinely differ — Sandel is dialectical and popular,
  Smith is textual and historical, Shapiro is systematic and takes sides.
  If forced to one: Smith, because the close reading transfers. Sandel
  loses on depth; Shapiro loses on accessibility as a first course.
- *American politics:* MIT 17.20 plus Patterson beats either alone. Neither
  standalone course is adequate — 17.20 has no lectures, Patterson has
  little rigor.
- *International relations:* Van Evera's 17.42 over 17.40 if you want
  theory, 17.40 if you want the American case history. Both are the same
  department's viewpoint; the free landscape has no serious constructivist
  or critical-IR alternative, which is a real gap — fill it with reading.
- *Political economy:* Rae's PLSC 270 over MRU's development material for
  breadth, and vice versa for growth mechanics.

---

## 3. Sociology

Thin, and you should know that going in. One outstanding theory course and
then a scattering of methods and topic courses, mostly from outside the
usual elite-American-university pipeline. There is no free equivalent of
Gruber's 14.01 for sociology.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Introduction to Sociology | NPTEL / IIT Kanpur | IIT Kanpur Humanities and Social Sciences | 40 | Video lectures plus weekly assignments, free. Competent, conventional, and covers what an intro course should — culture, socialization, institutions, stratification, change. Indian examples throughout, which is a feature rather than a limitation given how parochially American most sociology teaching is. This is the best free *intro* course, mostly by default. |
| Introduction to Sociology (OpenStax) | OpenStax / Rice | OpenStax authors | 40 | Not a course — a free, peer-reviewed, openly-licensed textbook with instructor resources. Better written than most commercial intro texts. Use it as the reading spine underneath whichever video course you pick. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| SOCY 151 Foundations of Modern Social Theory | Open Yale | Iván Szelényi | 40 | The best free sociology course by a wide margin. Full video, transcripts, reading list, exams. Hobbes, Locke, Rousseau, Smith, Marx, Durkheim, Weber, Freud, and the Frankfurt School, taught by someone who grew up under and studied actually-existing socialism and is unsentimental about all of it. **The Weber lectures — especially on the Protestant ethic and on bureaucracy and legitimate domination — are the ones to take even if you skip everything else.** Lecture-video-only in practice. |
| Social Norms, Social Change I and II | Penn / UNICEF (Coursera) | Cristina Bicchieri | 25 | Auditable. What a social norm actually is, how to measure one, and how to change one — with real field applications (open defecation, child marriage, female genital cutting). Rigorous in a way sociology courses often are not, because Bicchieri comes at norms from game theory and philosophy. Quizzes included in audit; the strongest free methods-adjacent course in this division. |
| Quantitative Methods | University of Amsterdam (Coursera) | Annemarie Zand Scholten | 25 | Auditable. Research design, measurement, validity, sampling, and inference for social scientists who are not economists. Clear and well-produced. Pair with the qualitative course below — most sociology programmes require both and most free catalogues offer neither. |
| Qualitative Research Methods | University of Amsterdam (Coursera) | Gerben Moerman | 25 | Auditable. Interviewing, participant observation, coding, grounded theory, and the epistemological arguments behind them. The only decent free qualitative-methods course I can point to, which is itself a finding about the state of open education. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| MCDB 150 Global Problems of Population Growth | Open Yale | Robert Wyman | 35 | Full video and transcripts. Nominally biology; substantively demography and social change — fertility decline, family structure, contraception, gender, religion, and the politics of population policy. Enormous historical and comparative range. Wyman has strong views on some contested questions (particularly around population policy and religion); the empirical material is excellent and the editorializing is easy to identify and discount. |
| Sociological Perspectives on Modernity | NPTEL / IIT Guwahati | Sambit Mallick | 30 | Video plus assignments, free. Modernity, rationalization, colonialism, and their critics, with substantial attention to non-Western modernity — a perspective almost entirely absent from the Yale and MIT offerings. Take it after SOCY 151 as a deliberate corrective. |
| Sociology of Development | NPTEL / IIT Guwahati | Sambit Mallick | 30 | Video plus assignments. Development theory from modernization through dependency and world-systems to post-development. This is the sociological tradition that economics courses on development mostly ignore; hearing both is the point. |
| Using Big Data to Solve Economic and Social Problems | Harvard | Raj Chetty | 30 | Listed under Economics above; it is equally a course on stratification and mobility, and it is the best free quantitative treatment of inequality available. Listed here so you do not miss it. |

**The spine — Sociology**

1. OpenStax *Introduction to Sociology* as reading, alongside the NPTEL
   intro lectures.
2. Open Yale SOCY 151, Szelényi — the theory canon.
3. Amsterdam *Quantitative Methods* and *Qualitative Research Methods*.
4. Bicchieri, *Social Norms, Social Change I* — norms done rigorously.
5. Chetty, *Using Big Data* — stratification with real data.
6. NPTEL *Sociological Perspectives on Modernity* — the non-Western
   corrective.

**Overlaps resolved — Sociology**

- *Theory:* SOCY 151 wins outright; nothing else is close. Its blind spot
  is post-1970 theory — no Bourdieu, Foucault, or Goffman to speak of —
  and no free course fills that. Books, not courses.
- *Intro:* the NPTEL course wins on being complete and free with
  assignments; OpenStax wins as a text. Use both, neither alone.
- *Inequality:* Chetty over any sociology-department offering, because the
  free sociology options on inequality are essentially non-existent. This
  gives you the quantitative-mobility literature and none of the
  qualitative or theoretical tradition — a real limitation to be aware of.

---

## 4. Anthropology and Archaeology

Small but decent. MIT's anthropology department publishes real syllabi with
real reading lists; the archaeology material is older but sound. Human
evolution is the best-served corner.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 21A.00 Introduction to Anthropology | MIT OCW | MIT Anthropology | 40 | Recent offering (Spring 2022) with full syllabus, readings, assignments, and exams; no video. What sets it apart is the reading list — actual ethnographies, current, well chosen. Treat it as a guided reading course rather than a lecture course, because that is what it is. |
| 21A.01 How Culture Works | MIT OCW | MIT Anthropology | 40 | Syllabus, readings, assignments. Narrower and sharper than 21A.00: what the concept of culture does and whether it holds up. Good second course, or a substitute if you find 21A.00's survey structure unmotivating. |
| Human Evolution: Past and Future | Wisconsin–Madison (Coursera) | John Hawks | 15 | Auditable. Hominin fossil record, ancient DNA, the Neanderthal and Denisovan story, and what evolution is doing to humans now. Hawks is an active researcher who writes for the public unusually well. Video plus quizzes. Short, current, and the clear best option for human evolution. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 3.986 The Human Past: Introduction to Archaeology | MIT OCW | Dorothy Hosler | 40 | Lecture notes, readings, assignments, study materials. Comparative treatment of the origins of agriculture and the rise of early states in the Near East and Mesoamerica. Taught out of Materials Science, so unusually strong on the physical evidence — what pots and metals and residues actually tell you. Older (2006) but archaeology's core methods have not moved as fast as its findings. |
| 3.985 Archaeological Science | MIT OCW | MIT Materials Science and Engineering | 35 | The laboratory-methods companion: dating techniques, materials characterization, provenance studies, what you can and cannot infer from an artifact. Notes and assignments, no video. Take it if you want to be able to evaluate archaeological claims rather than just absorb them. |
| Archaeology's Dirty Little Secrets | Brown (Coursera) | Susan Alcock | 15 | A genuinely delightful course about how archaeology actually works, including its ethics, its politics, and its relationship with looting and with the countries whose past it excavates. **Check availability before planning around it** — it has been intermittently archived, and I would rate it as the least reliably accessible item in this catalogue. |
| MCDB 150 Global Problems of Population Growth | Open Yale | Robert Wyman | 35 | Listed under Sociology; the material on kinship, marriage systems, and fertility across societies is substantively anthropological and better than anything else free on those topics. |

**The spine — Anthropology and Archaeology**

1. MIT 21A.00 as a guided reading course — the ethnographies are the point.
2. Hawks, *Human Evolution: Past and Future* — biological anthropology.
3. MIT 3.986 *The Human Past* — archaeology proper.
4. MIT 21A.01 *How Culture Works* — the concept, interrogated.
5. Optional: MIT 3.985 if you want the science of evidence.

**Overlaps resolved — Anthropology and Archaeology**

- *Cultural anthropology:* 21A.00 over 21A.01 as a first course, purely on
  coverage; 21A.01 is the better course if you already know the field
  exists. Neither has video, and there is no good free lectured cultural
  anthropology course — this is the division's biggest hole.
- *Human evolution:* Hawks wins uncontested. Nothing else free is current
  on ancient DNA, which is the part of the field that has changed most.
- *Archaeology:* 3.986 over Alcock's Brown course for substance; Alcock
  over 3.986 for enjoyment and for the ethics material. Alcock loses on
  reliability of access.

---

## 5. Law

**Be honest with yourself here: free legal education is thin, and what
exists is unrepresentative.** Law schools do not open-license their
curricula the way engineering and economics faculties do. What you can get
free is: two or three excellent single-subject courses from Harvard, one
good American-law survey from Penn, a scattering of international law from
European universities, and free casebooks. What you cannot get free is a
systematic sequence in contracts, torts, property, civil procedure, and
criminal law — the actual first year. Do not mistake the courses below for
a legal education. They are enough to read a Supreme Court opinion
intelligently and to understand what lawyers are arguing about, which is a
worthwhile goal in itself.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| An Introduction to American Law | Penn (Coursera) | Penn Law faculty, including Kermit Roosevelt, Tom Baker, Shyam Balganesh, Cary Coglianese, Anita Allen, Stephen Burbank | 20 | Auditable. Six short modules — tort, contract, property, constitutional, criminal, and civil procedure — each by a specialist. Exactly the right shape for someone who wants to know what the fields *are* before deciding whether to go deeper. Shallow by construction; that is the deal. The tort law module (Baker) and the constitutional law module (Roosevelt) are the strongest. |
| Justice | Harvard | Michael J. Sandel | 25 | Listed under Political Science. It is also, functionally, the best free introduction to legal and moral reasoning available — the affirmative action, same-sex marriage, and conscription discussions are argued the way legal questions are argued. |
| Constitution 101 | National Constitution Center (with Khan Academy) | Jeffrey Rosen and a bipartisan drafting team | 30 | Not a university course, and included with that caveat. Fifteen modules covering the constitutional text, structure, and rights, with primary documents and — unusually and valuably — paired essays from a self-identified progressive and a self-identified conservative scholar on each contested clause. **For genuinely even-handed constitutional material this is the best free resource that exists**, precisely because the disagreement is built into the design rather than papered over. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| CopyrightX lectures | Harvard Law / Berkman Klein (copyx.org) | William Fisher | 30 | The full recorded lecture series is free and openly licensed at copyx.org and on YouTube, along with the reading materials and Fisher's remarkable concept maps. The live twelve-week course with seminars is also free but admission is selective and applications close in December for the January start. **The lecture on fair use and the sequence on the subject matter and scope of copyright are outstanding** — genuinely law-school-grade teaching, not a popularization. The best free law course in existence, full stop. |
| Contract Law: From Trust to Promise to Contract | HarvardX (edX) | Charles Fried | 25 | Free to audit. Formation, consideration, remedies, third-party rights, taught by a former Solicitor General and a major contracts theorist. Fried has a distinct jurisprudential position — contract as promise — and teaches from it openly, which makes the course more interesting than a neutral survey and means you should read the reliance-theory and efficient-breach critics. Fried died in 2024; the course materials remain. |
| Intellectual Property: Law and the Information Society | Duke (Center for the Study of the Public Domain) | James Boyle, Jennifer Jenkins | 60 | Not a course — a complete, free, openly-licensed casebook plus a free statutory supplement, both regularly updated. This is the substance a course would deliver, in the form law students actually use. Boyle and Jenkins write with unusual clarity and a definite public-domain-friendly viewpoint. Pair with CopyrightX. |
| International Law in Action: A Guide to the International Courts and Tribunals in The Hague | Leiden University (Coursera) | Leiden Law faculty | 20 | Auditable. The ICJ, ICC, and the ad hoc tribunals — what they actually do, how cases reach them, and what they can and cannot accomplish. Filmed partly on location. A follow-on course covers investigating and prosecuting international crimes. Descriptive and institutional rather than theoretical. |
| Introduction to International Criminal Law | Case Western Reserve (Coursera) | Michael Scharf | 20 | Auditable. Nuremberg through the ICC, with substantial attention to the practical questions of jurisdiction, immunity, and prosecutorial strategy. Scharf has actually done this work at the tribunals and the war stories are the value. |

**The spine — Law**

1. Penn, *An Introduction to American Law* — the map.
2. NCC *Constitution 101* — constitutional law, with the disagreements
   built in.
3. Harvard *CopyrightX* — one field done properly and deeply.
4. Boyle and Jenkins, *Intellectual Property* casebook alongside it.
5. Harvard *Contract Law*, Fried — a second field, done properly.
6. Leiden, *International Law in Action* — the international dimension.

**Overlaps resolved — Law**

- *Intro:* Penn's survey over anything else, because nothing else free
  covers the whole map. It loses on depth to every course below it.
- *Constitutional law:* the NCC's *Constitution 101* over HarvardX's
  *American Government: Constitutional Foundations* for law specifically —
  Patterson's course is political science about the Constitution, the
  NCC's is doctrine and text. There is no free course taught by a
  constitutional law professor covering the standard doctrinal syllabus,
  and I am not going to pretend otherwise.
- *Copyright and IP:* CopyrightX over everything. The Duke casebook is a
  complement, not a rival — Fisher lectures, Boyle and Jenkins supply the
  cases.
- *International law:* Leiden for institutions, Case Western for criminal
  law specifically. Neither covers treaty law, the law of the sea, or
  trade law in any depth. Another honest gap.

---

## 6. Business and Management

**Also thinner than it looks.** There is an enormous volume of free
business content online and most of it is not university teaching. The
genuine open-courseware material clusters at MIT Sloan, and much of it is
old — good bones, dated cases. Wharton's four foundation courses on
Coursera are the best modern free offering and are fully auditable. Where
free business education is weakest is exactly where business school is
supposedly most valuable: strategy, organizational behavior, and the case
method itself, which does not survive being made free.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Introduction to Financial Accounting | Wharton (Coursera) | Brian Bushee | 20 | Auditable. The best free accounting course. Bushee teaches you to read a balance sheet, income statement, and cash flow statement and to detect when something is off, rather than to prepare entries. Well-produced, quizzes included. Start here. |
| 15.501 Introduction to Financial and Managerial Accounting | MIT OCW | MIT Sloan | 40 | Lecture notes, problem sets, cases, exams, solutions. Explicitly written from the reader's viewpoint rather than the preparer's. Older (2004) but accounting fundamentals age well. Take it after Bushee if you want problems to work, which Bushee's audit track may not fully give you. |
| Introduction to Marketing | Wharton (Coursera) | Barbara Kahn, Peter Fader, David Bell (varies by offering) | 15 | Auditable. Branding, customer centricity, go-to-market, and the customer lifetime value material that is Wharton's real specialty. **The customer-lifetime-value and customer-centricity sections are the ones with actual analytical content**; the branding material is thinner. |
| Introduction to Operations Management | Wharton (Coursera) | Christian Terwiesch | 15 | Auditable. Process analysis, bottlenecks, Little's Law, quality, inventory. Terwiesch is excellent and the material is genuinely quantitative — this is the most rigorous of the four Wharton foundation courses and the most transferable outside business. |
| Introduction to Corporate Finance | Wharton (Coursera) | Michael R. Roberts | 15 | Auditable. Time value of money, discounting, NPV, interest rates. Short and mechanical, in a good way. It does not cover capital structure or valuation in depth — for that, go to MIT 15.401. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 15.401 Finance Theory I | MIT OCW | Andrew Lo | 60 | Full video lectures with slides, plus problem sets and solutions. This is the serious one: present value, fixed income, portfolio theory, CAPM, options, and capital budgeting, taught by a first-rate financial economist. **The portfolio theory and CAPM lecture sequence is the clearest free treatment of that material anywhere.** Take it after the Wharton finance course, not instead of it. |
| 15.665 Power and Negotiation | MIT OCW | MIT Sloan | 35 | Syllabus, readings, lecture notes, and — most usefully — the negotiation exercise structures. Reading-based; you will need a partner to run the exercises, which is the course's real limitation for a solo learner. Strong on the theory of power and on the distributive/integrative distinction. |
| Successful Negotiation: Essential Strategies and Skills | Michigan (Coursera) | George Siedel | 20 | Auditable. Video-based and designed to be done alone, which is exactly where 15.665 fails. Planning, psychology, the legal frame around agreements, and a full worked negotiation. Take this one if you are learning by yourself; take 15.665 if you have a study partner. |
| 15.390 New Enterprises | MIT OCW | Bill Aulet | 45 | Syllabus, assignments, and the structured 24-step framework that became *Disciplined Entrepreneurship*. The most systematic free entrepreneurship course — market segmentation, beachhead selection, customer personas, unit economics — as opposed to inspirational founder talks. No video in the OCW version. |
| How to Start a Startup (CS183B) | Stanford | Sam Altman, with Paul Graham, Peter Thiel, Marc Andreessen, Ben Horowitz, and others | 20 | Full video lecture series, free. Twenty guest lectures from practitioners. Wildly uneven by design and heavily survivorship-biased — these are the people it worked for — but several individual lectures are excellent. **Altman's "Ideas, Products, Teams and Execution" opener and Paul Graham's "Before the Startup" are the two worth watching regardless.** Treat as primary-source testimony, not as instruction. |
| 15.S21 Nuts and Bolts of Business Plans | MIT OCW | Joe Hadzima | 15 | Full session videos with slides. Short, practical, unglamorous: what actually goes in a plan, how the financial projections work, how founders get the legal and equity structure wrong. A good complement to 15.390's strategy focus. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Inspiring Leadership through Emotional Intelligence | Case Western Reserve (Coursera) | Richard Boyatzis | 20 | Auditable. The most substantive free leadership course, grounded in Boyatzis's intentional change theory and the underlying neuroscience of resonant versus dissonant leadership. Considerably better than the genre average, which is a low bar. Some of the underlying emotional-intelligence literature is contested; the coaching material stands on its own. |
| Financial Markets | Yale (Coursera) | Robert Shiller | 30 | Auditable. The Coursera repackaging of Open Yale ECON 252, updated, with quizzes. Take the Open Yale version for the guest lectures and the full-length treatment; take this version if you want a graded structure and a tighter edit. |

**The spine — Business and Management**

1. Wharton, *Introduction to Financial Accounting* (Bushee) — read the
   statements first, everything else depends on it.
2. Wharton, *Introduction to Operations Management* (Terwiesch) — the most
   rigorous and most transferable of the foundation courses.
3. MIT 15.401 *Finance Theory I* (Lo) — the real finance course.
4. Michigan, *Successful Negotiation* (Siedel) — the highest-return single
   skill on this list.
5. MIT 15.390 *New Enterprises* (Aulet) — building something.
6. Wharton, *Introduction to Marketing* — customer economics.

**Overlaps resolved — Business and Management**

- *Accounting:* Bushee over MIT 15.501 as the primary, on production
  quality and currency; 15.501 supplies problem sets Bushee's free track
  may not.
- *Finance:* MIT 15.401 (Lo) over Wharton's corporate finance course on
  depth, and over Shiller's ECON 252 on technique — but Shiller and Lo
  are answering different questions and both are worth doing. Wharton's
  loses on being a four-week introduction.
- *Negotiation:* Siedel over MIT 15.665 for a solo learner; the reverse if
  you have a partner. This is the clearest case in the catalogue where
  format, not quality, decides.
- *Entrepreneurship:* Aulet's 15.390 over Stanford CS183B for method;
  CS183B over 15.390 for texture and honesty about what the work is like.
  Neither is a substitute for the other.
- *Strategy and organizational behavior:* no good free option exists. This
  is the largest single hole in the business division and I would rather
  say so than list a content-marketing course.

---

## 7. Education

Small division, dominated by one enormously popular course that happens to
deserve its popularity. The learning-science end is well served; teaching
methods and education policy much less so.

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Learning How to Learn | McMaster / UC San Diego (Coursera) | Barbara Oakley, Terrence Sejnowski | 15 | Auditable. The most-enrolled online course in the world. Focused versus diffuse modes, chunking, spaced repetition, interleaving, procrastination, and testing effects — the actual cognitive science of studying, delivered in four weeks. **Take this before anything else in this entire catalogue.** It will change how you approach the other sixty courses. The production is homely; ignore that. |
| Uncommon Sense Teaching | Deep Teaching Solutions / UC San Diego (Coursera) | Barbara Oakley, Beth Rogowsky, Terrence Sejnowski | 15 | Auditable. The instructor-facing counterpart: working memory limits, retrieval practice, why direct instruction beats pure discovery for novices, how to handle mixed-ability rooms. Better evidence-grounding than most teacher-training material. |
| Leaders of Learning | HarvardX (edX) | Richard Elmore | 20 | Free to audit. Not about classroom technique — about how learning organizations are structured, and the hierarchical/distributed and individual/collective axes that Elmore uses to classify educational systems. The most intellectually serious free education course. Elmore died in 2021; the course remains available. |
| 5.95J Teaching College-Level Science and Engineering | MIT OCW | Janet Rankin | 20 | Complete syllabus, readings, and assignments for MIT's teaching-certificate seminar. Lesson design, active learning, assessment, and the specific problem of teaching technical material. Reading-based, no video. Short and unusually practical. |
| How to Learn Math: For Students | Stanford Online | Jo Boaler | 10 | Free, self-paced, always open. Mathematical mindset, the myth of the "math person", multiple representations, and the case against speed as a proxy for ability. Boaler's broader claims about tracking and about de-tracking curricula are actively contested in the research literature and in policy; the specific study-habit material is sound and useful. Know that you are hearing one side of a live argument. |
| 11.125 Introduction to Education: Understanding and Evaluating Education | MIT OCW | MIT Urban Studies and Planning | 30 | Syllabus, readings, and assignments built around classroom observation — curriculum design, standards, student misconceptions, assessment, the digital divide. The observation assignments assume access to a real school, which you will not have; the readings stand alone. |

**The spine — Education**

1. *Learning How to Learn* — do this first, in week one, before anything.
2. *Uncommon Sense Teaching* — the same science from the other side.
3. HarvardX *Leaders of Learning* — systems and institutions.
4. MIT 5.95J — how to actually run a class session.

**Overlaps resolved — Education**

- *Learning science:* Oakley's two courses are complements — the first is
  for you as a learner, the second for you as a teacher. Boaler's course
  overlaps the first on mindset and loses on breadth and on contestedness.
- *Education policy and institutions:* Elmore's course wins by default;
  MIT 11.125 is a reading list rather than a course. There is no good free
  course on education economics or on international comparison — the
  closest is the education material inside MIT 14.41 and 14.73.

---

## 8. Geography and Urban Studies

Split personality. GIS is exceptionally well served free — Penn State has
open-licensed a large portion of its professional geospatial curriculum,
which is a genuinely unusual act of generosity. Urban planning is decently
served by MIT. **Human geography as a discipline is close to absent from
free offerings**, and I have not padded this section to hide that.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 11.001J Introduction to Urban Design and Development | MIT OCW | MIT Urban Studies and Planning | 40 | Lecture notes, readings, assignments. How cities, suburbs, and metros take the shape they do, and how physical, social, political, and economic forces interact — Boston as the running case. Older (2006) but the structural analysis holds. The best free entry point to urban studies. |
| RES.STR-001 Geographic Information System (GIS) Tutorial | MIT OCW | MIT Libraries GIS staff | 10 | A three-level hands-on tutorial (introduction and mapping, then analysis, then more advanced work) with data provided. The fastest route from zero to making a real map. Do this before any longer GIS course. |
| Penn State open geospatial courseware | Penn State (e-education.psu.edu, geospatial.psu.edu) | Penn State Geography faculty | varies | Penn State has published substantial portions of 30-plus geospatial courses openly, covering GIS, cartography, remote sensing, geospatial intelligence, spatial data science, and programming. Full text, figures, and exercises; no grading, no instructor. **This is the largest free geography resource anywhere and most people do not know it exists.** Start with the foundational material on the nature of geographic information before the software-specific courses. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| GEOG 483 Problem Solving with GIS | Penn State (open courseware) | Penn State Geography | 40 | Vector and raster analysis, spatial and attribute queries, overlay, surface interpolation, and a project structure. Professional-programme material published openly. The most complete free GIS *course* as opposed to tutorial. |
| 11.205 Introduction to Spatial Analysis | MIT OCW | MIT Urban Studies and Planning | 35 | Recent offering with labs, readings, and assignments. Spatial data for planning questions specifically — where the analysis serves a policy argument rather than existing for its own sake. Complements the Penn State material, which is more technique-focused. |
| 11.520 A Workshop on Geographic Information Systems | MIT OCW | Joseph Ferreira | 35 | Lab exercises with data, plus lecture notes, oriented to planning and public management uses. Dated software references (2005) — the concepts transfer, the click-paths do not. Take it for the framing of what GIS is *for* in a planning agency, and do the actual software work in the Penn State or MIT tutorial materials. |
| Cities are Back in Town: Urban Sociology for a Globalizing Urban World | Sciences Po (Coursera) | Patrick Le Galès | 20 | Auditable. European urban sociology and political economy — governance, globalization, inequality, and the comparative politics of cities. A useful counterweight to the almost exclusively American case base of the MIT material. |
| The Age of Sustainable Development | Columbia (Coursera / SDG Academy) | Jeffrey Sachs | 30 | Auditable. Geography, development, health, energy, food systems, and urbanization at global scale — the closest free offering to a human geography course, though it is really development studies. Sachs argues strongly for a particular interventionist development agenda and has prominent critics (William Easterly and Angus Deaton most notably); read the criticism alongside. **The lectures on the geography of poverty and on urbanization are the ones most worth taking.** |

**The spine — Geography and Urban Studies**

1. MIT RES.STR-001 GIS Tutorial — hands on a map in a weekend.
2. Penn State foundational geospatial courseware — what geographic
   information actually is.
3. Penn State GEOG 483 — real analysis, real project.
4. MIT 11.001J — urban form and development.
5. MIT 11.205 — spatial analysis applied to planning questions.
6. Sciences Po, *Cities are Back in Town* — the comparative and political
   dimension.

**Overlaps resolved — Geography and Urban Studies**

- *GIS:* Penn State over MIT for technique and currency; MIT 11.205 over
  both for applying it to a planning question. MIT 11.520 loses on age —
  keep it for the framing chapters only.
- *Urban studies:* MIT 11.001J over Sciences Po for fundamentals, Sciences
  Po over MIT for anything outside the United States. Both are needed.
- *Human geography:* no adequate free course exists. Sachs's course and
  the Penn State foundational material together approximate a fraction of
  one. If human geography is your target field, plan on books and on
  paid or enrolled coursework — this is the thinnest area in the entire
  catalogue.

---

## Cross-cutting notes

**Five courses to do first, whatever your eventual concentration.**
*Learning How to Learn* (Oakley), *Justice* (Sandel), *Model Thinking*
(Page), *Mastering Econometrics* (Angrist), and CORE's *The Economy 2.0*.
Between them they give you study technique, moral reasoning, formal
models, causal inference, and an empirical picture of how economies work.
Everything else in this catalogue reads better afterwards.

**Where the free ecosystem is strongest:** economics, by a distance, then
political philosophy, then GIS. In each of these you can reach real
competence without paying anything.

**Where it is genuinely weak, and you should plan around it:** the law
school first-year curriculum, business strategy and organizational
behavior, human geography, post-1970 social theory, comparative politics
with actual lectures, and economic history. In those areas free courses
will get you oriented and no further.

**On political balance.** Economics here leans toward the empirical,
policy-oriented American mainstream, with MRU providing a market-oriented
counterweight and CORE a more institutionalist one; there is no free
course from a Marxian, Austrian, or post-Keynesian department worth
listing, and you should know that absence is a real distortion. Political
science here is stronger on liberal and realist traditions than on
conservative, critical, or non-Western ones — Van Evera and Sandel are
worth reading with critics in hand. The National Constitution Center's
paired-essay design is the only resource in this catalogue that builds
disagreement into its structure, which is why it is recommended despite
not being a university course.

**A note on Coursera and edX audit tracks.** "Free to audit" reliably means
video and readings. It sometimes means quizzes. It rarely means graded
assignments, and it never means a certificate. Several courses have also
moved between platforms or been retired since their launch. Check each one
before building a schedule around it.

---

# Humanities

All hour figures are rough — they count lecture-watching plus a realistic
amount of reading, not the full workload a matriculated student would carry.
Treat them as order-of-magnitude.

One structural warning before anything else. Almost every great free
humanities course is **lecture-video-only**. Open Yale Courses gives you
video, transcripts, and a syllabus — it does not give you graded work, and
in most cases it does not give you the books. The reading is on you, and in
the humanities the reading *is* the course. A history lecture course without
the primary sources is entertainment. Budget accordingly: for most of what
follows, plan roughly two hours of reading per hour of lecture, and buy or
library-borrow the texts.

MIT OpenCourseWare inverts this. Most MIT humanities courses have **no
video at all** but do have full syllabi, reading lists, essay prompts, and
sometimes graded problem sets. They are blueprints, not lectures. Used
correctly — as a reading list plus assignment schedule to hold yourself to —
they are more valuable than they look.

---

## History

Free history is the strongest division here for Europe and America, and
genuinely weak everywhere else. Read the gap notes at the end before you
plan around it.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| HIST 202 European Civilization, 1648–1945 | Yale (Open Yale Courses) | John Merriman | ~45 | The single best free history survey in existence. Merriman is a social historian with a stand-up comic's timing, and he is unashamedly interested in ordinary people rather than treaties. Lecture-video-only with transcripts and a syllabus; readings are standard trade books you must source. **Standout lectures worth hearing alone:** the lecture on the Dreyfus Affair, and the two on the origins of WWI — he demolishes the "sleepwalkers" cliché with more care than most books. |
| CLCV 205 Introduction to Ancient Greek History | Yale (OYC) | Donald Kagan | ~40 | Kagan is the eminent Peloponnesian War scholar and this is his life's argument compressed. Old-fashioned political-military history, openly so, and slightly conservative in framing — take it for the narrative command, supplement elsewhere for social and gender history. Video, transcripts, syllabus. Assumes Herodotus and Thucydides alongside. **Standout:** the lectures on the origins of the polis, and anything he says about Thucydides. |
| HIST 116 The American Revolution | Yale (OYC) | Joanne Freeman | ~35 | Freeman is the best pure lecturer in the OYC catalogue — narrative drive without loss of rigour, and unusually good on political culture and honour. Video-only. **Standout:** her lectures on the Constitutional Convention, and the one on why the Revolution was not inevitable. |
| HIST 119 The Civil War and Reconstruction Era, 1845–1877 | Yale (OYC) | David Blight | ~40 | Blight is the leading historian of Civil War memory and this course is as much about how Americans have *told* the war as about the war. Video-only. **Standout:** the final lectures on Reconstruction's collapse and on memory — arguably the two most important hours of American history lecturing available free anywhere. Take them even if you skip the rest. |
| Chinese Thought / ChinaX (multi-part) | HarvardX (edX) | Peter Bol, William Kirby | ~60 across parts | The only serious free survey of Chinese history from antiquity to the present. Auditable free; certificate paid. Modular, so you can take the Tang–Song parts and stop. Bol on intellectual history is the stronger half; Kirby carries the modern period. Includes readings and quizzes in audit mode, though graded elements may be certificate-gated. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| HIST 210 The Early Middle Ages, 284–1000 | Yale (OYC) | Paul Freedman | ~35 | The best introduction to the period in any medium, free or paid. Freedman treats the "fall of Rome" as a genuinely open historiographical question rather than a settled story, and gives Byzantium and the early Islamic conquests real weight instead of a paragraph. Video, transcripts, syllabus. **Standout:** Lecture 8, "Survival in the East," on why Byzantium did not fall — worth an hour on its own; also the lectures on the rise of Islam, which are more even-handed than most Western medieval surveys manage. |
| HIST 251 Early Modern England: Politics, Religion, and Society under the Tudors and Stuarts | Yale (OYC) | Keith Wrightson | ~35 | Wrightson is a social historian of enormous care, and this is the most methodologically instructive course in the OYC history set — you watch a historian reason from parish records rather than declaim. Slower than Merriman; more rewarding if you want to learn the craft. Video-only. **Standout:** the lectures on the social structure of Tudor England, and on the causes of the Civil War. |
| HIST 276 France Since 1871 | Yale (OYC) | John Merriman | ~35 | Merriman again, on his home turf. Deeper than HIST 202 on France specifically; overlapping, so take it *after* rather than instead. **Standout:** the Vichy lectures, which are unusually unsentimental. |
| AFAM 162 African American History: From Emancipation to the Present | Yale (OYC) | Jonathan Holloway | ~35 | Excellent, and the natural continuation of Blight. Holloway is strong on intellectual history — Washington, Du Bois, Wells-Barnett, Garvey — and on the tension between accommodation and confrontation. Video, transcripts. Recorded 2010, so nothing after that. **Standout:** the Du Bois/Washington lectures. |
| HIST 234 Epidemics in Western Society Since 1600 | Yale (OYC) | Frank Snowden | ~35 | A thematic history that doubles as an unusually good introduction to how social, economic, and scientific history interlock. Post-2020 this course found a second audience for obvious reasons. Video-only. **Standout:** the plague lectures and the one on cholera and the nineteenth-century city. |
| 21H.301 The Ancient World: Greece | MIT OCW | — | ~40 | **No video.** Syllabus, reading list, essay assignments. Its value is as a structured primary-source reading program in Greek history — pair it with Kagan's lectures and you have something close to a real course, with Kagan supplying the narrative and MIT supplying the written work. |
| 21H.302 / 21H.132 The Ancient World: Rome | MIT OCW | — | ~40 | **No video.** Same logic. Two OCW versions exist (an older 21H.302 and a 2017 21H.132); take the newer one for the better reading list. There is no free Roman-history lecture course of Kagan's quality, which is a real hole — this is the closest substitute. |
| Islamic Societies of the Middle East and North Africa: Religion, History, and Culture | MIT OCW | — | ~35 | **No video**, syllabus and readings only. I am not confident of the course number, so use the title to find it. Listed because free Middle East history is thin enough that a good reading list counts. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Historiography — no good free course exists | — | — | — | Stated plainly rather than padded. There is no open historiography course worth your time. Build it yourself from three sources: Blight's HIST 119 memory lectures, Wrightson's methodological asides in HIST 251, and Freedman's opening lectures in HIST 210 on periodisation. Then read Carr's *What Is History?* and Evans's *In Defence of History* unaccompanied. |
| Indian Philosophy / Indian history (NPTEL, Swayam) | IIT Madras / IGNOU | Satya Sundar Sethy and others | ~40 | Included under History as well as Philosophy because it is the main free route into South Asian intellectual history. Honest caveat: production values are poor, the lecturing is often read-aloud, and it is nothing like Yale in polish. It is, however, real university teaching by subject specialists and it covers material nothing Western and free touches. |

**The spine**
1. HIST 202 European Civilization, 1648–1945 (Merriman) — the anchor.
2. CLCV 205 Ancient Greek History (Kagan) + 21H.301 for the written work.
3. HIST 210 The Early Middle Ages (Freedman).
4. HIST 251 Early Modern England (Wrightson) — where you learn method.
5. HIST 119 Civil War and Reconstruction (Blight).
6. ChinaX (Bol/Kirby) — the only way to get out of the West for free.

**Overlaps resolved**
- **Merriman HIST 202 over HIST 276.** 202 is the survey; 276 is a deep
  cut on France that repeats a third of it. Take 202 first, 276 only if
  France specifically interests you.
- **Blight HIST 119 over Freeman HIST 116** if you take only one American
  course. Freeman is the better lecturer minute-for-minute, but Blight's
  course is about a larger question and its final third has no equal.
- **MIT 21H.132 over 21H.302** — same course, newer bibliography.
- **Kagan over any free Roman survey** — not because Greece beats Rome but
  because no free Roman lecture course reaches his level, so take Kagan for
  lectures and MIT for Rome as reading.

**Gaps, stated plainly.** Free university history of **Latin America,
Africa, and the modern Middle East is genuinely bad.** Aggregator sites
list things; almost none are full courses from named specialists with
usable materials. South Asia is served only by NPTEL/Swayam, at low
production quality. China is the sole non-Western region with a
first-rate free offering (ChinaX). Do not build a "global history"
concentration out of free material and expect it to be honest — supplement
with books, and know that you are supplementing.

---

## Philosophy

The best-served division after literature, largely because Peter Adamson's
podcast is a genuine world-historical survey and there is nothing like it
in any other field.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| General Philosophy | Oxford (podcasts.ox.ac.uk) | Peter Millican | ~15 | Eight weeks of Oxford's first-year lectures. The best free *introduction* to philosophy full stop — Millican is rigorous, historically grounded, and does not condescend. Audio and video, with Millican's own handouts available from his personal site (millican.org), which effectively gives you a workbook. Assumes nothing. Covers scepticism, induction, mind/body, free will, personal identity, God. **Standout:** the induction and personal-identity lectures. |
| PHIL 176 Death | Yale (OYC) | Shelly Kagan | ~30 | Famous, and deservedly so — Kagan argues live, cross-legged on a desk, and models analytic philosophy better than any course that announces itself as teaching method. Video, transcripts, syllabus; no assignments. Do not take it for the subject matter; take it to learn what an argument is. **Standout:** the Plato lectures on the soul, and the late lectures on whether death is bad for the person who dies. |
| Introduction to Philosophy | Coursera (Edinburgh) | Dave Ward, Duncan Pritchard, and others | ~20 | Multi-lecturer survey, auditable free. Weaker than Millican, but it has quizzes and structure, which Millican does not. Use it as the scaffolded option if you need graded checkpoints. |
| Critical Reasoning: A Romp Through the Foothills of Logic | Oxford (Dept for Continuing Education) | Marianne Talbot | ~8 | Six interactive lectures on recognising, analysing, and evaluating arguments, plus fallacies. Not a formal-logic course — it is the informal-reasoning prerequisite most people skip and shouldn't. Talbot also has a companion "Romp Through Formal Logic" series. |
| PHIL 181 Philosophy and the Science of Human Nature | Yale (OYC) | Tamar Gendler | ~40 | Pairs classical texts (Plato, Aristotle, Hobbes, Kant) with contemporary psychology and behavioural economics. Unusual and genuinely good, though it is as much cognitive science as philosophy. Video, transcripts. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| History of Philosophy Without Any Gaps | LMU Munich / King's College London | Peter Adamson (with Jonardon Ganeri, Chike Jeffers) | 500+ episodes, ~150+ | The spine of this entire division. Chronological, unhurried, and — this is the point — *actually global*: full multi-year series on philosophy in the Islamic world, classical Indian philosophy (with Ganeri), and Africana philosophy (with Jeffers), each treated as philosophy rather than as anthropology. Free audio plus transcripts at historyofphilosophy.net. No assignments, no readings assigned, but each episode names its sources. Also frequent interview episodes with working specialists. **Standout:** the al-Ghazālī and Ibn Rushd episodes; the Nyāya/Buddhist debate episodes in the India series; the early Africana episodes on Anton Wilhelm Amo. |
| 24.01 Classics of Western Philosophy | MIT OCW | — | ~40 | **No video.** Reading list plus essay prompts covering the canonical sequence. This is the primary-text counterweight to Adamson's narration — Adamson tells you what Descartes argued, MIT makes you read him and write about it. Use together. |
| 24.00 Problems of Philosophy | MIT OCW | Richard Holton (2010 version) | ~35 | **No video.** Problem-based rather than historical; full syllabus, readings, paper assignments. Two OCW versions exist (2010 and 2019). |
| Justice | HarvardX (edX) / justiceharvard.org | Michael Sandel | ~25 | The full Sanders Theatre lectures are free on the standalone Justice site as well as edX. Sandel is a superb performer and the Socratic exchanges with students are the real content. Fair criticism: it is a communitarian's tour of the alternatives, and Rawls in particular gets a sympathetic-but-brief treatment. Video with reading list. **Standout:** the two utilitarianism lectures with the lifeboat case, and the affirmative-action session. |
| Moralities of Everyday Life | Coursera (Yale) | Paul Bloom | ~20 | Moral psychology rather than moral philosophy — where morality comes from, empirically. Auditable free, with quizzes. Take it *beside* an ethics course, not instead of one. |
| Ancient Philosophy: Plato & His Predecessors / Aristotle & His Successors | Coursera (Penn) | Susan Sauvé Meyer | ~30 both | Two-part, auditable free, with quizzes and text-based structure. More disciplined than Adamson on the same period because it works directly from the dialogues. Meyer is a serious Aristotle scholar. |
| 24.241 Logic I | MIT OCW | Ephraim Glick | ~35 | **No video**, but this one has full problem sets *with solutions* — rare in the humanities and the reason to pick it. Sentential and predicate logic through soundness and completeness. Genuinely gradeable on your own. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 24.09 Minds and Machines | MIT OCW | — | ~35 | **No video.** Philosophy of mind: dualism, functionalism, consciousness, AI. Strong reading list; essay assignments. The standard free entry to phil of mind. |
| Philosophy and the Sciences | Coursera (Edinburgh) | Michela Massimi and others | ~20 | Philosophy of science, split between physical and cognitive sciences. Auditable free. Uneven across lecturers but Massimi's segments are excellent. The best free philosophy-of-science course I can verify. |
| Chinese Thought: Ancient Wisdom Meets Modern Science | edX (UBC) | Edward Slingerland | ~25 | Warring States thought — Confucianism, Daoism, Mohism, Legalism — read as live philosophy and set against cognitive science. Two parts, auditable free. Slingerland is a real sinologist, which distinguishes this from the wisdom-literature genre. |
| Indian Philosophy | NPTEL / Swayam (IIT Madras) | Satya Sundar Sethy | ~40 | Orthodox and heterodox systems: Nyāya, Vaiśeṣika, Sāṃkhya, Yoga, Mīmāṃsā, Vedānta, plus Cārvāka, Jain, and Buddhist schools. Video lectures. Blunt assessment: dry delivery, lecture-reading rather than lecturing, no Yale polish. Take it anyway, because Adamson's India series is narrative and this is systematic, and nothing else free covers the six darśanas properly. |
| Stanford Encyclopedia of Philosophy | Stanford | — (peer-reviewed, per-entry authors) | reference | Not a course. It is the reference spine for this whole division and should be open in a tab permanently. Every entry is by a specialist and peer-reviewed; the bibliographies are the best free graduate-level reading lists in the humanities. |

**The spine**
1. General Philosophy (Millican) — the real introduction.
2. Critical Reasoning (Talbot) then 24.241 Logic I (Glick) — argument
   hygiene first, formal apparatus second.
3. HoPWAG (Adamson) — run continuously in the background for two years,
   including the Islamic, Indian, and Africana series.
4. 24.01 Classics of Western Philosophy — the primary-text discipline that
   Adamson deliberately does not provide.
5. Justice (Sandel) for ethics and political philosophy.
6. 24.09 Minds and Machines for a specialism.

**Overlaps resolved**
- **Millican over Edinburgh's Introduction to Philosophy.** Millican is a
  better philosopher and a better lecturer; Edinburgh's only advantage is
  quizzes, which Talbot and MIT supply more rigorously anyway.
- **Adamson over Meyer for ancient philosophy breadth; Meyer over Adamson
  for Plato and Aristotle specifically.** Adamson gives you the map;
  Meyer makes you read the dialogues. If you have time for one, Adamson,
  because he is also your only route to non-Western philosophy.
- **PHIL 176 Death over PHIL 181 Human Nature** as the Yale pick. Kagan
  teaches you to argue; Gendler teaches you interesting results.
- **MIT 24.241 over any MOOC logic course** — the solutions sets make it
  the only one you can actually grade yourself on.

---

## Religious Studies

Small division, but two of the four best humanities courses on the open
internet live here.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| RLST 145 Introduction to the Old Testament (Hebrew Bible) | Yale (OYC) | Christine Hayes | ~35 | Outstanding, and the clearest available demonstration of what critical biblical scholarship *is* as distinct from either apologetics or debunking. Hayes assumes no Hebrew and no prior belief either way. Video, transcripts, syllabus; readings are the biblical text plus Michael Coogan's introduction. **Standout:** the opening lectures on the difference between the biblical God and Ancient Near Eastern deities, and the lectures on the Documentary Hypothesis — take those four hours even if you take nothing else in this division. |
| RLST 152 Introduction to New Testament History and Literature | Yale (OYC) | Dale B. Martin | ~35 | The companion, and nearly as good. Martin's method is to read each text as a historically situated document by a specific community rather than as part of a unified canon — the payoff is that Paul, Mark, and John stop sounding like the same person. Video, transcripts. **Standout:** the lecture contrasting the four gospels' passion narratives, and the lectures on the historical Paul versus the pseudonymous letters. |
| Religious Literacy: Traditions and Scriptures | HarvardX (edX) | Harvard Divinity School faculty | ~15 | The framing course for the XSeries below — how to study religion academically without either flattening it or preaching it. Auditable free. Short. Worth doing first. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| World Religions Through Their Scriptures (XSeries: Judaism, Christianity, Islam, Buddhism, Hinduism, Sikhism) | HarvardX (edX) | Harvard Divinity/FAS and Wellesley faculty — Shaye Cohen, Laura Nasrallah, Ali Asani, Charles Hallisey, Diana Eck among them | ~15 each, ~90 total | The best free comparative-religion offering, and the only one where each tradition is taught by a specialist in that tradition rather than one generalist. Modular — take Islam and Buddhism and skip the rest if you like. Auditable free. Caveat: I am confident about the roster of instructors but not about which name attaches to which module in every case; check the module page before citing. **Strongest modules:** Asani on the Qur'an and Hallisey on Buddhist texts. |
| Historical Jesus | Stanford Continuing Studies | Thomas Sheehan | ~15 | Ten lectures, Creative Commons, free on podcast platforms and YouTube. A historian's-not-theologian's account, and a bracing one: Sheehan argues Jesus understood himself as an eschatological prophet, and that divinity claims arose well after his death. Opinionated and contested — take it as a strong position to argue with, alongside Martin's more even-handed RLST 152. Audio-only, no materials. |
| Buddhism and Modern Psychology | Coursera (Princeton) | Robert Wright | ~15 | Auditable free, with quizzes. Wright is a science journalist rather than a Buddhologist, and the course is really about whether Buddhist claims about the self survive contact with evolutionary psychology. Engaging and honest about its own limits. Not a substitute for a Buddhist-studies course; take the HarvardX Buddhism module for that. |

### Advanced

Nothing free at genuine advanced level in this division that I can verify —
no free courses in rabbinics, hadith studies, Pali or Sanskrit textual
work, or advanced comparative method. Say so rather than pad. The SEP,
the Oxford Handbooks (library access), and Adamson's Islamic-world series
are the realistic continuation.

**The spine**
1. Religious Literacy (HarvardX) — the framing.
2. RLST 145 Hebrew Bible (Hayes).
3. RLST 152 New Testament (Martin).
4. HarvardX Islam module (Asani).
5. HarvardX Buddhism module (Hallisey).

**Overlaps resolved**
- **Hayes and Martin are both required** — they do not overlap, they
  interlock, and taking Martin without Hayes leaves the New Testament's
  citations of scripture illegible.
- **Martin over Sheehan** as the primary New Testament course. Sheehan is
  sharper and more provocative but is arguing a thesis; Martin is teaching
  a field. Take Sheehan second, as the argument.
- **HarvardX modules over Wright's Buddhism course** for actually learning
  Buddhism. Wright is better company; Hallisey is the scholar.

---

## Literature

The best-served division, mostly because Yale recorded its English
department at an unusually good moment.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| ENGL 300 Introduction to Theory of Literature | Yale (OYC) | Paul H. Fry | ~35 | The most useful single humanities course on the open internet. Fry walks the twentieth century — Russian formalism, New Criticism, structuralism, deconstruction, psychoanalysis, Marxism, New Historicism, queer theory, postcolonial theory — and, crucially, applies each one to the *same* short text so you can see what each method actually buys you. Video, transcripts, syllabus; readings from the Leitch *Norton Anthology of Theory and Criticism*, which you will need. **Standout:** the deconstruction lectures — Fry is one of very few people who can make Derrida both comprehensible and worth the trouble — and the semiotics lecture. Take those three hours even if you skip everything else in this catalogue. |
| ENGL 310 Modern Poetry | Yale (OYC) | Langdon Hammer | ~35 | Yeats through the mid-century, and the best demonstration of close reading available free. Hammer reads slowly and out loud, and the pedagogy is entirely in the pausing. Video, transcripts. **Standout:** the Eliot lectures on *The Waste Land*, and the Hart Crane lectures — Hammer is Crane's biographer and it shows. |
| Greek and Roman Mythology | Coursera (Penn) | Peter Struck | ~20 | Auditable free, with quizzes. Struck teaches myth as a system of meaning rather than as a story collection, working through Homer, Hesiod, tragedy, and Ovid. Good gateway into the classics division below. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| ENGL 220 Milton | Yale (OYC) | John Rogers | ~35 | A single-author course of a depth that free material rarely reaches — *Paradise Lost* read against Milton's prose, his politics, and his heresies. Rogers takes Milton's theology seriously as argument. Video, transcripts. Demanding; the reading is heavy and non-negotiable. **Standout:** the lectures on Satan's speeches in Books I–II, and the one on Milton's monism. |
| ENGL 291 The American Novel Since 1945 | Yale (OYC) | Amy Hungerford | ~30 | Excellent on the sociology of literature — publishing, readership, what a novel is *for* — as well as on the novels. Video, transcripts. **Standout:** the Nabokov *Lolita* lectures, which handle a genuinely difficult text without flinching or moralising, and the Marilynne Robinson lecture. |
| ITAL 310 Dante in Translation | Yale (OYC) | Giuseppe Mazzotta | ~35 | The whole *Commedia* plus the minor works, in translation, from one of the field's major scholars. Mazzotta is discursive and occasionally hard to follow — this is the one OYC course where the transcripts genuinely help. Worth the effort; there is nothing comparable free. **Standout:** the Ulysses canto (*Inferno* XXVI) lecture. |
| SPAN 300 Cervantes' Don Quixote | Yale (OYC) | Roberto González Echevarría | ~35 | In translation. A close reading of the whole novel in Renaissance and Baroque context by a Sterling Professor. Slower-paced than the English department courses; take it if the novel is your thing. |
| AMST 246 Hemingway, Fitzgerald, Faulkner | Yale (OYC) | Wai Chee Dimock | ~30 | Three-author modernism course. Weakest of the Yale literature set in lecturing verve, but Dimock on Faulkner is genuinely strong and Faulkner is the one of the three you most need help with. |
| Modern and Contemporary American Poetry (ModPo) | Coursera (Penn) | Al Filreis | ~30 | Structurally unlike everything else here: **not lectures**. Filreis and a seminar of teaching assistants close-read poems on camera, collaboratively, and you watch a discussion rather than a monologue. Whitman and Dickinson forward to the present, heavy on experimental and Language poetry. Free, runs as a live cohort annually with a huge active forum, and the peer-review writing assignments are real. Best free *participatory* humanities experience on the internet. |
| The Ancient Greek Hero | HarvardX (edX) | Gregory Nagy | ~35 | Homer, tragedy, Plato, and hero cult, via Nagy's own translations. Auditable free; the accompanying book *The Ancient Greek Hero in 24 Hours* is free online. Nagy is idiosyncratic — deeply invested in oral-formulaic theory and in Greek words left untranslated — and you either find that illuminating or maddening. Try two hours before committing. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Masterpieces of World Literature | HarvardX (edX) | David Damrosch, Martin Puchner | ~20 | Gilgamesh to the present, explicitly about *circulation* — how texts travel between cultures and change meaning in transit. Damrosch effectively invented the modern discipline of world literature and this is his argument. Auditable free. The genuinely global option in this division. |
| Shakespeare's Life and Work | HarvardX (edX) | Stephen Greenblatt | ~20 | Greenblatt is the founder of New Historicism and *Will in the World* is his. Auditable free. Fewer plays than you'd expect — it is a course about Shakespeare in his world, not a play-by-play survey. |
| Poetry in America (series) | HarvardX (edX) | Elisa New | ~20 each | Multi-part, period-based. Distinctive format: New reads poems with guests, including non-academics. Warmer and less technical than Hammer or ModPo; a good third poetry course, a poor first one. |
| 21L.001 Foundations of Western Literature: Homer to Dante | MIT OCW | — | ~40 | **No video.** Reading list and essay prompts. Useful as a written-work structure to attach to Nagy and Mazzotta. |
| 21L.004 Reading Poetry | MIT OCW | — | ~30 | **No video.** Explicitly a methods course rather than a survey — how to describe what a poem is doing. Good assignment prompts. |

**The spine**
1. ENGL 300 Introduction to Theory of Literature (Fry) — first, always.
   Everything else reads differently afterwards.
2. ENGL 310 Modern Poetry (Hammer) — close reading as practice.
3. ModPo (Filreis) — because you need to *write* about literature and be
   read, not just watch someone else do it.
4. ENGL 220 Milton (Rogers) — one hard single-author course.
5. ITAL 310 Dante (Mazzotta) or The Ancient Greek Hero (Nagy) — one
   pre-modern anchor.
6. Masterpieces of World Literature (Damrosch/Puchner) — to get out of
   English.

**Overlaps resolved**
- **Fry's ENGL 300 has no competitor.** Nothing else free covers literary
  theory systematically. This is not a close call.
- **Hammer's ENGL 310 over Poetry in America** for a first poetry course —
  Hammer teaches technique, New curates experience. Over ModPo? No: take
  both, they are different activities. Hammer first, then ModPo, because
  ModPo's experimental material is easier once you have the modernist
  vocabulary.
- **Dante over Don Quixote** if you take one non-English pre-modern
  course — Mazzotta's is the more intellectually dense course, and the
  *Commedia* is more load-bearing for everything else in the Western canon.
- **Damrosch over adding a fourth Yale English course.** The Yale set is
  overwhelmingly Anglo-American; you need one course that isn't.

---

## Linguistics

Adequately served at the introductory level, thin above it, and MIT
dominates because MIT *is* the field's centre of gravity for syntax.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 24.900 Introduction to Linguistics (Spring 2022) | MIT OCW | Norvin Richards | ~35 | **Full video lectures plus assignments** — the rare open humanities course that is genuinely complete. Covers phonetics, phonology, morphology, syntax, semantics, acquisition, historical change, and variation. Assumes no prior work; the problem sets are where the learning happens, so do them. This is the default choice. **Standout:** Lecture 23 on historical linguistics, and the acquisition lectures — both work as standalone hours. |
| 24.900 Introduction to Linguistics (Fall 2012) | MIT OCW | David Pesetsky | ~35 | The earlier version, with lecture notes rather than full video. Pesetsky is a more forceful lecturer than Richards on syntax specifically. Use its notes as a supplement to the 2022 video course rather than as a replacement. |
| Miracles of Human Language: An Introduction to Linguistics | Coursera (Leiden) | Marc van Oostendorp | ~20 | Auditable free, with quizzes. Structurally interesting: interviews with working linguists and with speakers of many languages, including a running informant exercise. Much gentler than MIT and much less formal apparatus — take it *first* if MIT looks intimidating, not instead of MIT. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 24.901 Language and Its Structure I: Phonology | MIT OCW | — | ~35 | **No video**, but full problem sets. Real analytical work — you sketch complete phonological analyses of unfamiliar languages. This is the correct next step after 24.900 and the reason to have done the 24.900 problem sets. |
| 24.902 Language and Its Structure II: Syntax | MIT OCW | — | ~35 | **No video.** Generative syntax proper. MIT's house theory, taught by its house, which is both the strength and the bias — you are learning Chomskyan syntax specifically, not a neutral survey of syntactic theory. Worth knowing that going in. |
| 24.903 Language and Its Structure III: Semantics and Pragmatics | MIT OCW | — | ~35 | **No video.** Compositional semantics and pragmatics. The hardest of the three and the one where the absence of a lecturer hurts most. Expect to need supplementary reading — Heim and Kratzer is the standard, and hard. |

### Advanced

Thin, and worth saying so. There is no good free standalone course in
**historical linguistics**, **psycholinguistics**, or **sociolinguistics**
that I can verify at university level. Substitutes:

- Historical linguistics: 24.900's Lecture 23, then read Campbell's
  *Historical Linguistics* alone.
- Psycholinguistics/acquisition: 24.900's acquisition lectures; MIT OCW
  lists graduate acquisition and psycholinguistics syllabi without video,
  which are usable as reading lists if you have library access.
- Phonetics as distinct from phonology: not covered well free. The UCLA
  Phonetics Lab archive and the IPA's own materials are the fallback, and
  they are resources, not courses.

**The spine**
1. 24.900 Introduction to Linguistics, Spring 2022 (Richards) — with the
   problem sets.
2. 24.901 Phonology.
3. 24.902 Syntax.
4. 24.903 Semantics and Pragmatics.
5. Miracles of Human Language (van Oostendorp) — optional, as a warm-up
   or as a breadth corrective to MIT's narrowness.

**Overlaps resolved**
- **24.900 Spring 2022 over Fall 2012** — the 2022 version has full video,
  which the 2012 version does not. Mine 2012's notes as supplement.
- **MIT over Leiden** for the actual training. Leiden is more enjoyable and
  more global in its examples; MIT is where you learn to do the analysis.
  If you only do one, do MIT and accept that it is a Chomskyan education.

---

## Classics & Ancient Languages

The thinnest division, exactly as expected. Classical *civilization* is
well served; the *languages* are not, and no amount of listing will change
that.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| CLCV 205 Introduction to Ancient Greek History | Yale (OYC) | Donald Kagan | ~40 | Listed again from History because it is also the classical-civilization anchor. See notes above. |
| Greek and Roman Mythology | Coursera (Penn) | Peter Struck | ~20 | See Literature. The best free entry to classical culture with actual assessments. |
| The Ancient Greek Hero | HarvardX (edX) | Gregory Nagy | ~35 | See Literature. Free companion book online. |
| Introduction to Ancient Greek (118 video lessons) | Brandeis / Harvard Center for Hellenic Studies | Leonard Muellner, Belisi Gillespie | ~100+ | **The best free ancient-language course that exists.** Two full semesters of college Greek, on YouTube, taught by a Homerist of standing. Video lessons; you supply the textbook and do the drills yourself. This is a real language course, and finishing it means you can begin reading. Nothing comparable exists for Latin. |
| Getting Started on Ancient Greek | Open University (OpenLearn) | — | ~10 | Free, self-contained, alphabet to simple sentences. A taster, honestly labelled as one. Use it to find out whether you want to commit to Muellner's 118 lessons. |
| Discovering Ancient Greek and Latin | Open University (OpenLearn) | — | ~10 | Same category — a taste of both languages, aimed at people who have read the classics in translation. Not a course in either language. |

### Core and Advanced

There is no free, complete, university-level **Latin** course. This is the
single largest gap in this entire catalogue and it should be stated
without softening. What exists:

- **Dickinson College Commentaries** (dcc.dickinson.edu) — free, superb,
  scholarly running commentaries on Caesar, Ovid, Vergil, Sulpicia and
  others, with vocabulary and notes. A resource for reading Latin, not a
  course that teaches you Latin.
- **Open University OpenLearn** Latin taster units — introductory only.
- Various free Latin video series exist outside universities. They vary
  from good to actively misleading and I will not vouch for any of them.

Realistic plan: buy Wheelock or *Lingua Latina per se Illustrata* and
work through it with the free answer keys and Dickinson's commentaries as
the reading payoff. Accept that this part of your degree is self-taught
from a book, and that this is how most classicists learned anyway.

For Greek beyond Muellner, the same applies: no free intermediate course
exists; move to the Dickinson-equivalent commentary resources and read.

**The spine**
1. CLCV 205 (Kagan) — the historical frame.
2. Greek and Roman Mythology (Struck) — the cultural frame.
3. The Ancient Greek Hero (Nagy) — the textual frame.
4. Introduction to Ancient Greek, 118 lessons (Muellner) — the language,
   if you do one.
5. Latin from a book. There is no fifth free course.

**Overlaps resolved**
- **Nagy and Struck overlap on Homer and myth.** Struck is the better
  structured course with real assessment; Nagy is the deeper reading.
  Struck first, Nagy second, or Struck only if time is short.
- **Muellner over the OpenLearn tasters** — the tasters are for deciding,
  Muellner is for learning. Do not mistake one for the other.

---

## Writing & Rhetoric

Small, practical, and the one division where the MOOCs beat the elite
lecture courses — because writing needs feedback, and feedback is exactly
what a recorded lecture cannot give.

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| English Composition I | Coursera (Duke) | Denise Comer | ~30 | Auditable free. The reason to take it over a lecture course: **peer-reviewed writing assignments**, which means someone actually reads your prose. Composition cannot be learned by watching. Standard first-year comp content — argument, evidence, revision, source use. |
| Rhetoric: The Art of Persuasive Writing and Public Speaking | HarvardX (edX) | James Engell | ~25 | Built on Engell's Harvard course "Elements of Rhetoric." Works through historical speeches and documents — Lincoln, Churchill, King — as engineering problems. Auditable free. Better on analysis than on production. **Standout:** the sessions on the Gettysburg Address and on Letter from Birmingham Jail. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 21W.747 Classical Rhetoric and Modern Political Discourse | MIT OCW | — | ~30 | **No video.** Aristotle, Cicero, and Quintilian read against contemporary political speech, with essay assignments. The theoretical counterpart to Engell's practical course. Take it as a reading list. |
| Creative Writing Specialization | Coursera (Wesleyan) | Amy Bloom, Salvatore Scibona, Brando Skyhorse, Amity Gaige | ~40 across courses | Auditable free per course; the capstone and certificate are paid. Four courses — craft fundamentals, plot, character, style, then a capstone. Real working writers, and peer review on every assignment. The individual craft courses are worth auditing even if you never touch the capstone. |
| Sharpened Visions: A Poetry Workshop | Coursera (CalArts) | Douglas Kearney | ~15 | Auditable free. A genuine workshop with prompts and peer review, not a poetry-appreciation course. Kearney is a working poet with a distinctive formal sensibility, and the assignments are more inventive than most. |

### Advanced

Nothing free at advanced level worth naming. Advanced writing instruction
is fundamentally a feedback relationship and no free course supplies it.
ModPo's peer-review forum (see Literature) is the closest substitute
available, and it is genuinely close — the community there reads carefully.

**The spine**
1. English Composition I (Comer) — get the peer review.
2. Rhetoric (Engell) — learn to see structure in persuasion.
3. 21W.747 — read Aristotle and Quintilian properly.
4. Creative Writing: the craft courses (Wesleyan) or Sharpened Visions
   (Kearney), depending on prose versus verse.

**Overlaps resolved**
- **Comer over Engell as the first course.** Engell is more intellectually
  interesting; Comer makes you write and be read, which at freshman level
  matters more.
- **Engell over 21W.747** if you take one rhetoric course — Engell has
  video and worked examples; MIT has a syllabus.
- **Wesleyan over Kearney** for prose writers, **Kearney over Wesleyan**
  for poets. They are not competing for the same slot.

---

## Cross-division notes

**Course count:** 62 entries, of which about eight are listed twice across
divisions (Kagan, Struck, Nagy, the NPTEL Indian philosophy course) because
they genuinely belong in both.

**Where the free ecosystem is honest and strong:** European and American
history, literary theory and English literature, biblical studies,
analytic philosophy, introductory linguistics, and Greek language.

**Where it is weak, stated plainly:** Latin (no complete free course at
all), historiography (nothing), Latin American, African, and Middle
Eastern history (nothing of quality), advanced linguistics subfields,
advanced religious studies, and non-Western literature outside the
Damrosch course. If your self-directed degree needs these, it needs books
and library access, not more courses.

**The single highest-value hours in this whole catalogue,** if you could
only take a handful: Fry's deconstruction lectures (ENGL 300), Hayes on
the Documentary Hypothesis (RLST 145), Blight's final lectures on memory
and Reconstruction (HIST 119), Freedman's Lecture 8 on Byzantium (HIST
210), and Millican on induction (General Philosophy).

**Uncertainties flagged.** MIT OCW instructor attributions are unreliable
for courses I could not open directly — where I could not confirm a name,
I left the field blank rather than guess. The MIT "Islamic Societies of
the Middle East and North Africa" course number is unconfirmed. The
mapping of individual HarvardX World Religions modules to individual
instructors is confident at the roster level but not module by module.
Course availability on edX and Coursera changes; audit access in
particular has been narrowing across both platforms, so verify before
planning around any of them.

---

# Arts and Engineering

A catalogue of free, openly available university courses across four arts
divisions and seven engineering divisions. Everything here is real and
findable; where I was not confident of an instructor's name I left the cell
blank rather than guess.

**All hour figures are rough estimates** — they assume you watch the lectures
and do a meaningful fraction of the assigned work, not that you skim. Treat
them as relative weights, not promises.

**Three things to understand before you start.**

*Auditing.* Most Coursera and edX courses let you watch every video and read
every reading for free, but lock graded assignments and the certificate behind
a paywall. That is fine for lecture-driven humanities courses and bad for
engineering, where the problem sets are the actual education. Where a course
is audit-only I say so.

*Video versus materials.* MIT OpenCourseWare publishes hundreds of courses
with complete problem sets, exams and solutions but **no video**. These are
often better than the video courses — you get the real assignments and the
real answer keys. But they demand that you already know how to teach yourself
from a syllabus and a textbook. NPTEL is the inverse: enormous video coverage,
lighter written material, uneven production.

*Studio practice.* Read the honest warning at the end of the Visual Art
division before you plan any studio work around this list.

---

## 1. Music

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| MUSI 112 Listening to Music | Yale (Open Yale Courses) | Craig Wright | 45 | The best free music course on the internet, no close second. 23 filmed lectures, full transcripts, syllabus, reading list, and the actual midterm and final with answer keys. Wright teaches ear-first — you learn to hear structure before you learn to name it. **Lecture 3 and 4 on rhythm** are worth watching even if you take nothing else; **Lecture 8, Bass Patterns: Blues and Rock**, is the single clearest explanation of why the same chord progression underlies Pachelbel, doo-wop and half of pop music. The live student-orchestra lectures are also unusually good. |
| Introduction to Classical Music | Yale via Coursera | Craig Wright | 30 | The MOOC rebuild of MUSI 112. Overlaps heavily. Audit-free with graded quizzes locked. Take this only if you want the quiz structure and shorter video segments; otherwise the Open Yale version is more complete and has no platform between you and the material. |
| Fundamentals of Music Theory | Univ. of Edinburgh via Coursera | Michael Edwards, Nikki Moran, John Kitchen, Zack Moir | 25 | The most solid free intro theory course — notation, intervals, scales, triads, seventh chords, basic harmonic analysis. Audit-free; graded quizzes locked, which matters here because theory needs drilling. Supplement with musictheory.net exercises, which are free and unlimited. |
| Developing Your Musicianship | Berklee via Coursera | George W. Russell, Jr. | 15 | Berklee's free-audit entry point. Practical rather than academic — chord construction, ear training, playing over changes. Better than the Edinburgh course if you already play an instrument, worse if you do not. |
| History of Rock, Part One | Univ. of Rochester via Coursera | John Covach | 20 | Covach is a serious musicologist writing about popular music, not a fan with a slideshow. Strong on the mechanics of how a genre transmits and mutates. Part Two continues to the 1980s. Audit-free. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 21M.220 Early Music | MIT OCW | — | 35 | Medieval and Renaissance music. Materials-only: syllabus, listening lists, assignments, no video. The value is the **listening list**, which is a curated path through chant, Ars Nova, Italian trecento and Elizabethan England that would take you years to assemble yourself. Treat it as a reading and listening program rather than a course. |
| 21M.030 Introduction to World Music | MIT OCW | — | 30 | Non-Western traditions studied structurally — how the music is built, not just where it comes from. Materials-only. Honest limitation: no video and no recordings bundled, so you are assembling the listening yourself from the syllabus. Still the best free framework for approaching non-Western music seriously. |
| Jazz Improvisation | Berklee via Coursera | Gary Burton | 20 | Burton is a genuine major figure — NEA Jazz Master, decades with Chick Corea. This is craft instruction from someone at the top of the field, which is rare in free material. Requires that you play. Audit-free. |
| Exploring Beethoven's Piano Sonatas | Curtis Institute via Coursera | Jonathan Biss | 20 | Unusual and excellent: a working concert pianist analysing repertoire he performs, at the keyboard, in detail. Several sequels exist. This is the closest free material comes to a conservatory masterclass. Audit-free. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 21M.301 Harmony and Counterpoint I | MIT OCW | — | 40 | Diatonic harmony, two-part counterpoint, figuration. Materials-only but the **assignments are the course** and they are published — this is real part-writing work with instructions. Pair with a piano and check your own work at the keyboard. 21M.302 continues into chromatic harmony. |
| Introduction to Music Production | Berklee via Coursera | Loudon Stearns | 20 | DAW-agnostic fundamentals: signal flow, EQ, compression, mixing. The best free entry to production. Audit-free, though the peer-graded assignments are where the learning is and those are gated. |

**The spine.** MUSI 112 (Yale, Wright) → Fundamentals of Music Theory
(Edinburgh) → 21M.301 Harmony and Counterpoint I (MIT) → 21M.220 Early Music
(MIT) → 21M.030 Introduction to World Music (MIT) → Exploring Beethoven's
Piano Sonatas (Biss). That is a coherent year: hear it, name it, write it,
then go deep chronologically and geographically.

**Overlaps resolved.** *Wright's Yale course beats Wright's Coursera course* —
same instructor, but Open Yale gives you full lectures, transcripts and exams
with no paywall on anything. *Edinburgh theory beats Berklee musicianship for
a beginner* — Berklee assumes you already play; Edinburgh assumes nothing.
Take Berklee second if you play. *MIT 21M.301 beats every free "music theory"
MOOC* for anyone past the basics, because it has actual part-writing
assignments rather than multiple-choice quizzes. *History of Rock beats the
various free "history of popular music" offerings* because Covach is a
musicologist and most of the competition is not.

---

## 2. Visual Art and Art History

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Smarthistory (hosted at Khan Academy and smarthistory.org) | Smarthistory / Khan Academy | Beth Harris, Steven Zucker, and a large contributor pool | 80+ | Not a course — a full art-history survey, and genuinely the best free art-history resource that exists. Hundreds of short conversational videos filmed in front of the actual objects, organised chronologically and geographically, with essays. Coverage of **non-Western art is far better than any single university survey course you could take free** — substantial Africa, Islamic world, South and East Asia, Pre-Columbian Americas, Oceania. No assignments, no assessment; you supply the discipline. Use the smarthistory.org site rather than the Khan mirror, it is better organised. |
| Modern Art & Ideas | MoMA via Coursera | MoMA educators and curators | 15 | Thematic rather than chronological — places, things, identity, transformation. Built around works MoMA actually owns, with curator and conservator interviews. Genuinely well made; museum production values. Audit-free. |
| 4.601 Introduction to Art History | MIT OCW | — | 30 | Euro-American traditions from the fourteenth to the twenty-first century, organised thematically rather than chronologically, with a real syllabus, reading list, two exams and three papers. Materials-only, no video. Its value next to Smarthistory is **structure and writing assignments** — Smarthistory teaches you to look, this teaches you to argue. Its limitation is that the coverage is explicitly Euro-American, which is exactly the gap Smarthistory fills. Use them together. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Seeing Through Photographs | MoMA via Coursera | Sarah Meister | 15 | The strongest of MoMA's courses. Photography from 1840 to now, organised around the gap between seeing an image and understanding it. Meister is a serious curator and the course is intellectually sharper than its packaging suggests. Audit-free. |
| What Is Contemporary Art? | MoMA via Coursera | MoMA curators | 15 | Post-1990 practice — installation, performance, video, social practice. Fills the gap almost every survey leaves. Weaker than Seeing Through Photographs but there is no free competition. Audit-free. |
| Fashion as Design | MoMA via Coursera | Paola Antonelli and others | 20 | Seventy garments as design objects, with manufacturers, historians and designers. Better than it sounds; a real materials-and-production education hidden inside an art course. Audit-free. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| In the Studio: Postwar Abstract Painting | MoMA via Coursera | Corey D'Augustine | 20 | The exception to everything I say below about studio work. D'Augustine, a conservator and painter, reconstructs the actual technique of Pollock, de Kooning, Rothko, Newman, Krasner and others — materials, ground preparation, mark-making — and paints on camera. If you want to understand how these paintings were physically made, this is the only free course that does it. Audit-free. |
| 4.602 Modern Art and Mass Culture | MIT OCW | — | 30 | Modernism read against advertising, photography and mass media. Materials-only, reading-heavy, and the reading list is demanding — Benjamin, Greenberg, Krauss. This is where the art history stops being descriptive and starts being theoretical. Only worth it after a survey. |

**On studio practice — read this before planning around the list.** You
cannot learn to draw, paint, sculpt or print from lectures. There is no free
online substitute and pretending otherwise wastes a year. What actually works:
(1) **do the work daily** — a drawing habit of an hour a day beats any course;
(2) **use free instructional books rather than courses** — Nicolaïdes's *The
Natural Way to Draw* and Bargue plate reproductions are both freely available
and are structured curricula with assignments; (3) **get critique from humans**
— a community college studio course, a local atelier, a life-drawing session
at an art centre, or an online critique community. Critique is the part that
cannot be automated and the part that produces improvement. The courses above
teach you to *see and think about* art. Making it is a separate program that
runs in parallel and mostly offline.

**The spine.** Smarthistory full survey (run it across the whole year, do not
try to finish it first) → 4.601 Introduction to Art History (MIT, for the
writing assignments) → Seeing Through Photographs (MoMA) → In the Studio:
Postwar Abstract Painting (MoMA) → 4.602 Modern Art and Mass Culture (MIT).
Plus a real studio practice, offline, from day one.

**Overlaps resolved.** *Smarthistory beats every university survey course
available free*, including the MIT one, on coverage, on non-Western breadth
and on quality of looking. MIT 4.601 survives only because it supplies the
writing assignments Smarthistory lacks — take it for the syllabus, not the
content. *Among MoMA's five courses, take Seeing Through Photographs and In
the Studio*; Modern Art & Ideas is the weakest and largely duplicates material
Smarthistory covers better, and What Is Contemporary Art? is worth it only
because nothing else covers post-1990.

---

## 3. Architecture and Design

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| HSAR 252 Roman Architecture | Yale (Open Yale Courses) | Diana E. E. Kleiner | 40 | Filmed lectures, transcripts, full syllabus, exams. Kleiner is superb and the course is far broader than the title — it covers urbanism, engineering, concrete technology and how buildings encode political power. **The lectures on Roman concrete and vaulting** are the best free explanation anywhere of why Roman construction was a genuine technical revolution, and are worth watching even if you skip the rest. |
| The Architectural Imagination | Harvard via edX | K. Michael Hays | 30 | The strongest free introduction to architecture as a discipline rather than a history. Teaches you to read a plan, a section and a diagram, then works through how buildings produce meaning. Audit-free, with drawing exercises you should actually do. Hays is a major theorist and the course is intellectually ambitious. |
| Fundamentals of Graphic Design | CalArts via Coursera | Michael Worthington | 20 | Imagemaking, typography, composition, colour. CalArts's design faculty is first-rate and this is by some distance the best free graphic design instruction. Audit-free; the peer critique is gated, which is a real loss because critique is the point. Part of a four-course sequence — the **typography course in the sequence is the strongest single unit**. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 4.605 Introduction to the History and Theory of Architecture | MIT OCW | Mark Jarzombek | 40 | A genuinely global survey — prehistory to the sixteenth century, and it treats Chinese, Indian, Mesoamerican and African building as central rather than as an appendix. Materials-only on OCW: lecture handouts, study guides, exam guides, no video. The lecture handouts are dense and usable on their own. Jarzombek co-wrote the standard global architectural history textbook, which is what this course is built from. |
| Introduction to User Experience Design | Georgia Tech via Coursera | Rosa Arriaga | 15 | Interaction design fundamentals — user research, personas, prototyping, evaluation. Compact and practical. Audit-free. Weaker theoretically than the UCSD human-centred design material but tighter and finishable. |
| Rethink the City: New Approaches to Global and Local Urban Challenges | TU Delft via edX | — | 25 | Urban design for rapidly growing cities in the Global South — informality, mobility, water, housing. Delft's urbanism faculty is one of the best in the world and this is unusual in being about the cities where most urban growth is actually happening. Audit-free. |
| 11.001J Introduction to Urban Design and Development | MIT OCW | Susan Silberberg | 30 | The American counterweight to the Delft course — how cities are actually produced by finance, regulation and politics rather than by designers. Materials-only, reading-heavy. Take it if you want to understand why cities look the way they do rather than how to draw one. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Urban Design for the Public Good: Dutch Urbanism | TU Delft via edX | — | 25 | Case-study driven — the Dutch approach to public space, water and density, which is the most-copied urban model in the world. Best taken after Rethink the City. Audit-free. |

**The spine.** The Architectural Imagination (Harvard, Hays) → HSAR 252 Roman
Architecture (Yale, Kleiner) → 4.605 Introduction to the History and Theory of
Architecture (MIT, Jarzombek) → Rethink the City (TU Delft) → 11.001J
Introduction to Urban Design and Development (MIT). Add Fundamentals of
Graphic Design (CalArts) separately if design rather than architecture is the
target.

**Overlaps resolved.** *Hays beats Kleiner as a first course* even though
Kleiner's is better produced, because Hays teaches you to read architectural
drawing, which every later course assumes. Take Kleiner second — it is a
better piece of lecturing but a narrower subject. *Jarzombek beats every other
free architectural history survey* on global coverage; the tradeoff is no
video, and you should accept it. *Delft beats MIT on urban design practice*;
*MIT beats Delft on urban political economy*. They are not substitutes — the
Delft courses teach you what good urbanism looks like, the MIT course teaches
you why it usually does not get built.

---

## 4. Film, Theatre and Media

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 21L.011 The Film Experience | MIT OCW | David Thorburn | 40 | The best free film course available. Complete video lectures — OCW assembled a full sequence from the 2007 and 2013 classes — plus a films-and-readings list and writing assignments. Thorburn is an exceptional lecturer of the old school; he talks, closely, about specific shots. Silent period through classical Hollywood genre to European and Japanese art cinema. **The Buster Keaton lecture and the Hitchcock lectures** are the ones to watch even if you skip everything else. You must screen the films yourself; OCW cannot supply them. |
| Introduction to Media Studies | MIT OCW | — | 25 | MIT's Comparative Media Studies introduction — how media technologies reshape narrative, publics and power, across print, broadcast, film and networked media. Materials-only, reading-heavy, genuinely rigorous. The reading list alone is a useful map of the field. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| The Language of Hollywood: Storytelling, Sound, and Color | Wesleyan via Coursera | Scott Higgins | 20 | Focused and technically specific — how the transitions to synchronised sound and to colour changed what films could do. Higgins is a real film scholar and this is much sharper than the generic "film appreciation" MOOCs. Audit-free. Best companion to Thorburn: Thorburn gives you the canon, Higgins gives you the technical history. |
| Script Writing: Write a Pilot Episode for a TV or Web Series | Michigan State via Coursera | — | 20 | The most usable free screenwriting instruction. Structure, beat sheets, dialogue, and an actual deliverable at the end. Audit-free, and the peer review is gated — which hurts more here than anywhere else on this list, because writing without readers does not improve. Find readers elsewhere. |
| Shakespeare and His World | Univ. of Warwick via FutureLearn | Jonathan Bate | 25 | Bate is one of the leading Shakespeare scholars alive and the course is built with the Shakespeare Birthplace Trust, using original objects and documents. Play-by-play across the career. FutureLearn's free access is time-limited per course run, which is an annoyance — check the current terms before committing. |
| 21M.600 Introduction to Acting | MIT OCW | — | 20 | Materials-only: exercises, scene assignments, reading. Included with the same caveat as studio art — you cannot learn acting from a syllabus. Its use is as a **structured exercise list to run with other people**, which is exactly what a local community theatre or a reading group can supply. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Upper-level film courses in MIT's Literature and CMS listings | MIT OCW | various | 30 | OCW carries a rotating set of advanced film courses on single directors, national cinemas and genres — materials-only, each built around a screening list and essay prompts. Browse the Literature and Comparative Media Studies departments and pick by subject rather than by code, since the offerings change. Treat them as excellent curated screening lists with writing assignments attached, which is what they are. |

**The spine.** 21L.011 The Film Experience (MIT, Thorburn) → The Language of
Hollywood (Wesleyan, Higgins) → Introduction to Media Studies (MIT) → Script
Writing (Michigan State) → Shakespeare and His World (Warwick, Bate). Screen
everything on Thorburn's list; that is the actual work.

**Overlaps resolved.** *Thorburn beats every free film survey* — it is the
only one with a complete filmed lecture sequence from a first-rate lecturer,
and the only one whose screening list is a real canon rather than whatever the
platform could license. Higgins does not compete with it, he complements it.
*Michigan State beats the various "creative writing" specialisations* for
screenwriting specifically because it ends with a finished script rather than
exercises. *There is no good free theatre course* — the acting and stagecraft
material on OCW is a set of exercises, not instruction. Theatre is the weakest
covered subject in this entire catalogue and you should plan to do it in
person.

---

## 5. Mechanical Engineering

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Introduction to Engineering Mechanics (statics) | Georgia Tech via Coursera | Wayne Whiteman | 30 | The best free statics course. Whiteman is a career teacher, not a researcher doing outreach, and it shows — worked examples, steady pace, no gaps. Audit-free with videos and worked problems visible; graded quizzes gated. First of a four-course Georgia Tech sequence that covers statics, applications, 2D dynamics and 3D dynamics. |
| Applications in Engineering Mechanics | Georgia Tech via Coursera | Wayne Whiteman | 30 | Continuation — trusses, frames, machines, friction, centroids, area moments. Take it; the first course alone leaves you unable to analyse a real structure. |
| 2.001 Mechanics and Materials I | MIT OCW | — | 45 | Statics plus deformable-body mechanics — stress, strain, beam bending, torsion. Materials-only but with **full problem sets, exams and solutions**, which is what makes it worth doing alongside the Georgia Tech videos. MIT gives you the hard problems; Whiteman gives you the explanation. Run them together. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 2.003SC Engineering Dynamics | MIT OCW | J. Kim Vandiver | 60 | The strongest free dynamics course anywhere. "SC" is OCW's Scholar format: complete video lectures, recitation videos, problem sets with solutions, concept questions. Covers kinematics through Lagrange's equations. Vandiver's treatment of **rotating-frame kinematics and gyroscopic effects** is the clearest I know of at any price. Demanding — this is genuinely a hard course and the problem sets are not optional. |
| Engineering Systems in Motion: Dynamics of Particles and Bodies in 2D Motion | Georgia Tech via Coursera | Wayne Whiteman | 30 | The gentler dynamics option. Take this *instead of* 2.003SC if you are struggling, or *before* it if you want a ramp. Do not take both in full. |
| Fluid Mechanics | NPTEL / IIT Kanpur | Gautam Biswas, Suman Chakraborty | 50 | NPTEL's flagship fluids course and the reason to take NPTEL seriously. Biswas and Chakraborty are both major figures in the field and the coverage is complete — statics, kinematics, integral and differential analysis, Navier-Stokes, boundary layers, pipe flow, turbomachinery. Video-led with assignments. Slower and more derivation-heavy than an American course, which is a feature if you actually want to understand where the equations come from. |
| Applied Thermodynamics | NPTEL / IIT Guwahati | Niranjan Sahoo, Pranab K. Mondal | 40 | Steam and gas power cycles, refrigeration, IC engine cycles. The applied follow-on to a first thermo course. NPTEL's thermodynamics coverage is deep — there are multiple parallel basic-thermo courses from different IITs and they are largely interchangeable; this applied one is the differentiated offering. |
| 2.005 Thermal-Fluids Engineering I | MIT OCW | — | 45 | MIT's integrated treatment of thermodynamics, fluid mechanics and heat transfer as one subject rather than three. Materials-only. Take it for the problem sets and for the integrated framing, which is unusual and good. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Advanced Fluid Mechanics | NPTEL / IIT Kharagpur | Suman Chakraborty | 45 | Chakraborty is the best lecturer on NPTEL that Western learners have never heard of. Potential flow, viscous flow, boundary layer theory, turbulence, compressible flow. If you liked the IIT Kanpur fluids course, this is the sequel. Video-led. |
| 2.810 Manufacturing Processes and Systems | MIT OCW | Timothy Gutowski | 35 | Machining, casting, forming, joining, injection moulding, and — unusually — the economics and systems view of how manufacturing decisions are actually made. Materials-only, with excellent lecture slides. Almost nothing else free covers manufacturing at this level. |
| Design of Machine Elements | NPTEL / IIT Kharagpur | — | 40 | Shafts, bearings, gears, springs, fasteners, welded joints — the design-table-and-standards work that no MIT course covers because MIT does not teach it that way. If you want to actually design a gearbox, this is where to go. Video-led with assignments. |
| 2.007 Design and Manufacturing I | MIT OCW | — | 40 | MIT's famous project-based design course, the one with the robot competition. Video content plus design methodology material. You cannot do the project without a shop, so take it for the **design process instruction** — sketch models, functional decomposition, prototyping strategy — which transfers even without the hardware. |

**The spine.** Introduction to Engineering Mechanics + Applications in
Engineering Mechanics (Georgia Tech, Whiteman) → 2.001 Mechanics and Materials
I (MIT) → 2.003SC Engineering Dynamics (MIT, Vandiver) → Fluid Mechanics
(NPTEL/IIT Kanpur) → 2.005 Thermal-Fluids Engineering I (MIT) → Design of
Machine Elements (NPTEL/IIT KGP).

**Overlaps resolved.** *Whiteman beats MIT 2.001 as your first statics
exposure* because he has video and MIT does not; *MIT 2.001 beats Whiteman on
assignments* because MIT publishes solutions to hard problems. Do Whiteman for
instruction and MIT for homework — this pattern repeats across all of
engineering. *Vandiver beats Whiteman's dynamics courses* for anyone who can
handle it: it is a real MIT course with real problem sets, and Whiteman's is a
MOOC. Take Whiteman only as a ramp. *NPTEL beats MIT on fluids* — MIT's fluids
material is scattered across 2.005/2.006 and assumes a lot, while the IIT
Kanpur course is a complete, self-contained, video-led fluid mechanics
education. *NPTEL beats everything on machine design and manufacturing
standards*, which American curricula largely stopped teaching.

---

## 6. Electrical and Electronic Engineering

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 6.002 Circuits and Electronics | MIT OCW | Anant Agarwal, Jeffrey H. Lang | 60 | Full video lectures plus problem sets, exams and solutions — one of OCW's most complete publications. Builds from the lumped circuit abstraction through the digital abstraction, amplifiers, first- and second-order dynamics, to op-amps. Agarwal's framing of **abstraction as the central idea in engineering** — the first two lectures — is worth watching regardless of what you study. The single best free electronics course. |
| Basic Electrical Circuits | NPTEL / IIT Madras | Nagendra Krishnapura | 40 | The best NPTEL circuits course and a legitimate alternative to 6.002. Krishnapura is a working analog IC designer and teaches like one — more careful about what an ideal element actually models. More systematic on network analysis techniques than 6.002; less conceptually ambitious. Video-led with assignments. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| RES.6-007 Signals and Systems | MIT OCW | Alan V. Oppenheim | 50 | The 1987 video lecture series by the man who wrote the textbook everyone still uses. The production is ancient — chalkboard and overhead transparencies — and it does not matter. Oppenheim explains convolution, Fourier analysis and sampling with a clarity nobody has improved on in forty years. **The sampling theorem lectures** are the canonical treatment. Video plus assignment materials. |
| 6.003 Signals and Systems | MIT OCW | Dennis Freeman | 50 | The modern MIT version, with video lectures and full problem sets. Better organised and better assigned than the Oppenheim series; less inspired. Take Freeman for the coursework and dip into Oppenheim for the topics you find hard. |
| Digital Signal Processing | EPFL via Coursera | Paolo Prandoni, Martin Vetterli | 40 | Unusually good — starts from vector spaces and builds DSP as applied linear algebra, which makes the whole subject click in a way the classical treatment does not. Vetterli is a major figure. Audit-free. Take after a signals course, not before. |
| Control Engineering | NPTEL / IIT Madras | Ramkrishna Pasumarthy | 40 | Solid classical control — modelling, transient response, root locus, frequency response, PID, stability. NPTEL has several parallel control courses from different IITs; this one and C. S. Shankar Ram's *Control Systems* (also IIT Madras) are both good and largely interchangeable. Video-led with assignments. |
| Digital Signal Processing | NPTEL / IIT Delhi | S. C. Dutta Roy | 40 | The classic NPTEL DSP series. Dutta Roy is an old-school lecturer of real authority; the treatment of digital filter design is thorough in a way the MOOCs are not. Video-led. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 6.012 Microelectronic Devices and Circuits | MIT OCW | — | 45 | Semiconductor physics into device models into circuit design — pn junctions, MOSFETs, BJTs, single-stage amplifiers, frequency response. Materials-only with problem sets and solutions. The natural sequel to 6.002 and the gateway to everything in IC design. |
| Power Electronics | NPTEL / IISc Bangalore | L. Umanand | 45 | The best free power electronics course. Devices, AC-DC and DC-DC converters, operating modes, analysis, an introduction to inverters. Umanand has been designing converters for decades and the course is practical without being a cookbook. Video-led with assignments. Nothing in the Western free catalogue matches this. |
| Power System Analysis | NPTEL / IIT Kharagpur | A. K. Sinha | 45 | Load flow, fault analysis, symmetrical components, stability, system operation. Power systems is almost entirely absent from free Western material — this course and its NPTEL siblings are effectively the only option, and they are good. Video-led. |
| Principles of Communication Systems | NPTEL / IIT Kanpur | Aditya K. Jagannatham | 45 | Analog and digital modulation, noise, detection, information theory basics. Jagannatham is one of NPTEL's clearest lecturers and works derivations fully on the board rather than presenting results. Video-led with assignments. |

**The spine.** 6.002 Circuits and Electronics (MIT, Agarwal) → 6.003 Signals
and Systems (MIT, Freeman) with Oppenheim's RES.6-007 as the companion →
Control Engineering (NPTEL, Pasumarthy) → 6.012 Microelectronic Devices and
Circuits (MIT) → then branch: Power Electronics (NPTEL, Umanand) for the
power track, or Principles of Communication Systems (NPTEL, Jagannatham) for
the communications track.

**Overlaps resolved.** *6.002 beats NPTEL's circuits courses as a first
course* — full video, full problem sets, full solutions, and Agarwal's
abstraction framing is the best conceptual scaffolding available. Krishnapura
is the fallback if you want more network-analysis drill. *Freeman beats
Oppenheim as the course you enrol in; Oppenheim beats Freeman as the lecturer
you listen to.* Use 6.003's problem sets and Oppenheim's explanations. *EPFL
DSP beats Dutta Roy for conceptual insight; Dutta Roy beats EPFL for filter
design practice.* If you only do one, do EPFL. *NPTEL wins power electronics
and power systems outright* — there is no serious free Western competition in
either subject, which is precisely the gap Western learners keep failing to
notice.

---

## 7. Civil and Structural Engineering

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 1.050 Engineering Mechanics I | MIT OCW | Markus J. Buehler | 45 | Statics and strength of materials from a civil-engineering starting point, with video lectures and problem sets. Buehler builds everything from the free-body diagram and equilibrium up, and is unusually good on **why the beam equations look the way they do** rather than just presenting them. |
| 3.091 Introduction to Solid-State Chemistry | MIT OCW | Donald Sadoway | 50 | Not a civil course, but the materials foundation for all of engineering, and Sadoway's lectures are among the most celebrated ever recorded at MIT — bonding, crystal structure, defects, diffusion, phase diagrams, mechanical behaviour, all with a showman's sense of pace. Video plus problem sets and exams. **Take the lectures on crystal defects and on phase diagrams even if you skip everything else** — they explain why materials fail. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Structural Analysis I | NPTEL | — | 45 | Determinate and indeterminate structures, influence lines, force and displacement methods, moment distribution. NPTEL runs several parallel structural analysis courses from different IITs at similar quality; take whichever current run has the best assignment schedule. Video-led with assignments. |
| Advanced Structural Analysis | NPTEL / IIT Madras | Devdas Menon | 50 | The standout. Menon wrote the standard Indian structural analysis textbook and the lectures are rigorous, matrix-methods-heavy and complete — stiffness and flexibility methods done properly, which is what you need before touching any structural software. The **matrix stiffness method lectures** are the best free treatment I know of. Video-led. |
| Soil Mechanics / Geotechnical Engineering | NPTEL | — | 45 | Soil classification, effective stress, permeability, consolidation, shear strength, earth pressure, bearing capacity. Multiple IIT versions exist at comparable quality. Geotechnical engineering is essentially unavailable free outside NPTEL — this is another gap NPTEL uniquely fills. Video-led with assignments. |
| Transportation Engineering | NPTEL / IIT Bombay | Tom V. Mathew | 35 | Traffic flow theory, highway geometric design, pavement design, transport planning. Mathew's accompanying free lecture notes are widely used as a reference in their own right and are worth having regardless of whether you watch the videos. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Design of Reinforced Concrete Structures | NPTEL | — | 45 | Limit state design of beams, slabs, columns, footings. Code-based and therefore written to Indian standards — the design philosophy transfers cleanly, the specific code clauses do not. Know that going in. Video-led. |
| 1.011 Project Evaluation and Project Management | MIT OCW | — | 30 | Cost-benefit analysis, discounting, risk, public infrastructure decision-making. Materials-only. The subject civil engineers most often need and least often study. Unglamorous and genuinely useful. |

**The spine.** 1.050 Engineering Mechanics I (MIT, Buehler) → 3.091 Solid-State
Chemistry (MIT, Sadoway) → Structural Analysis I (NPTEL) → Advanced Structural
Analysis (NPTEL, Menon) → Soil Mechanics (NPTEL) → Design of Reinforced
Concrete Structures (NPTEL).

**Overlaps resolved.** *MIT 1.050 and MIT 2.001 substantially overlap* — both
are statics plus mechanics of materials. Pick one: 1.050 if you are heading
civil (video, structural framing), 2.001 if you are heading mechanical (better
problem sets). *Menon beats every other structural analysis course free or
paid* on matrix methods; the introductory NPTEL courses are prerequisites, not
competitors. *NPTEL dominates this entire division.* MIT publishes almost no
undergraduate civil design coursework, TU Delft's civil offerings are mostly
paid, and Coursera's civil catalogue is thin. If you want civil engineering
free, you are going to be watching IIT lectures, and you should be glad they
exist.

---

## 8. Chemical Engineering

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Fundamentals of Transport Processes I | NPTEL / IISc Bangalore | V. Kumaran | 50 | The best free transport phenomena course. Kumaran teaches momentum, heat and mass transfer as one unified subject built on shell balances and scaling arguments, which is the right way and the way Bird, Stewart and Lightfoot do it. Demanding and mathematically honest. Video-led with assignments. |
| 10.213 Chemical and Biological Engineering Thermodynamics | MIT OCW | — | 45 | Chemical thermodynamics — equations of state, phase equilibrium, chemical equilibrium, activity coefficients. Materials-only with problem sets and solutions. The prerequisite for everything else in the division. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Fundamentals of Transport Processes II | NPTEL / IISc Bangalore | V. Kumaran | 50 | Continuation into boundary layers, turbulent transport, multicomponent diffusion. Take it — transport is the core of the discipline and one course does not cover it. |
| Chemical Reaction Engineering | NPTEL / IISc Bangalore | Jayant M. Modak | 45 | Rate laws, ideal reactors, non-ideal flow, catalysis, reactor design. Clear, well-paced and complete. Video-led with assignments. The natural companion to Kumaran's transport sequence — between them, IISc gives you the two pillars of chemical engineering free. |
| 10.37 Chemical and Biological Reaction Engineering | MIT OCW | William H. Green | 45 | MIT's version, materials-only but with strong problem sets, and stronger than Modak's on **kinetics and mechanism** — how you actually derive a rate law from a proposed mechanism. Green is a combustion kineticist and it shows. Use Modak's videos for instruction and Green's problem sets for practice. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 10.302 Transport Processes | MIT OCW | — | 45 | Heat and mass transfer with the MIT problem sets. Materials-only. Overlaps Kumaran heavily; take it for the homework, not the coverage. |
| Process Control / Process Design (NPTEL, various IITs) | NPTEL | — | 40 | Process control and plant design are the two subjects that turn coursework into an engineer, and NPTEL is close to the only free source. Several parallel offerings exist across IIT Bombay, Kharagpur and Madras at comparable quality; pick by current run schedule. Video-led with assignments. Be aware that process design courses lean on simulation software you may not have. |

**The spine.** 10.213 Chemical and Biological Engineering Thermodynamics (MIT)
→ Fundamentals of Transport Processes I (NPTEL/IISc, Kumaran) → Fundamentals
of Transport Processes II (Kumaran) → Chemical Reaction Engineering
(NPTEL/IISc, Modak) with 10.37's problem sets → Process Control (NPTEL).

**Overlaps resolved.** *Kumaran beats MIT 10.302* as the transport course you
learn from, because it has video, is unified across momentum-heat-mass, and is
taught by someone who thinks in scaling arguments. Use 10.302 only as a
problem bank. *Modak and Green split the reaction engineering job* — Modak
lectures better, Green assigns better. Run both. *This division has the
thinnest free coverage of any engineering discipline here.* Process design in
particular is barely available; expect to fill the gap with textbooks
(Seider, or Towler and Sinnott) rather than courses.

---

## 9. Aerospace Engineering

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| Introduction to Aeronautical Engineering | TU Delft via edX | Joris Melkert and colleagues | 35 | The best free aerospace introduction. Structured in blocks — history of flight, aerodynamics of airfoils and wings, flight mechanics across climb, cruise and descent. Delft's aerospace faculty is among the world's strongest and the production is excellent. Audit-free with the graded work gated. |
| Introduction to Aerospace Engineering — Flight | NPTEL / IIT Bombay | Rajkumar S. Pant | 30 | Ten two-lecture capsules covering the whole field at survey level. Pant is an aircraft design specialist and the course is notably good on **how an aircraft configuration is actually chosen** — the tradeoffs, not just the physics. Video-led. Good complement to the Delft course, which is stronger on aerodynamics and weaker on design reasoning. |
| Introduction to Aerospace Structures and Materials | TU Delft via edX | René Alderliesten | 30 | Structural design and material selection for airframes — loads, fatigue, composites, damage tolerance. Fills the structures half that most aerospace introductions skip. Audit-free. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 16.07 Dynamics | MIT OCW | — | 45 | Particle and rigid-body dynamics with an orbital-mechanics emphasis — two-body problem, orbit transfer, rigid body rotation, gyroscopics. Materials-only with problem sets. The prerequisite for anything spacecraft-related. |
| 16.06 Principles of Automatic Control | MIT OCW | — | 40 | Classical control taught for flight vehicles — root locus, Bode, stability margins, aircraft dynamic modes. Materials-only. Take the generic NPTEL control course instead if you want video; take this if you want the aerospace framing and the problem sets. |
| Rocket Propulsion | NPTEL / IIT Madras | K. Ramamurthi | 45 | Excellent and unmatched in free material. Motion in space, the rocket principle, nozzles, chemical propellants, solid and liquid and hybrid and monopropellant rockets, combustion instability, electric propulsion. Ramamurthi worked at ISRO before IIT Madras and the course carries real design experience. Video-led. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 16.100 Aerodynamics of Viscous Fluids | MIT OCW | Mark Drela | 45 | Drela wrote XFOIL and AVL — the airfoil and aircraft analysis tools that half the small-aircraft and UAV world runs on. Boundary layers, transition, separation, drag prediction. Materials-only, no video, and hard. The **lecture notes are effectively a short textbook** by a leading practitioner and are worth downloading whether or not you take the course. |
| 16.885J Aircraft Systems Engineering | MIT OCW | Jeffrey Hoffman, Aaron Cohen | 30 | A systems-engineering course taught entirely as a Space Shuttle case study, with **video lectures by the engineers and astronauts who actually built and flew it** — including Hoffman, a five-flight Shuttle astronaut, and Cohen, former Johnson Space Center director. Historically remarkable and pedagogically excellent. Take it even if you have no aerospace ambitions; it is the best available course on how large engineering systems really fail and succeed. |
| Space Mission Design and Operations | EPFL via edX | Claude Nicollier | 30 | Nicollier flew four Shuttle missions including a Hubble servicing EVA. Orbital mechanics, mission phases, launch, rendezvous, re-entry. Audit-free. Pairs naturally with 16.885J. |

**The spine.** Introduction to Aeronautical Engineering (TU Delft) →
Introduction to Aerospace Structures and Materials (TU Delft) → 16.07 Dynamics
(MIT) → Rocket Propulsion (NPTEL, Ramamurthi) → 16.885J Aircraft Systems
Engineering (MIT, Hoffman and Cohen) → 16.100 Aerodynamics of Viscous Fluids
(MIT, Drela).

**Overlaps resolved.** *Delft beats Pant's NPTEL course as the first aerospace
course* on production, structure and aerodynamic depth; take Pant afterwards
for the design-reasoning material Delft omits. *Ramamurthi beats everything on
propulsion* — MIT's propulsion coursework is fragmentary on OCW and the
Coursera offerings are shallow. *16.885J is not really an aerospace course and
that is why it is on the spine* — it is the best free systems-engineering
education available, dressed as a Shuttle retrospective. *Skip generic
"introduction to rocket science" MOOCs entirely*; they cover in six hours what
Ramamurthi covers properly in forty-five.

---

## 10. Biomedical Engineering

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| BENG 100 Frontiers of Biomedical Engineering | Yale (Open Yale Courses) | W. Mark Saltzman | 35 | Filmed lectures, transcripts, syllabus, problem sets and exams. Saltzman surveys the whole field — biomechanics, biomaterials, imaging, drug delivery, tissue engineering, bioelectricity — at a level a first-year can follow without dumbing it down. The best free entry point to the discipline and the only one with a full open-courseware treatment. |
| 7.01SC Fundamentals of Biology | MIT OCW | — | 60 | Not a BME course, but you cannot do biomedical engineering without biochemistry, genetics and molecular biology, and most engineering students arrive without them. OCW Scholar format: video lectures, problem sets, exams, solutions. Do this before the core courses if your biology is thin. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 20.310J Molecular, Cellular, and Tissue Biomechanics | MIT OCW | — | 45 | Mechanics of biological materials from molecules up — polymer elasticity, cytoskeletal mechanics, cell adhesion and motility, tissue-level constitutive behaviour. Materials-only with problem sets. The most quantitatively serious free BME course. |
| 6.021J / 2.791J Quantitative Physiology: Cells and Tissues | MIT OCW | — | 45 | Membrane biophysics, transport, the Hodgkin-Huxley model, action potentials, muscle contraction. Materials-only. This is where physiology becomes differential equations, and it is the foundation of neural engineering and bioelectronics. |
| HST.542J Quantitative Physiology: Organ Transport Systems | MIT OCW | Roger Mark and colleagues | 45 | The organ-system counterpart from the Harvard-MIT Health Sciences and Technology program — cardiovascular and respiratory mechanics modelled quantitatively. Materials-only. HST courses are taught to a mixed audience of engineers and medical students and are consistently among OCW's best-designed publications. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| BE.441 / 2.79J Biomaterials-Tissue Interactions | MIT OCW | Ioannis V. Yannas | 40 | Yannas co-invented artificial skin — this is the person who did the foundational work teaching the subject he founded. Host response to implants, scaffold design, regeneration versus repair. Materials-only, reading-heavy, and the reading list is largely primary literature. |
| Biomedical Signal Processing | NPTEL / IIT Kharagpur | — | 40 | ECG, EEG and EMG acquisition, filtering, feature extraction, artefact removal. The applied instrumentation side that MIT's OCW BME catalogue largely skips. Video-led with assignments. Take after a general signals and systems course. |

**The spine.** BENG 100 Frontiers of Biomedical Engineering (Yale, Saltzman) →
7.01SC Fundamentals of Biology (MIT) if needed → 6.021J Quantitative
Physiology: Cells and Tissues (MIT) → 20.310J Molecular, Cellular, and Tissue
Biomechanics (MIT) → HST.542J Quantitative Physiology: Organ Transport Systems
(MIT) → BE.441 Biomaterials-Tissue Interactions (MIT, Yannas).

**Overlaps resolved.** *Saltzman's Yale course beats every "introduction to
biomedical engineering" MOOC* — it is a real course with real exams and full
video, and the MOOC competition is mostly career-orientation content with a
thin technical layer. *MIT's OCW BME catalogue is materials-only across the
board*, so expect no video after the Yale course; this is the price of the
best free BME coursework existing at MIT rather than on a video platform.
*NPTEL is weaker here than in the other engineering divisions* — biomedical
instrumentation is covered, but the quantitative physiology and biomaterials
teaching at MIT has no NPTEL equivalent.

---

## 11. Energy and Environmental Engineering

### Introductory

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 22.081J / 2.650J Introduction to Sustainable Energy | MIT OCW | — | 40 | A quantitative survey of the whole energy system — resources, conversion technologies, economics, environmental impact, policy. Materials-only. What makes it good is that it is **numerate**: it makes you calculate whether a technology can plausibly scale rather than describe it. That skill separates useful energy thinking from the rest. |
| Solar Energy Engineering | TU Delft via edX | Arno Smets | 40 | Outstanding, and the single best free renewable-energy course. Semiconductor physics of the solar cell, cell and module design, PV system engineering, sizing. Smets is an excellent lecturer and the accompanying textbook, *Solar Energy*, is **freely downloadable** — an unusually generous package. Audit-free. |

### Core

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 2.60J Fundamentals of Advanced Energy Conversion | MIT OCW | — | 45 | Thermodynamics and fluid mechanics applied to power cycles, combustion, fuel cells and conversion efficiency. Materials-only with problem sets. The engineering course that sits underneath all the survey courses. Requires thermodynamics first. |
| Wind Energy | TU Delft via edX | — | 30 | Rotor aerodynamics, turbine design, wind resource assessment, offshore siting, grid integration. Delft is one of the two or three leading wind research institutions in the world. Audit-free. The natural pairing with Smets's solar course. |
| Introduction to Drinking Water Treatment | TU Delft via edX | — | 30 | Coagulation, sedimentation, filtration, disinfection, distribution — the actual unit processes of a treatment plant. Delft's water group is world-leading and this is genuinely a professional-level introduction. Audit-free. Sister courses cover urban sewage treatment. |

### Advanced

| Course | Institution | Instructor | Hrs | Notes |
|---|---|---|---|---|
| 1.061 Transport Processes in the Environment | MIT OCW | — | 40 | Diffusion, dispersion and advection in rivers, groundwater, lakes and the atmosphere — how contaminants actually move. Materials-only with problem sets. The quantitative core of environmental engineering, and much more rigorous than the sustainability survey courses. |
| 12.340 Global Warming Science | MIT OCW | — | 35 | Radiative transfer, climate feedbacks, ocean circulation, carbon cycle, model structure. Materials-only. Physics, not policy — take it if you want to be able to evaluate climate claims from first principles rather than repeat them. |

**The spine.** 22.081J Introduction to Sustainable Energy (MIT) → Solar Energy
Engineering (TU Delft, Smets) → 2.60J Fundamentals of Advanced Energy
Conversion (MIT) → Wind Energy (TU Delft) → 1.061 Transport Processes in the
Environment (MIT) → 12.340 Global Warming Science (MIT).

**Overlaps resolved.** *MIT beats Delft on the physics and the assignments;
Delft beats MIT on the technologies and the video.* Use MIT for the
quantitative core and Delft for solar, wind and water, where MIT publishes
little at undergraduate level. *Smets's solar course beats every other free
renewables course* by a wide margin, largely because of the free textbook.
*Avoid the large population of free "sustainability" and "climate leadership"
MOOCs* — they are policy-literacy courses wearing engineering clothes and will
not teach you to size a system or run an energy balance.

---

## Cross-cutting notes

**What is missing and cannot be fixed from this list.** Mathematics. Every
engineering division above assumes single- and multivariable calculus,
differential equations and linear algebra. MIT OCW's 18.01SC, 18.02SC, 18.03SC
and 18.06 (Gilbert Strang's linear algebra) are all Scholar-format with video
and full problem sets, and they are the best free mathematics courses in
existence. Do them first or you will stall in week three of anything on this
list.

**Physics.** MIT OCW's 8.01 and 8.02 are the standard route. Note that Walter
Lewin's celebrated lecture videos were removed from MIT's platforms in 2014;
current OCW physics uses other instructors. Unofficial mirrors of the Lewin
lectures circulate but I would not build a curriculum on them.

**A pattern worth internalising.** Across nearly every engineering division,
the best free setup is the same: **watch NPTEL or a MOOC for instruction, do
MIT OCW problem sets for practice.** Video courses teach; published problem
sets with solutions are what actually convert watching into competence. Most
self-directed learners do only the first half and then wonder why the material
did not stick.

**On NPTEL specifically.** It is the largest engineering course catalogue on
earth and Western learners systematically ignore it because of the production
values and the accents. That is a costly mistake. NPTEL is the only free
source of serious coverage in power systems, power electronics, geotechnical
engineering, machine design, transportation engineering, process control and
rocket propulsion. The courses run on semester schedules with live assignment
windows, but the archived video and materials remain permanently accessible at
nptel.ac.in and archive.nptel.ac.in. Search both — the archive holds the older
full-length series, several of which are better than their modern
replacements.

---

