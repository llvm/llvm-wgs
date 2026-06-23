# Notes - July 2025

## Participants

### EU/Asia-friendly (Tuesday 2025/07/01, 5:30PM JST, 1h)

- Carlos Ramirez (WbyT)
- Ferdinand Lemaire (WbyT)
- Jessica Paquette (WbyT)
- Jorge Pinto Sousa (Critical TechWorks)
- Mikhail Maltsev (Arm)
- Oliver Pajonk (Elektrobit)
- Petar Jovanovic (HTEC)
- Petter Bertnsson (Arm)
- Sameera Deshpande (Quadric)
- Sandeep (Arm)
- Shivam Gupta (Raincode Labs)
- YoungJun (NSHC)
- Wendi Urribarri (WbyT)

### Americas-friendly (Wednesday 2025/07/02, 6:00AM JST, 1h)

- Alan Phipps (Texas Instruments)
- Allen Miller (Texas Instruments)
- Chris Apple (self/RTSan owner)
- Florian Gilcher (Ferrous Systems)
- John Regehr (University of Utah/Alive2)
- Lucile Nihlen (Google)
- Nigel Drago (Quadric)
- Oscar Slotosch (Validas)
- Pete LeVasseur (WbyT)
- Petr Hosek (Google)
- Todd Snider (Texas Instruments)
- Wendi Urribarri (WbyT)

## Agenda

- Welcome & Intros
- Code of Conduct
- Collaboration format
- Early topics & activities
- Focus discussion: Requirements & Traceability
- Next steps?

