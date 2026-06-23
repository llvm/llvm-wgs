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

[github.com/llvm/llvm-wgs](https://github.com/llvm/llvm-wgs/pull/3)

#### [[QualWG] Add initial working group directory (#3)](https://github.com/llvm/llvm-wgs/pull/3)

`main` ← `uwendi:qual-wg-initial-directory`

opened 12:12AM - 11 May 26 UTC

[![](https://us1.discourse-cdn.com/flex021/uploads/llvm/original/3X/7/a/7aa32a6a4017f3997e8fe38b1cd6ebb1b8664a28.jpeg)
uwendi](https://github.com/uwendi)

[+9
-0](https://github.com/llvm/llvm-wgs/pull/3/files)

This PR adds the initial top-level directory for the LLVM Qualification Working […](https://github.com/llvm/llvm-wgs/pull/3)Group.
For now, the directory only contains a short README with a brief description of the group, a reference to the existing LLVM Qualification Working Group page, and a note that the directory structure and contents are still under definition by the group.

At the moment, no one in the WG has write access to the repository, so the group cannot merge the PR directly yet.

The group also discussed the possible structure of the WG directory. The current idea is:

```
llvm-wgs/
  fusa-qual-wg/
    README.md
    onboarding/
      YoungJun's document in Markdown format
    presentations/
      Links to presentations, for example LLVM conference presentations
    proposals/
      Links to RFCs and related proposals
    sync-ups/
      Meeting materials in Markdown format
      Links to Wendi's Google Drive, if needed
    libraries_qual/
      Methodology
      PoCs
      Workflow
      Templates
      Examples
    tools_qual/
      Workflows
      Templates
      Guidelines
      Examples / toy projects
    safety_model/
      Work in progress related to the safety model
```

The structure is still under discussion and will be refined by the group.

## Technical topics

### General status

May has been a relatively slow month for the WG for several reasons.

However, some topics are still progressing, even if at a slow pace. For example, [@uwendi](https://discourse.llvm.org/u/uwendi) and [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) have continued some work on the safety model topic.

The group also noted that having the GitHub directory available in `llvm-wgs` should help progress work more efficiently. It would allow the group to make artifacts available in an LLVM project GitHub repository and to formalize reviews through pull requests.

### Constant-time coding support

During the Americas-friendly sync-up, [@kumarak](https://discourse.llvm.org/u/kumarak) raised a request for guidance from the WG regarding the following LLVM PR:

[github.com/llvm/llvm-project](https://github.com/llvm/llvm-project/pull/166702)

#### [[ConstantTime][LLVM] Add llvm.ct.select intrinsic with generic SelectionDAG lowering (#166702)](https://github.com/llvm/llvm-project/pull/166702)

`main` ← `users/wizardengineer/ct-select-core`

opened 05:46AM - 06 Nov 25 UTC

[![](https://us1.discourse-cdn.com/flex021/uploads/llvm/original/3X/a/b/ab732db5a023fd2d2b361aa4ccefbf9b7655bb3c.jpeg)
wizardengineer](https://github.com/wizardengineer)

[+2787
-4](https://github.com/llvm/llvm-project/pull/166702/files)

This is in reference to our [[RFC] Constant-Time Coding Support](https://discour[…](https://github.com/llvm/llvm-project/pull/166702)se.llvm.org/t/rfc-constant-time-coding-support/87781) proposal.
## Summary
This PR introduces core infrastructure for constant-time selection operations in LLVM, providing a foundation for cryptographic code that prevents timing side-channels. This is the first PR in a stacked series implementing comprehensive constant-time selection support across multiple architectures.
## Changes
### 1. Core Intrinsic Definition
Adds the `llvm.ct.select` intrinsic family to LLVM IR:
- Provides constant-time selection semantics: `result = condition ? true\_value : false\_value`
- Guarantees execution time independent of both the condition value and the values being selected
- Prevents timing side-channel attacks in security-sensitive code
- Defined in `llvm/include/llvm/IR/Intrinsics.td`
> \*\*Note:\*\* On some architectures, the constant-time guarantee may be conditional on
> hardware features being enabled at runtime (e.g., ARM DIT/DOIT). Target-specific
> lowering is responsible for emitting instructions that uphold constant-time
> semantics given the appropriate hardware configuration.
### 2. Generic Fallback Implementation
Implements architecture-agnostic SelectionDAG lowering using bitwise operations:
- \*\*Pattern\*\*: `result = (true\_val & mask) | (false\_val & ~mask)` where `mask = -(condition)`
- Works on any architecture without specialized instruction support
- Ensures constant-time execution through branch-free operations
- Located in `llvm/lib/CodeGen/SelectionDAG/SelectionDAGBuilder.cpp`
The fallback implementation converts boolean conditions into bitmasks and uses bitwise arithmetic to achieve constant-time selection:
```
condition (0 or 1) → NEG → mask (0x0000... or 0xFFFF...)
result = (true\_val & mask) | (false\_val & ~mask)
```
This approach guarantees:
- No conditional branches that could leak timing information
- Constant execution time regardless of condition value or selected operand values
- Portable implementation across all LLVM targets
### 3. Test Coverage
Includes basic test cases demonstrating fallback functionality:
- \*\*RISC-V\*\*: `llvm/test/CodeGen/RISCV/ctselect-fallback.ll` - Generic fallback pattern verification
- \*\*X86\*\*: `llvm/test/CodeGen/X86/ctselect.ll` - Demonstrates generic lowering before optimization
These tests verify that the intrinsic correctly lowers to constant-time bitwise operations on architectures without native support.
## Architecture Support
This PR provides the \*\*fallback implementation\*\* that works on all architectures. Subsequent PRs in the stack will add:
- Clang frontend support (`\_\_builtin\_ct\_select`)
- Architecture-specific optimizations (CMOV, conditional moves, etc.)
- Comprehensive test suites for each target
## Security Properties
The fallback implementation ensures:
1. \*\*No conditional branches\*\* - Execution path is independent of condition value
2. \*\*Constant execution time\*\* - Execution time is independent of the condition and the values being selected
3. \*\*No data-dependent memory access\*\* - All memory operations are unconditional
4. \*\*Compiler barrier semantics\*\* - Prevents optimization across ct.select boundaries
\*\*Platform considerations:\*\* On certain architectures, constant-time behavior may depend on runtime hardware configuration (e.g., ARM Data Independent Timing mode). See the target-specific PRs for details on per-architecture requirements.
## Related PRs
This is part of a stacked PR series implementing constant-time selection:
1. \*\*#166702\*\* (this PR): Core infrastructure and fallback implementation
2. \*\*#166703\*\*: Clang frontend support (`\_\_builtin\_ct\_select`)
3. \*\*#166708\*\*: RISC-V comprehensive tests
4. \*\*#166705\*\*: MIPS comprehensive tests
5. \*\*#166709\*\*: WebAssembly comprehensive tests
6. \*\*#166704\*\*: X86/i386 optimizations and tests
7. \*\*#166706\*\*: AArch64 (ARM64) optimizations and tests
8. \*\*#166707\*\*: ARM32/Thumb optimizations and tests
## Testing
All changes pass existing regression tests. New tests verify:
- Correct lowering to bitwise operations
- Absence of conditional branches in generated code
- Proper handling of various data types (integers, pointers, floats)
## References
- RFC Discussion: https://discourse.llvm.org/t/rfc-constant-time-coding-support/87781
cc @nikic, @dtcxzyw

This PR introduces the `llvm.ct.select` intrinsic as part of the constant-time coding support RFC:

![](https://sea1.discourse-cdn.com/flex021/user_avatar/discourse.llvm.org/kaoudis/48/24832_2.png)

[[RFC] Constant-Time Coding Support](https://discourse.llvm.org/t/rfc-constant-time-coding-support/87781) [LLVM Project](https://discourse.llvm.org/c/llvm/5)

> Constant-Time Coding Support
> Summary
> We ([@kumarak](https://discourse.llvm.org/u/kumarak), [@frabert](https://discourse.llvm.org/u/frabert), [@hbrodin](https://discourse.llvm.org/u/hbrodin), [@wizardengineer](https://discourse.llvm.org/u/wizardengineer), and myself of Trail of Bits) propose a Clang “constant-time selection” builtin for cryptographers to use to ensure that their compiled C and C++ code selects between values in constant time consistently across target architectures. Our builtin will selectively bypass optimizations that are beneficial for most compiled code but that can replace intended constant-time operations with variable-time jumps or bran…

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
