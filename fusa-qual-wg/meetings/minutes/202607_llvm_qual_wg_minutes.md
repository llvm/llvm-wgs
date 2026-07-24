# Notes - July 2026

## Participants Americas-friendly sync-up - Friday 2026/07/10, 9:00AM JST, 1h

* [@mrragava](https://discourse.llvm.org/u/mrragava) 
* [@michaelrj-google](https://discourse.llvm.org/u/michaelrj-google)
* [@petrhosek](https://discourse.llvm.org/u/petrhosek)
* [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
* [@uwendi](https://discourse.llvm.org/u/uwendi)

## Participants EU/Asia-friendly sync-up - Tuesday 2026/07/14, 5:30PM JST, 1h

* [@slotosch](https://discourse.llvm.org/u/slotosch)
* [@petbernt](https://discourse.llvm.org/u/petbernt)
* [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
* [@uwendi](https://discourse.llvm.org/u/uwendi)

## Links

https://docs.google.com/presentation/d/1SzWci_czUXXArIuBEiNuudciL2jIItaHD4hh-APbWxc/edit?usp=sharing

## Discussion

The monthly meetings per region covered different topics.
The Americas discussion covered threat/safety models, component-level trust, traceability, binary/API constraints, and WG scope, while the EU/Asia meeting covered mainly merged/open/planned PRs, LLVM conference submission, RFC work, and AI-related discussion.

### WG artifacts and meeting materials in `llvm-wgs`

The group reviewed the ongoing migration of WG materials from Google Drive to the `llvm-wgs` repository, under `fusa-qual-wg`. The goal is to use the GitHub repository as the longer-term storage location for WG outputs, including:

* meeting agendas/minutes/materials
* library-related qualification material
* software-tool-related qualification material
* safety model material
* development-process and quality assessment notes

The group agreed that storing LLVM-related WG material in LLVM-managed infrastructure is preferable to relying on personal Google Drives for long-term availability.

The meeting materials have started to be migrated to Markdown, with images used only where needed. This is intended to keep the materials lightweight, reviewable, and easier to maintain.

The group discussed the remaining access issue in `llvm-wgs`, related to unknown owners in the CODEOWNERS. As this is an infrastructure/project policy issue rather than something the WG can fix directly, [we communicated it to Infra](https://discourse.llvm.org/t/where-should-wg-meeting-materials-live/88913/48?u=uwendi). As a temporary workaround, WG members who cannot be manually added as reviewers may still be able to participate by commenting directly on PRs, where possible.

### Open PRs and current review work

The group reviewed [several ongoing PRs](https://docs.google.com/presentation/d/1SzWci_czUXXArIuBEiNuudciL2jIItaHD4hh-APbWxc/edit?slide=id.g3f816531502_0_4#slide=id.g3f816531502_0_4) related to the WG repository and the LLVM documentation. The following areas were discussed:

* already-merged PRs for meeting materials, agendas, and minutes
* open PRs related to WG artifacts and workflow material
* review comments on [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)’s PR
* [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)’s PR related to workflow views and graph generation
* the update to the main LLVM Qualification Group documentation page to point to the new `llvm-wgs/fusa-qual-wg` directory

For [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)’s graph-generation work, the group discussed whether relying on an external third-party rendering service is appropriate. The suggestion was to check whether an internal or locally available command-line solution, such as a Mermaid-based tool, could be used instead. Moreover, the workflow diagrams will be reviewed further to fix any wording issues.

### Security threat model and functional safety model

The Americas-friendly meeting included an extended discussion with [@mrragava](https://discourse.llvm.org/u/mrragava) about the Security Response Group’s threat-model work and possible overlap with the Qualification WG’s safety-model work.

[@mrragava](https://discourse.llvm.org/u/mrragava) explained that applying standard threat-modeling approaches directly to LLVM components is difficult because LLVM components can be used in very different ways. For example:

* an offline compiler used as a development tool is usually expected to run in a trusted environment
* components such as Clang tooling, language servers, libraries, or compiler services may be integrated into other products or services
* shader compilers or dynamic code generation may involve different data flows and trust boundaries
* the LLVM project cannot define one universal threat model that fits every possible downstream composition

The discussion therefore highlighted the need to reason at the component level, rather than trying to define a single global threat model for all of LLVM. 

The participants also discussed the parallel with functional safety. In safety standards, libraries and tools are treated differently:

* libraries may be embedded in the final safety-related system and therefore may need to be considered as "software components"
* software tools, such as compilers or analyzers, are not usually part of the final system, but their outputs may need to be trusted or verified

Libraries should probably be prioritized first from the qualification perspective, because they may become part of downstream safety-related systems. However, tool-related confidence remains relevant, especially where tool outputs cannot be fully verified downstream.

The participants identified a possible opportunity to avoid duplication between the Security Response Group’s threat-model work and the Qualification WG’s safety-model work. Rather than maintaining two independent models that could later diverge or contradict each other, there is a possibility of consolidating relevant safety and security considerations into a shared living document, including:

* component-level classification
* "trust" assumptions
* safety and security relevance
* validation expectations
* known limitations
* examples or prior defects
* rationale for how issues are triaged

[@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) noted that safety and security should not fundamentally contradict each other, since both can be seen as part of a broader software quality umbrella. If contradictions are found, they should be analyzed and resolved explicitly.

### Development process, quality frameworks, and upstream improvements

The participants discussed how the Qualification WG can provide value to the broader LLVM community without implying that upstream LLVM is responsible for downstream qualification.

The WG’s position remains that upstream cannot guarantee suitability for every downstream safety-critical product. However, upstream practices, documentation, tests, traceability, and assumptions can still provide useful evidence or context for downstream users.

[@uwendi](https://discourse.llvm.org/u/uwendi) explained that the current direction is to analyze LLVM practices using existing open-source quality and safety-oriented frameworks. She already presented a[ first examination of LLVM based on ELISA / Linux Foundation open-source quality checklist work](https://www.researchgate.net/publication/398600910_What_ELISA's_Lighthouse_OSS_Best_Practices_Reveal_About_LLVM's_State_of_Practice?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJwcm9maWxlIiwicHJldmlvdXNQYWdlIjoiaG9tZSIsInBvc2l0aW9uIjoicGFnZUNvbnRlbnQifX0). As a further step, she's planning to do a cross-analysis reusing OpenSSF best-practice material and a previous LLVM-related assessment done by Tom Stellard against their checklist. The goal would be to extract actionable insights that could be communicated back to the LLVM community, for example:

* areas where LLVM already has strong practices
* areas where documentation could be clearer
* parts of the process that could benefit from automation
* possible improvements to development policies or contribution workflows

This work is intended to support quality in general, not only functional safety.

### Library traceability RFC

[@petbernt](https://discourse.llvm.org/u/petbernt) reported on the draft RFC for conformance-test traceability in libc++. The draft has been shared with some runtime libraries maintainers for feedback before publication. Moreover, the topic could be relevant for the runtimes workshop at the LLVM Developers’ Meeting.

This topic, like the development process and quality assessment, also has a broader motivation than functional safety. Better traceability may also help with general quality, test coverage understanding, security-related concerns, maintainability of library conformance work, and downstream confidence arguments.

### Binary/API constraints and backend issues

[@petrhosek](https://discourse.llvm.org/u/petrhosek) raised an issue that is not fully covered by source-level traceability or conformance testing: binary-level and ABI/API constraints. He described backend changes that can break runtime libraries for some targets even though the source code itself is technically correct. The problem is related to target-specific binary/API expectations that are not currently easy to express or verify. There is a lack of tooling to describe and enforce such constraints. [@petrhosek](https://discourse.llvm.org/u/petrhosek) compared the desired tooling to something like a Clang-Tidy equivalent for binaries or object files.

This is relevant to the Qualification WG’s broader quality scope, even if it is not narrowly a functional safety topic. From [@uwendi](https://discourse.llvm.org/u/uwendi)'s point of view, translation-validation tools (which is a subtopic in the WG, related to backend verification) addresses ABI/API constraints, but needs to have a look again ([past demo](https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148/3?u=uwendi) from [@regehr](https://discourse.llvm.org/u/regehr)), and maybe extract some insights/ideas for [@petrhosek](https://discourse.llvm.org/u/petrhosek). 

### AI-assisted workflows and AI-related qualification topics

The group discussed two separate AI-related topics.

First, [@petbernt](https://discourse.llvm.org/u/petbernt) plans to add a section to the traceability RFC on how AI agents or AI-assisted workflows might help generate or refine atomic requirements, behavior descriptions, candidate tests, and traceability links.

The group agreed that AI could help reduce the manual burden of creating traceability information, but that human review remains essential. Any AI-generated requirements, tests, or traceability information would still need to be reviewed by contributors and maintainers before being upstreamed.

The group also noted that [LLVM already has a policy on AI tool usage](https://llvm.org/docs/AIToolPolicy.html), and that this policy should be referenced where relevant. The contributor remains responsible for what they submit.

Second, [@slotosch](https://discourse.llvm.org/u/slotosch) raised a separate topic: how to qualify compilers for AI models, such as compiler infrastructure that takes machine-learning representations or models and generates code for GPUs or other targets. This is distinct from using AI as a development assistant. It raises interesting questions about determinism, evidence, and qualification of tools used for AI model compilation. He will explore whether this topic is already being discussed in the broader LLVM community.

### Planned upcoming PRs

[@uwendi](https://discourse.llvm.org/u/uwendi) mentioned several planned PRs for the WG repository, including:

* publication of initial templates for confidence in the use of software tools
* additional workflow or onboarding material
* library-related methodology material from [@petbernt](https://discourse.llvm.org/u/petbernt)’s traceability work
* quality and development-process assessment notes
* possible material from [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) related to quality findings and defect prediction

The goal is to continue moving WG work from temporary or personal storage into the `llvm-wgs/fusa-qual-wg` repository, where it can be reviewed and maintained by the community.

## Actions

* [@mrragava](https://discourse.llvm.org/u/mrragava) to refine the Security Response threat-model draft and address [comments raised by the Qualification WG](https://docs.google.com/document/d/1Iqu6LIcXTVM9QUJJtYG8-m3l01FAuDaQ3UHspWxRVjw/edit?tab=t.0); review the Qualification WG safety-model spreadsheet and identify information that may overlap with the security threat-model work.
* [@mrragava](https://discourse.llvm.org/u/mrragava), [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez), and [@uwendi](https://discourse.llvm.org/u/uwendi) to explore whether the security threat model and functional safety model can be aligned into a common living document, avoiding duplication or contradictions; and how safety and security considerations can be framed together under a broader quality scope.
* [@mrragava](https://discourse.llvm.org/u/mrragava) to keep the WG updated on Discord, for example on where to work on / store the consolidated security+safety model.
* [@uwendi](https://discourse.llvm.org/u/uwendi) to follow up with Infra on the CODEOWNERS and access issue in `llvm-wgs`.
* [@petbernt](https://discourse.llvm.org/u/petbernt) to follow up with relevant maintainers regarding the libc++ conformance-test traceability RFC if no feedback is received by the end of the week.
* [@petbernt](https://discourse.llvm.org/u/petbernt) to add a section to the traceability RFC discussing possible AI-assisted workflows for generating or refining requirements, tests, and traceability links.
* [@slotosch](https://discourse.llvm.org/u/slotosch) to explore whether the LLVM community is already discussing qualification questions related to compilers for AI models.
* [@uwendi](https://discourse.llvm.org/u/uwendi) to prepare upcoming PRs for the initial tool-confidence templates and related WG artifacts.
* [@uwendi](https://discourse.llvm.org/u/uwendi) to continue preparing quality/development-process assessment notes, including the possible comparison between ELISA checklist results and OpenSSF-related LLVM assessment material.
* [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) and [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee) to review and address the remaining comments on their open PRs.