![](https://us1.discourse-cdn.com/flex021/uploads/llvm/original/3X/1/4/14714c36061f406b48ba0191e00d8fbc4d2ee769.png)
[Mentimeter](https://www.menti.com/alistrrjqwbc)

![](https://us1.discourse-cdn.com/flex021/uploads/llvm/optimized/3X/0/9/09109185c45710cc377642d3f530d4d0e48dfe66_2_690x376.jpeg)

### [llvm-fusa-qual-wg-sync-up-1 - Mentimeter](https://www.menti.com/alistrrjqwbc)

Be heard, collaborate, and share ideas—make meetings and classes more engaging with real conversations.

## Links

- Code of Conduct: <https://mypads2.framapad.org/mypads/?/mypads/group/llvm-qualification-wg-cwt6z99x/pad/view/llvm-qualification-wg-code-of-conduct-2mt7z9lc>
- Meeting minutes (Discourse): [LLVM Qualification WG sync-ups meeting minutes](https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148)
- Discord channel: [Discord](https://discord.com/channels/636084430946959380/1389362444169773117)
- Our page: [LLVM Qualification Group — LLVM 22.0.0git documentation](https://llvm.org/docs/QualGroup.html)
- [Slides](https://www.dropbox.com/scl/fi/lcn3qbtc7ceg78s9ci2wd/LLVM-Qualification-WG-July-2025.pdf?rlkey=zkrcdgwswrlg7yl7y9iy2xfy0&st=rc7s8cef&dl=0) (will be migrated to GitHub later)
- [Open source requirements management tools · GitHub](https://gist.github.com/stanislaw/aa40eb7de9f522ad482e5d239c435ff8)
- [Free and Open Source Software Requirements Management Tools](https://www.requirementsmanagementtools.com/opensource.php)
- Clang C/C++ Language WG (meeting notes): [Clang C/C++ Language Working Group Meetings - Google Docs](https://docs.google.com/document/d/1x5-RbOC6-jnI_NcJ9Dp4pSmGhhNe7lUevuWUIB46TeM/edit?tab=t.0#heading=h.h5r993hcns4l)

## Highlights

### EU/Asia

- **Approaches to Linking Tests and Requirements:** Jessica discussed different methods for associating tests with requirements, such as adding text to existing tests or creating a directory to reference them. She suggested that adding text to the tests might be the most practical initial step. Wendi noted this down as a potential solution.
- **Leveraging Existing Specifications and Tests:** Wendi inquired about existing specifications from the C/C++ working group. Jessica mentioned that implicit requirements might already exist in the test directory where clang’s behavior is checked for specific code. Jorge suggested utilizing golden samples as tests and mapping them to requirements using LLVM’s existing testing infrastructure.
- **Command Line Option Testing**: Mikhail proposed checking which command line options are used by which tests during test suite runs to ensure all specified options are tested. Wendi asked about typical requirements management practices, noting the need for unique IDs and clear, verifiable descriptions.
- **Requirements Management Tools:** Wendi shared links to free and open-source requirements management tools, mentioning Basil. Oliver described a similar tool used for tracing links between requirements, tests, and other elements, capable of generating coverage reports. Jorge offered to investigate in the Eclipse SDV/S-Core group what they use for requirements.
- **Automating Traceability**: The discussion addressed automating the mapping between specifications and tests, either within the tests or using a requirements management tool. Oliver described how traceability tools use commands with IDs to link requirements to various artifacts and check for coverage.
- **Scope and Maintenance of Specifications**: Wendi raised the question of what should be specified, by whom, and how it can be maintained, initially suggesting a focus on clang and C++. Oliver cautioned that this task should not be underestimated due to the potential workload. Jessica suggested that while specifying every compiler transformation might be difficult, existing tests could catalog behavior, and tools like Alive2 could verify semantic equivalence for certain optimizations. Petar emphasized the potential enormity of the effort required for detailed specification and maintenance.
- **Black Box Testing and Trust**: Petar shared experience from qualifying GCC by treating it as a black box and using clang for result comparison. They suggested that a similar approach of extensive testing might be necessary for LLVM, focusing on building trust rather than deep internal analysis. Oliver seconded this, noting the difficulty of qualifying the Linux kernel through code analysis and suggesting the possibility of safety monitors or limiting the scope of usable compiler options. Jorge mentioned that qualified commercial compilers often come with safety manuals and usage guidelines.
- **Qualification of Standard/Runtime Libraries and Linker**: Petar inquired about the qualification of the standard library. Jessica suggested working on libraries after addressing clang. Mikhail expressed interest in qualifying open-source runtimes. Wendi noted this point for future discussion.
- **Next Steps and Continued Discussion**: Wendi suggested continuing the discussion on the Discord channel or Discourse and encouraged participants to add their thoughts to the notes.

### US/Canada

- **Proposed Work Breakdown for Qualification**: Wendi presented a suggestion coming from JR Simoes to split the qualification work into three parts: front-end, middle-end, and back-end, with an initial focus on the C/C++ front-end due to its broad use in safety-critical applications. Noted that other languages like Rust and relevant tools could be included later. Key discussion points for confidence in use of the compiler include specifications, testing, formal verification, sanitizers, runtime diagnostics, quality of compiler inputs, known issues analysis, and documentation (user manuals, safety manuals, release notes). The qualification of standard and runtime libraries was also added as a topic based on a suggestion during the EU/Asia session.
- **Challenges in Defining and Tracing Specifications**: Wendi highlighted critical questions regarding specifications: whether existing specifications for front-ends like Clang can be reused, how to define partial specifications if none exist, and how to trace specifications with existing open-source verification means, such as the 25,000 tests, to achieve bidirectional traceability. Posed questions about the ownership and maintainability of these specifications. Opinions from the EU/Asia session suggested annotating tests with unique IDs linked to requirements or grouping tests into directories associated with specific requirements.
- **Recommendations for Specification and Test Organization**: Florian shared his experience with Rust, suggesting that specifications should reuse as much as possible from existing project documentation and be built in a format conducive to linking, such as HTML. Oscar pointed out that C/C++ benefits from existing ISO standardization documents, so the focus should be on LLVM-specific features rather than creating new language specifications. Both Florian and Oscar agreed that structuring tests in directories that mirror the C standard’s chapters and sub-chapters is a practical and accepted approach for C/C++ compiler qualification, making maintenance easier for both safety-critical and non-safety-critical maintainers.
- **Completeness Argument and Requirements Management Tools**: Oscar emphasized the need for a “completeness argument” in qualifying open-source software, explaining that beyond code coverage, it is essential to demonstrate why test cases are sufficient, often by using equivalence classes and programming constructs to define comprehensive test strategies. Wendi inquired about the use of free or open-source requirements management tools. Oscar indicated that he uses a proprietary model for linking functional specifications to test cases.
- **Experiences with Requirements Management Tools:** Florian shared his experience, stating that while tools like Sphinx needs are useful for general software and libraries, programming language specifications are too dense for typical requirements writing tools. They opted for a custom Sphinx extension for language specification to test tracing, finding it more suitable than trying to adapt existing tools not designed for this specific task. Pete supported this, noting that Sphinx and Sphinx needs were adopted for the Rust coding guidelines within the safety-critical Rust consortium, finding them useful for building verifications and ensuring traceability.
- **Feature-Based Qualification Structure**: Oscar suggested structuring the qualification based on logical features (e.g., language compliance, optimization rules, target-specific features) rather than technical components like front-end, middle-end, and back-end, as this logical structure is more relevant for certifiers who may not understand internal compiler architecture, and that tool qualification is typically a black-box activity. John clarified that the split front-end/middle-end/back-end is driven by the capabilities of existing formal verification tools like Alive2 and their translation validation work, which currently can validate optimizations on the middle-end and back-end but not the front-end. Oscar and Wendi agreed that tools used for tool qualification do not need to be qualified themselves, simplifying the process. Florian expressed interest in separately qualifying linkers, but Oscar argued that qualifying a tool always involves documenting its environment and configuration, making it an integrated process.

## Actions

Wendi:

- Create calendar for the group, with regular invitations to the sync-ups
- Update Online Sync-ups page: [Getting Involved — LLVM 22.0.0git documentation](https://llvm.org/docs/GettingInvolved.html#online-sync-ups)
- Update group’s page with new info: [LLVM Qualification Group — LLVM 22.0.0git documentation](https://llvm.org/docs/QualGroup.html)
- Talk to the Clang C/C++ working group about specifications and how to build a language-compliant suite, e.g., C++17
- Add the topic of what to do with libraries as a backlog item

Jorge:

- Check the Eclipse Safety Core (S-core) for requirements management (definition, traceability) and report back

All:

- Continue the discussion on next steps in the Discord channel & Discourse
