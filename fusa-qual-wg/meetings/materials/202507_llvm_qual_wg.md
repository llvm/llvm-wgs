# LLVM Qualification Working Group - July 2025

- Sync-up meeting #1
- Focus: _Specifications_

## Contents

- Welcome & Intros
- Code of Conduct
- Collaboration Format
- Early Topics & Activities
- Today’s Focus Discussion: Requirements & Traceability
- Next Steps?

## Welcome: Why We’re Here

- Shared interest in increasing trust, ensuring quality, and enabling _qualification_ of LLVM components and LLVM-based toolchains for safety-critical _and_ non-safety-critical developments
- Shared vision of building a foundation for reusable and community-driven _qualification_ artifacts upstream, through collaboration and transparency

## Introductions

Quick round: name, affiliation, interest in this group.  
One word you associate with _qualification_.

## Code of Conduct

Short reminder (based on LLVM CoC): Respect, constructive discourse, inclusion  
We listen to understand  
We share, not sell  
If issues arise, contact moderators (e.g. Wendi for now)

Link: [Code of Conduct (for review by all members before publishing)](https://mypads2.framapad.org/mypads/?/mypads/group/llvm-qualification-wg-cwt6z99x/pad/view/llvm-qualification-wg-code-of-conduct-2mt7z9lc)

## Communication - Collaboration Format

Support async input and real-time ==coordination== equally

1. **Discussion**
   - LLVM Discourse under “Community”
   - Discord channel [#fusa-qual-wg](https://discord.com/channels/636084430946959380/1389362444169773117)
2. **Meetings**
   - Monthly sync-ups + async follow-up via posts
   - [Meeting minutes](https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148) (Discourse thread)
3. **Docs**
   - GitHub (version-controlled, open to all)
   - Shared templates, references, process experiments
4. **Other tools**
   - Any suggestions?

## Early Topics & Activities

- Modular Breakdown
- Split the qualification work across key components
  1. **Frontend**: Language-specific aspects (e.g. Clang)
  2. **Middle-end**: Optimizations, analysis, IR transformations
  3. **Backend**: Target-specific code generation
- Initial focus on Clang
  - C/C++ as a starting point
  - Broadly used in safety-critical applications
- Other relevant tools and commands: `llvm-cov`, `clang-tidy`, `Autocheck`, etc

## Pieces of the confidence-in-use puzzle

- ==`Specifications`: Expected behavior, constraints==
- `Testing`: Coverage, regression, etc.
- `Formal Verification`: Translation validation, equivalence checking
- `Sanitizer Use`: e.g., RTSan, ASan, UBSan
- `Runtime Diagnostics`: Error and Warning messages
- `Source Code Quality`: Coding guidelines, autochecks
- `Known Issues Analysis`: Workarounds and countermeasures
- `Documentation`: User & safety manual, release notes, configuration options
- `Other pieces`: Any other suggestions?

## First piece: Specifications

How to define clear and structured specifications as a foundation for testing, traceability, and reusable qualification artifacts

1. Balancing specification clarity with upstream feasibility
2. Enabling traceability between specifications and verification means
3. Defining scope, ownership, and sustainability

## Facing the challenges

***Challenge 1:*** How to define and structure requirements in a way that supports qualification, without placing undue burden on the upstream OSS community

**Key considerations:**

- Minimal overhead for contributors
- Leverage existing artifacts where possible
- Align with community practices (e.g. formatting, annotations)
- Use a free and OSS Requirements Management Tool? e.g. [(1)](https://gist.github.com/stanislaw/aa40eb7de9f522ad482e5d239c435ff8) and [(2)](https://www.requirementsmanagementtools.com/opensource.php)

***Challenge 2:*** Establish mechanisms for bidirectional traceability between specs and verification/validation elements (e.g. tests, static checks, sanitizer results)

**Key considerations:**

- How and where to annotate tests with requirements
- Manual vs automated traceability
- Prototyping with a well-scoped target

***Challenge 3:*** Determine what should be specified, by whom, and how it can be maintained across language targets, components, and organizations

**Key considerations:**

- Different needs for Frontend, Middlend, Backend, Linker
- Specs vs implementations (e.g. language standards vs behavior)
- Toolchain coverage, automation, and potential for a Safety Manual
- Reusability by downstream users (e.g. adding their own constraints)

## Next Steps?

- ==We’re here!== July 2025 - Specifications - Let’s continue the conversation on Discourse & Discord
- Aug-Sep 2025 - Summary of ideas? - Proposed solutions
- Oct-Nov 2025 - Initial prototyping? - Test with a well-scoped target

## Open Discussion

Let's discuss any doubts or concerns.  
If something comes up later, contact the Working Group on Discourse or Discord.
