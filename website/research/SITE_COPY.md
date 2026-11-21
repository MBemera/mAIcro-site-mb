# mAIcro site copy (final)

*21 Nov 2026. This is the copy used, word for word, in [`../site/index.html`](../site/index.html). Lines starting with "> Note:" are for the editor and don't appear on the page. Reasoning is in [PAIN_POINTS.md](PAIN_POINTS.md); the competitor evidence is in [COMPETITORS.md](COMPETITORS.md).*

> Note: Every capability below is taken from mAIcro's own site copy, its Docker image or the maicroverse repo. Re-check the items marked **[check]** before publishing, because they change with releases.

---

## Page meta

- **Title:** mAIcro: a self-hosted backend toolbox in one Docker container
- **Description:** Postgres, GraphQL, vectors, graphs, workflows and an MCP server in one Docker container. Free to run on your own machine. Alpha.

## Header

mAIcro (home link)

Navigation: Who it's for · What it fixes · Features · Limits · Compare · Get started · Ask your agent

---

## Hero

# mAIcro is a self-hosted backend in one Docker container: Postgres, GraphQL, vectors, graphs and an MCP server your AI agent can use.

Build and test small tools and prototypes on your own machine, on a real database your agent can query and update. You decide what it can reach. Free to download and run. Early alpha, built by one developer in Perth.

**[Get started]** → `#get-started`
**[Ask your agent about mAIcro and how it would work with your projects]** → copies the prompt and moves to `#ask-agent`

Needs Docker and a terminal. Not a hosted service, and not a no-code app builder.

---

## Who it's for

- **Developers and tinkerers who build with AI agents.** You use Claude Code, Cursor, Claude Desktop or another MCP client, and you want a local backend to point it at.
- **Educators and learners.** You want to see how tables, APIs, vectors, graphs and agents fit together, on an instance you can reset.
- **Teams prototyping something sensitive.** You want the database on a machine you control while you test an idea with sample data, before any vendor decision is made.
- **Anyone who wants a local MCP toolbox for their own data.** Notes, documents and records in Postgres, with an agent that can work with them.

### Who it isn't for (yet)

- If you want a working app without opening a terminal, use Dyad or Lovable.
- If you're shipping to real users and need accounts, hosting and compliance, use Supabase, Nhost or Xano.

---

## What it fixes

### Your agent can write code. It still needs somewhere to put things.

An AI agent can draft a schema in seconds. Then you spend the afternoon standing up a database, an API and an MCP server so it can actually use them.

In mAIcro you define tables and reload the schema, and the GraphQL types, queries and mutations are generated for you. Turn on MCP and compatible AI clients can see those operations and the schema, and call them. You choose the client, decide what it may access, and review what it changes.

### A prototype shouldn't need five services.

A database here, a vector store there, a graph database, a job scheduler, then glue code for the APIs. Most of a prototype's first week goes on plumbing.

mAIcro puts PostgreSQL 18, pgvector, Apache AGE, workflow chains, cron jobs and an embedded IDE in one container. One install, and one place to look when something breaks.

### Rows aren't enough.

Real problems have relationships (who worked where, which document belongs to which client) and fuzzy questions (which passage answers this?).

Store embeddings next to your data and use similarity search. Model relationships as a graph and query them with openCypher. Both sit in the same Postgres as your tables, and both can be wrapped as GraphQL operations. Similarity isn't the same as truth, so check what comes back against the source.

### Learn how it works, not just that it works.

App builders hide the mechanism. That's fine until you need to teach it, debug it or explain it to someone else.

mAIcroverse is a separate learning instance with guided courses: Markdown Foundations, Data Import, Book Club, HR Graph, API Wrappers, Scheduled Weather Collector, AI Signatures and Types, Forms, Browser Automation and more. Each course states what you'll learn and what its setup will delete. Break it, reset it, try again.

### Keep the database on a machine you control.

You want to test an idea about client or patient workflows, but you can't put real records into a cloud trial to find out.

mAIcro runs on your computer or your own server. The database and files live in a data folder you choose (~/maicro-data by default). The Forms course walks through an aged-care intake form with demonstration data.

**Know where the edges are.** Anything you send to an AI model or an external API leaves your machine, and the learning setup uses OpenRouter. mAIcro isn't a compliance tool. Use sample data until you know where everything goes.

### No account, and nothing to pause.

Hosted free tiers pause idle projects, cap records or throttle requests, usually mid-experiment.

mAIcro is a public Docker image. Pull it, run it, leave it for a month and come back. Model usage is billed by your own provider, through your own key.

---

## Simpler personal software, explained

