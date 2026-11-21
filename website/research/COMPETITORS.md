# Competitor marketing deep dive: what eight direct competitors say, and how it lands against mAIcro

*Prepared 21 Nov 2026 (AEDT) for Matthew Bright. Companion files: [PAIN_POINTS.md](PAIN_POINTS.md), [SITE_COPY.md](SITE_COPY.md). Product facts about mAIcro come from `/workspace/maicro-review/REPORT.md` and its notes.*

## How this was gathered

- Each homepage (and pricing page where it mattered) was fetched with `curl` on 21 Nov 2026. The visible copy (title, meta description, headings, paragraphs, button and link labels) was pulled out with a small HTML parser. The extracted text for every page is in [`sources/`](sources/), so each quote below can be checked.
- **Lovable** blocks non-browser requests (HTTP 403). Its copy comes from the Internet Archive snapshot of 17 Nov 2026: `https://web.archive.org/web/20261117225947/https://lovable.dev/`.
- **n8n** renders plan prices client-side. Those figures come from the prior report, not from this fetch.
- Quotes are exact unless marked *paraphrase*. Where a site split a headline across two lines, I've joined them with " / ".
- "What they avoid saying" is my reading of what's missing from the page, checked by searching the extracted copy for the term (e.g. "Hasura", "open source", "self-host", "credits").

---

## 1. Supabase

**URL:** https://supabase.com/ (pricing: https://supabase.com/pricing)

**Headline + subhead**
- Title: "Supabase | The Postgres Development Platform"
- H1: **"Build in a weekend / Scale to millions"**
- Sub: "Start your project with a Postgres database. Add Authentication, Data APIs, Edge Functions, Realtime Data, Storage, and Vector embeddings."
- Supporting line: "Use one or all. Best of breed products. Integrated as a platform."
- Open-source block: "Open source from day one … Read, contribute, self-host. You're never locked in, and always in control."

**Persona.** Developers and startups who want to ship a production app quickly. Increasingly it's also AI app builders: the nav has "AI Builders" and "Vibe Coders" sections, and the lead testimonial is from Lovable.

**Core pain (their words).** Assembling a backend yourself takes too long. They borrow a customer's voice for it: "If I had to go and build all these components myself, we wouldn't even have launched." The second pain is outgrowing your stack: "Scale to millions".

**Proof.**
- GitHub star count in the nav (115.2K).
- Customer stories, each with a metric: Lovable "Powering millions of AI-generated apps with a complete Supabase backend"; eXp Realty "2,000+ employees"; Chatbase "Scaled from zero to $10M ARR"; Rally "fully licensed fintech in three months".
- "Trusted by fast-growing companies worldwide", community tweets, and "SOC2 Type 2 Certified" in the footer.

**CTA pattern.** "Start your project" (primary), with "Request a demo" beside it. The pricing page says "Start building for free".

**What they avoid saying.**
- The homepage doesn't describe the self-hosting effort; self-hosting is a single verb in the open-source block. The self-hosting docs tell a different story: "you should **never** start your self-hosted Supabase using these defaults". On MCP: "Currently, it does not offer OAuth 2.1 authentication, and is not intended to be exposed to the Internet … By default, all connections to the MCP server are denied" ([self-host MCP guide](https://supabase.com/docs/guides/self-hosting/enable-mcp)).
- Free-tier limits only appear on the pricing page: "Free projects are paused after 1 week of inactivity. Limit of 2 active projects."
- No graph database, no built-in workflow chains, nothing about learning.

**Against mAIcro's real product.**
- **Supabase wins** any contest about "a Postgres backend for your app": auth, hosting, a big ecosystem, compliance, maturity, and a free hosted tier you can try in a minute. Its local tooling also gives anyone a free local Postgres with pgvector. If mAIcro leads with "Postgres + vectors + MCP", Supabase has already said it, louder and with proof.
- **Supabase loses** where it says nothing:
  - graphs (Apache AGE / openCypher) in the same database;
  - workflows, cron, AI tasks with typed outputs and API wrappers built into the backend;
  - an embedded IDE and guided courses;
  - MCP designed in from the start for a single-user local container, with no cloud account.
- Its "scale to millions" framing also leaves room for a deliberately small promise: software for one person or one team that never needs to scale.

---

## 2. Xano

**URL:** https://www.xano.com/ (pricing: https://www.xano.com/pricing/)

