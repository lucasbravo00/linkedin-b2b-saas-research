# LinkedIn Organic Content Strategy for B2B SaaS — Playbook / SOP

**Author:** Lucas Bravo · **Version:** 1.1 · **Date:** August 2026 (corpus collected June 2026)
**Evidence base:** 25 LinkedIn posts, 4 video transcripts (~37,500 words) and 1 algorithm report, all in [`/research`](../research). Sources and selection logic: [`research/sources.md`](../research/sources.md).

---

## How to read this document

**Every recommendation carries its source inline**, in the form
`(source: Author, URL — DD.MM.YYYY)`. The date is the publication date of the cited post or video, not the date I collected it.

Three conventions matter:

- **`[SYNTHESIS]`** marks a recommendation I assembled from several sources where no single expert says the thing directly. The parts are cited; the assembly is mine.
- **`[ORIGINAL]`** marks something I did not find in the corpus at all. Full reasoning in [§8](#8-my-original-ideas).
- **`[WEAK EVIDENCE]`** marks a recommendation I am keeping despite a problem with its source — an untested claim, a paid partnership, a stale transcript, or a number I could not verify. The problem is always named on the spot.

One note on quotations: the four video transcripts are auto-generated speech, so quotes from them are lightly cleaned of filler words ("like", "you know") and transcription stutters, with the wording otherwise untouched. Written posts are quoted verbatim, including their errors (marked [sic] where relevant).

Where the corpus contradicts itself, I do not average the advice. I pick a side and say why ([§6](#6-where-experts-disagree)).

**Scope.** This playbook is for a B2B SaaS company between roughly $0 and $30M ARR where a founder or executive is willing to write in public under their own name. It is not a general "grow on LinkedIn" guide, and [§0](#0-before-you-start-the-channel-fit-gate) exists to tell some readers to stop reading.

---

## 0. Before you start: the Channel Fit Gate

**`[ORIGINAL]`** — Nothing in the corpus does this, and that absence is the point. Reasoning in [§8.1](#81-the-channel-fit-gate).

Every expert in this corpus succeeded on LinkedIn. None of them can tell you what failure looks like, because none of them experienced it. The single exception is one throwaway line from Adam Robinson, who — after describing going "psychotic" to become the best content creator on LinkedIn — stops to say:

> "I am in a perfect situation with respect to LinkedIn, meaning I am my ICP and my ICP lives on LinkedIn because we're selling to revenue leaders. If you're selling to hospitals I would not recommend going psychotic like I did in trying to be literally the best content creator on LinkedIn. Not worth it."
> (source: Adam Robinson, https://www.youtube.com/watch?v=6PmFWV0DRj0 — 15.05.2024)

He says it once and moves on. Nobody in the corpus builds on it. So here is the gate:

**Score each item 0 or 1. Run this playbook only at 4+.**

| # | Question | Score 1 if… |
|---|---|---|
| 1 | **Are you your own ICP?** | You have personally held the job you are selling to, within ~5 years. |
| 2 | **Does your ICP post, comment, or lurk on LinkedIn weekly?** | You can name 20 real target-account individuals and find recent LinkedIn activity for at least 10. |
| 3 | **Is your deal size worth the time?** | ACV × realistic close rate justifies ~10 founder-hours/week ([§3](#3-production-what-the-week-actually-looks-like)) for 12 months before payback. |
| 4 | **Is there a person willing to be the face?** | A named founder/exec will publish under their own name and be publicly wrong sometimes. Not "the company page." |
| 5 | **Can you survive 12 months of no attributable pipeline?** | Runway and management patience both extend past a year. |

**Scoring 0–1 on Q1 or Q2 is disqualifying regardless of total.** If your buyer is a hospital procurement officer, a shop-floor manager, or a municipal clerk, the honest answer is that this playbook is not for you — run the same effort into the channel where those people actually are.

Why the gate is placed first: item 5 is the one that kills programs. Robinson is explicit that it took him twelve months to get traction, and he credits the framing to Devin Reed: *"Devin Reed has this idea of content market fit, and getting content market fit I think is as hard as product market fit for a startup"* (source: Adam Robinson, https://www.youtube.com/watch?v=6PmFWV0DRj0 — 15.05.2024). A team that has not consciously agreed to a twelve-month horizon will cancel the program at month five, having paid the entire cost and collected none of the return.

---

## 1. Positioning: decide what you are known for

You cannot execute a content system before you know what argument you are making. The failure this playbook most expects is not a production failure — it is posting competently about nothing in particular.

### 1.1 Pick one of three positioning strategies

Anthony Pierri reduces positioning to three, with explicit selection criteria:

1. **Position in a mature category against existing vendors.** Upside: "Customers already have budget for it, actively search for it, and don't need educating." Risk: entrenched players. Choose it if the category is large enough for your growth goals *and* you can compete head-to-head — or you deliberately target an underserved subsegment.
2. **Take a small existing category to a new audience.** Less direct competition, but you inherit the category's reputation and must educate the market. His examples: DocuSign did not invent e-signature; Dropbox did not invent file sharing.
3. **Create your own category.** Full control of the framing, but "first movers rarely win (Airbnb beat Vrbo, Google beat AltaVista)," and incumbents copy proven blueprints — "as Microsoft did to Slack."

(source: Anthony Pierri, https://www.linkedin.com/posts/anthonypierri_people-overcomplicate-positioning-there-activity-7468383258863423488-Phf2 — 04.06.2026)

**Recommendation:** default to strategy 1 with a deliberately narrow subsegment. Strategies 2 and 3 both require years of market education, which collides directly with Gate item 5. Pierri himself notes that category creation demands you be "prepared to invest years building awareness from scratch."

### 1.2 Know which question your market is actually asking

Before writing a single post, determine whether your buyer is asking *"why this category?"* or *"why you?"* Pierri frames it as two mutually exclusive messaging modes:

- **Immature market → "WHY AI?"** — the audience does not know the category exists. His example of this mode is Notion's "agents capture knowledge, answer questions, and push projects forward — all while you sleep," a definition that "could apply to every other agent on the market," and therefore only works on an audience unaware of the alternatives.
- **Mature market → "WHY OUR AI?"** — the audience is already evaluating competitors, so you must differentiate at the mechanism level. His example is Octonomy's "The best AI platform for complex knowledge. 95% accuracy. No hallucinations."

(source: Anthony Pierri, https://www.linkedin.com/posts/anthonypierri_ai-companies-are-your-prospects-asking-activity-7458172886483189760-6kmU — 07.05.2026)

Getting this backwards is the most common failure Pierri finds in teardowns: companies in crowded categories writing outcome-level copy that never says what the product does differently. Reviewing a YC company scoring 3/5, he writes: *"they need to immediately explain at a capability level how their product is different — not just in the outcomes, but in the MECHANISM"*
(source: Anthony Pierri, https://www.linkedin.com/posts/anthonypierri_i-ranked-five-y-combinator-startup-homepages-activity-7467936879464783872-nsQk — 03.06.2026).

### 1.3 Do not hide the product behind outcomes

There is a widespread piece of advice — "nobody cares about your product, just talk about outcomes" — that Pierri calls out by name as bad advice when the market is mature: *"I'm guessing this company got the (BAD!) advice that 'nobody cares about your product! Just talk about outcomes you drive!'"*
(source: Anthony Pierri, https://www.linkedin.com/posts/anthonypierri_i-ranked-five-y-combinator-startup-homepages-activity-7467936879464783872-nsQk — 03.06.2026).

**Recommendation:** in a category with named competitors, lead with mechanism. Outcome-only messaging is for markets that do not yet know the category exists.

---

## 2. What to actually make

### 2.1 The two formats that carry the program

Fletch built its content programme on two formats, which Pierri credits explicitly to Wes Kao:

> "We follow this lady named Wes Kao… She had these two concepts that were so game-changers for us at the very beginning… One of them she calls the super specific how, which is explaining how to do something at a great, great level of detail. […] Those two concepts, spiky opinion, super specific how, have been like a North Star since the beginning."
> (source: Anthony Pierri, https://www.youtube.com/watch?v=0OtTo6yMmZk — 02.01.2025)

**Format A — Spiky opinion.** A position that a competent peer could disagree with. Pierri's examples of the genre are Robinson's "don't take VC money" and Jason Fried's "keep your company small" — *"all these things are contrary to what most people think, and so it creates this audience."* He also notes a sub-variant that performs: making the point through humour, "poking fun at bad advice… almost like memes" (source: Anthony Pierri, https://www.youtube.com/watch?v=0OtTo6yMmZk — 02.01.2025).

The test for whether an opinion is actually spiky: **could a reasonable expert in your field publicly argue the opposite?** If not, it is a platitude. "Ship fast" is not spiky. "Your product managers may be silently destroying your ability to go to market" is — and Pierri runs exactly that argument, connecting Marty Cagan's four product risks to positioning damage (source: Anthony Pierri, https://www.linkedin.com/posts/anthonypierri_your-product-managers-may-be-silently-destroying-activity-7457088895650910208-a6AL — 04.05.2026).

**Format B — Super specific how.** Teach one thing at a depth that would be irresponsible to give away, using named real companies rather than hypotheticals. Pierri's homepage teardown scores five real named startups 0–5 with stated criteria (source: Anthony Pierri, https://www.linkedin.com/posts/anthonypierri_i-ranked-five-y-combinator-startup-homepages-activity-7467936879464783872-nsQk — 03.06.2026). Emily Kramer's LLM-crawling explainer walks through three CMS architectures with a stated verdict on each (source: Emily Kramer, https://www.linkedin.com/posts/emilykramer_framerpartner-activity-7467276044736253952-AA6A — 01.06.2026).

**Recommendation:** run roughly two "super specific how" posts for every one "spiky opinion." Spiky opinions earn reach; specific how-tos earn the follow. A feed of pure contrarianism reads as a person with opinions and no job.

### 2.2 Research-as-content: the highest-leverage format available

The single strongest format in the corpus is original research, because it produces a claim nobody else can make. Emily Kramer's example:

> "Only 39 out of 100 B2B companies with a demo request flow let you book a meeting on the spot."

She states her method in the post itself — *"We extended our MKT1 State of Marketing research in Claude and went through the 100 high-growth B2B companies with demo request flows"* — which is what makes the number usable rather than decorative.
(source: Emily Kramer, https://www.linkedin.com/posts/emilykramer_revenueheropartner-activity-7470886898958315520-wQim — 11.06.2026)

**`[WEAK EVIDENCE]`** — That same post is a paid placement. The URL slug is `revenueheropartner`, it recommends a specific vendor, and it closes with an affiliate discount. The *method* is sound and worth copying; the *conclusion* is sponsored. See [§7.4](#74-rejected-kramers-vendor-recommendation-keep-the-method) for what I do with that.

**Recommendation:** commit to one original research piece per quarter. Pick a question you can answer by examining 50–100 public artifacts (pricing pages, onboarding flows, job postings, docs sites) and publish the method alongside the finding. This is the only format in the corpus where the moat is the work itself.

### 2.3 Vulnerability, with a specific definition

Robinson's differentiator is disclosure that costs him something:

> "It's like things that I would share with my wife, maybe not even my employees, but like things that I would tell my best friend, and I'm sitting here writing it, sending it into the world."
> (source: Adam Robinson, https://www.youtube.com/watch?v=6PmFWV0DRj0 — 15.05.2024)

Executed in practice: *"Last Wednesday I gave up on my new startup MoltSets entirely. I was devastated. Today, I think it's a $10m ARR biz because of ONE CHANGE we made to the offer"* — followed by the actual pricing mistake, the actual customer feedback that corrected it ("There's probably 10-30 people who would pay $500/mo for that"), and the reasoning (source: Adam Robinson, https://www.linkedin.com/posts/retentionadam_last-wednesday-i-gave-up-on-my-new-startup-activity-7468681453845983233-4HIm — 05.06.2026).

**The distinction that matters:** vulnerability is only content when the disclosure is *specific and costly*. "Building a company is hard!" costs nothing. A named pricing hypothesis you got wrong, with the number, costs something.

Amelia Sordell runs the same mechanic on a personal-history axis — "At 19, I was working 3 jobs. Had zero self-worth. And I was broke… At 35, I passed £3.8M in revenue" (source: Amelia Sordell, https://www.linkedin.com/posts/ameliasordell_at-19-i-was-working-3-jobs-had-zero-self-worth-activity-7465683347617243136-WYid — 28.05.2026). **`[WEAK EVIDENCE]`** — that same post later states "$4million in revenue," a different figure in a different currency for what reads as the same milestone. I would not cite either number as fact; the format is the lesson, not the metric.

### 2.4 Newsjacking, with a real time window

Lattanzio puts a number on the opportunity that most teams miss:

> "On LinkedIn, you're always days late. A story breaks on X, trends on Reddit, and by the time it hits your feed here, half your industry has already had the take. The window to be first is 24 to 48 hours."
> (source: Sara Stella Lattanzio, https://www.linkedin.com/posts/saralattanzio_that-little-girl-in-the-questionable-minnie-activity-7469728816962367488-phDm — 08.06.2026)

Thormeier's execution of the format is a good template: when LinkedIn hired a new CPO, he published a numbered wishlist that doubled as a demonstration of platform expertise — including the widely-known-but-rarely-stated point that *"everyone who knows Linkedin knows not to use the reshare button because it absolutely tanks engagement"* (source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_linkedin-just-hired-their-new-cpo-anthony-activity-7469694317117468672-ByKK — 08.06.2026).

**Recommendation:** newsjack only where you have standing to comment. The format rewards being early, but being early with no expertise is how a feed becomes noise.

### 2.5 Writing craft: the layer everyone assumes and nobody teaches

Wes Kao is the only source in the corpus operating at sentence level. Two rules worth adopting wholesale:

**Delete hedges.** Her list of nine words to cut includes *just*, *honestly*, *very/really/truly*, *however*, and double negatives — the reasoning for double negatives being that *"when you say 'not,' your reader has to think of what is — then think of the opposite. It adds cognitive load."*
(source: Wes Kao, https://www.linkedin.com/posts/weskao_to-improve-your-writing-delete-these-9-words-activity-7341112272137715713-Hus- — 18.06.2025)

**Replace authority with reasoning.** Her contrast:
> 🚫 "Trust me. I've done this many times."
> ✅ "I'm recommending X because [evidence, data points, thought process]. I saw something similar play out with [previous example]…"

(source: Wes Kao, https://www.linkedin.com/posts/weskao_trust-me-ive-done-this-many-times-activity-7325892206081318913-7dVf — 07.05.2025)

This second rule is the highest-value item in the entire corpus for a founder with no audience yet, and it is the reason this playbook prefers reasoning-led posts over credential-led ones. You do not have authority yet. You do have logic.

---

## 3. Production: what the week actually looks like

### 3.1 Budget the real number

Fletch's cost per post, stated plainly by Pierri and confirmed on the record in the same conversation: **90 minutes to 3 hours per post, ~2 hours average** — with the interviewer noting that daily posting would therefore be "10 hours you spend every week just creating LinkedIn content," and Pierri answering "sounds about right" (source: Anthony Pierri, https://www.youtube.com/watch?v=0OtTo6yMmZk — 02.01.2025).

The majority of that time goes to thinking and writing, not design.

**Recommendation:** budget 10 founder-hours per week, or reduce cadence until the arithmetic works. Do not budget 2 hours per week and expect Fletch's results — that mismatch is how the program fails silently, with quality eroding long before anyone decides to stop.

### 3.2 Schedule capture, not creation `[SYNTHESIS]`

The corpus appears to disagree sharply on planning discipline ([§6.1](#61-disagreement-rigid-calendar-vs-posting-from-the-hip)). It resolves once you notice what the loose operator is actually doing:

> "We each separately have just Apple Notes. If I were to open up my Apple Notes, you would see probably 1,300 entries, vignettes of ideas to come back to for when you get into that writing time."
> (source: Fletch — Anthony Pierri & Rob Kaminski, https://www.youtube.com/watch?v=0OtTo6yMmZk — 02.01.2025)

Fletch improvises the *schedule*, never the *inventory*. Thormeier's case study improvises neither — Tycho Luijten's team blocks a recurring 2.5-hour slot every two weeks, sets a 20-minute silent timer to generate ideas, then forces a decision: *"They now need to PICK an idea. No going back"* (source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_i-interviewed-tycho-luijten-one-of-the-most-activity-7470797663593013249-MSi8 — 11.06.2026).

**Recommendation:** run a permanent capture file and add to it daily. Schedule *creation* blocks; do not schedule *topics* more than a week out. A content calendar filled with titles invented a month ago is how teams end up publishing things they no longer believe.

### 3.3 Script anything with a camera in it

For video specifically, Thormeier's case study is unambiguous:

> "The script is everything. A good idea with a bad script is a bad video."

The same team splits output into a "hero video" with real production and other people involved (half a day to a full day of shooting) and a "lean and mean" video recorded on a phone, and explicitly does *not* "wake up in the morning and hope they have a funny idea."
(source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_i-interviewed-tycho-luijten-one-of-the-most-activity-7470797663593013249-MSi8 — 11.06.2026)

### 3.4 Where AI belongs — and the one place it does not

The clearest operating rule in the corpus comes from Emily Kramer's workflow, documented by Thormeier. She uses Claude for: analysing large raw inputs (crawling hundreds of B2B startup sites for a research piece), restructuring messy notes, tightening paragraphs she has already drafted, a custom copy-editing skill for final review, adding links, and writing subject lines — noting Claude is better at subject lines because *"Claude doesn't get self-conscious about just leading with the strongest statement."*

And then the exclusion, stated as a hard line:

> "What she doesn't use Claude for: writing the first full draft of her newsletter."

(source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_how-emily-kramer-uses-claude-code-to-write-activity-7470408576868720640-QY1H — 10.06.2026)

Dave Gerhardt describes the same shape from the other side. His newsletter takes "two hours plus to really write a good one," and his process is to hand Claude the podcast transcript, prior related pieces, an example of what good looks like, and background — then have it come back with questions:

> "This is where Claude is amazing. It's like having a creative agency partner on the side."

He is emphatic that this is not one-shotting: *"I didn't just give it to AI and one-shot it and we have some shitty newsletter that we're putting out."*
(source: Dave Gerhardt, https://www.youtube.com/watch?v=obXLy-AU5m4 — 12.05.2026)

**Recommendation:** adopt Kramer's line verbatim. AI for research, structure, editing, and packaging; never for the first draft and never for the point of view. See [§6.3](#63-disagreement-how-much-ai-belongs-in-production) for the disagreement this resolves.

### 3.5 Stop over-editing

Devin Reed's answer to what makes content work:

> "The first is to stop overediting. There's like messaging by committee, which waters it down. And I've also seen great ideas get overedited by like even one or two people. And what happens accidentally is you strip out that passion and the rawness and some of the little mistakes."
> (source: Devin Reed, https://www.youtube.com/watch?v=df3t4BNBRmI — 25.09.2025)

This sits in genuine tension with Kao's argument against shipping sloppy work ([§6.2](#62-disagreement-consistency-vs-craft)). My reading: Reed is talking about *voice*, Kao about *rigour*. Remove committee smoothing; do not remove proofreading.

---

## 4. Distribution

### 4.1 Format choice is a reach decision

**`[WEAK EVIDENCE — see §11]`** From van der Blom's 2025 Algorithm Insights Report, as summarised in this repo: document carousels (PDFs) reach ~6.60% engagement, the highest of any format, while a single external link in the post body costs ~18.8% of median reach. Organic reach is reported down ~50% year over year, engagement down ~25%, follower growth down 59%.
(source: Richard van der Blom, https://sales.richardvanderblom.com/content-algorithm-playbook/ — October 2025, via [`research/other/richard-van-der-blom-algorithm-insights-report.md`](../research/other/richard-van-der-blom-algorithm-insights-report.md))

I flag this as weak evidence not because I doubt van der Blom — he is the most rigorous source in the corpus — but because **what this repo holds is a 17-line secondhand summary, not the report.** I have not read the primary document. Anyone relying on these specific percentages should.

**Recommendation:** keep links out of the post body and put them in the first comment or the following-up newsletter. This costs nothing even if the 18.8% figure is imprecise, which is the correct way to act on an unverified number.

### 4.2 Reach the buying committee, not just the buyer

The most strategically interesting idea in the corpus is Thormeier's proposal for enterprise deals: rather than one founder posting for everyone, have each of your executives publish for their counterpart on the buying committee.

> "We now take our own CFO and create thought leadership content from her perspective and publish it on her LinkedIn. It's not content that a CISO will find interesting, but other CFOs will. Now we do the same thing for our own CTO, CIO, CEO, Head of Procurement, Head of Legal…"

Then connect each executive to their 500 counterparts across the target account list, and use LinkedIn's Thought Leader ads to guarantee distribution. His production mechanism keeps the executive cost at roughly one hour per week: interview each exec for an hour every two weeks in an "internal podcast," then *"pull video clips and text posts that we prepare into almost-done LinkedIn posts for them. All they need to do is look over the posts, make a couple changes, and publish."*
(source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_one-strategy-im-dying-to-try-at-an-enterprise-activity-7471171087670874113-wUvp — 12.06.2026)

**`[WEAK EVIDENCE]`** — This is a hypothesis, not a case study, and Thormeier says so twice in his own post: it opens with *"One strategy I'm DYING to try"* and closes with *"No large B2B company is actually doing this."* It is the best untested idea in the corpus. Treat it as a well-reasoned bet, not a proven play, and pilot it on a single executive pair before staffing it.

### 4.3 Repurpose from a hero asset, on a real clock

Reed's system: record once, distribute many times, on a fixed turnaround.

> "Talk for 5 to 10 minutes about why I think whatever I think about it, ship that to our team, and have them chop it up, put it into a YouTube video, the podcast, and clips like 24, 36 hours later."

His phase-one plan was pure repurposing — "three shorts per day for 3 months on YouTube, Instagram and TikTok" — drawn from an existing library of roughly 15 hours of produced material.
(source: Devin Reed, https://www.youtube.com/watch?v=df3t4BNBRmI — 25.09.2025)

Reed also flags a counterintuitive winner: a blooper reel from one of his videos outperformed the original by "three, four, five times." He credits the explanation to his then-advisor "Chris Lockhead" (the transcript's spelling — most likely Christopher Lochhead, the category-design author): *"the content about the content is the stuff people want"* (source: Devin Reed, https://www.youtube.com/watch?v=df3t4BNBRmI — 25.09.2025).

### 4.4 Own the endpoint

LinkedIn is rented. Gerhardt runs Exit Five's actual measurement on owned channels — *"list growth, engagement, opens, clicks, replies, unsubscribe rate"* — and is blunt that inside a media business those are the real metrics, not the ones B2B marketers are told to dismiss (source: Dave Gerhardt, https://www.youtube.com/watch?v=obXLy-AU5m4 — 12.05.2026).

**Recommendation:** every post should have somewhere to go. Newsletter subscription is the cheapest durable endpoint; Lattanzio closes her posts this way (source: Sara Stella Lattanzio, https://www.linkedin.com/posts/saralattanzio_that-little-girl-in-the-questionable-minnie-activity-7469728816962367488-phDm — 08.06.2026).

---

## 5. Measurement

### 5.1 Accept that attribution will not work, then measure anyway

Lattanzio's framing is the most useful in the corpus:

> "Last touch attribution is like giving the waiter credit for the meal. They're the last person you see before you pay, but that doesn't mean they cooked it."

She cites 92% of buyers already having a vendor in mind by the time they fill out a form, and reports lifts for accounts exposed to LinkedIn content — 46% higher paid search conversion, 43% better SDR meeting-to-deal, 112% lift in content marketing conversion — sourced to Factors.ai's LinkedIn benchmark report.
(source: Sara Stella Lattanzio, https://www.linkedin.com/posts/saralattanzio_last-touch-attribution-is-like-giving-the-activity-7471180380616863745-GdYn — 12.06.2026)

**`[WEAK EVIDENCE]`** — Lattanzio is careful in a way worth copying: she states that the underlying study measured *paid* LinkedIn content and marks her extension to organic as belief, not finding — *"I believe organic does even more heavy lifting."* Those three percentages should not be quoted as evidence for organic. I include them because her honesty about the gap is itself the lesson.

### 5.2 Run self-reported attribution — and know its limit

Gerhardt's method is the cheapest thing in this playbook:

> "We ask every single person that either joins our email list or joins our community, we say how did you hear about us."

And then, unprompted, the limitation:

> "Honestly, we don't learn that much from it other than it reaffirms what we're doing is already working."

(source: Dave Gerhardt, https://www.youtube.com/watch?v=obXLy-AU5m4 — 12.05.2026)

**Recommendation:** add the question to every signup form. It costs one field and gives you directional channel data no analytics tool can. But heed his second sentence: a measurement that only ever confirms you should continue is not a decision tool. Pair it with [§5.4](#54-set-a-kill-condition-in-advance).

### 5.3 Measure audience composition, not audience size

Robinson's stated numbers: roughly 75% of his audience matches his ICP, and about 85% of engagers are unique post to post.

**`[WEAK EVIDENCE]`** — In the same breath he is asked how it was measured and answers that someone else ran the analysis for him and he does not know the method. Treat 75% and 85% as illustrative of *what to care about*, not as benchmarks to hit.
(source: Adam Robinson, https://www.youtube.com/watch?v=6PmFWV0DRj0 — 15.05.2024)

**Recommendation `[SYNTHESIS]`:** once a month, take the 50 most recent people who engaged with your posts and hand-classify each as ICP / adjacent / irrelevant. Fifty rows takes twenty minutes and produces the only number that matters: are the right people showing up? This makes Robinson's metric reproducible, which his own account does not.

### 5.4 Set a kill condition in advance

**`[ORIGINAL]`** — a corollary of the Channel Fit Gate ([§8.1](#81-the-channel-fit-gate)). Nothing in the corpus specifies what result would justify stopping. Given a twelve-month commitment ([§0](#0-before-you-start-the-channel-fit-gate)), write down the failure condition before month one — for example: *"by month 9, fewer than 2 inbound conversations per month from classified-ICP individuals."* Decide the number while you are still objective about it.

---

## 6. Where experts disagree

Five real conflicts in the corpus. In each, I take a side.

### 6.1 Disagreement: rigid calendar vs. posting "from the hip"

**Finn Thormeier** documents a highly disciplined system: a recurring 2.5-hour slot every two weeks, always with the same two people, in a new coffee shop each time; a 20-minute silent timer for idea generation; a forced pick with "no going back"; then the script, written word for word. He is explicit about the anti-pattern: *"Here's what they DON'T do: wake up in the morning and hope they have a funny idea. Or go with any random idea that pops into their head. Or improvise."*
(source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_i-interviewed-tycho-luijten-one-of-the-most-activity-7470797663593013249-MSi8 — 11.06.2026)

**Anthony Pierri / Fletch** do close to the opposite. Asked whether they know what they are posting tomorrow, the answer is *"I do not."* Their description of their own process: *"very much from the hip in terms of planning. We don't overly orchestrate our content."* They defend it on the grounds that improvising keeps them close to live client problems — over-planning would mean *"we'll lose a grasp of what it's like to actually struggle with some of these things."*
(source: Fletch — Anthony Pierri & Rob Kaminski, https://www.youtube.com/watch?v=0OtTo6yMmZk — 02.01.2025)

**My position: Thormeier is right about video, Pierri is right about text — and the apparent conflict is mostly an illusion.** Pierri is not improvising from nothing. He is drawing from ~1,300 captured idea fragments in Apple Notes. The disagreement is not discipline vs. spontaneity; it is *when* the discipline is applied. Thormeier's team front-loads it into a scheduled decision meeting because video has a production tail — a bad idea costs a shoot day. Text has no such tail, so Fletch defers commitment to the last responsible moment and buys freshness with it.

**What I do:** capture daily and non-negotiably ([§3.2](#32-schedule-capture-not-creation-synthesis)); schedule creation blocks; commit to text topics no more than a week ahead; apply Thormeier's full timer-and-script ritual to anything requiring a camera. I side against pre-planned editorial calendars for text specifically, because Pierri's objection — drifting away from live market problems — is the failure mode I find most credible and the hardest to detect from inside.

### 6.2 Disagreement: consistency vs. craft

**Amelia Sordell** states a ratio: *"Building a personal brand is 10% quality content, but 90% consistency in posting it."* Her diagnosis of failure is entirely about persistence — *"most people fail because they never stick with anything long enough to win. Not because their content sucks. Not because the algorithm is broken. Because they're inconsistent."*
(source: Amelia Sordell, https://www.linkedin.com/posts/ameliasordell_1-doom-scrolling-if-youre-spending-hours-activity-7470746670398418945-ZyJA — 11.06.2026)

**Anthony Pierri** argues effort is the differentiator, not persistence: *"LinkedIn is more of a meritocracy than a lot of these platforms and it really is more like the higher effort wins… the bar is so unbelievably low on LinkedIn that if you just try a little harder than everyone else — don't try to automate it, don't try to write it just all with AI, all the hacks — just actually try to write something thoughtful and create a probably higher effort graphic to go along with it."* His revealed preference backs this: 90 minutes to 3 hours per post.
(source: Anthony Pierri, https://www.youtube.com/watch?v=0OtTo6yMmZk — 02.01.2025)

**Wes Kao** supplies the third position, against "done is better than perfect": *"If you make a sloppy attempt, is 'done' really better?"* — arguing poor execution is slower net-net because you will have to redo it or keep burning through new tactics.
(source: Wes Kao, https://www.linkedin.com/posts/weskao_we-all-love-the-phrase-done-is-better-than-activity-7308139027839242241-tLxH — 19.03.2025)

**My position: Pierri and Kao, decisively, for B2B SaaS.** The reason is audience size, and it is why Sordell's ratio can be true for her and wrong for you. Sordell operates a ~370k-follower general professional audience where the addressable pool is effectively unlimited and a weak post costs almost nothing. A B2B SaaS founder is addressing a few thousand people who could ever buy — sometimes a few hundred. In that regime a mediocre post is not neutral, it is a withdrawal: it teaches the exact people you need that reading you is optional.

**What I do:** treat cadence as an output of quality, not an input. Determine the highest quality bar you can sustain, then publish at whatever frequency that bar allows — even if that is twice a week. I keep Sordell's underlying point that *quitting* is the dominant failure mode, and address it with the sustainable-cadence rule rather than by lowering the bar.

### 6.3 Disagreement: how much AI belongs in production

**Adam Robinson** rejects it at the level of perspective: *"The LIE of AI is thinking that it can actually offer perspective… a lot of people, they're like, oh I'll start using it to post on LinkedIn, but people don't want that crap. People want a point of view."*
(source: Adam Robinson, https://www.youtube.com/watch?v=6PmFWV0DRj0 — 15.05.2024)

**Sara Stella Lattanzio** sits at the other end, publishing eight AI content-ops workflows including scheduled newsjacking that produces finished drafts before you open your laptop: *"Set it to run at 6am, research the latest news in your niche, and drop ready-to-edit LinkedIn post drafts into a folder."* She reports one such draft pulling 208K impressions for a client.
(source: Sara Stella Lattanzio, https://www.linkedin.com/posts/saralattanzio_anthropic-is-giving-paid-users-double-cowork-activity-7470093561720500224-njHp — 09.06.2026)

**Emily Kramer** draws an explicit boundary: heavy AI use across research, structuring, editing, linking and subject lines — but *"what she doesn't use Claude for: writing the first full draft."*
(source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_how-emily-kramer-uses-claude-code-to-write-activity-7470408576868720640-QY1H — 10.06.2026)

**Dave Gerhardt** adds a warning about the genre itself: *"If you go to YouTube and you type in Claude and marketing, you're going to see 20 videos that say 'I replaced my marketing team with Claude Code in 20 minutes'… there's a huge cash grab"* — and notes the gap between that content and what marketing leaders actually do.
(source: Dave Gerhardt, https://www.youtube.com/watch?v=obXLy-AU5m4 — 12.05.2026)

**My position: Kramer's line, adopted verbatim.** It is the only rule in the corpus stated precisely enough to follow, and it survives both critiques — Robinson's objection is to AI supplying the POV, which Kramer's rule forbids; Lattanzio's efficiency gains are almost entirely upstream of the draft, which Kramer's rule permits.

Two source-critical notes that shape this call. First, **Robinson's transcript is from May 2024** — the oldest item in the corpus by a year — so his position was formed against materially worse tools and should be weighted as a claim about *perspective*, which still holds, rather than about *capability*, which has moved. Second, Gerhardt's warning applies uncomfortably well to Lattanzio's own post, which is pegged to a promotional window ("double Cowork usage… until July 5") and is exactly the genre he describes. That does not make her workflows wrong — several are genuinely good — but it is why I take the boundary from Kramer, who is describing her actual practice, rather than from a post whose timing is set by a vendor promotion.

### 6.4 Disagreement: the founder's own voice vs. ghost-produced executive content

**Adam Robinson** and **Amelia Sordell** both locate the value in unmediated personal authorship. Robinson's standard is disclosure he would hesitate to make to his own employees ([§2.3](#23-vulnerability-with-a-specific-definition)); Sordell's is refusing to sound like anyone else — *"Stop trying to be the next Steven Barlett [sic] or Alex Hormozi and start being the first YOU"* (source: Amelia Sordell, https://www.linkedin.com/posts/ameliasordell_1-doom-scrolling-if-youre-spending-hours-activity-7470746670398418945-ZyJA — 11.06.2026).

**Finn Thormeier** proposes an industrialised alternative: interview each executive fortnightly, then hand them *"almost-done LinkedIn posts… All they need to do is look over the posts, make a couple changes, and publish. 1h/week."*
(source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_one-strategy-im-dying-to-try-at-an-enterprise-activity-7471171087670874113-wUvp — 12.06.2026)

**My position: both, assigned to different roles — and Robinson's model should never be delegated.** Thormeier's is the only approach in the corpus that addresses the actual structure of an enterprise B2B SaaS deal, where a CISO's signature depends on a CFO, a Head of Legal and a procurement lead who will never read your founder's posts. But it works precisely because the content it produces is *professional-expertise* content, which survives ghost-production. Robinson-style disclosure does not survive it: a ghostwritten confession is not vulnerable, it is a liability.

**What I do:** founder writes their own posts, always, unedited by committee ([§3.5](#35-stop-over-editing)). Non-founder executives run Thormeier's interview-to-draft pipeline. And I hold Thormeier's model to its own author's caveat — he has never run it ([§4.2](#42-reach-the-buying-committee-not-just-the-buyer)) — so it gets piloted with one executive, not staffed across seven.

### 6.5 Disagreement: is LinkedIn organic right for everyone?

**Amelia Sordell** presents personal branding as universally available and purely a matter of discipline: *"Personal branding isn't hard — but it does take discipline… Pick a strategy. Stick with it for 12 months."*
(source: Amelia Sordell, https://www.linkedin.com/posts/ameliasordell_1-doom-scrolling-if-youre-spending-hours-activity-7470746670398418945-ZyJA — 11.06.2026)

**Adam Robinson** disqualifies whole categories of company: *"If you're selling to hospitals I would not recommend going psychotic like I did… Not worth it,"* explaining that his own results depend on the coincidence that he is his own ICP and that ICP lives on the platform.
(source: Adam Robinson, https://www.youtube.com/watch?v=6PmFWV0DRj0 — 15.05.2024)

**My position: Robinson, emphatically — and this is the disagreement with the highest stakes.** Sordell's framing makes non-response a discipline problem, which means a founder whose buyers are simply not on LinkedIn will conclude they need to try harder. That is the most expensive possible misdiagnosis: twelve months and ~500 founder-hours spent proving a channel was never viable.

It is also the disagreement the rest of the corpus is structurally unable to adjudicate, because every voice in it is a LinkedIn success case. Robinson is the only one who names a disqualifying condition, and he names it in one sentence before moving on. [§0](#0-before-you-start-the-channel-fit-gate) is my attempt to give that sentence the weight it deserves.

---

## 7. What I rejected and why

### 7.1 Rejected: engineering the first 60–90 minutes

**The idea.** The algorithm summary in this repo holds that the first 60–90 minutes are decisive, with early engagement signalling whether to amplify or suppress. The tactical conclusions drawn from it in my own earlier outline were: comment on your own post within 5–10 minutes, and have your team, friends and inner circle engage inside the first hour.
(source: Richard van der Blom, https://sales.richardvanderblom.com/content-algorithm-playbook/ — October 2025, as summarised in [`research/other/`](../research/other/richard-van-der-blom-algorithm-insights-report.md))

**Why I rejected it.** Three reasons, in ascending order of importance.

First, evidence quality: the underlying claim reaches me through a 17-line secondhand summary. That is thin ground for a tactic that shapes daily behaviour.

Second, it is coordinated inauthentic engagement wearing a respectable name. Organising colleagues to engage on a schedule is engagement-pod behaviour; the distance between "ask the team to comment early" and the pods LinkedIn actively suppresses is one of degree, not kind. Thormeier's own wishlist for LinkedIn's incoming CPO opens with banning AI comments and adding community notes to fight clickbait (source: Finn Thormeier, https://www.linkedin.com/posts/finnthormeier_linkedin-just-hired-their-new-cpo-anthony-activity-7469694317117468672-ByKK — 08.06.2026). A playbook cannot endorse that complaint and simultaneously recommend gaming the same signals.

Third and decisively, it optimises the wrong variable. This playbook's own measurement section says audience *composition* is the metric and raw engagement is not ([§5.3](#53-measure-audience-composition-not-audience-size)). Manufacturing early engagement inflates precisely the number we have agreed to stop trusting, and corrupts the only honest read available on whether real buyers care.

**What I kept.** The defensible half: reply to genuine comments quickly, and do not schedule posts for times you cannot be present. Being available is not the same as being organised.

### 7.2 Rejected: "90% consistency, 10% quality" as an operating ratio

**The idea.** *"Building a personal brand is 10% quality content, but 90% consistency in posting it"* (source: Amelia Sordell, https://www.linkedin.com/posts/ameliasordell_1-doom-scrolling-if-youre-spending-hours-activity-7470746670398418945-ZyJA — 11.06.2026).

**Why I rejected it.** The full argument is in [§6.2](#62-disagreement-consistency-vs-craft). In short: the ratio is stated without evidence, and it is calibrated to a large general audience where a weak post is harmless. In B2B SaaS the reachable buying population is small enough that repeated low-value posts actively train your buyers to skip you. Pierri's competing claim — higher effort wins because the bar is low — comes with a disclosed cost structure (90 minutes to 3 hours per post) that makes it checkable. Sordell's does not.

**What I kept.** Her failure diagnosis. Quitting really is the dominant failure mode, and her three named traps — doom-scrolling into a consumer mindset, imitating other creators, and changing strategy every five minutes — are well observed. I address them with a sustainable cadence rather than a lowered bar.

### 7.3 Rejected: Robinson's 5-step growth plan as a content template

**The idea.** A numbered playbook for taking a new product to $1M ARR: build the founder brand, ride a wave (the Claude/LinkedIn surge), trade visibility to creators for UGC, keep the product painfully simple, run operations on AI.
(source: Adam Robinson, https://www.linkedin.com/posts/retentionadam_ive-bootstrapped-0-1m-arr-3-times-and-activity-7470149161821052928-omiK — 09.06.2026)

**Why I rejected it.** It is a promotional artefact for a product that had not launched. The post is for MoltSets, which at the time was pre-beta with a waitlist, and it closes as a waitlist CTA. Robinson himself marks the plan unvalidated in the same post: *"There's also a few core things I have NO IDEA if they will work or not."* Step 3 is explicitly improvised — *"I'm not exactly sure how I'm going to do this."*

Citing this as playbook guidance would mean treating a founder's marketing for an unlaunched product as evidence. The fact that his *previous* companies succeeded does not validate *this* plan; that is survivorship reasoning applied prospectively, which is worse than the usual kind.

**What I kept.** The post as a *format* exemplar — a numbered founder plan with real specifics is a strong structure — and Robinson's demonstrated, retrospective results at RB2B, which are checkable in a way the forward-looking plan is not.

### 7.4 Rejected: Kramer's vendor recommendation (keep the method)

**The idea.** Companies should let prospects book a meeting directly in the demo flow, and RevenueHero solves the routing objections; adding immediate booking yields "62% conversion from form fill → meeting booked."
(source: Emily Kramer, https://www.linkedin.com/posts/emilykramer_revenueheropartner-activity-7470886898958315520-wQim — 11.06.2026)

**Why I rejected it.** The post is a paid partnership. The URL slug is `revenueheropartner`, the named vendor is the sponsor, and the post ends with an affiliate discount. The 62% figure has no stated methodology and is, on its face, vendor-supplied. None of this means Kramer is wrong — the underlying advice is probably right, and she discloses the relationship in the slug — but a playbook that cites sponsored conclusions as independent findings is not doing its job.

This applies to Kramer's other collected post too: the LLM-crawling explainer sits under a `framerpartner` slug and concludes in favour of Framer (source: Emily Kramer, https://www.linkedin.com/posts/emilykramer_framerpartner-activity-7467276044736253952-AA6A — 01.06.2026). Two of her three collected posts are commercial placements. That is worth knowing before treating her feed as neutral analysis.

**What I kept.** The research method, which is excellent and independent of the sponsor: pick a checkable question, examine 100 real companies, publish the finding *with* the methodology. That is [§2.2](#22-research-as-content-the-highest-leverage-format-available), and it is the single most valuable transferable technique in the corpus.

---

## 8. My original ideas

Two ideas I did not find in the corpus, and one honest note about a third.

### 8.1 The Channel Fit Gate

**The idea.** A five-question qualifying gate, run *before* any content work, that can return the answer "do not run this playbook." Operational version in [§0](#0-before-you-start-the-channel-fit-gate).

**Why it is missing from the corpus.** Not by oversight — by construction. All ten experts are LinkedIn success cases, and eight of the ten *sell services to marketers*: Pierri sells positioning, Thormeier sells founder-led content engines, Sordell sells personal branding, Reed sells content strategy, Gerhardt sells a marketing community, Kramer and Lattanzio sell advisory, van der Blom sells an algorithm report. A corpus assembled this way cannot produce a disqualification test, because no member of it has an incentive to tell a prospective client the channel is wrong for them, and none of them has the failure data anyway.

Robinson is the only exception, and only for one sentence — the hospitals line ([§6.5](#65-disagreement-is-linkedin-organic-right-for-everyone)). He can afford to say it because he sells software, not content services.

**Why it could work.** Three arguments.

1. *It is cheap to run and expensive to skip.* The gate takes an hour. Failing to run it costs the twelve months the corpus itself says are required before signal appears ([§0](#0-before-you-start-the-channel-fit-gate)) — roughly 500 founder-hours at the 10-hours-a-week budget the corpus also supplies ([§3.1](#31-budget-the-real-number)). No other decision in this playbook has that asymmetry.

2. *It converts an unfalsifiable belief into a checkable one.* "Keep going, it takes time" is unfalsifiable, and it is the standard advice — Sordell's twelve-month instruction is exactly this. Gate item 2 replaces it with an observation anyone can make in twenty minutes: list twenty named individuals at target accounts and look for recent activity. If ten of twenty are not there, no amount of discipline changes the outcome.

3. *It protects the rest of the playbook from its own survivorship bias.* Every other section here is derived from winners. The gate is the only part that asks whether you are in the population those winners generalise to.

**How I would test it.** Retrospectively, and cheaply: apply the five questions to companies that visibly ran founder-led LinkedIn programmes and stopped. If abandoned programmes cluster at 0–3 and sustained ones at 4–5, the gate has predictive content. If they are indistinguishable, the gate is decoration and should be cut. I have not run this test, and [§9](#9-weaknesses-of-this-playbook) says so.

### 8.2 The Correction Post

**The idea.** A recurring, deliberate format: publish a post that revises a position you previously published. Not a humblebrag about a small mistake — a specific reversal of a specific public claim, naming what you said, what changed your mind, and what you now think. Roughly once a quarter.

Structure:
1. Quote your own prior claim, with a link to it.
2. State the evidence that moved you — the customer conversation, the failed test, the argument you lost.
3. State the revised position, and what would move you again.

**Why it could work.** Four reasons, each anchored to something the corpus already establishes.

1. *It is the intersection of the corpus's two strongest credibility mechanics.* Robinson's vulnerability works because the disclosure is costly ([§2.3](#23-vulnerability-with-a-specific-definition)); Kao's reasoning rule works because showing your logic beats asserting authority ([§2.5](#25-writing-craft-the-layer-everyone-assumes-and-nobody-teaches)). A correction is the only format that is both at once: it costs status *and* it is pure exposed reasoning.

2. *It is structurally hard to fake, in a feed where everything else is becoming easy to fake.* Robinson's complaint about AI slop and Gerhardt's about the "cash grab" genre ([§6.3](#63-disagreement-how-much-ai-belongs-in-production)) describe the same problem: the cost of producing plausible content has collapsed. A correction post requires a real prior public position, a real reversal, and a real willingness to be seen changing. A model can generate the prose; it cannot generate the two years of published record that make the prose mean anything.

3. *It solves the spiky-opinion trap.* [§2.1](#21-the-two-formats-that-carry-the-program) requires taking positions a competent peer could dispute. Do that for two years and you will accumulate positions you no longer hold. Most founders resolve this by quietly never mentioning them again, which slowly converts a body of work into a body of stale claims. The correction post makes holding strong opinions survivable, and therefore makes the spiky-opinion strategy sustainable rather than self-limiting.

4. *It generates the highest-quality comments available.* The corpus wants comments from real buyers ([§5.3](#53-measure-audience-composition-not-audience-size)). "I was wrong about X" reliably draws out the people who disagreed silently the first time — which is exactly the population you most want to hear from and least often reach.

**The honest caveat.** Wes Kao does something adjacent: her "done is better than perfect" post revises her own earlier thinking (source: Wes Kao, https://www.linkedin.com/posts/weskao_we-all-love-the-phrase-done-is-better-than-activity-7308139027839242241-tLxH — 19.03.2025). But she revises a *received* piece of conventional wisdom she had adopted, not a position she published; she does it once; and nobody in the corpus proposes it as a repeatable format or argues for it on defensibility grounds. The format is mine; the raw material for it is hers, and I would rather say so than claim more novelty than I have.

**How I would test it.** Track two things across four correction posts: the ICP share of commenters ([§5.3](#53-measure-audience-composition-not-audience-size)) versus a baseline post, and whether any correction post is referenced back to you in a sales conversation. If corrections do not out-perform on composition, the idea is wrong and the format is just self-flagellation.

### 8.3 A third idea I am not claiming

I considered proposing "harvest buyer language from sales-call transcripts" as original. It is not — Lattanzio publishes exactly that workflow (source: Sara Stella Lattanzio, https://www.linkedin.com/posts/saralattanzio_anthropic-is-giving-paid-users-double-cowork-activity-7470093561720500224-njHp — 09.06.2026). I mention it only because "original idea" sections are easy to pad, and the useful signal is which ideas I checked and withdrew.

---

## 9. Weaknesses of this playbook

Written to be usable against me.

**1. The corpus is ten people, and eight of them sell marketing services.** Pierri, Thormeier, Sordell, Reed, Gerhardt, Kramer, Lattanzio and van der Blom all monetise marketing expertise. Their public content is simultaneously their evidence and their advertising, and the incentive runs one way: toward "this channel works, here is how." Only Robinson sells non-marketing software — and his buyers are still GTM professionals, so even he does not test whether this works when your ICP is not a marketer. **Nothing in this playbook is validated against a B2B SaaS company selling to a non-marketing buyer.** That is a serious limit given that most B2B SaaS does exactly that.

**2. Total survivorship bias, and I could not correct for it.** There is not one failed LinkedIn programme in the corpus. Every practice here is reconstructed from winners, which means I cannot distinguish practices that caused success from practices winners happen to share. The Channel Fit Gate ([§8.1](#81-the-channel-fit-gate)) is an attempt to name this problem, not a solution to it — and it is untested.

**3. Every outcome number is self-reported by someone selling something.** Robinson's 75% ICP figure comes with an admission that he does not know how it was calculated ([§5.3](#53-measure-audience-composition-not-audience-size)). Sordell's revenue appears as two different figures in two currencies within one post ([§2.3](#23-vulnerability-with-a-specific-definition)). Kramer's 62% conversion statistic appears in a sponsored post ([§7.4](#74-rejected-kramers-vendor-recommendation-keep-the-method)). I have independently verified none of it, and none of it is verifiable from outside.

**4. My only quantitative foundation is secondhand.** Every algorithm figure in [§4.1](#41-format-choice-is-a-reach-decision) — the 6.60% carousel engagement, the −18.8% link penalty, the reach and follower declines — reaches me through a 17-line summary in this repo, not van der Blom's actual report. I did not read the primary source. If that summary misstates the report, this playbook inherits the error silently.

**5. Two of four transcripts are old enough to be describing a different platform.** Robinson's is May 2024 and Pierri's is January 2025. Reported reach dynamics changed materially over that period ([§4.1](#41-format-choice-is-a-reach-decision)), and both men's claims about what works are anchored to conditions I cannot confirm still hold. Where their claims are about human behaviour they probably travel; where they are about the algorithm they may not.

**6. The operating cadence is invented.** The 10-hours-a-week budget in [§3.1](#31-budget-the-real-number) is Fletch's disclosed number, but the weekly structure built around it is assembled by me from several sources and has never been run by anyone. Treat it as a starting configuration, not a validated system.

**7. Untested assumptions I am aware of.** That the twelve-month horizon generalises beyond Robinson. That Thormeier's buying-committee model works at all — its own author has never run it ([§4.2](#42-reach-the-buying-committee-not-just-the-buyer)). That "higher effort wins" survives further reach compression. That a founder-written voice remains distinguishable from AI-assisted content to readers, which is an assumption with a visible expiry date.

**8. Sample size, stated plainly.** Twenty-five posts across seven authors is a handful of posts each. Three of Sordell's, three of Kao's, three of Kramer's. On that basis I can characterise formats, but claims like "this is what author X believes" are drawn from a thin slice of their output, and any of them could be misrepresented by it.

**9. What is missing entirely.** No non-English-language markets. No regulated industries. No enterprise sales cycles longer than ~12 months. No evidence about company pages, employee advocacy, or paid amplification beyond a single mention of Thought Leader ads. No cost-of-failure data. And no treatment of what happens when the founder who *is* the channel leaves the company — a single-point-of-failure risk this playbook creates and does not address.

---

## 10. Who I would NOT recommend following, and why

The brief asks which of the ten I would steer people away from. Three answers, at three levels of severity.

### 10.1 Would not recommend for this topic: Amelia Sordell

Sordell is a genuinely accomplished creator with a large audience and a real business, and she is excellent at the craft of the personal-brand post. I would still not recommend her to a B2B SaaS practitioner looking for LinkedIn strategy, for four reasons.

**Topical fit.** Of her three posts in this corpus, none is about B2B SaaS. Post 2 is a general life-advice listicle arguing everyone should work in sales (source: https://www.linkedin.com/posts/ameliasordell_most-people-cant-sell-and-that-is-why-90-activity-7467485264651837440-K1v8 — 02.06.2026). Post 3 is a personal-empowerment origin story that funnels to a women's retreat (source: https://www.linkedin.com/posts/ameliasordell_at-19-i-was-working-3-jobs-had-zero-self-worth-activity-7465683347617243136-WYid — 28.05.2026). Only post 1 is about content strategy at all. Our own `sources.md` conceded at selection time that "her remit is broader than SaaS"; having now read the corpus, I think that undersold the gap.

**The advice is not falsifiable.** "Stop scrolling. Stop comparing. Pick a strategy. Stick with it for 12 months." There is no condition under which this can be shown to have failed — if it does not work, you were insufficiently disciplined. Compare Pierri, who states a cost (90 minutes to 3 hours per post) that lets you check whether you are actually doing the thing.

**Numbers that do not reconcile.** One post gives "£3.8M in revenue" and then "$4million in revenue" for what reads as the same milestone. It is a small thing; it is also the only revenue claim she makes in the corpus, and it does not survive a careful read of a single post.

**It contradicts the strongest operator evidence available.** Her 90/10 consistency ratio is asserted; Pierri's competing "higher effort wins" comes with a disclosed cost structure and a business built on it ([§6.2](#62-disagreement-consistency-vs-craft)).

**Recommendation:** study her *formats* — the origin-story arc and the three-mistakes listicle are among the best-constructed posts in the corpus — and do not take her *strategy* claims as evidence for a B2B SaaS programme.

### 10.2 Would not recommend *for this topic*, for a different reason: Wes Kao

This is a category error rather than a quality problem. Kao is the best writer in the corpus and [§2.5](#25-writing-craft-the-layer-everyone-assumes-and-nobody-teaches) leans on her more than on almost anyone else. But she does not write about LinkedIn strategy or B2B SaaS: her collected posts are about workplace communication — word choice, showing reasoning, a cliché about perfectionism. They are also the oldest LinkedIn posts in the corpus, from March–June 2025.

Someone following Kao expecting LinkedIn growth guidance will not get it, and `sources.md` was right to flag that she is present "for the sentence-level quality that the others assume but rarely teach." **Read her for writing. Do not follow her for this topic** — and note that Fletch's entire content strategy is built on two of her concepts ([§2.1](#21-the-two-formats-that-carry-the-program)), so her influence here is real even though her subject is not.

### 10.3 Follow, but apply a discount: Adam Robinson

I would still recommend Robinson — he is the most instructive founder-led case in the corpus and the only source who volunteers a disqualifying condition ([§6.5](#65-disagreement-is-linkedin-organic-right-for-everyone)). But he should be read with a standing correction applied, because his feed is now substantially a launch engine for his own products.

Of his five collected posts, four end in a conversion ask: two waitlist CTAs for MoltSets (11.06.2026 and 09.06.2026), one live-event CTA (31.05.2026), and one post whose narrative arc resolves into the MoltSets pricing story (05.06.2026). The fifth redefines "autonomous business" in terms that position RB2B as the leading example (06.06.2026).

That is not a criticism of the technique — it is the technique, executed well, and it is precisely why he is worth studying. But it means his posts are simultaneously the evidence and the advertisement, and claims that flatter the strategy he is currently selling deserve more scepticism than his retrospective accounts of RB2B. [§7.3](#73-rejected-robinsons-5-step-growth-plan-as-a-content-template) is where that discount gets applied concretely.

**One thing I will not hold against him:** he is the only expert here who tells a reader the channel might be wrong for them, and he did it in a sentence that cost him nothing to omit. That earns more trust than the CTAs cost.

---

## 11. Source integrity notes

Problems found auditing the corpus against its own sources. Several were errors in my *own* earlier work, corrected in commit `f38568b`.

| # | Finding | Where it lands |
|---|---|---|
| 1 | **A quote attributed to Robinson does not exist.** My earlier outline cited "4th down month in a row, down 2.3%, we're in the woods" to Robinson post 3. Post 3 (06.06.2026) is about defining an "autonomous business"; the quote appears nowhere in this repo. Struck through in [`playbook-outline.md`](playbook-outline.md) rather than deleted. | Replaced with a verified quote from post 4 ([§2.3](#23-vulnerability-with-a-specific-definition)) |
| 2 | **The README overstated recency.** It claimed 9/10 experts had June 2026 content; the true figure is 6/10. Two transcripts are from 2024–early 2025. | Corrected in README; consequences in [§9.5](#9-weaknesses-of-this-playbook) and [§6.3](#63-disagreement-how-much-ai-belongs-in-production) |
| 3 | **Two of Kramer's three posts are paid placements** (`revenueheropartner`, `framerpartner`). Disclosed by her in the slug, but not flagged anywhere in this repo before now. | [§7.4](#74-rejected-kramers-vendor-recommendation-keep-the-method) |
| 4 | **Robinson cannot explain his own headline metric.** Asked how the 75% ICP figure was measured, he says someone else ran it and he does not know the method. | [§5.3](#53-measure-audience-composition-not-audience-size) |
| 5 | **The algorithm "report" in this repo is a 17-line summary,** not van der Blom's actual report. Every quantitative claim in [§4.1](#41-format-choice-is-a-reach-decision) rests on it. | [§9.4](#9-weaknesses-of-this-playbook) |
| 6 | **Thormeier's flagship strategy is explicitly untested** — "one strategy I'm DYING to try," "no large B2B company is actually doing this." Presented in my earlier outline without that qualifier. | [§4.2](#42-reach-the-buying-committee-not-just-the-buyer), [§6.4](#64-disagreement-the-founders-own-voice-vs-ghost-produced-executive-content) |
| 7 | **Lattanzio's own caveat was being dropped.** The 46%/43%/112% lifts come from a study of *paid* LinkedIn content; she says so and marks the organic extension as belief. | [§5.1](#51-accept-that-attribution-will-not-work-then-measure-anyway) |
| 8 | **Two ideas are misattributed in circulation.** "Content-market fit" is credited by Robinson to Devin Reed, and "the content about the content" is credited by Reed to Chris Lockhead. Both are cited to their originators here. | [§0](#0-before-you-start-the-channel-fit-gate), [§4.3](#43-repurpose-from-a-hero-asset-on-a-real-clock) |
| 9 | **`sources.md` attributes a "95:5 rule" and a "Content Island" concept to Devin Reed.** Neither phrase appears anywhere in the collected corpus, and the README's expert table echoed "(95:5)" until v1.1. Nothing in this playbook cites either. | Noted; not used. README wording corrected |
| 10 | **`sources.md` had an unfilled `[your name]` placeholder** in the byline of the submitted research. | Fixed |

---

## 12. Citation index

Every source cited or referenced above, with dates. Full annotations in [`research/sources.md`](../research/sources.md). (Two entries — Kramer's billboard ride-along and Robinson's launch posts — are referenced in [§7.4](#74-rejected-kramers-vendor-recommendation-keep-the-method) and [§10.3](#103-follow-but-apply-a-discount-adam-robinson) by date or count rather than quoted directly.)

**Anthony Pierri — Fletch PMM**
- Positioning strategies — [post](https://www.linkedin.com/posts/anthonypierri_people-overcomplicate-positioning-there-activity-7468383258863423488-Phf2) — 04.06.2026
- YC homepage teardown — [post](https://www.linkedin.com/posts/anthonypierri_i-ranked-five-y-combinator-startup-homepages-activity-7467936879464783872-nsQk) — 03.06.2026
- "Why AI" vs "why OUR AI" — [post](https://www.linkedin.com/posts/anthonypierri_ai-companies-are-your-prospects-asking-activity-7458172886483189760-6kmU) — 07.05.2026
- Product managers & positioning — [post](https://www.linkedin.com/posts/anthonypierri_your-product-managers-may-be-silently-destroying-activity-7457088895650910208-a6AL) — 04.05.2026
- Fletch $100k/month content playbook (with Rob Kaminski) — [video](https://www.youtube.com/watch?v=0OtTo6yMmZk) — 02.01.2025

**Adam Robinson — RB2B / Retention.com**
- MoltSets launch / objection handling — [post](https://www.linkedin.com/posts/retentionadam_im-tired-tired-tired-of-data-companies-activity-7470870334712217600-vpxm) — 11.06.2026
- 5-step $0–1M plan — [post](https://www.linkedin.com/posts/retentionadam_ive-bootstrapped-0-1m-arr-3-times-and-activity-7470149161821052928-omiK) — 09.06.2026
- "What is an autonomous business" — [post](https://www.linkedin.com/posts/retentionadam_what-actually-is-an-autonomous-business-activity-7469089758158163968-kgi_) — 06.06.2026
- "I gave up on MoltSets" — [post](https://www.linkedin.com/posts/retentionadam_last-wednesday-i-gave-up-on-my-new-startup-activity-7468681453845983233-4HIm) — 05.06.2026
- Roger Bannister narrative — [post](https://www.linkedin.com/posts/retentionadam_in-2017-a-45-minute-podcast-interview-with-activity-7466917942220255232-YMhW) — 31.05.2026
- Organic LinkedIn growth interview — [video](https://www.youtube.com/watch?v=6PmFWV0DRj0) — 15.05.2024

**Finn Thormeier — Project 33**
- Buying-committee exec content — [post](https://www.linkedin.com/posts/finnthormeier_one-strategy-im-dying-to-try-at-an-enterprise-activity-7471171087670874113-wUvp) — 12.06.2026
- Tycho Luijten production system — [post](https://www.linkedin.com/posts/finnthormeier_i-interviewed-tycho-luijten-one-of-the-most-activity-7470797663593013249-MSi8) — 11.06.2026
- How Emily Kramer uses Claude Code — [post](https://www.linkedin.com/posts/finnthormeier_how-emily-kramer-uses-claude-code-to-write-activity-7470408576868720640-QY1H) — 10.06.2026
- LinkedIn CPO wishlist — [post](https://www.linkedin.com/posts/finnthormeier_linkedin-just-hired-their-new-cpo-anthony-activity-7469694317117468672-ByKK) — 08.06.2026

**Amelia Sordell — Klowt**
- 3 personal-branding mistakes / 90-10 ratio — [post](https://www.linkedin.com/posts/ameliasordell_1-doom-scrolling-if-youre-spending-hours-activity-7470746670398418945-ZyJA) — 11.06.2026
- "Most people can't sell" — [post](https://www.linkedin.com/posts/ameliasordell_most-people-cant-sell-and-that-is-why-90-activity-7467485264651837440-K1v8) — 02.06.2026
- Origin story → retreat CTA — [post](https://www.linkedin.com/posts/ameliasordell_at-19-i-was-working-3-jobs-had-zero-self-worth-activity-7465683347617243136-WYid) — 28.05.2026

**Emily Kramer — MKT1**
- Demo-booking research (sponsored) — [post](https://www.linkedin.com/posts/emilykramer_revenueheropartner-activity-7470886898958315520-wQim) — 11.06.2026
- SF billboard ride-along — [post](https://www.linkedin.com/posts/emilykramer_i-went-on-a-multi-hour-sf-billboard-ride-along-activity-7470148298318880768-H8cK) — 09.06.2026
- LLM crawling / CMS explainer (sponsored) — [post](https://www.linkedin.com/posts/emilykramer_framerpartner-activity-7467276044736253952-AA6A) — 01.06.2026

**Sara Stella Lattanzio**
- Last-touch attribution — [post](https://www.linkedin.com/posts/saralattanzio_last-touch-attribution-is-like-giving-the-activity-7471180380616863745-GdYn) — 12.06.2026
- 8 AI content-ops workflows — [post](https://www.linkedin.com/posts/saralattanzio_anthropic-is-giving-paid-users-double-cowork-activity-7470093561720500224-njHp) — 09.06.2026
- Newsjacking agent / 24–48h window — [post](https://www.linkedin.com/posts/saralattanzio_that-little-girl-in-the-questionable-minnie-activity-7469728816962367488-phDm) — 08.06.2026

**Wes Kao**
- Delete these 9 words — [post](https://www.linkedin.com/posts/weskao_to-improve-your-writing-delete-these-9-words-activity-7341112272137715713-Hus-) — 18.06.2025
- Show your reasoning — [post](https://www.linkedin.com/posts/weskao_trust-me-ive-done-this-many-times-activity-7325892206081318913-7dVf) — 07.05.2025
- "Done is better than perfect" — [post](https://www.linkedin.com/posts/weskao_we-all-love-the-phrase-done-is-better-than-activity-7308139027839242241-tLxH) — 19.03.2025

**Dave Gerhardt — Exit Five**
- Why most B2B communities die — [video](https://www.youtube.com/watch?v=obXLy-AU5m4) — 12.05.2026

**Devin Reed — The Reeder**
- Making great B2B content — [video](https://www.youtube.com/watch?v=df3t4BNBRmI) — 25.09.2025

**Richard van der Blom — Just Connecting**
- Algorithm Insights Report 2025 — [report](https://sales.richardvanderblom.com/content-algorithm-playbook/) — October 2025 *(held in this repo only as a secondhand summary — see [§9.4](#9-weaknesses-of-this-playbook))*

---

*Playbook v1.1 — Lucas Bravo, August 2026. Corrections welcome; [§11](#11-source-integrity-notes) is the log of the ones already made.*