mAIcro's tagline is "simpler personal software". In practice that means software for one person or a small team, built on parts you can open and read. A book club's dataset with search and a graph of how it connects. A client register with linked documents. A job that collects weather readings on a schedule. Markdown reports from ASX market data.

Those examples come straight from the courses. Not every idea needs to become a company or scale to millions of users. Most need a database, a way to query it, and a way to run the next step.

> Note: "Not every idea needs to become a company" is mAIcro's own line, from the blog post *A smaller kind of software*.

---

## Features: What's in the container

| Feature | What it does |
|---|---|
| PostgreSQL 18 and generated GraphQL | Define tables, reload the schema, and query through generated GraphQL types, queries and mutations. Connect your own frontend to the same API. |
| Vectors | Store embeddings with pgvector and run similarity search alongside your data. |
| Graphs | Model relationships with Apache AGE and query them with openCypher. Wrap Cypher as reusable GraphQL operations. |
| Workflows and cron jobs | Compose operations into chains, including AI and data-processing steps, and run them on a schedule. |
| AI tasks with typed outputs | Define AI tasks and signatures whose outputs are backed by registered GraphQL types. |
| API and SQL wrappers | Bring external REST APIs or SQL into your schema as named GraphQL operations. |
| TypeScript modules | Extend the platform with your own code. |
| MCP server | Compatible AI clients can access mAIcro's tools, including GraphQL operations and schema information. |
| Embedded IDE | Work in your browser, with a Markdown wiki, file storage, forms, charts and dashboards, and memory blocks. |
| Files as data | Query CSV and JSONL files in file storage directly as GraphQL results. |
| Browser automation | Script browser sessions, interact with pages and extract data. |
| Local help and CLI | Documentation served from your own instance, plus a command-line tool. |

---

## Limits, plainly

mAIcro is early. Here's what that means before you install it.

- **It's alpha.** Version 0.1.x, with new releases every few days. Expect changes. Don't use it for production or real client data yet. **[check]**
- **It's one person's project.** mAIcro is built by Chris Nurse at BloxEZ in Perth, Western Australia.
- **You need Docker.** Docker Desktop on macOS or Windows, or Docker Engine on Linux. The image is about 635 MB. **[check]**
- **Read the installer first.** The install command downloads and runs a script. It can start Docker, ask for administrator privileges, create configuration and data folders, and replace an existing container named maicro.
- **Change the defaults.** The installer uses default credentials and signing secrets unless you configure them, the learning instance resets its admin key to a known value, and ports are published on your machine. Keep it to yourself until you've changed them.
- **AI goes through your own provider.** The learning setup asks for an OpenRouter API key. Local-model support isn't documented yet. **[check]**
- **Source and terms aren't published yet.** The courses repo is GPL-3.0. The platform source, licence and terms aren't public. **[check]**
- **There's no hosted version.** No browser trial, and no published pricing.

---

## Compare: mAIcro or something else?

These are good tools. Pick the one that matches the job.

**Supabase**
- Choose Supabase when you're shipping an app to real users and need auth, storage and a hosted path to production.
- Choose mAIcro when you're prototyping or teaching on your own machine and want graphs, workflows and MCP in the same container.

**Xano**
- Choose Xano when a team needs a governed, compliant backend in production.
- Choose mAIcro for the prototype that comes before that.

**Dyad or Lovable**
- Choose Dyad or Lovable when you want a working app without opening a terminal.
- Choose mAIcro when you want the backend underneath: data, vectors, graphs and workflows your agent can work with.

**n8n**
- Choose n8n when the job is moving data between lots of SaaS tools.
- Choose mAIcro when the job is storing, relating and querying your own data, with workflows next to it.

**PocketBase**
- Choose PocketBase when you want the smallest possible backend, with auth built in and no Docker.
- Choose mAIcro when you need Postgres, GraphQL, vectors, graphs and MCP together.

---

## Get started

You'll need Docker and a terminal.

1. **Install and start Docker.** Docker Desktop on macOS (Intel or Apple Silicon) or Windows, or Docker Engine on Linux. On Windows you can use PowerShell, or WSL 2 with Docker integration turned on.
2. **Read the install script, then run it.** On macOS, Linux or WSL:
   ```
   curl -fsSL https://raw.githubusercontent.com/bloxez/maicroverse/main/maicro-install/run.sh | sh
   ```
   For PowerShell on Windows, use the command on the mAIcro get-started page.
3. **Open the local help.** Go to http://localhost:4321/help/ide/ to get to know the IDE and finish setup. Use your own port if you changed it. Data is kept under ~/maicro-data by default. If the page doesn't open, check Docker and run docker logs maicro.
4. **Optional: add the learning instance and courses.** With the container running:
   ```
   docker exec -it maicro bash -lc 'curl -fsSL https://raw.githubusercontent.com/bloxez/maicroverse/main/create-mv.sh | bash'
   ```
   It asks for an OpenRouter API key, resets the learning instance's admin key, and allows outbound requests to any host. Treat that instance as disposable.

