# Notes - November 2026

> Use of AI assistance for auto-transcription was done as explained in the [LLVM Qualification Group's AI Transcription Policy](https://llvm.org/docs/QualGroup.html#ai-transcription-policy).

## Participants EU/Asia-friendly sync-up - Tuesday 2026/11/10, 5:30 PM JST, 1h

[@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
[@edjones](https://discourse.llvm.org/u/edjones)
Micael Borgefeldt
[@slotosch](https://discourse.llvm.org/u/slotosch)
Victor Lu
[@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
[@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)
[@uwendi](https://discourse.llvm.org/u/uwendi)

## Participants Americas-friendly sync-up - Friday 2026/11/13, 9:00 AM JST, 1h

[@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
Christopher Bell
[@michaelrj-google](https://discourse.llvm.org/u/michaelrj-google)
[@petrhosek](https://discourse.llvm.org/u/petrhosek)
Victor Lu
[@uwendi](https://discourse.llvm.org/u/uwendi)

## Links

https://docs.google.com/presentation/d/1OjPy6bhwrQ4Irj8dxHzqWoJonj28TjiArd5YxQCFLqM/edit?usp=sharing

- [Runtimes Workshop notes](https://discourse.llvm.org/t/llvm-dev-meeting-2026-runtimes-workshop/92707)
- [RFC on lightweight conformance test traceability for libc++](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468)
- [libc++ PoC behavior file for array](https://github.com/petbernt/llvm-project/blob/libcxx_qual_poc/libcxx/behavior/array.yaml)
- [libc++ PoC mapped test for array::fill](https://github.com/petbernt/llvm-project/blob/libcxx_qual_poc/libcxx/test/std/containers/sequences/array/array.fill/fill.pass.cpp)
- [llvm-libc PoC](https://github.com/petbernt/llvm-project/tree/libc_qual_poc)
- [clang-doc documentation](https://clang.llvm.org/extra/clang-doc.html)
- [Erick Velez's US LLVM 2025 presentation on clang-doc](https://youtu.be/vuHF_ZeAPVI?si=QQK_oivunDwnTJu3)
- [SPDX for Functional Safety presentation](https://lists.spdx.org/g/spdx/attachment/1759/0/SPDX%20for%20Functional%20Safety.pdf)
- [Revisiting LLVM's development practices](https://discourse.llvm.org/t/revisiting-llvms-development-practices/92763)

## Discussion

### US LLVM conference feedback

- [@uwendi](https://discourse.llvm.org/u/uwendi) shared feedback from the talk and Runtimes Workshop. [@petbernt](https://discourse.llvm.org/u/petbernt) presented the workshop remotely, and [@uwendi](https://discourse.llvm.org/u/uwendi) delivered the talk in person. Feedback on both sessions was positive.
- [@ldionne](https://discourse.llvm.org/u/ldionne) requested responses to the RFC comments and a PR allowing libc++ maintainers to review the PoC. The WG discussed what should be clarified or improved before preparing that PR.
- Questions after the talk included how the WG could help with the recurring shortage of reviewers and what insights from the LLVM assessment using the ELISA Lighthouse checklist could be shared with the community. [@uwendi](https://discourse.llvm.org/u/uwendi) referred members to the Discourse post on LLVM's development practices. She also shared the WG's process documentation with Flang contributors interested in time-zone arrangements and decision making.

### Behavior file specification and standard applicability

- Following [@petbernt](https://discourse.llvm.org/u/petbernt)'s suggestions, participants supported starting a shared specification for behavior files, defining the metadata fields, their meaning, and how to interpret them. This would provide a basis for a schema and schema validator.
- The EU/Asia discussion used the array behavior file and its mapped tests to examine the current metadata. Participants supported replacing the single `standard` string with a `standards` list to describe applicability across several standard editions without duplicating entries for each edition.
- During the Americas discussion, @michaelrj-google and @uwendi also discussed a list of standards and suggested considering bounds such as `from-std-version` and `up-to-std-version`. These were additional options for expressing applicability.
- [@michaelrj-google](https://discourse.llvm.org/u/michaelrj-google) supported formalizing the semantics and addressing known gaps while the PoCs are still small, when changes are relatively inexpensive. He noted that this work could also benefit the llvm-libc PoC.
- [@slotosch](https://discourse.llvm.org/u/slotosch) highlighted the difficulty of tracking requirements whose section references change between standard editions while their meaning stays the same. The specification needs to account for source references and changes across editions, including defect reports raised in the RFC discussion.
- [@uwendi](https://discourse.llvm.org/u/uwendi) recalled [@Endill](https://discourse.llvm.org/u/endill)'s feedback about requirements stated outside the clauses describing individual functions. Examples include rules applying to a whole header or library, such as namespace and addressability rules.
- Participants discussed classes, types, templates, and compile-time behavior as further cases to consider. Function-level examples provide a starting point, while broader requirements need further discussion.
- [@slotosch](https://discourse.llvm.org/u/slotosch) and [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) discussed the relationship between specified library behavior and support provided by particular compilers. They supported leaving compiler-specific information out of the behavior files and documenting the scope of the approach clearly.

### Formats and traceability tooling

- [@petbernt](https://discourse.llvm.org/u/petbernt)'s openness to alternatives to YAML was recalled. Participants discussed choosing a manageable initial representation and defining its semantics and validation needs.
- During the Americas discussion, [@petrhosek](https://discourse.llvm.org/u/petrhosek) suggested exploring clang-doc and whether behavior descriptions could be integrated into documentation comments. This could make use of Clang's source parsing and documentation extraction infrastructure and reduce the amount of custom extraction code needed by the checker. The proposed use case would require investigation and potentially extensions to clang-doc.
- Participants discussed identifying a minimum viable implementation and whether clang-doc contributors might be interested in supporting it. Erick Velez's US LLVM 2025 presentation was shared as background. [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) and [@uwendi](https://discourse.llvm.org/u/uwendi) expressed interest in this direction, and [@uwendi](https://discourse.llvm.org/u/uwendi) favored building on tools developed within the LLVM community where the WG could also contribute.
- Victor Lu suggested investigating SPDX as another way to represent behaviors, traceability links, and relationships between components. Participants noted that agreeing on the semantics could make it easier to support different representations as the approach matures.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) emphasized the reliability of the checker and extraction tooling. If users rely on their outputs for safety-critical work, confidence in those tools, and potentially qualification, would need consideration according to their use.

### Maintenance and wider collaboration

- The questions of who will write, review, and maintain behavior descriptions remain important. [@uwendi](https://discourse.llvm.org/u/uwendi) recalled [@ldionne](https://discourse.llvm.org/u/ldionne)'s suggestion to discuss the initiative with WG21 and other implementations as a possible route toward sharing the work.
- [@petbernt](https://discourse.llvm.org/u/petbernt) described his interest in an ecosystem of tools built on LLVM to support software quality. The WG expressed support for these initiatives and interest in contributing where they could also benefit safety-critical uses.

## Actions

- [@uwendi](https://discourse.llvm.org/u/uwendi): Share a document on Discord where WG members can collaborate on the behavior file specification.
- WG members:
  - Continue the discussion asynchronously on Discord and contribute to the specification, including standard applicability, broader requirement scopes, and validation expectations.
  - Provide further comments on the RFC and checker.
  - Define the checker changes and supporting validation needed with @petbernt as the specification develops.
- [@uwendi](https://discourse.llvm.org/u/uwendi) [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez): Explore a minimum viable clang-doc integration and possible collaboration with its contributors.
- [@uwendi](https://discourse.llvm.org/u/uwendi): Investigate whether SPDX could support the behavior and traceability model.
