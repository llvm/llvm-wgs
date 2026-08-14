# Notes - August 2026

## Participants Americas-friendly sync-up - Friday 2026/08/14, 9:00 AM JST, 1h
* [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
* [@uwendi](https://discourse.llvm.org/u/uwendi)

## Participants EU/Asia-friendly sync-up - Tuesday 2026/08/11, 5:30 PM JST, 1h
* [@slotosch](https://discourse.llvm.org/u/slotosch)
* [@petbernt](https://discourse.llvm.org/u/petbernt)
* [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
* [@uwendi](https://discourse.llvm.org/u/uwendi)
* [@zakyhermawan](https://discourse.llvm.org/u/zakyhermawan)

## Links

https://docs.google.com/presentation/d/17J933rV0cDPilqLjEI0pe7C-J6kDsrsOhQzNjnRVrkY/edit?slide=id.p1#slide=id.p1

* [2026 LLVM Developers’ Meeting program](https://discourse.llvm.org/t/announcing-the-2026-llvm-developers-meeting-program/91470)
* New [RFC: Lightweight Conformance Test Traceability for libc++](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468)
* [Open WG pull requests](https://github.com/llvm/llvm-wgs/pulls)
* Examples shared during the EU/Asia-friendly meeting:
  * [llvm-project PR #128142](https://github.com/llvm/llvm-project/pull/128142)
  * [LLVM libc header implementation status](https://libc.llvm.org/headers/index.html)
  * [llvm-project issue #122006](https://github.com/llvm/llvm-project/issues/122006)

## Discussion

### WG news and focus before October

*LLVM in Safety-Critical Industries: Toward a Shared Qualification Layer Upstream*, was accepted as a technical talk for the 2026 US LLVM Developers’ Meeting. A complementary discussion on *Lightweight Conformance Test Traceability for LLVM Runtime Libraries* is also planned for the Runtimes Workshop.

Before October, the WG would like to complete (or at least clearly frame) the main areas of current work:
* the LLVM safety model (identifying the LLVM components and behaviors that may be relevant to safety-critical usage)
* lightweight conformance traceability for runtime libraries (connecting expected behaviors with implementation and test evidence)
* the tool-confidence templates, guides, and workflows (for tool evaluation and qualification activities, and safety manual)
* and other quality-related areas: defect prediction, Alive2 and translation-validation tools, assessment of LLVM development practices...

The presentation should explain the value of this work not only for safety compliance, but also for broader software, documentation, and process quality. At the same time, it should acknowledge that stronger assurance may require some additional effort from upstream contributors.

Given the 20-minute presentation slot, the material should be concise and visual.

### Open contributions and review coordination

The group discussed the limited review bandwidth available for the current pull requests. Detailed reviews should continue asynchronously on GitHub and Discord, while synchronous meetings should focus on blockers and decisions. Additional reviewers from the broader LLVM community would be welcome, particularly when they can contribute compiler, library, documentation, or infrastructure expertise.

For the workflow diagrams being developed by [@zakyhermawan](https://discourse.llvm.org/u/zakyhermawan), the group agreed to use GitHub’s native Mermaid rendering instead of maintaining a separate third-party rendering script. The native solution provides sufficient readability while avoiding an additional tool and its associated maintenance burden.

[@zakyhermawan](https://discourse.llvm.org/u/zakyhermawan) and [@uwendi](https://discourse.llvm.org/u/uwendi) will review the remaining comments on the workflow contribution together. [@petbernt](https://discourse.llvm.org/u/petbernt) has also started reviewing the open pull requests incrementally.

### Accessibility of the templates and standards-related guidance

The qualification template and guide currently under preparation will compare qualification concepts and methods across several safety standards. The guide is expected to explain concepts such as tool validation and test coverage without reproducing standards text.

Participants emphasized that the documentation should provide enough context for readers who do not already know the standards. The main challenge is not only technical correctness, but also translating standards terminology into language that compiler and library engineers can understand and use.

The Americas-friendly discussion also identified a potential ambiguity between:
* the confidence currently supported by the available evidence for a tool or library, and
* the confidence required for a particular tool or library usage.

This distinction should be made explicit in the documentation and presentation material, keeping the WG artifacts sufficiently generic to support the different standards-based approaches. The intended use, applicable standard, safety integrity level, and existing evidence influence the qualification strategy and the methods selected, but do not require different templates for each integrity level.

A deeper treatment of AI-based tool qualification was considered a possible future topic.

### Specification and documentation of LLVM behavior

A recurring concern is that some expected LLVM behaviors remain implicit, are documented only in code-review discussions, or are described by referring to another implementation such as GCC or glibc. LLVM components may intentionally make different implementation choices, making those external references insufficient as durable specifications.

The examples shared during the meeting illustrated several related problems:
* implementation decisions and intentional divergences may be visible in a pull-request discussion but not in long-term documentation
* implementation-status pages may be incomplete or no longer aligned with the code
* contributors often prioritize implementation work over documenting the resulting behavior

These gaps are relevant to the runtime-library traceability RFC. Durable descriptions of expected behavior, connected to implementation and test evidence, would improve both conformance visibility and general software quality.

The classification of compiler-generated built-ins and the boundary with Compiler-RT was also raised. It is not always clear whether a built-in should be treated as compiler behavior, generated target code, or library software. This remains a grey area and may deserve a future WG position or guidance.

### Known-issue analysis and traceability

The analysis of known LLVM issues represents a substantial effort for downstream users. A downstream project may need to examine thousands of reports to determine whether an issue is relevant to its version, configuration, target, language, optimization settings, or set of used features.

The group discussed how better issue metadata and traceability could reduce this effort. Useful improvements could include associations between issue reports and:
* affected LLVM components and features
* relevant command-line options
* optimization levels and source languages
* affected and fixed versions
* the version or change in which a defect was introduced

Improved tooling could then automate part of the filtering that downstream users currently perform manually. This topic is relevant to both functional safety and security and was identified as a possible future initiative.

### Translation validation and formal methods

On several occasions (example [here](https://docs.google.com/presentation/d/1hbXKpUSMP1PxCAEZGv8lqMS6EhGgDlOqcS_3PuGjp9k/edit?slide=id.g3c2c04e355e_0_646#slide=id.g3c2c04e355e_0_646)), the WG has highlighted the potential value of formal methods (including translation validation and tools such as Alive2) as sources of confidence and qualification evidence for compiler transformations.

Alive2 would benefit from additional contributor capacity to extend its coverage and support broader use. However, identifying a practical way for the Qualification WG to contribute directly remains challenging. Translation validation also depends on sufficiently precise semantics for LLVM IR: complex or underspecified behavior can limit what can be validated and how the results can be interpreted.

[@uwendi](https://discourse.llvm.org/u/uwendi) and [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee) will discuss Alive2 and related translation-validation tools in more detail, with the aim of explaining more clearly how these techniques could contribute to compiler qualification.

The WG does not currently plan to establish formal methods as a separate workstream, particularly because LLVM already has a Formal Specifications WG. Future coordination with that group may nevertheless help connect formal specifications, translation validation, and qualification needs.

## Actions

* [@zakyhermawan](https://discourse.llvm.org/u/zakyhermawan): update the workflow contribution to use GitHub-native Mermaid rendering
* [@zakyhermawan](https://discourse.llvm.org/u/zakyhermawan) and [@uwendi](https://discourse.llvm.org/u/uwendi): meet to address the remaining review comments on the workflow contribution
* [@uwendi](https://discourse.llvm.org/u/uwendi): finalize the tool qualification template and guide, open the PR, and share it on Discord for review
* [@uwendi](https://discourse.llvm.org/u/uwendi): complete the review of the current safety-model (Google Drive) and prepare a PR to add it to the WG repository
* [@uwendi](https://discourse.llvm.org/u/uwendi) and [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee): Discuss Alive2 and other translation-validation tools in more detail
* [@uwendi](https://discourse.llvm.org/u/uwendi): add the candidate future directions raised during the meetings to the WG backlog
* [@uwendi](https://discourse.llvm.org/u/uwendi) and [@petbernt](https://discourse.llvm.org/u/petbernt): start framing the October presentation around the safety model, runtime-library traceability, and tool-confidence artifacts
* [@uwendi](https://discourse.llvm.org/u/uwendi): coordinate the September review cadence and the facilitation of the September 8th meeting, which [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) tentatively offered to host
* **All:** Continue reviewing and commenting on the open WG pull requests and the runtime-library traceability RFC asynchronously
