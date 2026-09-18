# LLVM Qualification Working Group

This directory contains documentation and working materials for the
LLVM Qualification Working Group.
The group explores how LLVM components and practices can better support
users of safety-critical and other high-assurance systems.

> [!NOTE]
> For more information about the group, see the
> [LLVM Qualification Working Group page](https://llvm.org/docs/QualGroup.html).

## Target audience

This documentation is for:

- LLVM contributors and maintainers, including readers with little or no
  functional safety experience;
- users integrating LLVM components into safety-related systems;
- tool and library developers;
- functional safety, quality, reliability, and security specialists; and
- current and prospective participants in the Working Group.

## Motivation

LLVM components, including libraries, compilers, and related tooling, may be
used in the development of safety-critical and high-assurance systems.
In such contexts, users may need to establish a certain degree of *confidence*
in these components, for example by understanding their intended use,
development practices, testing, traceability, known limitations, and the evidence
available to support downstream *qualification* or *certification* activities.

### What is Functional Safety?

Functional safety concerns risks caused by an electrical, electronic, or
programmable system behaving incorrectly. It asks questions such as:

- *What could go wrong and lead to harm?*
- *Which parts of the system help prevent or control that harm?*
- *What behavior is required from those parts?*
- *How can we verify the behavior and preserve evidence that the work was done?*
- *How do we control changes so that earlier conclusions remain valid?*

Software is *safety-related* when its behavior can contribute to preventing,
controlling, or causing an unsafe situation.
The software does not need to make an obvious safety decision itself.
For example, a runtime-library function, compiler, test framework, or
configuration-management tool may affect software that implements a safety
function.

Functional safety is related to software quality, reliability, availability,
maintainability, and security, but these concepts are not interchangeable:

- **Software quality** concerns whether software and its development practices
  meet relevant needs and expectations.
- **Reliability** concerns consistent operation over time and under stated conditions.
- **Availability** concerns whether a system is able to perform its required function
  when needed.
- **Maintainability** concerns how effectively a system can be restored, corrected,
  or modified.
- **Security** concerns resistance to intentional threats and unauthorized actions.
- **Functional safety** concerns freedom from *unacceptable risk* caused by incorrect
  system behavior.

Reliability, availability, maintainability, and safety are often considered together
under the acronym **RAMS**.
This terminology is particularly established in railway engineering, but it is also
used in other industries involving complex, long-lived, or safety-critical systems.
RAMS highlights the interactions and possible trade-offs among these properties.
For example, measures intended to increase availability must not prevent a system
from reaching a safe state.
In this context, safety is a broader system property. RAMS and functional
safety therefore overlap, but they are not synonymous.

These disciplines overlap.
Clear requirements, reviews, testing, traceability, controlled changes, and
well-documented limitations can support several of them.
However, strong performance in one area does not automatically demonstrate another:
reliable or highly available software is not necessarily safe, and evidence of good
general quality does not by itself demonstrate suitability for a particular
safety-related use.

### Why does this matter for LLVM?

LLVM components can play different roles in a safety-related project.
The role determines the questions that users need to answer.

| Role | Examples | Why an error matters | Typical assurance question |
| --- | --- | --- | --- |
| **Software included in the deployed product** | libc, libc++, compiler-rt, other runtime components | Incorrect behavior can directly affect the software running in the system. | *Is the selected component suitable and sufficiently verified for this defined use, configuration, and environment?* |
| **Software used to develop or verify the product** | compiler, linker, analyzer, test or coverage tool | Incorrect behavior can introduce an error into the product or fail to detect an existing error. | *Can the project rely on the tool for this defined activity, or are additional checks or qualification measures needed?* |

This distinction is important. A runtime library and a compiler may both be
LLVM components, but safety and software-assurance standards generally treat
product software and development tools differently.

- See [Qualification evidence for runtime libraries](libs/README.md) for work
  related to libc and libc++.
- See [Confidence in the use of software tools](tools/README.md) for work
  related to compilers and other development or verification tools.

## Cross-industry perspective

Safety standards reflect their industries, regulatory contexts,
and histories.
They use different terminology and do not define one universal
functional safety or qualification process.

| Standard | Main application area | How it can relate to LLVM |
| --- | --- | --- |
| **DO-178C** | Airborne software | Defines objectives for software used in airborne systems. Runtime components included in airborne software need to be addressed as product software. |
| **DO-330** | Software tools used in high-assurance development | Defines tool-qualification considerations. It applies to supporting tools under defined reliance conditions, not to runtime libraries merely because they are software. |
| **EN 50716** | Railway applications | Defines requirements for railway software development, including the treatment of software components and supporting tools within the applicable railway lifecycle. |
| **IEC 61508** | General electrical, electronic, and programmable electronic safety-related systems | Provides a cross-industry functional safety framework. LLVM runtime components may form part of safety-related software, while LLVM development tools may require confidence or qualification measures depending on how they are used. |
| **IEC 62304** | Medical-device software | Defines medical-device software lifecycle processes. Existing software for which adequate development records are unavailable may be treated as software of unknown provenance, commonly abbreviated as **SOUP**. |
| **ISO 26262** | Road vehicles | Addresses automotive safety-related software, qualification of some pre-existing software components, and confidence in the use of software tools. |

Standards also use different classifications to express the safety relevance of
software and the rigor expected from its development and verification. Examples
include Safety Integrity Levels (SILs), Automotive Safety Integrity Levels
(ASILs), medical-device software safety classes, and airborne software levels.
These classifications are not directly interchangeable.

The Working Group provides cross-industry guidance where common ground exists,
while preserving important differences among standards. Users remain
responsible for consulting the applicable standard and deciding which
requirements apply to their system and use case.

## Principles shared across safety lifecycles

Although their detailed requirements differ, the safety and
software-assurance standards considered by the Working Group often ask for
evidence of several recurring practices:

| Recurring practice | Purpose |
| --- | --- |
| **Define the scope and intended use** | Identify the software, version, selected functions, configuration, environment, and how the project will rely on it. |
| **Describe the required behavior** | Record what the software is expected to do, including assumptions, limitations, and behavior under abnormal or boundary conditions. |
| **Identify relevant risks and failures** | Consider how incorrect behavior could affect the safety-related system and what prevents or detects it. |
| **Verify the software and its integration** | Use reviews, analysis, and tests appropriate to the defined use and its safety relevance. |
| **Maintain traceability** | Keep explicit links among expected behavior, implementation, verification, results, and other supporting evidence. |
| **Control configurations and changes** | Make it possible to identify what was assessed and determine when a change requires earlier work to be repeated. |
| **Record anomalies and limitations** | Make known problems, unsupported uses, assumptions, and required user actions visible. |
| **Preserve reviewable evidence** | Retain information that another person can inspect to understand what was done, why it was considered sufficient, and where responsibility remains with the user. |

The amount of work and the required independence or rigor depend on the
applicable standard, safety classification, project context, and potential
consequences of failure.

These practices also provide a foundation for software quality more broadly.
The Working Group's [`quality`](quality/README.md) workstream examines how LLVM
applies such practices, what public evidence is available, where gaps may
remain, and how quality information can support more focused qualification
activities.

## Key terms and acronyms

The definitions below are plain-language introductions. Individual standards
may define the terms more precisely or use them differently.

| Term or acronym | Plain-language meaning |
| --- | --- |
| **ASIL — Automotive Safety Integrity Level** | An ISO 26262 classification used to express automotive safety risk and determine the rigor expected from development and verification activities. |
| **Assurance** | Justified confidence, supported by evidence, that software or an activity satisfies defined expectations. |
| **Certification** | Acceptance or approval within a defined regulatory or certification scheme. Qualification does not automatically constitute certification. |
| **Downstream user** | An organization or project that selects, configures, and integrates LLVM components into its own product or development process. |
| **Evidence** | Reviewable information such as requirements, source references, design descriptions, review records, tests, results, coverage, and anomaly reports. |
| **Functional safety** | Safety that depends on an electrical, electronic, or programmable system behaving correctly in response to its inputs and failures. |
| **OSS — Open Source Software** | Software whose source code is available under a license that permits use, study, modification, and redistribution under stated conditions. |
| **Qualification** | An assessment, supported by evidence, that a component or tool is suitable for a defined use under stated conditions. Its formal meaning and required activities vary among standards. |
| **RAMS — Reliability, Availability, Maintainability and Safety** | A lifecycle-oriented way of considering four related system properties together, particularly established in railway engineering. The properties influence one another but remain distinct; high reliability or availability alone does not demonstrate safety. |
| **Safety-related software** | Software whose correct or incorrect behavior can contribute to preventing, controlling, or causing an unsafe situation. |
| **SIL — Safety Integrity Level** | A classification used by IEC 61508 and some related standards to express the required level of risk reduction and associated rigor. Its detailed meaning is standard-specific. |
| **SOUP — Software of Unknown Provenance** | IEC 62304 terminology for certain existing software for which adequate development-process records may not be available. It does not mean that the software is necessarily unsafe. |
| **Structural coverage** | Information showing which parts of the implementation, such as statements or branches, were exercised by tests. |
| **Threat model** | A structured description of relevant assets, assumptions, trust boundaries, threats, vulnerabilities, responsibilities, and controls from a security perspective. |
| **Traceability** | Explicit, maintainable links between related information, such as a required behavior and the tests intended to verify it. |
| **Upstream** | The LLVM community and repositories where shared components are developed and reviewed. |
| **Validation** | Checking that the resulting system or software is suitable for its intended use in its actual or representative environment. |
| **Verification** | Checking that an artifact or implementation satisfies its specified requirements or other defined criteria. |

## Upstream evidence and downstream responsibility

Open-source communities can create valuable assurance inputs upstream, such as:

- clear descriptions of intended behavior and supported configurations;
- links between behavior, implementation, and tests;
- repeatable test and analysis procedures;
- test results and coverage information;
- development-process documentation; and
- information about known limitations and open issues.

Upstream artifacts can reduce duplicated work and improve LLVM for all users.
They do not determine whether a component is safe or compliant in every
possible context. A downstream user still needs to define the exact version and
usage, assess relevance and completeness, perform project- and target-specific
activities, and construct any required safety or compliance argument.

The Working Group therefore aims to provide reusable building blocks rather
than an upstream certification claim.

## Activities and initiatives

### LLVM functional safety model

The [`safety-model`](safety-model/README.md) workstream is at an early
exploratory stage. Its structure, terminology, and eventual published artifacts
have not yet been agreed.

The intended work is broader than assigning possible safety-related roles to
LLVM components. It aims to:

- describe relevant components, usage assumptions, functions, possible
  failures, safety impacts, and the extent to which users might prevent or
  detect those failures;
- relate the functional safety model to the Security Response Group's
  [trust-based threat-model proposal](https://github.com/mrragava/llvm-project/blob/ragava/threat-model-proposal/llvm/docs/ThreatModel.md),
  while preserving the purpose and responsibility of each model: the Security
  Response Group develops the security threat-model proposal, while the
  Qualification Working Group explores the functional safety perspective;
- identify where the safety and security views share assumptions, risks,
  mitigations, tests, or evidence needs, and communicate any important
  differences or conflicting conclusions; and
- derive practical insights for the LLVM community about how implementing and
  preserving good upstream practices can help manage both functional safety and
  security risks.

Examples of such practices may include making assumptions and responsibility
boundaries explicit, linking requirements or mitigations to tests, performing
robust review and automated analysis, reporting and resolving defects, and
preserving evidence that downstream integrators can inspect. The goal is to
explain the risk-management value of these practices to LLVM developers and
maintainers, not to impose an industry-specific safety or security process on
the upstream community.

### LLVM quality

The [`quality`](quality/README.md) workstream examines LLVM development
practices, quality evidence, observed defects, and changes over time. From a
qualification perspective, this information can help users understand the
upstream foundation on which component- or tool-specific arguments rely.

The following areas are at different stages of development:

| Area | Intended contribution to quality and qualification | Current status |
| --- | --- | --- |
| [Assessment of the development process](quality/process/assessment/README.md) | Evaluate LLVM's documented practices and observable evidence across areas such as governance, contribution, review, testing, security, documentation, and sustainability. The assessment can identify reusable strengths, limitations, and gaps that may affect downstream confidence. It can build on the [ELISA Lighthouse OSS assessment of LLVM](https://www.researchgate.net/publication/398600910_What_ELISA%27s_Lighthouse_OSS_Best_Practices_Reveal_About_LLVM%27s_State_of_Practice), the [comparison with other OSS best-practice frameworks](https://www.researchgate.net/publication/407070022_Comparing_ELISA_Lighthouse_OSS_SIG_Checklist_with_Existing_OSS_Best-Practice_Frameworks), and LLVM's existing [OpenSSF Best Practices passing-badge assessment](https://www.bestpractices.dev/en/projects/8273/passing). | Planned; related exploratory assessments already exist outside this repository. |
| [Defect prediction](quality/process/defects-prediction/README.md) | Explore methods for identifying code or changes that may be more likely to contain defects. Results could help prioritize review, analysis, and testing, but would not by themselves prove that an area is correct or safe. | Planned; Carlos Andrés Ramírez is expected to develop this area. |
| [Defect reports](quality/defects-reports.md) | Record defects discovered through Working Group activities and report them to the appropriate LLVM project. Findings may come from defect-prediction tools, qualification experiments, testing, analysis, or other investigations. Tracking the upstream report and resolution preserves evidence that findings were acted upon. | The reporting location exists; its detailed format and process remain to be developed. |
| [Status reports](quality/status-reports/README.md) | Potentially provide periodic summaries of quality-relevant observations, evidence, findings, trends, and Working Group activities. Such reports could help downstream users understand change over time, similar in spirit to the [LLVM Security Group Transparency Reports](https://llvm.org/docs/SecurityTransparencyReports.html). | Proposal under discussion; purpose, scope, content, ownership, and publication frequency are not yet agreed. |

### Qualification evidence for runtime libraries

This work explores upstream artifacts that can improve the quality of LLVM
runtime libraries and support downstream assurance. The current proof of
concept focuses on explicit, machine-checkable links between selected library
behaviors and the tests intended to verify them.

See [Qualification evidence for runtime libraries](libs/README.md).

### Confidence in the use of software tools

This work explores how tool developers and users can determine whether evidence
of confidence is needed for a defined tool usage, plan and perform evaluation or
qualification activities where applicable, and communicate the conditions for
appropriate use.

See [Confidence in the use of software tools](tools/README.md).

## Standards referenced

| Reference | Title |
| --- | --- |
| **DO-178C** | *Software Considerations in Airborne Systems and Equipment Certification* |
| **DO-330** | *Software Tool Qualification Considerations* |
| **EN 50716:2023** | *Railway applications - Requirements for software development* |
| **IEC 61508:2010** | *Functional safety of electrical/electronic/programmable electronic safety-related systems* |
| **IEC 62304:2006+A1:2015** | *Medical device software - Software life cycle processes* |
| **ISO 26262:2018** | *Road vehicles - Functional safety* |

Projects must determine the applicable edition and any associated regulatory,
industry, or organizational guidance.

## Repository structure

This directory is organized into the following areas.

```
fusa-qual-wg/
├── README.md                    # this file
├── meetings/                    # meeting materials, agendas, and minutes
│   ├── materials/               # meeting slide content
│   ├── minutes/                 # published agendas and minutes
│   └── img/                     # images referenced by the materials
├── tools/                       # confidence in the use of software tools
│   ├── templates/               # process templates and their guides
│   ├── workflows/               # tool-provider and tool-user workflows
│   └── examples/                # examples of application
├── quality/                     # LLVM quality activities and information
│   ├── defects-reports.md       # defect reports
│   ├── process/
│   │   ├── assessment/          # assessment of the development process
│   │   └── defects-prediction/  # defects prediction
│   └── status-reports/          # status reports
├── libs/                        # libraries qualification
└── safety-model/                # LLVM functional safety model
```

## Related public talks and papers

### Introductory resources

- **Recording:** [2025 AsiaLLVM - LLVM in the Automotive Industry: Bringing Functional Safety to Open Source](https://www.youtube.com/watch?v=wAQ1XBjXfog)
- **Slides:** [urribarri-automotive.pdf](https://llvm.org/devmtg/2025-06/slides/technical-talk/urribarri-automotive.pdf)

> [!NOTE]
> The presentation uses automotive examples. The Working Group now considers
> cross-industry needs and the standards summarized above.

### Presentations

> [!NOTE]
> Links to related presentations can be added here in the future.

### Papers

> [!NOTE]
> Links to related papers can be added here in the future.

### Requests for comments (RFCs)

- [Proposal to establish a Safety Group in LLVM](https://discourse.llvm.org/t/rfc-proposal-to-establish-a-safety-group-in-llvm/86916)
- [Collecting Community Input on Qualification of LLVM Tools & Libraries](https://discourse.llvm.org/t/rfc-collecting-community-input-on-qualification-of-llvm-tools-libraries/88569)
- [Lightweight Conformance Test Traceability for libc++](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468)
