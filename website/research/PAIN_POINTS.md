# mAIcro: pain points, what not to claim, and the message architecture

*21 Nov 2026. Builds on [COMPETITORS.md](COMPETITORS.md) and the product facts in `/workspace/maicro-review/REPORT.md`. Every capability named here comes from mAIcro's own site copy, its Docker image layers, or the maicroverse repo. Nothing is assumed.*

## The real core users

The site currently speaks to curious non-coders. The product, though, needs Docker, a terminal and GraphQL. The people it actually serves are:

1. **Technical builders who work with AI agents.** Developers and tinkerers who use Claude Code, Cursor, Claude Desktop or another MCP client and want a real local backend to point it at.
2. **Educators and serious learners.** People teaching or learning how data, APIs, graphs, vectors and agents fit together, who need something they can reset and inspect.
3. **Privacy-sensitive prototypers, especially in Australia.** Aged care, community services, social enterprise and government teams who want to test an idea without putting records into a cloud trial. This only works with sample data and with clear honesty about the AI provider.
4. **People who want a local MCP data toolbox.** They want their own notes, documents and records in Postgres, with vectors and a graph, and an agent that can work with them.

---

## Ranked pain points mAIcro can honestly solve

The ranking weighs how much it hurts the core user, how directly mAIcro solves it today, and how much it stands out from competitors.

| # | The pain, in the user's words | Who | What mAIcro actually does | Evidence | Who else solves it | Caveat to state |
|---|---|---|---|---|---|---|
| 1 | **"My agent can write code, but it has nowhere real to put things."** It can draft a schema in seconds, then I spend hours wiring up a database, an API and an MCP server. | Builders, MCP toolbox | Tables become generated GraphQL types, queries and mutations ("reload the schema"). With MCP turned on, compatible clients can access "mAIcro's tools, including GraphQL operations and schema information". | Site copy; blog *A toolbox for you and your agents* | Supabase (hosted MCP; self-hosted MCP "not intended to be exposed to the Internet"), Xano MCP (paid tiers for real use), Directus MCP | You decide what the agent can reach. Review mutations and external requests. |
| 2 | **"A prototype shouldn't need five services."** Postgres, a vector store, a graph database, a scheduler, glue code. | Builders, educators | PostgreSQL 18, pgvector, Apache AGE, workflow chains, cron jobs, TypeScript modules and an embedded IDE in one container ("All in a single local Docker container"). | Site copy; image layers (`PG_MAJOR=18`, `vector.so`, `age.so`) | Nobody in the set bundles a graph, vectors and workflows together. Supabase comes closest. | ~635 MB image; needs Docker. |
| 3 | **"Rows aren't enough. I need relationships and similarity."** Who worked where, which note belongs to which client, which passage answers this question. | Builders, educators, MCP toolbox | Embeddings with similarity search next to your data. Graphs queried with openCypher via Apache AGE. Cypher and SQL can be wrapped as GraphQL operations. | Site copy; HR Graph, Book Club and *From documents to useful answers* | Supabase (vectors, no graph); Neo4j-style tools (graph, separate service) | "Similarity isn't the same as truth" (mAIcro's own blog). Say that too. |
| 4 | **"App builders hide how it works. I need to teach it, or understand it."** | Educators, learners | mAIcroverse: a separate, resettable learning instance with guided courses (Markdown Foundations, Data Import, Book Club, HR Graph, API Wrappers, Scheduled Weather Collector, AI Signatures and Types, Forms, Browser Automation and more). Each states its objective and what its setup deletes. | Course catalogue in the site bundle; maicroverse repo (GPL-3.0) | None of the eight competitors offers a learning path like this | Course setups wipe data, so use a disposable instance. The learning setup needs an OpenRouter key. |
| 5 | **"I can't put client records into a US cloud trial just to test an idea."** | Privacy-sensitive AU prototypers | Runs on your own machine or server. The database and files sit in a data folder you control (`~/maicro-data` by default). There's a worked aged-care intake form example. | Installer `run.sh`; Forms course; site: "Local hosting doesn't mean every connected service is local" | PocketBase, self-hosted Supabase, self-hosted n8n and Directus also run locally | **Not a compliance tool.** Anything sent to an AI model (OpenRouter) or an external API leaves the machine. The learning setup "allows outbound fetches to any host". Use sample data. |
| 6 | **"Free tiers pause, cap or throttle me mid-experiment."** | Builders, educators | A public Docker image. No account, no project pausing, no record cap or request limit on your own machine. Model costs go through your own OpenRouter key. | Docker Hub (public image) | PocketBase, self-hosted Supabase / n8n | No published pricing or terms. Don't promise "free forever" (that's a LinkedIn intention, not an offer). |
| 7 | **"Small jobs and API glue have no home."** A nightly fetch, a wrapped REST API, an AI step with a structured output. | Builders | Cron jobs, external REST APIs wrapped as named GraphQL operations, TypeScript modules, AI tasks and "AI signatures" with typed outputs backed by GraphQL types. | Scheduled Weather Collector, API Wrappers, AI Tasks, AI Signatures and Types courses | n8n (better for many SaaS integrations); Val Town (shutting 10 Jan 2027) | Some examples need external API keys and internet access. |
| 8 | **"I need to show people a working thing, not slides."** | Builders, educators, AU prototypers | Forms, charts and dashboards, a Markdown wiki and file storage in the IDE, or connect your own frontend to the GraphQL API. | Course catalogue; site: "iterate in the embedded IDE or connect your own frontend" | Lovable and Dyad (far stronger for visible apps) | This is backend-first. It isn't an app builder. |

