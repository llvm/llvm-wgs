# Notes - November 2025

## Participants

### Tuesday 2025/11/05, 13:00 UTC, 1h

- [@evodius96](https://discourse.llvm.org/u/evodius96)
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
- [@capitan-davide](https://discourse.llvm.org/u/capitan-davide)
- [@petarj](https://discourse.llvm.org/u/petarj)
- [@petbernt](https://discourse.llvm.org/u/petbernt)
- [@uwendi](https://discourse.llvm.org/u/uwendi)
- [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)

## Agenda

Refer to [LLVM Qualification WG sync-ups meeting minutes - #14 by uwendi](https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148/14)

## Links

[docs.google.com](https://docs.google.com/presentation/d/1syRmtUd3ARJxYAsYc7z7KCYjL6WdQDGWG80fojig82Q/edit?usp=sharing)

### [202511\_llvm\_qual\_wg](https://docs.google.com/presentation/d/1syRmtUd3ARJxYAsYc7z7KCYjL6WdQDGWG80fojig82Q/edit?usp=sharing)

LLVM Qualification WG Sync-up meeting #5 November 2025 Focus: Progress round-up

- [[RFC] Collecting Community Input on Qualification of LLVM Tools & Libraries](https://discourse.llvm.org/t/rfc-collecting-community-input-on-qualification-of-llvm-tools-libraries/88569)
- [RFC: Require Pull Requests for all llvm-project commits](https://discourse.llvm.org/t/rfc-require-pull-requests-for-all-llvm-project-commits/88164)
- [Lighthouse SIG - OSS Practices](https://docs.google.com/spreadsheets/d/1jR0oGQpwJTdThJAOtWP70GrdWSz7K-ol84j5BWX2h8g/edit?gid=1722310808#gid=1722310808)

## Highlights

Gemini notes taken, modified by [@uwendi](https://discourse.llvm.org/u/uwendi)

### Non-technical topics

**Pull Requests and Meeting Materials**

- The latest Pull Request (PR), prepared by [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee) was merged and there are no currently pending PRs.
- There is a concern regarding meeting materials being stored only in a personal Google Drive. We stopped storing them on GitHub due to feedback from 2 people in the community. We’ll consider contacting the infrastructure team to determine a suitable storage location, possibly archiving quarterly PDFs on GitHub while continuing to share links from the Google Drive for collaboration.

**Takeaways from the US LLVM Conference**

- [@evodius96](https://discourse.llvm.org/u/evodius96) attended the presentation from Peter Smith from ARM which was interesting and showing a practical example relevant to compiler qualification.
- [@uwendi](https://discourse.llvm.org/u/uwendi) attended [@slotosch](https://discourse.llvm.org/u/slotosch)’s round table. Other attendees asked questions about the group’s work. Feedback from Peter Smith is that he would like to see a keynote from the group next year outlining our vision. Directed the attendees to [@petbernt](https://discourse.llvm.org/u/petbernt)’s request for comments.
- Does Solid Sands only provide a test suite for toolchain quality, as suggested by a [previous conference talk](https://www.youtube.com/watch?v=Rgb1CH9D86M)? Looks like they currently offer a broader selection, including libraries qualification. Some concerns exist because it seems that they do not participate in the ISO C and C++ committees, potentially impacting their ability to keep up with language changes and interpretations.
- Discussed the challenge of judging the quality of conformity test kits without insight into the build and testing processes. Suggestion: false positives might be an indicator of quality.
- Conference presentation and group visibility: there might be motivation for the group to do more for next year’s conference, possibly a keynote, round table, or talk, to create more awareness. It was too early to present at the recent conference. April’s LLVM Europe conference might be a target, or potentially a conference in Asia if one is organized.
- Operational Maturity and Code Reviews: [@uwendi](https://discourse.llvm.org/u/uwendi) attended the operational maturity round table, discussing code reviews as a way to prevent errors. There is an RFC from Infra about enforcing pull requests. Noted that 30% of commits from 5% of contributors are reviewed post-merge, and issues include a lack of reviewers and long post-commit review times.

### Technical topics / Round-robin updates

**Status of the Qualification RFC and Library Proposal**

- Concern from [@petbernt](https://discourse.llvm.org/u/petbernt) that non-context-aware readers might misunderstand the RFC.
- [@petbernt](https://discourse.llvm.org/u/petbernt) agreed to post it in other Discord channels to increase visibility.
- [@petbernt](https://discourse.llvm.org/u/petbernt) also has a small proposal for library qualification that is not yet finished but could be shared later in the week.

**Tutorial Preparation**

- [@uwendi](https://discourse.llvm.org/u/uwendi) provided materials to [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee) that could be helpful to prepare the tutorial / set of initial documents for newcomers.
- Open to further assistance with the interpretation of the functional safety standards
- [@uwendi](https://discourse.llvm.org/u/uwendi) can contact old colleagues from the railways industry for materials related to their standards.
- [@uwendi](https://discourse.llvm.org/u/uwendi) shared personal efforts regarding the ISO 26262 standard, noting a successful submission and acceptance of around 30 simple comments and plans for two or three significant (possibly controversial) upcoming comments regarding the description of methods 1b and 1c (evaluation of the development process and validation of the software tool).
- [@uwendi](https://discourse.llvm.org/u/uwendi) expressed concerns about the wording and requirements for method 1b, suggesting that evaluation of the tool development process should be highly recommended for all ASILs.

**Software Tool Experiments and Automation**

- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) shared results from his quality-focused experiments on the development process, which were conducted on LLVM and Alive2, confirming at least 12 defects in Alive2 that still need to be reported.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) noted that adoption of this strategy will face resistance unless the process is fully automated to prevent extra effort for developers. He will work on automation, possibly involving git hooks, and prepare templates and documentation for the group, emphasizing that this work relates to “evaluation of the development process” (Method 1b in ISO 26262).
- [@uwendi](https://discourse.llvm.org/u/uwendi) requested a demo; agreed to schedule offline.

**LLVM Developer Policy Suitability Analysis**

- [@uwendi](https://discourse.llvm.org/u/uwendi) presented a draft analysis of the LLVM developer policy’s suitability based on the open-source software practices checklist from the Elisa project’s Lighthouse OSS SIG. She gave an initial, rough evaluation based on gut feeling due to the immaturity of the maturity scale, but stated that the written process generally “looks good”.
- Areas rated as having “limited maturity” included one item in security/supply chain (SBOMs) and the lack of a formal bus factor metric program.
- While the written process looks good, measuring its execution and follow-through requires automation, leading to being stuck due to the undecided maturity scale.
- The checklist for LLVM’s suitability would support Method 1B, evaluation of the development process, and argued that a best practices list is more suitable than requiring assessment against a national or international standard, especially for open source.
- [@uwendi](https://discourse.llvm.org/u/uwendi) proposed a new action for herself to start writing templates for the workflow steps outlined in the previous sync-up. These templates would be useful for both downstream and upstream. For tool qualification, the idea is to include worksheets for each method.

## Actions / Next steps

- [@petbernt](https://discourse.llvm.org/u/petbernt) will post some slides with a small proposal for library qualification, and post the RFC in other channels in Discord, to make it more visible.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) will report the confirmed bugs found in Alive2.
- [@uwendi](https://discourse.llvm.org/u/uwendi) will contact the infrastructure team to discuss where meeting materials could be stored, possibly archiving quarterly PDFs in GitHub while continuing to share links to her Google Drive.
- [@petbernt](https://discourse.llvm.org/u/petbernt) will ask Peter Smith from ARM to add a comment to the RFC about input request from the community.
- [@uwendi](https://discourse.llvm.org/u/uwendi) will contact an old colleague from the railways industry to ask if they have materials and can help with the new version of the railway standard for tool qualification.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) will work on automation using git hooks or similar mechanisms for the development process quality strategy and prepare templates and documentation for the human-centered approach to finding defects to share with the group.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) will give a demo of the defect finding experiments at a dedicated slot or the next sync-up.
- [@uwendi](https://discourse.llvm.org/u/uwendi) will start writing templates for the gray boxes in the workflow from the last sync-up and share them with the group for review and improvements.
- [@petbernt](https://discourse.llvm.org/u/petbernt) will send some presentations about Solid Sands and how their super test and super framework works.
