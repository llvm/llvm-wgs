# Notes - June 2026

**NOTE:** Americas-friendly sync-up **cancelled**.

## Participants EU/Asia-friendly sync-up - Tuesday 2026/06/09, 5:30PM JST, 1h

- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
- [@Lorenzo](https://discourse.llvm.org/u/lorenzo)
- [@slotosch](https://discourse.llvm.org/u/slotosch)
- [@petbernt](https://discourse.llvm.org/u/petbernt)
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)
- [@uwendi](https://discourse.llvm.org/u/uwendi)

## Links

[docs.google.com](https://docs.google.com/presentation/d/128UiQp0UDyg-BRDKrsNi5esa-jRQVguRa_kHnmiWTu8/edit?slide=id.p1#slide=id.p1)

### [202606\_llvm\_qual\_wg](https://docs.google.com/presentation/d/128UiQp0UDyg-BRDKrsNi5esa-jRQVguRa_kHnmiWTu8/edit?slide=id.p1#slide=id.p1)

LLVM Qualification WG Sync-up meeting #12 June 2026 Focus: Ongoing actions

## 1. Working Group updates

The group marked its first anniversary.

The initial `fusa-qual-wg` directory has been created in the `llvm-wgs` repository. However, the requested write and merge permissions, as well as the proposed `CODEOWNERS` update, were still pending at the time of the meeting.

The group agreed to remain patient while the LLVM Infrastructure team processes the permissions request.

## 2. Conversion of qualification workflows to Mermaid

[@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) presented initial work to convert the qualification workflow diagrams from presentation slides into Mermaid.

The main expected benefits are:

- diagrams stored in a text-based format
- easier review of diagram changes through pull requests
- flexible styling
- export to formats such as SVG and PNG
- improved integration into GitHub documentation

Four workflows are currently expected to be converted:

1. software library qualification methodology
2. determination of the need for confidence in software-tool usage
3. software-tool confidence workflow from the tool provider’s perspective
4. software-tool confidence workflow from the tool user’s perspective

The group expressed a preference for vertical layouts when diagrams are intended for GitHub pages or Markdown documentation. Horizontal versions may remain useful for presentations.

Mermaid may also support hyperlinks when diagrams are rendered through HTML or another interactive format, although links would not remain interactive in ordinary image exports.

[@slotosch](https://discourse.llvm.org/u/slotosch) noted that the term **SBOM** may be misleading in the context of the safety-oriented workflow under discussion. An SBOM normally describes the software components contained in a product or tool and is especially associated with security and supply-chain analysis. For the workflow in question, a simpler term such as “list of tools” or a description of tool dependencies may be more appropriate.

[@slotosch](https://discourse.llvm.org/u/slotosch) also observed that the need to consider a tool for qualification ultimately depends on how the tool is used in the project’s safety or compliance argumentation. A tool that contributes to a claimed safety activity may enter the scope, whereas the same tool might remain outside the scope when it is not relied upon for that argument.

The group acknowledged that there can be several valid ways to structure the early tool-confidence analysis and that the proposed workflows are intended as guidance rather than the only possible interpretation of ISO 26262.

In conclusion, the initial Mermaid conversion was positively received. [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) will continue experimenting with the remaining and more complex workflows.

## 3. libc++ qualification-enablement proof of concept

[@petbernt](https://discourse.llvm.org/u/petbernt) presented an update and demonstration of his proof of concept for improving behavior-to-test traceability in `libc++`.

The approach is based on:

- describing library behavior as small, atomic requirements
- assigning stable identifiers to those behaviors
- mapping the identifiers to relevant test cases
- checking the consistency and completeness of the mappings with scripts
- executing only the tests associated with the annotated behaviors
- generating coverage information for the annotated tests

The demonstration showed that the tooling can detect:

- unknown requirement identifiers
- requirements that have not been mapped to tests
- inconsistent or missing traceability annotations

[@petbernt](https://discourse.llvm.org/u/petbernt) has discussed the concept with members of the `libc++` community. The response was encouraging, and Louis offered to help formulate an RFC so that the proposal can be presented to the broader LLVM community for feedback.

[@slotosch](https://discourse.llvm.org/u/slotosch) asked how the behavior descriptions would relate to requirements from specific versions of the C++ standard. [@petbernt](https://discourse.llvm.org/u/petbernt) explained that the upstream mechanism would describe the behavior implemented by the library rather than copy normative text directly from the C++ standard. A downstream qualification effort could then map the stable behavior identifiers to the applicable clauses of a specific C++ standard version.

This separation is useful because:

- the ISO C++ standard is copyrighted
- clause numbering changes between standard editions
- normative clauses often contain several behaviors that need to be decomposed into atomic requirements before they can be traced meaningfully to tests

[@slotosch](https://discourse.llvm.org/u/slotosch) characterized the proposed upstream mechanism as providing a substantial part of the necessary traceability infrastructure, while leaving the final mapping to a specific standard and qualification context to downstream users.

The group also discussed test-design information such as equivalence classes and boundary-value analysis. These may eventually be useful additions, but [@petbernt](https://discourse.llvm.org/u/petbernt) emphasized the importance of starting with a lightweight, incremental proposal that has a realistic chance of being accepted upstream.

The mechanism may also be useful beyond `libc++`, for example to trace compiler options, security features, or other LLVM functionality to their tests.

The group supported continuing the proof of concept and preparing an RFC for wider LLVM community review. [@petbernt](https://discourse.llvm.org/u/petbernt) also indicated that the work still needs to undergo the required internal intellectual-property review before it can be published from his current private repository.

## 4. LLVM Functional Safety Model

[@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) presented the current draft of the LLVM Functional Safety Model. The objective is to establish criteria for identifying which LLVM components may be relevant in safety-related contexts. The work is inspired in part by the LLVM Security Response Group’s threat model, while addressing safety-specific concerns.

The current draft contains a table covering LLVM components and proposed information such as:

- assumptions
- safety lifecycle phases
- representative use cases
- possible failures
- rationale

The document is still an early draft, and the group was invited to review both its structure and its technical content.

[@slotosch](https://discourse.llvm.org/u/slotosch) recommended making an explicit distinction between:

- **tools**, which are used during development but do not become part of the delivered product
- **libraries or runtime components**, which are incorporated into the product
- potentially, other software components that are deployed as part of the final system

This distinction is important because the applicable safety activities and expectations differ significantly. For example:

- development tools may be addressed through tool-confidence or tool-qualification activities
- libraries and runtime components that become part of the product may require software requirements, traceability, testing, and structural coverage evidence
- a JIT compiler deployed in the target product would need to be considered differently from an offline compiler used only during development

The group also noted that security and safety classify components differently. Security analysis often examines the internal composition and dependencies of both tools and libraries. Safety analysis is more strongly driven by intended use, system integration, functional requirements, and the role of the component in the safety argument.

[@uwendi](https://discourse.llvm.org/u/uwendi) suggested coordinating again with the Security Response Group, particularly with the authors of the threat model, to discuss alignment of structure and terminology while preserving the differences between safety and security analysis.

## Actions

- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) Continue converting the qualification workflows to Mermaid, including the more complex diagrams.
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) Explore both vertical and horizontal layouts and the available options for styling and links.
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) / [@uwendi](https://discourse.llvm.org/u/uwendi) Reconsider the use of the term “SBOM” in the safety workflow and replace it where it may be misleading.
- [@petbernt](https://discourse.llvm.org/u/petbernt) Begin preparing an RFC describing the behavior-to-test traceability proposal.
- [@petbernt](https://discourse.llvm.org/u/petbernt) Share the RFC draft with the Qualification Working Group for review.
- [@petbernt](https://discourse.llvm.org/u/petbernt) Initiate the required internal IP review so that the proof of concept can be published.
- **All:** Review and comment on the draft Functional Safety Model.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) / [@uwendi](https://discourse.llvm.org/u/uwendi) Update the Functional Safety Model to distinguish tools from libraries and other product-integrated components.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) / [@uwendi](https://discourse.llvm.org/u/uwendi) Consider arranging a follow-up exchange with the LLVM Security Response Group after another internal review round.