**Pains 1–4 lead the page.** Pain 5 gets its own section because it's the clearest local angle for Australia, but the caveat has to sit right next to the claim, never in a footnote. Pains 6–8 go into the feature list.

---

## Pain points mAIcro should NOT claim

| Don't claim | Why not | Say this instead |
|---|---|---|
| "Try it now in your browser" / hosted trial | There's no hosted version. The only route is Docker. | "Runs on your machine in Docker." |
| "No coding needed" / "anyone can build an app" / one-click apps | Needs Docker, a terminal, a curl-to-shell installer and GraphQL. Dyad and Lovable really deliver no-code, in minutes. | "If you want an app without a terminal, use Dyad or Lovable." |
| "Production-ready", "scale", "enterprise" | Version 0.1.x, alpha, one maintainer. | "Alpha. For prototypes and learning." |
| Compliance (SOC 2, ISO, Privacy Act, health-grade, "secure by default") | None exists. The installer uses default credentials and signing secrets, the learning admin key is reset to a known string, and ports 4321 and 443 are published. | "Change the defaults before anyone else can reach it." |
| "Private" / "your data never leaves your machine" | The learning setup uses OpenRouter, and external APIs receive whatever you send them. | "The database stays on your machine. What you send to a model or an API doesn't." |
| Local / offline AI models (Ollama, LM Studio) | Promised on the older bloxez.com but not documented on maicro.app. | Say nothing until it's documented. |
| "Open source" (for the platform) | Only the maicroverse courses repo is public (GPL-3.0). The platform repo link returns Not Found. | "The courses are GPL-3.0. The platform source isn't public yet." |
| Auth / end-user accounts / multi-user teams | Not evidenced in the current product. Hosted multi-user is an undecided idea. | Leave it out. |
| User numbers ("32k pulls"), community size, testimonials, logos | Pull counts include CI and updates. The Discord has about 3 members. There are no published users. | Show the courses and the stack. Proof by inspection. |
| Raspberry Pi support | A stated target on LinkedIn, not documented. | Leave it out. |
| "Free forever" / any price | Stated intent, not a published offer. | "Free to download and run." |
| Named AI characters (mAIql etc.) or "your AI builds it for you" | Leftover from the BloxEZ era. It contradicts "you decide what the agent may access." | "You and the agent you choose." |

---

## Message architecture

### Primary promise
> **A real backend for you and your AI agent, in one Docker container on your own machine.**
> Postgres, GraphQL, vectors, graphs, workflows and an MCP server, already connected, so you can build and test small software without assembling the plumbing first.

### Three supporting pillars

