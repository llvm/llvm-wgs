# Notes - August 2025

## Participants

### EU/Asia-friendly (Tuesday 2025/08/05, 5:30PM JST, 1h)

- Davide Cunial: Interest in Clang-Tidy Qualification
- Oscar Slotosch: Contribute and Learn about TQ, AI Tool Classification
- Carlos Ramirez: Tokyo, SW Quality, Safety & Security, phd in human-error centric quality
- Erik Tomusk: Interest in qualifying GPU Accelerators and use LLVM
- Petar Jovanovic: Compiler Engineer, Open-Source Enthusiast, Static Analysis Tool
- YoungJun Lee: Korea, Obfuscation Compiler, Alive2, SAST
- Wendi Urribarri: Tokyo, Functional Safety Engineer, Formal Methods

### Americas-friendly (Wednesday 2025/08/06, 6:00AM JST, 1h)

- Peter LeVasseur: WbyT
- Wendi Urribarri: WbyT
- Vlad Serebrennikov: invitee from the Clang C/C++ Working Group

## Agenda

- [Participant Introduction and Membership Criteria Form](https://forms.gle/yH2eV9UH1xXoouGJ7)
- [C++ Conformance Test Suite (RFC)](https://discourse.llvm.org/t/rfc-c-conformance-test-suite/69821)

## Links

- [NASE Study about AI](https://ntrs.nasa.gov/api/citations/20250001849/downloads/NASA-TM-20250001849.pdf)
- [Proposal of Membership Criteria](https://mypads2.framapad.org/p/group-composition-pqp2g9zl)
- [Clang conformance - summary from RFC](https://mypads2.framapad.org/p/clang-conformance-dipcg9xo)
- Rust language references: [The Rust Reference](https://doc.rust-lang.org/stable/reference/) and [FLS](https://rust-lang.github.io/fls/)

## Highlights

### EU/Asia

- **Meeting Kick-off and Participant Introductions**: as a previous step to discussing membership criteria, introduction of each attendee, sharing background and interest in the LLVM qualification group.
- **AI in Software Development and Qualification:** Carlos and Oscar discussed the role of AI in software development, particularly in the context of ISO 26262 compliance. Oscar mentioned a study where AI tools were classified as TCL1 due to uncertainties in their qualification, unlike other tools often classified as TCL3, emphasizing the human ability to detect errors. Carlos expressed skepticism about AI-generated code making it into production for critical software within the next decade due to liability issues and AI’s current limitations in understanding broad code context, which was supported by an experiment showing AI’s failure to recognize dependencies.
- **Accelerators and Safety Critical Spaces**: Erik focuses on high-performance computing and runtimes, and bringing this technology to safety-critical spaces like automotive. They clarified that their work involves certified runtime components that depend on LLVM for qualification, positioning themself more as a runtime specialist rather than a compiler expert in this context.
- **Open Source Static Analysis Tools and Legal Challenges**: Petar shared their experience in trying to open-source a static analysis tool for automotive standards like MISRA and AUTOSAR. They explained that legal issues, particularly concerning the exact wording of error reports and the reuse of standard parts, prevented the tool’s public release, despite having presented it five years prior. Davide affirmed a similar experience, noting that MISRA and AUTOSAR checks cannot currently be open-sourced, highlighting the legal complexities involved.
- **Discrepancies in Open Source Standards Access**: Oscar expressed surprise regarding the difficulties with open-sourcing AUTOSAR-related implementations, as AUTOSAR specifications are freely available, unlike MISRA documents which require payment. Petar clarified that while AUTOSAR standards are free to download, reusing parts of them requires written permission from the consortium, which has been difficult to obtain. This discussion underscored the legal and logistical hurdles in leveraging open-source initiatives for automotive industry standards.
- **LLVM Component Qualification by Validas**: Oscar detailed Validas’s experience in qualifying LLVM components, including LLVM-based compilers and clang-tidy. They highlighted the usefulness of clang’s feature to log optimization rules for qualification purposes and also mentioned their qualification kit for clang-tidy, which requires qualifying each rule individually. Additionally, Oscar noted their ongoing process of qualifying the STL template library, having identified and contributed fixes for issues in its implementation.
- **Compiler Optimizations and Safety Concerns**: Petar raised a question about “wrong” optimizations in compilers, stating that as a compiler developer, they see nothing inherently wrong with optimizations and that issues are typically bugs, not inherent flaws in optimization. Oscar provided examples of optimizations that can lead to incorrect or unexpected behavior, such as integer overflow issues or deviations in floating-point calculations due to differences in host versus target accuracy. The discussion emphasized the need for careful configuration and understanding of compiler behavior in safety-critical contexts to ensure deterministic output.
- **Managing Known Bugs in Open Source Tools**: Oscar discussed the importance of managing known bugs in open-source tools for qualification purposes, noting that the existence of bugs is acceptable as long as workarounds are available. They suggested that improving the classification and mapping of known bugs to specific features would significantly aid in filtering and scanning for relevant issues, making the analysis process faster and easier for developers.
- **Internal Process Changes and Membership Criteria**: Wendi briefly introduced a proposal for changes in the group’s internal process, including membership criteria and participation expectations. They shared a link to the detailed description, emphasizing the need for clear expectations regarding contributions and acknowledging the limited time and bandwidth of participants.
- **Valuing Small Contributions**: Wendi emphasized the significance of small contributions, stating that even a few minutes or one hour per month dedicated to the group would be meaningful and important. They encouraged attendees to review and comment on the shared document, noting that it was a lightweight version of the security response definition of group composition.
- **RFC Summary and Offline Review**: Wendi shared a link to a summary of the main points from an RFC written in April 2023, which is related to Clang conformance. They requested that participants review it offline and share their opinions on Discord rather than the Discourse forum.

### US/Canada

- **Proposed Internal Process for the Group**: Wendi presented a proposal for a new lightweight internal process to address concerns about group efficiency and the need for a more structured approach. They highlighted the importance of recognizing and respecting members’ limited bandwidth and valuing small contributions, as some members might have mistakenly believed that only full-time commitment was expected.
- **C++ Conformance Testing Challenges**: Wendi shared insights from their contact with the Clang C/C++ working group regarding Clang conformance specifications and testability. An RFC from April 2023 indicated that developing a C++ conformance test suite faced resource limitations, preventing any current action despite a good description of how it could be done. A significant hurdle was the licensing issues with test vendors, as they only allowed reporting pass/fail results but not opening tests to analyze failures, making error analysis impossible for open-source use.
- **Clang CXX Directory and Defect Reports**: Vlad elaborated on the `clang/test/CXX` directory, noting its two main parts: `DRs` (defect reports) and everything else. They maintained the `DRs` section, which contained about 700 tests for defect reports, far exceeding other implementations. Vlad mentioned that much of the work in this directory, particularly the first 600 defect reports, was done around 2014 by Richard Smith, but progress stopped after that.
- **Challenges with External Conformance Test Suites**: Vlad explained that efforts to use external test suites like those from Perennial and Plum Hall in Clang were unsuccessful due to restrictive licensing, which would essentially require these companies to forfeit their business. They also mentioned that some of these test suites were not ideal and could even contain bugs. Wendi confirmed similar issues with SolidSands, stating that it was difficult to use such suites in an open-source context.
- **C++ Standard and Compiler Conformance**: Vlad discussed the historical decision not to include many C++ examples in the standard, which created long-term issues for language evolution and caused increasing disagreement among implementations, especially for newer features. They emphasized the RFC’s primary goal: to find a way to write and maintain a test suite that avoids decay, proposing tracking the git repository of the draft to reflect updates to the standard in updated tests. Vlad explained that compilers often do not conform to published standards due to subsequent defect reports and accepted papers, citing the “relaxed template template parameter” debacle as an example.
- **Private Compiler Qualification and Test Suite Quality**: Wendi inquired how companies privately qualify their LLVM-based compilers given the lack of proof of conformance to standards. Vlad expressed skepticism about the quality of such private test suites, stating that Clang itself does not claim full conformance due to known unresolved issues, such as the incomplete implementation of the 2019 name lookup paper. Vlad also detailed challenges with “complete class context” rules, where compilers are expected to handle dependencies correctly but often do not due to performance concerns, making it difficult for external parties to fix.
- **Current Status of RFC**: Wendi summarized the RFC’s status, confirming with Vlad that nothing had changed regarding the feasibility of in-house effort or external conformance test suites due to resource and licensing issues. Vlad stressed the need for ongoing communication with the core working group to correctly interpret the standard and identify parts considered “garbage” that require rewriting.
- **Safety Critical Rust Consortium**: Pete discussed their work with the Safety Critical Rust Consortium, which aims to identify and address gaps in the Rust ecosystem and language for safety-critical applications. They explained that the consortium seeks to enable Rust’s use in more safety-critical industries and at higher safety criticality levels. Vlad raised concerns about the completeness of Rust’s specifications, noting that the specification for name lookup was unclear. Pete acknowledged that Rust, as a less mature language, had gaps in its documentation, but efforts were underway to improve the reference and FLS documents.

## Actions

- **All participants**: review description of the [proposal of internal process update](https://mypads2.framapad.org/p/group-composition-pqp2g9zl), share thoughts on the Discord channel, and add comments or modify directly in the FramaPad for improvement.
- **All participants**: review the [Clang conformance summary](https://mypads2.framapad.org/p/clang-conformance-dipcg9xo) and send feedback and questions on the Discord channel. The Clang C/C++ WG members are open to answer to our questions and concerns.
- **Wendi**: try to find a conversation with Robert C. Seacord about Plum Hall’s test suite and update Vlad.
- **Wendi**: plan contacting Plum Hall.
