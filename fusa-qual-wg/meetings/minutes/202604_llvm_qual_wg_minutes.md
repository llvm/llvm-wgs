# Notes - April 2026

## Participants Americas-friendly sync-up - Friday, 2026/04/10, 9:00 AM JST, 1h

[@ppenzin](https://discourse.llvm.org/u/ppenzin)
[@uwendi](https://discourse.llvm.org/u/uwendi)

## Participants EU/Asia-friendly sync-up - Tuesday, 2026/04/14, 5:30 PM JST, 1h

[@slotosch](https://discourse.llvm.org/u/slotosch)
[@uwendi](https://discourse.llvm.org/u/uwendi)
[@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
[@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)

## Links

[Backlog - LLVM Qualification Working Group](https://docs.google.com/document/d/10YZZ72ba09Ck_OiJaP9C4-7DeUiveaIKTE3IkaSKjzA/edit)

[Safety Model [WIP]](https://docs.google.com/spreadsheets/d/1ShQjRBoAVWmIxdLpLZQWPAiwgOsxZTwg5gkBqidiau0/edit)

## Non-technical topics

- Following discussion about [where to store the group’s artifacts](https://discourse.llvm.org/t/where-should-wg-meeting-materials-live/88913), we requested the creation of a dedicated repository for the WG. The [issue](https://github.com/llvm/llvm-project/issues/186063) is still open. A similar situation exists for the [Clang Area Team](https://github.com/llvm/llvm-project/issues/186108) and the [OpenMP WG](https://github.com/llvm/llvm-project/issues/185932).
- We updated the WG’s [sync-up schedule and calendar links](https://llvm.org/docs/GettingInvolved.html#online-sync-ups) to reflect the reintroduction of the two-meeting setup along with new shared Google Calendar links.
- We also updated the [WG page](https://llvm.org/docs/QualGroup.html) to reflect the outcome of the first biannual membership review and to clarify active contributor status.

## Technical topics

- Our [backlog](https://docs.google.com/document/d/10YZZ72ba09Ck_OiJaP9C4-7DeUiveaIKTE3IkaSKjzA) needs to be updated to reflect the current status of the various topics the WG is working on. We completed a partial update during the sync-up.
- Last month was relatively slow for the WG. However, two progress items can be highlighted:
  - [@petbernt](https://discourse.llvm.org/u/petbernt) and [@uwendi](https://discourse.llvm.org/u/uwendi) discussed the proposal for a methodology to enable qualification of LLVM libraries with libc and libc++ maintainers, Michael Jones and Louis Dionne, respectively. They agreed that the Qual WG will develop:
    - a proof of concept showing how the methodology works using a sufficiently “interesting” real function in libc++, and
    - a proposal for the ISO C++ standard regarding formalization of requirements, possibly using contracts.
      The latter is outside the scope of the Qual WG’s objectives, but it could support the long-term maintenance of qualification artifacts if the methodology is applied upstream.
  - Following [last month’s sync-up](https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148/24) with members of the Security Response WG, we started drafting a [safety model](https://docs.google.com/spreadsheets/d/1ShQjRBoAVWmIxdLpLZQWPAiwgOsxZTwg5gkBqidiau0) roughly equivalent to their [threat model](https://github.com/mrragava/llvm-project/blob/ragava/threat-model-proposal/llvm/docs/ThreatModel.md). At the moment, it resembles a very high-level failure mode analysis per LLVM component. We have not yet agreed on the appropriate granularity for splitting components in the safety model relative to the threat model. [@uwendi](https://discourse.llvm.org/u/uwendi) also tried to reach out to the author of the threat model, but without success so far.
- During the Americas-friendly call, [@ppenzin](https://discourse.llvm.org/u/ppenzin) and [@uwendi](https://discourse.llvm.org/u/uwendi) discussed the importance of MISRA and AUTOSAR checks for the functional safety of automotive in-vehicle software, as well as the interest in upstreaming implementations of such checks. Within LLVM, only the libraries could be part of in-vehicle software. For software tools, MISRA and AUTOSAR do not play a role in qualification. For compilers such as Clang, however, they are useful for checking compliance of the input source code, including libraries, against those standards. See [Petr’s Discourse post](https://discourse.llvm.org/t/changes-for-misra-autosar-coding-standards/90502).

## Actions

- **All:** participate in updating the backlog and continue ongoing actions to the extent of their availability
- **Wendi:** schedule a meeting with [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) about updating the workflows for software tool qualification
- **Wendi:** follow up again with [@infra-area-team](https://discourse.llvm.org/groups/infra-area-team) regarding the new repository
- **Wendi:** try again to reach out and set up a dedicated call with [@mrragava](https://discourse.llvm.org/u/mrragava) to share feedback and ask questions about the threat model in order to progress on the safety model