**Headline + subhead**
- Title: "Xano | Backend Platform to Build, Run & Govern AI Software"
- H1: **"One backend platform to build, run and govern AI-built software"**
- Sub: "Build apps, APIs and MCP servers with AI. Test, deploy and observe everything you ship."
- Section head: **"Business-critical systems in production, not prototypes."**
- Closer: "Built something that's becoming real? You built it with AI. It works. Now someone else needs to touch it: a teammate, a client, IT. Xano is where AI-built projects grow up." / "AI builds software. Xano makes it trustworthy."

**Persona.** Teams, agencies and enterprises who already have AI-built software and need to govern it: engineering leads, IT, agencies ("Xano for agencies").

**Core pain (their words).** AI-built software can't be trusted or governed. "Any agent can build. Your team's rules decide what passes." "See what was built, even when AI built it."

**Proof.**
- "Trusted by enterprises building business-critical workflows around the globe."
- One quote, attributed by title only: "Xano provides that stability - you can deploy and not worry about the infrastructure." (VP of Engineering at Deriv)
- Compliance on the pricing page: "GDPR, ISO, and SOC 2 & 3 compliance" on the Essential plan.
- Enterprise features: "SSO with Google, GitHub, and Microsoft Entra ID (SAML)".

**CTA pattern.** "Start building, free" plus "Talk to sales". Later, "Start free - bring your agent" and "Book a demo".

**What they avoid saying.**
- No prices on the homepage. The free-tier limits sit on the pricing page: "The Free plan is limited to 10 API requests per 20 seconds"; "AI-ready Postgres database (up to 100K records)"; "1 GB image storage (watermarked)". Paid plans start at $85/mo billed annually ($99 monthly).
- The word "no-code", which used to be Xano's identity, is gone from the homepage copy.
- Self-hosting only shows up as "Your cloud or ours".
- Beginners and individuals aren't addressed at all.

**Against mAIcro's real product.**
- Xano has **explicitly vacated the prototype stage**: "in production, not prototypes". That is the most useful line in this whole review for mAIcro, because mAIcro's honest job is the stage Xano now treats as someone else's problem.
- Xano wins on governance, compliance, managed hosting and teams.
- mAIcro wins for the solo builder, educator or tinkerer: free, on your own machine, no request rate limit or record cap, no watermark, and the same building blocks (Postgres, generated API, logic, MCP).
- Positioning should be sequential, not combative: *prototype in mAIcro; move to a governed platform when it becomes real.* (The founder is ex-Xano, which is another reason not to snipe.)

---

## 3. n8n

**URL:** https://n8n.io/ (pricing: https://n8n.io/pricing/)

**Headline + subhead**
- Title: "AI Workflow Automation Platform - n8n"
- H1: **"Build the agent. Understand its workflow."**
- Sub: "n8n is the platform for agents and workflows you can follow. Open any step, see what it does, and explain to anyone who runs it."
- Meta: "…giving technical teams the flexibility of code with the speed of no-code."
- Section: "The USB-C for your AI stack … 500+ native integrations. Any API via HTTP. Any agent or coding assistant via MCP."
- Self-host block: "Self-host your AI stack. Deploy on-prem or with Docker to keep your data in your own environment. Access the source code on GitHub, or use the hosted version."
- Banner: "Meet Nod, an open-source personal agent from n8n Labs."

**Persona.** Technical teams inside businesses (ops, IT, security, revenue ops). The stories name individuals doing named jobs: "How Tom automated new user onboarding", "How Cécile automated threat investigation", "How Konsti automated alert triage", "How Alicia automated lead qualification".

**Core pain (their words).** You can't see or trust what AI agents do: "See + understand + trust your agents"; "Put rules around AI actions". Also "Move fast + break nothing".

**Proof.**
- "Trusted by Fortune 500 companies".
- "Huel saved 1,000 hours with an AI-first culture" and "Vodafone delivers £2.2M security operations win".
- The integration count, and an animated refund workflow in the hero that shows the product working.

**CTA pattern.** "Get started" / "Talk to sales". On pricing: "Start free trial", plus a separate "Community Edition: A standard, self-hosted version of n8n is available on GitHub."

**What they avoid saying.**
- The platform copy says "Access the source code on GitHub" rather than "open source". The only "open-source" on the page refers to Nod, not n8n. n8n's licence is its own source-available "fair-code" licence, which is worth checking before you build on it.
- Prices aren't on the homepage. Plans are metered by "monthly workflow executions" (Starter €20/mo and Pro €50/mo annual, per the prior report).
- n8n isn't a database and doesn't say so; it moves data between other tools.

