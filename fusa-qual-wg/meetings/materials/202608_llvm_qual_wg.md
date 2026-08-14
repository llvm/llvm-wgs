# LLVM Qualification Working Group - August 2026

- Sync-up meeting #14
- Focus: _Recent momentum → Collective choices_

## Non-technical topics

### Summary of last month's PRs

Merged:

In `llvm-wgs`:

- \[fusa-qual-wg\] Draft onboarding/tutorial guide in README: [#37](https://github.com/llvm/llvm-wgs/pull/37)
- \[fusa-qual-wg\] Add July 2026 materials, agenda, and minutes: [#53](https://github.com/llvm/llvm-wgs/pull/53)

In `llvm-project`:

- \[Docs\] Document Qualification WG artifacts and meeting archive: [#209382](https://github.com/llvm/llvm-project/pull/209382)

Open:

In `llvm-wgs`:

- \[fusa-qual-wg\] Add Workflow Views and Graph Generator: [#38](https://github.com/llvm/llvm-wgs/pull/38)
- \[fusa-qual-wg\] Add TPL-001 / need of tool confidence template: [#46](https://github.com/llvm/llvm-wgs/pull/46)
- \[fusa-qual-wg\] Add TPL-006 / safety considerations template: [#47](https://github.com/llvm/llvm-wgs/pull/47)
- \[fusa-qual-wg\] Add TPL-002 / tool usage plan template: [#48](https://github.com/llvm/llvm-wgs/pull/48)
- \[fusa-qual-wg\] Add TPL-003 / tool classification report template: [#57](https://github.com/llvm/llvm-wgs/pull/57)

Link to our docs: [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)

### US LLVM and Runtimes workshop

The proposal for the [US LLVM Dev Meeting](https://discourse.llvm.org/t/announcing-the-2026-llvm-developers-meeting-program/91470) was accepted as a technical talk (20min).

- LLVM in Safety-Critical Industries: Toward a Shared Qualification Layer Upstream
- Speaker(s): Petter Berntsson, Wendi Urribarri
- Authors: W. Urribarri, P. Berntsson, C. Ramirez, Z. Hermawan,Y. Lee, O. Slotosch

Also, a discussion session at the Runtime Libraries workshop is planned, to discuss the Conformance Test Traceability for libc++ [RFC and its related PoC](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468) with runtime libraries maintainers

## Technical topics: Current blockers and future directions

### To be completed — or at least clearly framed — before October

The work done in this WG is evolving around several opportunities for “easier” enablement — from upstream — of the usage of LLVM components in safety-critical industries:

- Functional Safety Model
- Behavior-to-tests traceability for runtime libraries
- Tool-confidence workflows / guidelines / templates
- Defects prediction techniques
- Description of role of Alive2 and translation validation tools
- Assessment of the state-of-the-art of OSS best practices in the LLVM development policy
- (...and other ideas already mentioned in the monthly meetings, but not yet fully developed/explored…)

We have a “base” and we are working towards publishing in `llvm-wgs`.

The planned [US LLVM talk](https://discourse.llvm.org/t/announcing-the-2026-llvm-developers-meeting-program/91470) and Runtimes workshop discussion can create opportunities for feedback, interest, adoption, new ideas, new contributors, etc…

### Blockers / Problems to solve

1. Do we need another tool to generate Mermaid graph?
   - [GitHub natively renders Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) files, but you need to render it under *.mmd or *.md file
   - Having additional script means code to maintain. We might want to write some tests for it.
   - Examples on Zaky’s repo:
     - For .mmd file: [link](https://github.com/ZakyHermawan/llvm-wgs/blob/main/fusa-qual-wg/tools/workflows/tool_usage_confidence_for_developers.mmd)
     - For .md file: [link](https://github.com/ZakyHermawan/llvm-wgs/blob/test-mermaid/fusa-qual-wg/tools/workflows/test.md)
2. Do we lack reviewers for the open PRs?
3. Other blockers?

### What should we complete, validate, and explore next?

_*Question*_: _What future free/non-commercial open source directions, initiatives, outcomes would be most valuable for the LLVM upstream project, that we could contribute from this WG?_

_*Examples*_:

| Complete | Validate | Explore |
|---|---|---|
| Unblock current and planned contributions | Apply artifacts to concrete LLVM use cases | Binary and ABI constraint assurance |
| Continue discussions on [Petter’s RFC](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468) | Exercise traceability with libc/libc++ | Links between safety and security evidence |
|  | Gather feedback from potential adopters (for example, Xen) | AI-based software tools |

## Open Discussion

Let's discuss any doubts or concerns.  
If something comes up later, contact the Working Group on [Discourse](https://discourse.llvm.org/t/rfc-proposal-to-establish-a-safety-group-in-llvm/86916) or [Discord](https://discord.com/channels/636084430946959380/1389362444169773117).
