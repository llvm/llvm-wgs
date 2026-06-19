# LLVM Qualification Working Group - October 2025

- Sync-up meeting #4
- Focus: _Upstream efforts and backlog_

## Non-technical topics

### New members (September)

🎉 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 🤝

| Name  | Discourse    | Discord    | GitHub       |
| ----- | ------------ | ---------- | ------------ |
| Jorge | sousajo-cc   | sousajo-cc | sousajo-cc   |
| José  | jr-simoes    | jr_simoes  | iznogoud-zz  |
| Zaky  | ZakyHermawan | quarkz99   | zakyHermawan |

### Summary of our interests (from our answers to the Google form)

| Name     | Interests                                                                                                                  |
| -------- | -------------------------------------------------------------------------------------------------------------------------- |
| Alan     | Qualification processes, qualification of runtime libraries, code coverage                                                 |
| Carlos   | Software quality, quality processes, early detection of software defects                                                   |
| Davide   | Analysis tools such as clang-tidy, the clang static analyzer, and clang sanitizers                                         |
| Jorge    | Testing and quality                                                                                                        |
| José     | Qualification of the optimizer / middle-end                                                                                |
| Oscar    | Qualification of tools and libraries                                                                                       |
| Petar    | Qualification of Clang/LLVM and standard libraries, Autocheck tools, static analysis tools                                 |
| Petter   | Traceability (reqs, overall qual process); approaches for producing structured, auditable evidence for LLVM qualification  |
| Wendi    | Practical solutions to increase confidence in OSS & to prevent and detect errors in software, software quality             |
| YoungJun | Application of translation validation tools to real-world code, and as part of a practical compiler qualification workflow |
| Zaky     | Sanitizers, Fuzzing                                                                                                        |

### Summary of docs updates (September)