**Against mAIcro's real product.**
- n8n wins anything framed as "workflow automation": visual builder, hundreds of integrations, a mature self-host story and a big community. If mAIcro says "workflows" first, it loses.
- mAIcro wins as **the place the data lives**: tables, vectors, a graph and documents, with workflows (chains, cron, AI tasks) running next to that data and exposed as GraphQL operations and MCP tools.
- The two are complementary, since an n8n workflow can call a GraphQL endpoint. n8n's shift towards a "personal agent" (Nod) is worth watching; it shows the personal-software space is getting crowded.

---

## 4. Dyad

**URL:** https://www.dyad.sh/

**Headline + subhead**
- Title: "Dyad – Free, Local, Open-Source AI App Builder"
- H1: **"The open-source AI app builder on your desktop"**
- Sub: "Turn your ideas into web apps without coding. Use your favorite AI models. Own your code. Zero lock-in."
- Four pillars, each stated in a few words:
  - "Local first: Runs on your machine. Your data, your control."
  - "Use any AI model: Use OpenAI, Anthropic, Ollama, LM Studio, and more."
  - "Real code you own: Export clean, runnable code. No lock-in, ever."
  - "Open source: Transparent by design."
- Data layer: "Full-stack database & auth: Connect Supabase or Neon with 1 click."
- "Local, honest, & transparent … No cloud lock-in, no telemetry traps, and full visibility into every prompt and diff."
- "MCP extensible: Plug in Chrome DevTools, web browsing, custom APIs, or any MCP server."

**Persona.** Non-developers who tinker with AI, plus people leaving cloud builders. A quote on the page: "I fall into the category of a non-developer who likes to tinker with AI". Another: "I have used Lovable, Base44, bolt, and replit, and DYAD is the best tool out there!"

**Core pain (their words).** Lock-in and walled gardens in cloud app builders: "No walled garden, pure flexibility. Bring your own API keys, choose any model (even offline ones), and keep 100% of your source code."

**Proof.** GitHub stars ("20k GitHub stars" in the hero, "22kstars on GitHub" lower down; the page is inconsistent), Reddit-handle testimonials and named comparisons with competitors.

**CTA pattern.** Direct OS download buttons above the fold ("Download for macOS", "Download for Windows", "Download for Linux (.deb)"). There's no signup and no "talk to sales". Paid Pro sits lower on the page, sold on AI credits.

**What they avoid saying.**
- The headline says "local first", but the recommended database and auth are hosted (Supabase or Neon), so the data layer isn't local by default.
- Model costs are pushed to "bring your own API key", and the homepage doesn't mention what a prompt costs.
- No mention of what happens when a generated app needs real data modelling, graphs or scheduled jobs.

**Against mAIcro's real product.**
- **Dyad is the biggest threat to mAIcro's current homepage message.** "Make software that works for you, no coding" is Dyad's whole pitch. Dyad delivers it with a desktop download and a visible app in minutes; mAIcro delivers a GraphQL backend after a Docker install. mAIcro can't win that framing.
- Dyad *is* the stronger version of mAIcro's local, no-lock-in, any-model story for frontends.
- Its data layer is someone else's cloud, and it plugs into "any MCP server". The honest counter is a division of labour: Dyad builds the app; mAIcro is a local backend with data, vectors, a graph and workflows that an agent can drive. I haven't verified a Dyad-to-mAIcro connection, so the site must not claim one.

---

## 5. PocketBase

**URL:** https://pocketbase.io/ (docs: https://pocketbase.io/docs/)

**Headline + subhead**
- Title / hero: **"Open Source backend / in 1 file"**, followed by four nouns: "Realtime database / Authentication / File storage / Admin dashboard"
- Meta: "Open Source backend in 1 file with realtime database, authentication, file storage and admin dashboard"
- Section: "Ready to use out of the box"
- "Extendable: Use as a standalone app OR as a framework, that you can extend via Go and JavaScript hooks to create your own custom portable backend."
- Docs: "Please keep in mind that PocketBase is still under active development and full backward compatibility is not guaranteed before reaching v1.0.0. PocketBase is NOT recommended for production critical applications yet, unless you are fine with reading the changelog and applying some manual migration steps from time to time."

**Persona.** Developers (JavaScript/Dart/Go) who want a small self-hosted backend for an app, often indie or side projects.

