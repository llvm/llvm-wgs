# LLVM Qualification Working Group - September 2026

- Sync-up meeting #15
- Focus: _Progress, blockers, and new topics_

## Non-technical topics

### Communication channels

| Channel | Intended use |
|---|---|
| Google Meet / Sync-up meetings | Technical discussion<br>Decisions<br>Unblocking |
| Discord | Coordination<br>Quick questions<br>Preliminary discussion |
| Discourse | Public announcements<br>Broader discussions<br>Meeting records |
| GitHub PRs | WG artifacts, including the meeting archive<br>Tracked reviews<br>Merge readiness |
| _(to be considered)_ GitHub Issues | Backlog<br>Visualization of proposed actions |

### Process-related questions

Shared on Discord:

- Should we [track WG actions in GitHub Issues](https://discord.com/channels/636084430946959380/1389362444169773117/1544556070972825610)?
- What review is [sufficient to merge a WG artifact](https://discord.com/channels/636084430946959380/1389362444169773117/1544586549365047367)?
- How can we ensure sufficient reviewing capacity?
- Do we agree with the proposed roles of the different channels?
- Should GitHub be the authoritative place for artifact reviews and their outcomes?

Thoughts, concerns, suggestions?

### Should we track WG actions in GitHub Issues?

Shared on Discord:

- Current topics and actions are split between the [backlog](https://llvm.org/docs/QualGroup.html#current-topics-backlog) and [meeting minutes](https://github.com/llvm/llvm-wgs/tree/main/fusa-qual-wg/meetings/minutes)
- Ownership and status are therefore not visible in one operational view
- Proposal: conduct a 2-3-month pilot using **GitHub Issues** to track actionable WG work
  - Leave issues **unassigned** for volunteers, or assign them when someone **explicitly** accepts an action
  - Link issues from the minutes - close them through the resulting PR(s)
  - Retain the backlog for high-level topics, if useful

[Issues in `llvm/llvm-wgs`](https://github.com/llvm/llvm-wgs/issues)

### What review is sufficient to merge a WG artifact?

WG artifacts follow the standard GitHub review process, but specific review thresholds are not defined

Possible distinction:

- Meeting records: merge without formal review — archival material
- Routine/editorial changes: one reviewer — must they be a WG member?
- New/substantial artifacts: one substantive review from a WG member to merge as Draft?
- From Draft to WG-reviewed: two substantive reviews? WG consensus?
- WG position/process changes: consensus first; formal vote only if needed; review PR by one reviewer?
- Should merge criteria depend on the type of change and artifact “maturity”?


[Current decision-making process](https://llvm.org/docs/QualGroup.html#decision-making) (incl. definition of consensus)

### Summary of last month’s PRs

Merged:

In `llvm-wgs`:

- \[fusa-qual-wg\] Add TPL-001 / need of tool confidence template: [#46](https://github.com/llvm/llvm-wgs/pull/46)

In `llvm-project`:

- None

Open:

In `llvm-wgs`:

- \[fusa-qual-wg\] Add Workflow Views and Graph Generator: [#38](https://github.com/llvm/llvm-wgs/pull/38)
- \[fusa-qual-wg\] Add TPL-006 / safety considerations template: [#47](https://github.com/llvm/llvm-wgs/pull/47)
- \[fusa-qual-wg\] Add TPL-002 / tool usage plan template: [#48](https://github.com/llvm/llvm-wgs/pull/48)
- \[fusa-qual-wg\] Add TPL-003 / tool classification report template: [#57](https://github.com/llvm/llvm-wgs/pull/57)
- \[fusa-qual-wg\] Add TPL-004 / tool qualification report template: [#73](https://github.com/llvm/llvm-wgs/pull/73)
- \[fusa-qual-wg\] Add TPL-005 / safety manual template: [#75](https://github.com/llvm/llvm-wgs/pull/75)

In `llvm-project`:

- None

Link to our docs: [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)

## Technical topics: Progress, blockers, and new topics

### On Alive2 and TV tools for LLVM-based-compiler qualification

Proposal to prepare a **positioning article/technical perspective** on the relevance of Alive2 and translation-validation tools for LLVM compiler qualification:

- It would become the WG’s position **only after review and agreement**
- Proposed questions to prepare this document: [link](https://docs.google.com/document/d/1062NWJwmS9SQcJjhEGalznQZRPVZb1f2_FmlvOecihE/edit?tab=t.0#heading=h.g6n79zvmhd04)

YoungJun would write the starting point/first draft. Other volunteers could contribute to this work later on.

### What else shall we discuss?

## Open Discussion

Let's discuss any doubts or concerns.  
If something comes up later, contact the Working Group on [Discourse](https://discourse.llvm.org/t/rfc-proposal-to-establish-a-safety-group-in-llvm/86916) or [Discord](https://discord.com/channels/636084430946959380/1389362444169773117).