Merged:
- \[QualGroup\] Add August and September 2025 slides and unify Meeting Materials: [#156897](https://github.com/llvm/llvm-project/pull/156897)
- \[docs\] Refactor QualGroup.rst: add membership rules, restructure sections: [#157804](https://github.com/llvm/llvm-project/pull/157804)
- LLVM Qualification Group - Backlog documentation and Discussion Updates: [#156184](https://github.com/llvm/llvm-project/pull/156184)
- \[QualGroup\] Update Slides Section, Add AI Transcription Policy, Clean Up: [#158842](https://github.com/llvm/llvm-project/pull/158842)
- \[QualGroup\]\[docs\] Reorganize QualGroup docs under Reference section: [#160021](https://github.com/llvm/llvm-project/pull/160021)

Open:
- \[QualGroup\]\[docs\] Add new members to LLVM Qualification Working Group: [#161113](https://github.com/llvm/llvm-project/pull/161113)

Link to our docs: [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)

### Decision taking in the WG

**Background**

- Recent discussions (e.g., LLVM US presence) highlighted uncertainty about how the group reaches decisions
- [Question from Oscar to the group members](https://discord.com/channels/636084430946959380/1417386396213051442/1422072577970671678): How does the group take decisions in general? Is it by majority vote?

**Key questions**

- What constitutes “consensus” for this group?
- Should we set a time limit to avoid long, open-ended debates?
- When is a formal vote appropriate vs. simple agreement in discussion?

**Example**

1. Aim for open discussion on Discord, seek broad agreement first
2. If no new viewpoints after an agreed time (e.g., 2 weeks), the “chair” or a “moderator” can call for a quick vote (✅ / ⛔)

Document the process in [QualGroup docs](https://llvm.org/docs/QualGroup.html) for future reference

## Technical topics: Upstream efforts and action plan

### From our last sync-up meeting...

### Confidence in the usage of software tools

![Workflow 1](../img/202509_workflow1.png)

_**References**_
- IEC 61508 Part 3 - Annex H
- ISO 26262 Part 8 - Chapter 11

See also slides 11 to 14 in AsiaLLVM 2025’s [presentation](https://llvm.org/devmtg/2025-06/slides/technical-talk/urribarri-automotive.pdf)

### Need to provide evidence of tool usage confidence

![Workflow 4](../img/202509_workflow4.png)

| Question | Description |
| -------- | ----------- |
| **Q1 - Is the software tool used to support a safety-related activity or task?** | Does the the software tool play a role in executing any of the required activities or tasks defined by the reference safety standard (IEC 61508, EN 50128, ISO 26262…) standard for systems, hardware, or software? e.g., safety analysis, design, implementation, verification, testing and validation tasks, requirements management, configuration management, change management, overall safety management. |
| **Q2 - Does the activity or task rely on the correct functioning of the software tool?** | Is there a dependency of any of the activities or tasks on the accurate operation of the software tool? Does the successful completion of the activity or task hinge on the software tool performing its functions correctly? If the correct functioning of the tool is vital, some malfunctions or errors could compromise the safety of the final developed system, hardware, or software. Understanding this dependency is important to identify, at an early stage of the tool's development what are the high-level potential risks and implications of tool failures on crucial activities or tasks, contingency plans to address potential tool malfunctions and ensure continuity of operations, and the necessity for rigorous testing / validation of the tool. |
| **(Optional) Q3 - Are the relevant outputs completely/thoroughly/sufficiently examined or verified for the applicable process step(s)?** | For example: by reviews, checks, or verification procedures in place to assess the quality (i.e., completeness, correctness, consistency) of the relevant outputs produced by the software tool. Or, do you foresee any chance that some errors in the outputs of the tool will remain undetected by subsequent verifications or examination? Understanding this is important to identify the effectiveness of existent verification procedures to detect potential issues in the relevant outputs early, allowing for corrective actions to be taken before they escalate into significant problems, and reducing the likelihood of errors affecting subsequent steps in the development process of the system, hardware, or software developed with the software tool. |

### Two perspectives on upstream efforts

Currently:

1. Use classical black-box _**validation**_ strategy _**upstream**_ e.g., Clang C/C++ conformance test kit 💻⚙️
or
2. Improve _**confidence**_ in sub-components _**upstream**_ e.g., Alive2 for middle-end, translation validation tools for backends 🖧 🛠️

They are non-exclusive efforts, do not contradict each other (though, the 2nd one can tend to a gray-box approach)

In any case, perform an evaluation of the development process _**upstream**_

- Development process: [LLVM Developer Policy - Documentation](https://llvm.org/docs/DeveloperPolicy.html)
- Evaluation that a suitable software development process has been applied, using for example:
  - [Good Quality / Best Practices in Open Source Standard](https://github.com/elisa-tech/lighthouse-oss) ([Lighthouse SIG](https://lists.elisa.tech/g/lighthouse) in [ELISA](https://lists.elisa.tech/g/main))
  - [Human-factors metrics for defect prediction](https://discourse.llvm.org/t/rfc-a-human-centered-approach-to-proactively-improve-llvm-code-and-documentation-quality/87903)

### Constraints

❌ Selection of qualification methods for _**downstream**_ efforts is not our business

🎯 But we strive for _**reusability**_ of our artifacts

⚠️ Need of resources/sponsorship for the development of Clang C/C++ conformance test kits that could be used upstream without licenses issues

⚠️ Need of resources/sponsorship to continue the development and for improvement of formal verification tools for middle-end (Alive2…), translation validation tools for back-ends (arm-tv…)

⚠️ [Good Quality / Best Practices in Open Source Standard](https://github.com/elisa-tech/lighthouse-oss) is progressing but still under development (early stages)

⚠️ Effort to use the [human-factors metrics for defect prediction](https://discourse.llvm.org/t/rfc-a-human-centered-approach-to-proactively-improve-llvm-code-and-documentation-quality/87903) framework: time that it takes for triage, root-cause analysis, documenting issues, adding in issue tracker…

### Meanwhile…

### Tutorial or Introduction (YoungJun)

A “tutorial” or a set of “key documents” for newcomers:

- Simply organizing the presentations and qualification-related projects or documents that formed the foundation of our group would be a sufficient tutorial.
  - Paper or documents
  - Presentation
  - Projects (Tools)
    - Compiler
      - Front end (clang-tidy, …), Middle end (alive2, …), Back end (arm-tv, …)
    - Code coverage, Sanitizer
      - llvm-cov, ASan etc …
- It would be even better if each document were linked to the specific requirements of the relevant standards (e.g., ISO 26262). For example, code coverage tools correspond to ISO 26262-6, clause 10.4.5 and DO-330.

📄 LLVM Qualification WG Tutorial: [Draft (Google Docs)](https://docs.google.com/document/d/1rhPMoXHFeJjCsf39iNqjnRO6r8ERwNQmnYO0PGo410Y/edit?tab=t.0)

Link: [Discord](https://discord.com/channels/636084430946959380/1418159298449510411/1419463176101040260)

### Qualification focus areas (Petter & Oscar)

Explore small qualification focus areas (Petter) and gather inputs from the community (Oscar)

- Tracing a few existing LLVM tests (e.g., for Clang)
- Drafting lightweight templates
- Concrete examples to point to

General open question: _Which areas would make the most sense to prioritize first, and at what scope?_

📜 RFC: Collecting Community Input on Qualification of LLVM Tools & Libraries: [Draft (FramaPad)](https://mypads2.framapad.org/p/rfc-petter-311qpv9ni)

Link: [Discord](https://discord.com/channels/636084430946959380/1418159298449510411/1418514196907294840)

### Other actionable subjects

Based on the workflow

1. Capture the need to provide evidence of tool usage confidence
   - For Clang? For other compilers? For other tools in the LLVM framework?
2. Create templates for Tool Specification, Tool Evaluation, Tool Qualification, Safety Manual?
   - For only IEC 61508 (general standard)? For specific standards (ISO 26262,...)?
3. Document general, high-level use cases (e.g., for Clang)?
4. Start exploring other error prevention and detection mitigation actions that can be documented
5. Other actions, based on [our interests](https://docs.google.com/presentation/d/1ND2SkjgcHvcEbQmMd8ExL-PpRXouP49T-wfy3xf2yRQ/edit?slide=id.g38ef004fb04_0_0#slide=id.g38ef004fb04_0_0) 🤓

## Open Discussion

Let's discuss any doubts or concerns.  
If something comes up later, contact the Working Group on Discourse or Discord.

