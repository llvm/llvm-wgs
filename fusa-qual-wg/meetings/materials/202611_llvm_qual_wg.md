# LLVM Qualification Working Group - November 2026

- Sync-up meeting #17
- Focus: _Next steps for libc++ conformance test traceability_

## Recent contributions (Merged)

In `llvm-wgs`:

- \[fusa-qual-wg\] Add TPL-007 / tool list template - [#78](https://github.com/llvm/llvm-wgs/pull/78)
- \[fusa-qual-wg\] Replace libraries README placeholder with test traceabeability PoCs - [#105](https://github.com/llvm/llvm-wgs/pull/105)

In `llvm-project`:

- None

### Artifacts awaiting review (Open)

In `llvm-wgs`:

- First version of our Safety Model ( based on the table version discussed during our monthly meetings) - [#103](https://github.com/llvm/llvm-wgs/pull/103)
- \[fusa-qual-wg\] Add README for software tool confidence guidance - [#116](https://github.com/llvm/llvm-wgs/pull/116)
- \[fusa-qual-wg\] Carrying feedback from Xen Fusa WG into LLVM - [#124](https://github.com/llvm/llvm-wgs/pull/124)

In `llvm-project`:

- None

Link to our docs: [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)

## US LLVM workshop and talk

- From the Runtime Libraries workshop – [Notes](https://discourse.llvm.org/t/llvm-dev-meeting-2026-runtimes-workshop/92707)
  - Positive feedback from libc++ lead maintainer
  - Requests:
    - Reply to [comments on the RFC](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468) ⇒ _Ongoing_
    - Create PR to extend review of the PoC to libc++ maintainers ⇒ _To be done_
  - From the talk
    - Lack of reviews is a recurring issue in the community – How could our WG help?
    - What insights can be brought back from LLVM project’s assessment to the community?
      - First step: [Discourse post](https://discourse.llvm.org/t/revisiting-llvms-development-practices/92763)
  - Side note
    - Experience in WG process definition from our WG can help Flang (i.e. decision making process, having 2 sync-up calls, etc) ⇒ Shared [our page](https://llvm.org/docs/QualGroup.html) with Alexis Perry-Holby and Tarun Prabhu

## Focus: Conformance test traceability for libc++

Two main questions from the [RFC](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468) (see also [PR #105](https://github.com/llvm/llvm-wgs/pull/105)):

- **How will behavior files account for different C++ versions and defect reports?**
- **Who will write, review, and maintain them?**

Ideas from Petter for a next step:

- Agree on most important metadata fields in the behavior files, their meaning, then define a schema and add a schema validator
- That could also help agents to draft behavior files with a clear structure and validation feedback, though the descriptions and mappings to certain claims would still need human review
- No particular attachment to yaml format for the files; it might be useful to consider another format if it would simplify parsing and validation of the behavioral files while staying human readable as well

**Can we pick one behavior and its mapped test, identify the minimum metadata it needs, and find someone to sketch the example for Petter to review?**
