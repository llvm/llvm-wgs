# Notes - May 2026

## Participants Americas-friendly sync-up - Friday 2026/05/15, 9:00 AM JST, 1h

[@kumarak](https://discourse.llvm.org/u/kumarak)
[@uwendi](https://discourse.llvm.org/u/uwendi)

## Participants EU/Asia-friendly sync-up - Tuesday 2026/05/12, 5:30 PM JST, 1h

[@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
[@Lorenzo](https://discourse.llvm.org/u/lorenzo)
[@slotosch](https://discourse.llvm.org/u/slotosch)
[@petbernt](https://discourse.llvm.org/u/petbernt)
[@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
[@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)
[@uwendi](https://discourse.llvm.org/u/uwendi)

## Links

- Initial PR to create the Qualification WG directory in `llvm-wgs`:
  [[QualWG] Add initial working group directory by uwendi · Pull Request #3 · llvm/llvm-wgs · GitHub](https://github.com/llvm/llvm-wgs/pull/3)
- Directory structure draft / working document:
  [Safety Model [WIP] - Google Sheets](https://docs.google.com/spreadsheets/d/1ShQjRBoAVWmIxdLpLZQWPAiwgOsxZTwg5gkBqidiau0/edit?gid=0#gid=0)
- Supporting presentation / discussion material:
  [202605\_llvm\_qual\_wg - Google Slides](https://docs.google.com/presentation/d/1AAQsUqNDev_Rm2qgoVQtjDx_SJNo1OF-5OowvnD2KHs/edit?slide=id.p1#slide=id.p1)
- Constant-time coding support RFC:
  [[RFC] Constant-Time Coding Support](https://discourse.llvm.org/t/rfc-constant-time-coding-support/87781)
- PR introducing the `llvm.ct.select` intrinsic:
  <https://github.com/llvm/llvm-project/pull/166702>

## Non-technical topics

### New membership request

The group received a self-nomination from [@Lorenzo](https://discourse.llvm.org/u/lorenzo) for active membership.

[@Lorenzo](https://discourse.llvm.org/u/lorenzo) has been working as a safety assessor for the past five years. He is mainly interested in understanding how the group is approaching the challenge of reconciling the open-source nature of LLVM with the requirements of functional safety standards such as ISO 26262 and CENELEC standards.

He is currently particularly interested in the qualification of operating systems such as Xen and Zephyr. During the discussion, the following ideas were proposed:

- Look at what is being done in the ELISA project to address similar challenges, for example:
  [ELISA Seminar – Functional safety with Xen, Zephyr and Linux for avionics, automotive and industrial – ELISA](https://elisa.tech/event/elisa-seminar-functional-safety-with-xen-zephyr-and-linux-for-avionics-automotive-and-industrial/)
- Consider inviting Gabriele from ELISA to present work related to requirements engineering in the Linux context.
- Alternatively, review existing ELISA recordings on related topics, for example:
  <https://www.youtube.com/watch?v=MA_f68E0_qE>
  <https://www.youtube.com/watch?v=f5v6q3OFv88>
  <https://www.youtube.com/watch?v=hh_Unzvkf6g>
  <https://www.youtube.com/watch?v=eXtOowhlu7I>

For the moment, [@Lorenzo](https://discourse.llvm.org/u/lorenzo) will participate as an observer.

### Qualification WG directory in `llvm-wgs`

A PR was created to add the initial top-level directory for our WG in the new `llvm-wgs` repository:

[[QualWG] Add initial working group directory (#3)](https://github.com/llvm/llvm-wgs/pull/3)

## Technical topics

### General status

May has been a relatively slow month for the WG for several reasons.

However, some topics are still progressing, even if at a slow pace. For example, [@uwendi](https://discourse.llvm.org/u/uwendi) and [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) have continued some work on the safety model topic.

The group also noted that having the GitHub directory available in `llvm-wgs` should help progress work more efficiently. It would allow the group to make artifacts available in an LLVM project GitHub repository and to formalize reviews through pull requests.

### Constant-time coding support

During the Americas-friendly sync-up, [@kumarak](https://discourse.llvm.org/u/kumarak) raised a request for guidance from the WG regarding the following LLVM PR:

[[ConstantTime][LLVM] Add llvm.ct.select intrinsic with generic SelectionDAG lowering (#166702)](https://github.com/llvm/llvm-project/pull/166702)

This PR introduces the `llvm.ct.select` intrinsic as part of the constant-time coding support RFC:

[[RFC] Constant-Time Coding Support](https://discourse.llvm.org/t/rfc-constant-time-coding-support/87781) [LLVM Project](https://discourse.llvm.org/c/llvm/5)

[@kumarak](https://discourse.llvm.org/u/kumarak) is looking for guidance on how to move this work forward.

[@uwendi](https://discourse.llvm.org/u/uwendi) suggested that Akshay send a message through the Qualification WG Discord channel to ask whether any WG members can provide guidance or feedback.

## Potential topic for the US LLVM Developers’ Meeting

The group briefly discussed whether some of the ongoing work could be presented at the US LLVM Developers’ Meeting.

Several activities are currently in progress within the group, and one or more of them could potentially become the basis for a presentation. There is still time to decide, as the proposal deadline is expected to be in July.

## Actions

- **All:** Participate in updating the backlog and continue ongoing actions, to the extent of each member’s availability.
- [@uwendi](https://discourse.llvm.org/u/uwendi): Continue monitoring the status of the PR to create the Qualification WG directory in `llvm-wgs`, and consider pinging [@petrhosek](https://discourse.llvm.org/u/petrhosek) for merging if needed.
- [@uwendi](https://discourse.llvm.org/u/uwendi): Schedule a meeting with [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) to discuss the update of the software tool qualification workflows.
- [@uwendi](https://discourse.llvm.org/u/uwendi): Try again to set up a dedicated call with the author of the threat model, to share feedback and ask questions needed to progress on the safety model topic.