1. **Real parts you can inspect.** PostgreSQL 18, generated GraphQL, pgvector and Apache AGE (openCypher). There's no proprietary visual language to learn first. What you learn transfers, and your data is in Postgres.
   *Proof:* the image layers; GraphQL generated from your tables; SQL, Cypher and REST wrapped as GraphQL operations.
2. **Built for working with agents.** The MCP server exposes GraphQL operations and schema information to compatible clients. Workflow chains, cron jobs and AI tasks with typed outputs give the agent somewhere to do the next step. You choose the agent and what it can reach.
   *Proof:* site copy on MCP; AI Tasks and AI Signatures courses; the blog *A toolbox for you and your agents*.
3. **On your machine, at your own pace.** It's a free public Docker image with your data in a folder you choose. A separate, resettable learning instance with guided courses lets you break things and start again.
   *Proof:* Docker Hub; the installer; the mAIcroverse course catalogue.

### Objections and rebuttals

| Objection | Rebuttal (honest) |
|---|---|
| "Why not just self-host Supabase?" | If you need auth, storage and a hosted path to production, do. mAIcro adds what Supabase doesn't bundle: graph queries, workflow chains, cron jobs, REST APIs wrapped as GraphQL operations, an IDE and courses, all in one container with MCP designed in. |
| "I don't know Docker or GraphQL." | You'll need Docker; there's no way around it today. The GraphQL is generated from your tables, the courses walk through it, and your agent can write the queries. If you want no setup at all, Dyad or Lovable will suit you better. |
| "It's alpha and one person. Can I rely on it?" | Not for production or real client data yet. Use it to prototype and learn. It's Postgres underneath, so your schema and data aren't trapped in a proprietary format. |
| "Is my data private?" | The database and files stay on your machine. Prompts sent to an AI model (via your OpenRouter key) and calls to external APIs leave it. Use sample data until you know where everything goes. |
| "Is it secure?" | Not by default for shared use. The installer uses default credentials and secrets, and the learning instance resets its admin key. Keep it on your own machine and change the defaults before exposing it. |
| "curl piped to sh?" | Read the script first. It's public on GitHub and the site says what it does: starts Docker, may ask for admin rights, creates data folders, and replaces an existing `maicro` container. |
| "What does it cost?" | Downloading and running the image costs nothing. AI model usage is billed by your own provider. There's no hosted plan and no published pricing. |
| "Is it open source?" | The courses repo is GPL-3.0. The platform source and licence aren't published yet. |
| "Why not n8n?" | n8n is better at moving data between lots of SaaS tools. mAIcro is where your data lives, with workflows that run next to it. |

### Counter-positioning one-liners

- **vs Supabase:** Supabase is for shipping an app to users. mAIcro is for working out what the app should be, on your own machine, with graphs, workflows and your agent in the same box.
- **vs Xano:** Xano says it's for "production, not prototypes". mAIcro is for the prototype.
- **vs Dyad:** Dyad builds the app. mAIcro is the backend your agent works with: data, vectors, graphs and workflows.
- **vs n8n:** n8n moves data between your tools. mAIcro is where the data lives, and its workflows run next to it.
- **vs PocketBase:** PocketBase is a small backend in one file. mAIcro is a bigger toolbox in one container: Postgres, GraphQL, vectors, graphs, workflows and MCP.
- *(Also)* **vs Lovable:** Lovable asks you to depend on it end to end. mAIcro runs on your machine, on Postgres you can inspect.
- *(Also)* **vs Nhost:** the same Postgres-to-GraphQL core, aimed at learning and prototyping rather than scaling.
- *(Also)* **vs Directus:** Directus is a team admin over your database. mAIcro is one person's toolbox, with vectors, graphs and AI tasks built in.

### Word list

- **Use:** backend, Docker container, Postgres, GraphQL, vectors, graphs, workflows, MCP, your machine, prototype, learn, inspect, alpha, sample data.
- **Avoid:** unlock, empower, magic, effortless, seamless, revolutionary, "what could you make possible", "scale", "production-grade", "no code", "private" (unqualified), AI personas, emoji.
- **Spelling:** Australian (organise, licence as a noun, recognise, colour, behaviour, summarise).
