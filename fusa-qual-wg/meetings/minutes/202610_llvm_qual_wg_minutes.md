# Notes - October 2026

The Americas-friendly sync-up scheduled for Friday 2026/10/09 at 9:00 AM JST was cancelled due to an unforeseen constraint.

An additional meeting was held on Friday 2026/10/09 at 9:00 PM JST with WG members to resolve all remaining review comments on the slides for the US LLVM talk.

> Use of AI assistance for auto-transcription was done as explained in the [LLVM Qualification Group's AI Transcription Policy](https://llvm.org/docs/QualGroup.html#ai-transcription-policy).

## Participants EU/Asia-friendly sync-up - Tuesday 2026/10/13, 5:30 PM JST, 1h

[@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
[@petbernt](https://discourse.llvm.org/u/petbernt)
[@uwendi](https://discourse.llvm.org/u/uwendi)
Victor Lu
[@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
[@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)

## Links

https://docs.google.com/presentation/d/1Kdv8fND4bXNH_Flgw8FbA8htOFG-FJyZTfmHscmIBBA/edit

- [WG documentation and workstreams](https://github.com/llvm/llvm-wgs/blob/main/fusa-qual-wg/README.md)
- [GitHub issue tracker](https://github.com/llvm/llvm-wgs/issues)
- [RFC: Forbid AI-generated communication](https://discourse.llvm.org/t/rfc-forbid-ai-generated-communication/92414)

## Discussion

### Proposed changes to the LLVM AI Tool Use Policy

Invited members to read the RFC on AI-generated communication and consider its implications for WG documents, PRs and meeting minutes. Questions included whether the WG's transcription policy should be revised and whether a transparency note about AI assistance would be appropriate, particularly for minutes prepared using Gemini transcripts. No change to the WG's practices was agreed during this meeting.

### Recent progress and workstreams

- Reviewed recent merges and the expanded main README in `llvm-wgs/fusa-qual-wg` were discussed.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) raised the need for clearer goals and priorities for future work.
- [@uwendi](https://discourse.llvm.org/u/uwendi) recalled that backlog items had been converted into GitHub issues and encouraged contributors to volunteer for topics that interest them. Where self-assignment is unavailable, contributors can comment on an issue so that an authorized member can assign it to them.
- [@uwendi](https://discourse.llvm.org/u/uwendi) emphasized the voluntary nature of participation and the need to set expectations according to contributors' available capacity. Different workstreams may progress at different rates. No common delivery schedule or set of commitments for the coming year was agreed.
- [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee) demonstrated GitHub Projects as a possible way to organize issues and visualize work. [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) suggested using it to track experiments and draft work before deciding which results should be added to the WG's documentation.

### US LLVM conference preparation

- The WG's work is still exploratory, with a small number of contributors.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) proposed considering how to assess the impact of the talk and workshop, including interest in the WG's work, feedback, use of its artifacts and eventual adoption.
- [@uwendi](https://discourse.llvm.org/u/uwendi) emphasized using the shared Discord and Discourse channels for engagement, so that questions and feedback remain accessible to the group. The closing slide already includes links to these channels. The WG would welcome concrete problems and use cases from the community.
- Participants explored GitHub traffic statistics as a possible indication of interest. A snapshot before the conference and a comparison afterwards were suggested.
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) also suggested a dedicated GitHub issue for interaction after the presentation.
- [@uwendi](https://discourse.llvm.org/u/uwendi) asked members to suggest questions that might arise during the talk and workshop. Topics identified included:
  - When a worked example applying the templates to an LLVM tool, such as `llvm-cov`, will be available.
  - Who would create and maintain runtime-library traceability evidence: WG contributors, library maintainers or others.
  - How the traceability approach would handle different C and C++ standards and differences in specified behavior.
  - Which tools, LLVM releases, architectures and configurations an initial qualification effort would cover.
  - How qualification evidence would be maintained across LLVM releases.
  - What support the WG can provide and what remains the responsibility of downstream users.
- [@petbernt](https://discourse.llvm.org/u/petbernt) suggested that initial traceability work would likely need to come from the WG to demonstrate its value. He also described using metadata for the applicable language standard and distinct identifiers where behaviors differ.
- Maintaining evidence across releases is already captured in the GitHub issue titled “Define how qualification evidence is maintained across LLVM versions”. Its implementation and schedule remain open.

## Actions

- WG members :
  - Read the AI communication RFC and share views on its implications for WG documentation, transcription and minutes.
  - Before the conference, suggest likely audience questions for the US LLVM talk and workshop.
- [@uwendi](https://discourse.llvm.org/u/uwendi) and [@petbernt](https://discourse.llvm.org/u/petbernt) : Share feedback and outcomes from the conference with other WG members at the next sync-up.
- To be confirmed :
  - Explore the GitHub Project setup, including its name and access permissions.
  - Capture a GitHub traffic baseline and compare it with traffic after the conference.
