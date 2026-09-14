# Notes - September 2026

## Participants EU/Asia-friendly sync-up - Tuesday 2026/09/08, 5:30 PM JST, 1h

- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
- [@petbernt](https://discourse.llvm.org/u/petbernt)
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)

## Participants Americas-friendly sync-up - Friday 2026/09/11, 9:00 AM JST, 1h

- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
- [@michaelrj-google](https://discourse.llvm.org/u/michaelrj-google)

## Links

- [September meeting materials](https://docs.google.com/presentation/d/1JiWbpLf9drgqComGOmczhSivjn2JhOZCy_unCJlV0zc/edit?usp=sharing_eil_se_dm&ts=6a95523a)
- [Open WG pull requests](https://github.com/llvm/llvm-wgs/pulls)
- [Proposed questions](https://docs.google.com/document/d/1062NWJwmS9SQcJjhEGalznQZRPVZb1f2_FmlvOecihE/edit?tab=t.0#heading=h.g6n79zvmhd04) to prepare **positioning article/technical perspective** on the relevance of Alive2 and translation-validation tools for LLVM compiler qualification.
- [LLVM libc code-coverage documentation](https://libc.llvm.org/dev/code_coverage.html)

## Discussion

### Communication Channels

- The groups are agree to use sync-up meetings to do technical discussion, making decisions, and unblocking issues that are prevent WG from moving forward.
- Discord will be used for doing coordination, quick questions, or some preliminary discussion for example, before sync-ups.
- In general, discourse will be used for public announcements, discussions to the broader communities, and can also be used to send links to the meeting records (if any), however, discourse can also be used to visualize and propose actions, depends on the use case, because is better for some use cases, for example, in discourse, you can easily reply to each other, and see the reply-tree, so you know who is replying to what, so discourse would be favored if it feels we need to do a lot of discussions.
- GitHub will be the authoritative place for artifact reviews and their outcomes.
- Github PRs will be used to store artifacts and documents because it is easier to track reviews there.
- Github issues will be used to store or discussion backlogs and also proposing actions that is need to be tracked or if it quite simple and don’t need a lot of discussion.

### Working Group process related discussions

The WG members agree that, we need at least 1 reviewer for trivial Pull Requests, such as storing meeting slides. However, for non-trivial PRs, we need at least 2 reviewer from WG members, each WG members can use either github approval to approve a PR, or just write something obvious in the PR comment that shows the approval of a PR, such as “LGTM”, or “Looks Good to Me.” Both method are equal.

To ensure sufficient reviewing capacity, there are 3 proposed ideas:

1. [@petbernt](https://discourse.llvm.org/u/petbernt) p    Proposed for rotation, let’s say a week or so.
    assign people to each category so that the people with related category to the PR will need to help review it, but for this, we need to do further discussion to determine which category we have and who will be assigned to that category.
    The one who create the PR will tag the people that might have related knowledge to help the review, however it is encouraged to everyone to review any pull request, so we can merge it faster.

The conclusions of this is that, we can choose any method (can be one of the 3 proposed methods, or we could use other methods) and see which one works.

### Summary of last month’s PRs

**Merged PR:**

- \[fusa-qual-wg\] Add TPL-001 / need of tool confidence template: [#46](https://github.com/llvm/llvm-wgs/pull/46)

**Open PRs:**

- \[fusa-qual-wg\] Add Workflow Views and Graph Generator: [#38](https://github.com/llvm/llvm-wgs/pull/38)
- \[fusa-qual-wg\] Add TPL-006 / safety considerations template: [#47](https://github.com/llvm/llvm-wgs/pull/47)
- \[fusa-qual-wg\] Add TPL-002 / tool usage plan template: [#48](https://github.com/llvm/llvm-wgs/pull/48)
- \[fusa-qual-wg\] Add TPL-003 / tool classification report template: [#57](https://github.com/llvm/llvm-wgs/pull/57)
- \[fusa-qual-wg\] Add TPL-004 / tool qualification report template: [#73](https://github.com/llvm/llvm-wgs/pull/73)
- \[fusa-qual-wg\] Add TPL-005 / safety manual template: [#75](https://github.com/llvm/llvm-wgs/pull/75)

[@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) will address feedbacks on [#38](https://github.com/llvm/llvm-wgs/pull/38) so it can be merged as soon as possible, since this PR already have enough reviewers, and [#47](https://github.com/llvm/llvm-wgs/pull/47) have enough review already, so it can be merged once no more changes that is need to be addressed.

The other open PRs are still not being merged due to lack of reviewers.

- [#48](https://github.com/llvm/llvm-wgs/pull/48) need at least 1 more reviewer
- [#57](https://github.com/llvm/llvm-wgs/pull/57) need at least 1 more reviewer
- [#73](https://github.com/llvm/llvm-wgs/pull/73) need at least 2 reviewers
- [#75](https://github.com/llvm/llvm-wgs/pull/75) need at least 2 reviewers

[@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) raises concern about our bottleneck on the approve access on the Pull Request, and he also mention that we need to get the open PRs to be merged as soon as possible, because it is already September and the conference will be held on October.

### On Alive2 and TV tools for LLVM-based-compiler qualification

The group currently prepare a **positioning article/technical perspective** on the relevance of Alive2 and translation-validation tools for LLVM compiler qualification. It would become the WG’s position **only after review and agreement**. Proposed questions to prepare this document: [link](https://docs.google.com/document/d/1062NWJwmS9SQcJjhEGalznQZRPVZb1f2_FmlvOecihE/edit?tab=t.0#heading=h.g6n79zvmhd04). Members are encouraged to reviews the proposed questions on the document, and give comments (if any). Other volunteers could contribute to this work later after the first draft is done.

### LLVM-libc code coverage

During the Americas-friendly sync-up, [@michaelrj-google](https://discourse.llvm.org/u/michaelrj-google) shared an update about recent progress on LLVM libc’s code-coverage infrastructure:

- An intern has enabled the generation of structural code-coverage reports for LLVM libc. The project previously did not have an established coverage-reporting or coverage-analysis capability.
- The initial support is now working and can provide visibility into which parts of the implementation are or are not exercised by the existing tests. This could help identify coverage gaps, guide additional testing, and potentially uncover defects.
- Coverage reporting is not enabled or run by default. It currently requires an explicitly configured coverage build, followed by manual steps to execute the tests, collect the profiling data, generate the reports, and analyze the results.
- The [documentation](https://libc.llvm.org/dev/code_coverage.html) covers standard line and branch coverage, as well as optional MC/DC coverage.

## Actions

- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) will address requested changes on [#38](https://github.com/llvm/llvm-wgs/pull/38).
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) [@petbernt](https://discourse.llvm.org/u/petbernt) will help to do more reviews on the PRs.
- **All**: We need to help on reviewing open PRs so it can be merged faster, the conference will be in less than 2 months.
- **All**: It will be helpful if others also review the questions on the documents about WG positioning article on Alive2 and TV tools for LLVM-based-compiler qualification on the link above.