Links: Full install guide on maicro.app (https://maicro.app/get-started) · Install docs on GitHub (https://github.com/bloxez/maicroverse/blob/main/readme/install.md) · Course catalogue (https://maicro.app/courses) · Docker image (https://hub.docker.com/r/bloxez/maicro-g2a)

> Note: "Read the install script" links to https://github.com/bloxez/maicroverse/blob/main/maicro-install/run.sh. The Windows PowerShell command lives on maicro.app/get-started and isn't reproduced here, so this page can't drift out of sync with it.

---

## Ask your agent about mAIcro

Not sure it fits? Copy this prompt into Claude, ChatGPT, Cursor or whichever agent you use. It asks the agent to read mAIcro's public pages and Docker image, explain it plainly, map it to what you're building, and tell you when another tool would suit you better.

**[Ask your agent about mAIcro and how it would work with your projects]** (copies the prompt)

Confirmation: **Prompt copied — paste it into your agent.**

If copying fails: **Couldn't copy automatically. The prompt is selected below: press Ctrl+C (or Cmd+C) to copy it.**

Arriving by the direct link (`?prompt=1` or `#ask-agent`): the page scrolls to this section and tries to copy. Browsers usually only allow copying after a click, so if it can't copy the page shows: **The prompt is selected below. Press Ctrl+C (or Cmd+C) to copy it, or use the Copy prompt button.**

Above the prompt: **[Copy prompt]** · **Download prompt.txt** · **Direct link to this prompt** (`?prompt=1#ask-agent`)

The prompt (shown in full in a `<pre>`; identical to [`site/prompt.txt`](../site/prompt.txt)):

```text
I'm looking at mAIcro (https://maicro.app). Help me work out whether it fits my projects, and be straight with me.

1. Read the public sources first. If you can browse, fetch:
- https://maicro.app and https://maicro.app/get-started (the site is a JavaScript app, so a plain fetch may return very little text; if so, rely on the sources below)
- The Docker Hub image: https://hub.docker.com/r/bloxez/maicro-g2a
- The mAIcroverse repo with install docs and courses: https://github.com/bloxez/maicroverse (README, readme/install.md, maicro-install/run.sh)
If you can't browse, say so, and work only from this summary: mAIcro is a free, self-hosted backend toolbox that runs as one Docker image (bloxez/maicro-g2a). It bundles PostgreSQL 18 with generated GraphQL, pgvector for vectors and similarity search, Apache AGE for graphs (openCypher), workflow chains and cron jobs, AI tasks with typed outputs, TypeScript modules, wrappers that turn SQL or external REST APIs into GraphQL operations, an embedded IDE and an MCP server. Guided courses live in the mAIcroverse repo. AI models are configured with the user's own OpenRouter key. It is alpha software from a solo developer.

2. Explain what mAIcro is in plain terms, in a few sentences. Say what it is not: it is not a hosted service and not an app builder that writes a frontend for me.

3. Map it to my projects. If you don't know what I'm working on, ask me before going further: what the project does, who uses it, what data it handles, and which stack and AI tools I already use. Then tell me:
- which parts of mAIcro I would actually use (tables and GraphQL, vectors, graphs, workflows, MCP, courses) and for what
- what a first one-hour experiment would look like, using sample data
- how my agent would connect to it over MCP, and what I should and shouldn't let it access

4. Be honest about the trade-offs:
- It is alpha (0.1.x as of November 2026) and maintained by one person. Not for production or real client data yet.
- It needs Docker and a terminal. The installer is a curl-to-shell script I should read before running. Default credentials, the learning instance's admin key and published ports need changing before anyone else can reach it.
- Running it locally doesn't keep data local once it is sent to an AI model or an external API.
- The platform source and licence aren't public yet. The courses repo is GPL-3.0.
Then tell me plainly when something else would suit me better, for example: Supabase or Nhost for a production app with auth and hosting; Xano for a governed team backend; Dyad or Lovable to build an app without code; n8n to automate across many SaaS tools; PocketBase for the smallest backend with no Docker; Directus for a team admin over an existing database.

Don't overstate what mAIcro does. If the sources don't confirm a feature, say it's unconfirmed rather than guessing.
```

---

## Footer

mAIcro is built by Chris Nurse (BloxEZ), Perth, Western Australia.

Links: maicro.app · Docker image · mAIcroverse on GitHub · Courses

Draft page. Facts checked against public sources on 21 November 2026.

> Note: Remove the "Draft page" line once the page is approved and published by the mAIcro team.