**Core pain.** It's implied by the category line rather than stated: backends are heavy to run. Auth is pitched as "without the hassle".

**Proof.** Almost none in the usual sense. The proof is a working code sample on the homepage, a "Live demo", the version number in the header (v0.42.3) and the docs. There are no logos, testimonials or customer metrics.

**CTA pattern.** "Live demo" and "Read the documentation". No signup, no sales.

**What they avoid saying.** Anything about AI, agents, MCP or vectors. Any scaling claim (it's SQLite underneath). Any adjectives at all.

**Against mAIcro's real product.**
- PocketBase is the **model for how mAIcro's page should read**: the category in one line, a short list of nouns, a code sample, an honest pre-1.0 warning, and no signup.
- PocketBase wins on simplicity: a single executable, no Docker, auth built in.
- mAIcro wins on breadth for data and agent work: Postgres, generated GraphQL, vectors, graphs, workflows, MCP, an IDE and courses.
- The honest trade-off: mAIcro needs Docker and a ~635 MB image where PocketBase needs one file.

---

## 6. Nhost (lighter)

**URL:** https://nhost.io/

**Headline + subhead**
- Title: "Postgres Backend to Build, Deploy & Scale | Nhost"
- H1: **"Launch in minutes / Scale without limits"**
- Sub: "Nhost is a fully managed, extensible backend platform designed for speed, flexibility, and scale - without the infrastructure headaches."
- Meta: "…a managed backend platform with Postgres, GraphQL, Auth, Storage, and serverless Functions."

**Persona.** App developers, "from indie hacker side projects to the core infrastructure of scaling startups."

**Core pain (their words).** "Infrastructure headaches"; "Focus on building features your users will love, not wrestling with infrastructure."

**Proof.**
- Logos ("Trusted by developers at") and a GitHub count (7K).
- Case studies: "Midnight Society launched their game to 400,000+ users in just 6 weeks"; "React Flow implemented a complete subscription platform in just 2 months"; "RevTron achieved triple-digit growth".

**CTA pattern.** "Get started for free" / "Explore the docs" / "Book a demo". The closing section adds: "No credit card required for the free tier."

**What they avoid saying.** The GraphQL engine (Hasura) isn't named anywhere in the homepage copy. Self-hosting gets only "Develop locally. Ship globally."

**Against mAIcro's real product.**
- Nhost has the same core as mAIcro (Postgres → generated GraphQL), plus auth, storage and managed hosting. It wins for shipping an app.
- mAIcro adds vectors, graphs, workflows, MCP, an IDE and courses, and has no managed option.
- mAIcro shouldn't fight on "scale".

---

## 7. Lovable (message overlap only)

**URL:** https://lovable.dev/ (copy from the [17 Nov 2026 Wayback snapshot](https://web.archive.org/web/20261117225947/https://lovable.dev/))

**Headline + subhead**
- Title: "App & Website Builder | Build Software in Minutes | Lovable"
- Hero: **"Build something Lovable"** / "Bring a new product, internal tool, or entire company to life." (with a prompt box and a "Build" button)
- "If you can describe it, you can build it."
- Meta: "Describe what you want in plain language and Lovable builds it: full-stack apps, websites and internal tools. Start free."
- "Depend on Lovable, from end to end. Lovable handles your end-to-end infrastructure – from hosting and authentication to payments and integrations."

**Persona.** Anyone with an idea: non-coders, employees inside companies, founders, students.

**Core pain (their words).** You can't code, and SaaS doesn't fit. "eXp Realty has cancelled millions in SaaS contracts for custom software built with Lovable."

**Proof.** Brand logos ("Adidas", "Asana", "ElevenLabs", "Zendesk", "Workday", "Nvidia"), "Millions count on Lovable", customer stories, and an unfiltered user quote ("…this is the best thing I've ever seen in my life").

**CTA pattern.** The CTA *is* the product: a prompt box and "Build". Secondary is "Get started".

**What they avoid saying.**
- Credits and cost: the word "credits" doesn't appear on the homepage.
- The hosting dependency is framed as a benefit ("Depend on Lovable"), while also claiming "Your code and data stay yours. Always."
- Nothing about where data is processed, and nothing about self-hosting.

**Against mAIcro's real product.**
- mAIcro's current homepage lines ("A spreadsheet that has grown a life of its own…", "make software that works for you") are **Lovable's territory**. Lovable answers that promise in seconds, in a browser, with no install, so mAIcro loses every visitor who arrives with that expectation.
- The only honest contrast is in what you depend on. Lovable says "depend on Lovable, from end to end"; mAIcro's answer is that it runs on your machine, on Postgres you can inspect.

---

## 8. Directus (lighter)

**URL:** https://directus.com/ (pricing: https://directus.com/pricing)

**Headline + subhead**
- Title: "Directus | Collaborative Backend & Headless CMS"
- H1: **"The backend for your whole team."**
- Sub: "Connect any database. Get instant APIs, a no-code interface, and a native MCP server for your headless CMS."
- Section: "AI that acts on your data. Not a copy of it." … "AI agents operate under the same role-based access control as human users."
- Use-case lines: "Replace spreadsheets with structured data"; "Edit content without filing a ticket".

**Persona.** Mixed teams (content, ops, developers) sharing one database.

**Core pain (their words).** Teams blocking each other ("No tickets required"), spreadsheets standing in for databases, and AI working on stale copies of data.

**Proof.**
- Download counts, inconsistent on the same page: "Over 50 million downloads" and "Over 45 million downloads".
- GitHub (38K) and three short scenario stories, e.g. "Tag 500 images before lunch."

**CTA pattern.** "Try it yourself or book a demo", plus a CLI one-liner (`directus-template-cli@latest init`) right in the hero.

**What they avoid saying.**
- The homepage never says "open source".
- The licence terms only appear on the pricing page: "Organizations under $5M in annual revenue and fewer than 50 employees qualify for fully permissive access to Directus at no software cost." Cloud starts at "$89 … Billed yearly, or $99 monthly".

**Against mAIcro's real product.**
- Directus wins on a polished admin UI, role-based access for agents, any SQL database, and team collaboration.
- mAIcro wins on vectors, graphs, AI tasks with typed outputs, courses, and one container for one person.
- Directus's "AI that acts on your data. Not a copy of it." is close to mAIcro's real strength. mAIcro shouldn't copy the line, but it should make the same point in its own words: your agent works on the real tables through MCP.

---

## 9. Patterns across all eight

| | Category stated in hero? | Size of promise | Proof style | Primary CTA |
|---|---|---|---|---|
| Supabase | Yes ("Postgres Development Platform") | Scale to millions | Customer metrics, stars, SOC 2 | Start your project |
| Xano | Yes ("backend platform") | Govern AI-built software | Enterprise trust, compliance | Start building, free / Talk to sales |
| n8n | Yes ("workflow automation") | Agents you can follow | Fortune 500, £/hours saved | Get started / Talk to sales |
| Dyad | Yes ("AI app builder on your desktop") | Apps without coding | Stars, Reddit quotes | Download |
| PocketBase | Yes ("backend in 1 file") | Ready out of the box | Code sample, live demo | Live demo / Docs |
| Nhost | Partly ("Postgres Backend") | Scale without limits | Case-study metrics | Get started for free |
| Lovable | Yes ("App & Website Builder") | Build anything | Brand logos, "millions" | Prompt box: Build |
| Directus | Yes ("backend for your whole team") | Whole-team backend | Downloads, scenarios | Try it / Book a demo |
| **mAIcro (today)** | **No.** "Simpler personal software" never says Docker, Postgres or backend | "What could you make possible?" | None | Get started |

**What to take from this for mAIcro:**
1. **Every competitor names its category in the first line, and mAIcro doesn't.** That's the single biggest fix.
2. **Nobody else in this set offers graphs + vectors + workflows + MCP in one local container**, and nobody is selling to the prototype stage on purpose. Xano has left it, and Supabase and Nhost talk about scale. That's the honest opening.
3. **Copy PocketBase's form, not Supabase's.** A one-line category, a short list of nouns, a code block, an honest pre-1.0 warning and no signup. mAIcro has no customer metrics, so it shouldn't build a page that needs them.
4. **Stay out of Dyad and Lovable's lane.** "No coding" and "make an app" are taken by products that really do deliver that in minutes. mAIcro's site should say plainly that it is a backend and needs Docker.
5. **Borrow the "you can see it" theme** (n8n: "workflows you can follow"; Directus: "not a copy of it") and make it concrete. In mAIcro it's Postgres tables, GraphQL you can read, and an agent working through MCP on operations you can list.
6. **What mAIcro can't use:** logos, user counts, compliance badges, "scale", "production-grade". It has none of them, and borrowing them would be invented proof.
