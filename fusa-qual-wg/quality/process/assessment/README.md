# Assessment of the development process

This workstream examines how LLVM software is developed and maintained, and what public evidence is available about those practices.
It aims to make existing strengths, limitations, and open questions easier for LLVM contributors and downstream users to understand.

> [!NOTE]
> This assessment does not prescribe a quality management system for LLVM.

> [!NOTE]
> In a distributed open-source project, different contributors, maintainers, and downstream users may perform different parts of the work, so an assessment should make those responsibilities clear.

## Why look at development practices?

In a safety-related project, confidence depends partly on how work is planned, reviewed, tested, changed, and recorded.
For example, a test result is more useful when a user can identify the version tested and understand what happens when that version changes.
[Standards](../../../standards.md) have different requirements, but they illustrate why development and management practices matter alongside the behavior of the software itself.

There is a more direct connection for development tools such as compilers.
The automotive functional safety standard [ISO 26262-8:2018, Clause 11.4.8](https://www.iso.org/standard/68390.html) identifies *evaluation of the tool development process* as one possible tool qualification method.
When that method is applicable, evidence about how the relevant tool was developed can help a user assess whether an appropriate process was applied.
Useful evidence might include documented review and testing practices, change and release records, and how known defects are handled.

Development-process information can also help users of LLVM runtime libraries, although the assurance questions and applicable qualification methods for software included in a product differ from those for a development tool.
See the Working Group's [tool](../../../tools/README.md) and [runtime-library](../../../libs/README.md) activities for those more focused questions.

## Using open-source quality frameworks

Open-source projects often make their policies, code changes, reviews, tests, releases, and issue discussions public.
Quality frameworks provide questions or criteria for examining these practices and the evidence behind them.
They offer different views of a project. For example:

| Framework or initiative | Who develops it and what it emphasizes |
| --- | --- |
| [OpenSSF Best Practices Badge](https://openssf.org/projects/best-practices-badge/) | The OpenSSF Best Practices Working Group maintains public criteria covering development, quality, and security practices. Projects voluntarily explain how they meet the criteria. |
| [Eclipse Trustable Software Framework](https://projects.eclipse.org/projects/technology.tsf) | An Eclipse Foundation project develops a method for recording claims and connected evidence about software projects and their risks. |
| [Apache Project Maturity Model](https://community.apache.org/apache-way/apache-project-maturity-model) | The Apache Software Foundation's community describes how to examine the maturity of an Apache project's community and codebase. Some of its questions are useful outside Apache. |
| [ELISA Lighthouse OSS SIG](https://github.com/elisa-tech/lighthouse-oss) | An open ELISA group is developing a checklist and assessment guide from literature, existing frameworks, and observed open-source practices, with a broad software-quality focus. Its checklist is still being moved into the repository. |

These groups draw on experience developing, maintaining, or assessing open-source software, and publish their approaches for others to review and challenge.
That makes their criteria useful guidance, while each group still speaks from its own scope; none defines a universal test of OSS quality or decides what LLVM must do.
We should check the evidence for each observation and consider whether a criterion fits LLVM and the intended use.

## Existing starting points for LLVM

- **OpenSSF Best Practices Badge:** [LLVM's public entry](https://www.bestpractices.dev/en/projects/8273/passing) (T. Stellard) provides explanations and links for individual criteria.
  It is a voluntary self-assessment; the entry shows its last update in September 2024.
  It is a valuable record to review and refresh where practices or evidence have changed.
- **ELISA Lighthouse OSS checklist:** A [preliminary assessment of LLVM](https://eclipsesdv.org/wp-content/uploads/2025/12/Wendi-Urribarri-What-ELISAs-Lighthouse-OSS-Best-Practices-Reveal-About-LLVMs-State-of-Practice.pdf) (W. Urribarri) used an early/draft checklist for a learning exercise based on public information, covering governance, contributions, testing, security, documentation, and sustainability.
  The LLVM assessment has not yet been updated against the evolving [Lighthouse working checklist](https://docs.google.com/spreadsheets/d/1jR0oGQpwJTdThJAOtWP70GrdWSz7K-ol84j5BWX2h8g/edit).

A [preliminary comparison of OSS frameworks](https://directory.elisa.tech/workshops/2026-06-London/D3-10-00_Comparing_ELISA_Lighthouse_OSS_SIG_Checklist_with_Existing_OSS_Best-Practice_Frameworks.pdf) explores where the Lighthouse checklist overlaps with or complements the OpenSSF, Eclipse, and Apache approaches.
That comparison is an input to this work.

## Possible next steps

No consolidated, Working Group-reviewed assessment of LLVM has yet been published in this directory. Possible next steps are:

1. Define the scope and date of each assessment: LLVM-wide practices can differ from those of a particular component, release, or tool version.
2. Revisit the 2025 observations as the Lighthouse checklist and assessment guide develop, using LLVM’s current policies, development-process guidance, evidence of actual practice in the GitHub repositories, and evidence already gathered for LLVM's OpenSSF badge.
3. Link each observation to public evidence and distinguish a demonstrated practice, missing public evidence, and a criterion that does not fit the scope; lack of public evidence does not prove that a practice is absent.
4. Discuss possible gaps and improvements with the relevant LLVM contributors and maintainers before proposing changes to LLVM practices or documentation.
5. Record what has changed over time, and explain which observations might help downstream users with their more specific tool or library assurance work.

The aim is to make useful practices visible and offer constructive, evidence-based suggestions to the LLVM community.
The result should also show where a downstream user needs more information or must perform work for a particular safety-related use.
