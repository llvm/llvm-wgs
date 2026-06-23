# Notes - September 2025

## Participants

### EU/Asia-friendly (Tuesday 2025/09/02, 5:30PM JST, 1h)

- Carlos Ramirez (host)
- Davide Cunial
- Erik Tomusk
- Florian Gilcher
- Jorge Sousa
- José Rui Simoes
- Oscar Slotosch
- Petter Berntsson
- Vlad Serebrennikov
- Wendi Urribarri (co-host - note taking & check time)
- YoungJun Lee
- Zaky Hermawan

### Americas-friendly (Wednesday 2025/09/03, 6:00AM JST, 1h)

Cancelled - See <https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148/8>

## Agenda

Refer to <https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148/6>

## Links

- [Reminder] Introductions & Participation (Google Form): <https://forms.gle/zKBPZrma6tUMDCwh7>
- [Discord channel] `#fusa-qual-wg`: <https://discord.com/channels/636084430946959380/1389362444169773117>
- [RFC] C++ conformance test suite: <https://discourse.llvm.org/t/rfc-c-conformance-test-suite/69821>

## Highlights

### Non-technical topics

#### About note taking

- No shared concerns from “core members”
- One shared concern about AI writing down every word (from a non-member)
- Gemini not enabled today

#### New self-nomination through the Google Form - Zaky’s presentation

- EE student from Indonesia
- Coming as an individual
- Working with ISO/SAE 21434 (cybersecurity)

#### Oscar’s idea for the US LLVM 2025 conference (end of October)

- Proposal to have a corner about compiler qualification at the exhibition for sponsors
- Discuss with people and attract interest on it
- No conclusion about this point, to be taken for discussion to Discord

### Technical topics

Wrap-up about direction and focus of the discussions since July

#### Reference functional safety standard

- Members from several industries (automotive, trains, robots, etc), so different functional safety standards apply
- General framework for functional safety of E/EE/PE systems is IEC 61508, so makes sense to use it as first guidance
- As IEC 61508 is parent of other functional safety standards, the expectations around tool confidence are very similar

#### Need to provide evidence of tool usage

- Three questions from the safety standards (see slides)
- If answers Yes - Yes - No, then there is a need to provide the evidence
- Comments about question 3:
  - Most safety standards are written for users, so it depends on how much they examine the “relevant outputs”
  - In the case of a compiler, relevant output → final executable
  - More and more difficult to thoroughly verify the final executable (complexity)
  - Many of the tools that are traditionally used by vendors are closed, some open tools that can be used to check the relevant outputs

#### First target: Clang compiler

- As a tool provider of Clang, we don’t know what will be the usage
- As a tool user, you can restrict yourself (for example, using it only for debugging, not for mass-production)
- Users will need to rely on the compiler depending on the usage
- All the C++ parsing and semantic analysis is done by the Clang frontend
- Language + Standard => Version changes are fast
- Which flavor of C or C++?
  - C++ spec improves significantly
  - C spec is more rigorous
- Suggestion of small scope:
  - Limit to the lexer? Spec wise, it is more simple
  - Opinion 1: use of restricting to lexer is limited; from safety point of view, trust the lexer but what about the rest; requirements and association to what use cases
  - Opinion 2: agree, need of a valid use case for the lexer

#### About effort for a conformance test suite:

- Opinion 1: Amount of effort would be huge even for 1 version
- Opinion 2: Testing is laborious but not very hard
- Opinion 3: If you want to do a good conformance test, bottleneck is interpretation of the standard; testing specification against C/C++ is not as with Rust
- Comment: commercial test suites are expensive, 40-45K Euro to qualify only one version of a compiler
- What is generated is version dependent
- About usage of Alive2:
  - Replace the Clang front-end with Alive2 front-end and generate Alive2 IR from source code?
  - Clarification: `alivecc` doesn’t replace Clang itself; it simply adds a pass plugin for verification at the IR transformation stage

#### Grey-box approach

- Qualification is typically black-box activity
- Disadvantage: to be done for every combination, optimization options, etc
- Grey-box approach could be useful, but one limitation is lack of specification of intermediate I/O
- Example: specification of the IR
- Identification of regressions in IR could be useful

#### Possibility of LTS?

- From this RFC, this will not happen - <https://discourse.llvm.org/t/rfc-llvm-lts/84049>
- Labor can be massive
- Very difficult interpretation of what an LTS is
- In Rust community an LTS is 2 years
- Rather do qualification work incrementally on top of the main version
- Which C++ flavor to support is a big question

#### Example of funding

- Fleet of students
- Reasonable budget
- Example: University of Romania
- “Top leadership” needed to guide the students

#### Selection of qualification methods

- ISO 26262 proposes four qualification methods
- Evaluation of the tool dev process is highly recommended only for ASIL A and ASIL B
- Not to be used alone without Validation so to cover ASIL C and ASIL D
- Clarification:
  - Proposal is not about using Validation or Evaluation of dev process alone
  - Have a mix of both to cover all safety integrity levels with at least one highly recommended method
  - Many tool vendors already use a mix of these two methods for “certification“: validation by the vendor + audit by a certifying body

## Actions

Wendi :

- share summary of topics with the group and the community
- point out the possible ways to proceed
- create threads for each subject on Discord? (easier to communicate)

All : participate in the open discussions (preferred on Discord, but Discourse is also fine)
