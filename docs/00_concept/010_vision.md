# 010 — The original brief

> **Status:** verbatim transcript. Do not edit. Recorded 2026-09-19.
> Typographical and spelling irregularities are preserved deliberately.
> Commentary and disagreement belong in [020_critique.md](020_critique.md).

---

Allright, let's talk business intelligence. It is my profession. I've been doing this for 26 years, building dashboards, data warehouses, doing business analysis, being a product owner.

So I was thinking how we can put LLMs/AI to good use.

Here's my thought: part of building data environments is really deterministic, like building data logistics. But part of it is also very context driven, like interpreting what the data means, finding similarities across different data sets (to join data sets for example), figuring out how to turn raw data into actionable insights, doing regression testing etc.

So there is a role to fill for LLMs/AI.

Basically what I am thinking is that a properly instructed LLM with enough mandate and a workflow can build a data infrastructure autonomously, because the analysis part can be done independently. You could think of it like a web crawler, but instead it crawls the corporate network, scanning for data sources (of course with proper security clearance etc). But bear with me.

My working title is neural synaptic data network, but that's just a bunch of fancy words I threw together to evoke a kind of feeling. On the other hand there is a bit of an analogy here with dendrites that feel out, and try to make connections.

So what the system would do is:
-Poll available data sources, just to see what is available, of course with hints and tips from humans. We can view the data sources as the sensoric information that an organization has. And as the name implies, an organization is also a kind of organism.
-Then do some structured indexing, and also leave enough breadcrumbs for AIs to pick up. It can ask humans for more context, like, what is in this database, what is it for, but it can also infer it from the data itself. We're basically also building metadata on the available data sources.
-Then scan the table structures / meta data, the structured data, maybe even find patterns in available unstructured data. Again, build context and store it, and make it easily findable.
-Assess these data sources in terms of historization of data, volatility, basically assess if the data needs to be stored somewhere for future analysis. Here we are also already thinking in Data Vault terms. Do we see bags of keys / hubs, stuff that should be in satellites, if necessary, think of links. Can we leave the data in the system or is there a compelling reason to make copies?
-Then if necessary work out the data capture. Preferably light weight, open source technologies, again also building good indexes and trails of breadcrumbs everywhere and building meta data.
-Then look for similarities between data sets, see where more links can be set up between data sets. These would I guess be link tables in a Data Vault methodology. Again build link tables in a very lightweight, open source manner.
-Think of usefull aggregates that can be used for analyses.
-Think of gaps in the data, inconsistensies, data quality issues, make them known to humans, suggest fixes.
-Think of data marts, make propositions, build them, build analyses and visualizations, accompany them with story telling. We're thinking automated analyses. Also look at possibilities for machine learning, for predictive and anomaly detection.
-Assess the data infrastructure, the analyses, and think of ways to enrich the proprietary data with external data sources, open data, perhaps data that should be acquired, data that should be generated, in order to build better analyses.
-Have a test framework that constantly monitors for regression.
-Have an interface for humans to make suggestions, seek clarification etc.
-The whole system should be transparent to LLMs, it should be able to grow very large, but with enough breadcrumb trails everywhere that LLMs can still find their way without hogging the context windows, so really we need to make a kind of map of everything.
-To reiterate, the main themes are the autonomy of the LLM drive system, the LLMs decide where deterministic code is best applied, context is stored and made accessible, everything is done lightweight so it can be maintained to LLMs. There are a couple of human facing interfaces, for help in accessing data sources, for help in understanding the meaning of the data, the context, for help in accessing external data sources and the collection of extra data points (sensory information) and for discussing insights that the entire system produces. I don't think we can latch an LLM  decision making unit on top of it, but that could be an end goal. The data sources are sensory information, but the whole thing needs to be wired up, organized, connected and interpreted.

Your thoughts?

PS There is a folder connected, called C:\git\business-intelligence. I want to build another git repository, to first collect and organize these thoughts, and later on start building components. Please set up a git repository too and think of a basic folder structure to first organize these thoughts. I think you can see some steps ahead of what we need and where this is going.
