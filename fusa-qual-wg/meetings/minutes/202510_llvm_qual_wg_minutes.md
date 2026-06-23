# Notes - October 2025

## Participants

### EU/Asia-friendly (Tuesday 2025/10/07, 5:30PM JST, 1h)

- Carlos Ramirez
- Davide Cunial
- Oscar Slotosch
- Petter Berntsson
- Wendi Urribarri
- YoungJun Lee
- Zaky Hermawan

### Americas-friendly (Wednesday 2025/10/08, 6:00AM JST, 1h)

- Alan Phipps
- Wendi Urribarri

## Agenda

Refer to <https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148/12>

## Links

- [202510\_llvm\_qual\_wg](https://docs.google.com/presentation/d/1ND2SkjgcHvcEbQmMd8ExL-PpRXouP49T-wfy3xf2yRQ/edit?slide=id.p1#slide=id.p1)
- RFC Clang C++ conformance: <https://discourse.llvm.org/t/rfc-c-conformance-test-suite/69821>
- RFC Human-error prediction: <https://discourse.llvm.org/t/rfc-a-human-centered-approach-to-proactively-improve-llvm-code-and-documentation-quality/87903>
- ISO/PAS 8926: <https://www.iso.org/standard/83346.html>
- RFC (draft) to collect community input: <https://mypads2.framapad.org/p/rfc-petter-311qpv9ni>

## Highlights

Gemini notes taken in the EU/Asia meeting, modified by [@uwendi](https://discourse.llvm.org/u/uwendi)

### Non-technical topics

#### Meeting Logistics and New Members

- Slides shared on Discord before the meeting
- Addition of three new members
- Updated member list has been added into the official group webpage (PR not merged yet)

#### Challenges in Decision-Making

- Difficulties in making decisions within the group
- Cultural factors, challenges in reaching consensus, and time limits as primary issue
- What does consensus means for us, what constitutes it
- Find compromise, common understanding
- Clear when people have different opinions, but for people who are not giving an opinion, how can we know?
- Divided positions - What happens when 50/50?
- Consensus could mean no objections are raised, or majority rule if participation is lacking
- Engagement in early conversations and reasoning are necessary, but for clear yes/no decisions, voting with a >50% threshold should be used, excluding non-votes from the percentage => If someone doesn’t vote, we cannot count the vote
- If there a “gray” area, then maybe discuss it in next sync-up meeting
- What is the model from other WGs? In general, it’s done through “informal” decision making
- Don’t over complicate => Lightweight process

### Technical topics

#### Discussion on Confidence and Qualification Activities

- Two work threads: classical black box validation + component confidence
- These are explorations, not final decisions
- Suggestion: rephrase the “confidence” aspect as “gray/white box qualification approach by focusing on sub components” rather than “improving confidence,” explaining that tool confidence is a risk analysis that cannot be improved but rather risks can be reduced through qualification
- Counter-opinion: different providers can have different Tool Confidence Levels (TCLs) for the same tool due to mitigation actions, which could be seen as improving confidence
- Proposal: this WG could provide advice on activities to increase confidence in tool usage, beyond just qualification
- Suggested reformulation:

  - Create confidence in the use of the tools, e.g. by using them carefully and checking the tool results
  - This will help to reduce the tool confidence level (TCL) as defined in ISO 26262, which measure the tool risks
  - The remaining risks of the tools have to be reduced by tool qualification
  - The mostly used qualification method is validation
  - It can be performed as a black-box approach, just by testing the requirements, e.g. the compliance of a compiler with a C or C++ standard
  - Another validation strategy which can be applied to open-source tools is a white/grey box approach, i.e. by validating sub-components of the tools, e.g. a lexer, parser or backend of a compiler
- Different perspective:

  - Validation is acknowledged as a common method for qualification for usage of a tool for the higher risk contexts (SIL3/4, ASIL C/D…)
  - But, evaluation of the development process is another highly recommended method for lower criticality contexts (ASIL B)
  - Let’s document our arguments about suitability of LLVM’s development process upstream, and perform an assessment with auditors who could volunteer for it
  - Development process - LLVM developer policy + Evaluation of the process: OSS best practices + human factors metrics
  - A qualification could then be achieved up to ASIL B context usage
  - Validation would be a 2nd step approach for qualification for higher criticality levels

#### Tool Qualification and Library Qualification

- Tool qualification by validation: different strategies like using test suites or breaking down qualification by validating sub-components such as the lexer or parser
- Qualifying sub-components is useful for overall qualification
- Library qualification is more rigorous and typically requires a white box approach with code coverage measurements

#### Focus on Upstream LLVM and Reusability

- The group’s focus is exclusively on the upstream LLVM project, aiming to create reusable output that downstream companies can utilize
- The group strives for reusability, building general or usable tools for various standards

#### Challenges in Defining a Toy Project

- Several constraints, including the lack of resources and the difficulty in choosing a language (C, C++, Rust…), compiler version, language standard, and compiler flags for a deliverable “toy project”
- Agreeing on a toy project would help answer these questions and provide a concrete direction for the group’s work

#### Standard Library Function Qualification

- Start with function-level qualification of standard library functions within a limited scope, such as a single header file, as it would be easier to manage than qualifying the entire compiler
- Use publicly known sources like CPP reference for requirements and tracing tests, aiming to provide upstream qualification evidence and design that downstream users could then utilize
- Library qualification is more rigorous than tool qualification but selecting requirements for library functions is a good idea
- If the group explores the library qualification topic, it might focus on pure C language due to the significant differences and complexities of C++
- The difference between C and C++ standard libraries is substantial, C++ libraries change frequently
- ISO/PAS 8926:2024 to qualify software components (incl. libraries)
  - Planned to be merged with Part 8-Chapter 12 in next edition of ISO 26262 (2027)\
  - Two axes: analysis of provenance and analysis of complexity
  - Depending on results of the analysis, different qualification activities must be performed

#### Outputs and Collaboration

- Draft tutorial for newcomers, focusing on organizing documents, presentations, and projects like compiler and code coverage sanitizers
- External toolchains could be referenced
- RFC to gather community input, aiming to provide a framework for compiler qualification and enable sharable evidence for downstream users
- Other efforts can and will be explored in the future, and all members are encouraged to work on any of these subjects, based on their interests and bandwidth/availability

## Actions

- [@petbernt](https://discourse.llvm.org/u/petbernt) will make a proposal presentation for library qualification
- [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee) and [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) will help write the draft tutorial
- [@slotosch](https://discourse.llvm.org/u/slotosch) will put his thoughts on tool confidence and qualification activities in a message in the group’s Discord channel
- [@uwendi](https://discourse.llvm.org/u/uwendi) will continue working on analysis of the suitability of the LLVM Developer Policy as development process for safety-critical, and on how to reuse good quality best practices from ELISA as part of this analysis/assessment
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) will run experiments on LLVM and provide evidence to see what can be accomplished using human-centric metrics analysis in LLVM’s upstream development process
- All: provide feedback on [@petbernt](https://discourse.llvm.org/u/petbernt)‘s RFC (considering the potential library approach) by end of the current calendar week, then [@petbernt](https://discourse.llvm.org/u/petbernt) will publish it
