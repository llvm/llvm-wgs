# Qualification evidence for runtime libraries

This document introduces the functional safety considerations that can apply to LLVM runtime libraries such as libc and libc++.
It then describes exploratory work on lightweight behavior-to-test traceability.

Readers who are new to functional safety may wish to start with the [Working Group overview](../README.md), which explains the main concepts and terms used here and provides a cross-industry view of the relevant standards.

## What does functional safety mean for a runtime library?

As explained in the [Working Group overview](../README.md#why-does-this-matter-for-llvm), a runtime library such as libc or libc++ becomes part of the software executing in the deployed product.
Application code may call its functions for memory handling, algorithms, mathematical operations, containers, input and output, or other basic services.
Incorrect library behavior can therefore affect the behavior of safety-related software.

> [!NOTE]
> This differs from a compiler, test framework, or other development tool.
> A tool supports the creation or verification of the product; a runtime library becomes part of the product software itself.
> The two cases require different kinds of functional safety analysis and evidence.

In this documentation, *library qualification* is a convenient shorthand for the activities and evidence used to justify that a precisely identified library scope is suitable for a defined safety-related use.
It does not mean that an entire upstream library is universally qualified for every project, target, or safety standard.

The general division between reusable upstream evidence and project-specific downstream responsibility is described in [Upstream evidence and downstream responsibility](../README.md#upstream-evidence-and-downstream-responsibility).
This document focuses on how that distinction applies to runtime libraries.

The LLVM Qualification Working Group explores upstream artifacts that can:

- improve the quality and maintainability of LLVM libraries;
- make their behavior and verification easier to understand;
- reduce duplicated evidence-building work among downstream users; and
- support, but not replace, project-specific qualification or certification activities.

## What may a downstream project need to demonstrate?

The [principles shared across safety lifecycles](../README.md#principles-shared-across-safety-lifecycles) apply to runtime libraries through a defined library scope (including defined configuration and environment) and its supporting evidence.
The exact expectations depend on the industry, standard, safety classification, intended use, and evidence already available.

The project normally starts by defining a bounded scope:

- the library and exact version or revision;
- the selected functions or components;
- the build options and relevant configuration;
- the compiler, target architecture, operating environment, and other dependencies;
- the expected behavior, inputs, assumptions, and limitations; and
- how the surrounding software will use and check the library behavior.

Relevant evidence may then include:

- descriptions of the expected behavior and their authoritative sources;
- assumptions, preconditions, unsupported cases, and usage constraints;
- information about the design and implementation;
- explicit links from expected behavior to implementation and tests;
- tests derived from the expected behavior, together with their results;
- structural coverage, meaning information about which statements, branches, or other parts of the implementation were exercised by tests;
- known anomalies and their impact on the intended use;
- configuration, version, change, and problem-management information; and
- evidence that the library works correctly when integrated into the target system.

Some of this information can be created, reviewed, and maintained upstream.
Target-specific test execution, coverage analysis, system safety analysis, integration evidence, and the final compliance argument remain downstream responsibilities.

## How do standards approach existing libraries?

The [cross-industry overview](../README.md#cross-industry-perspective) introduces the standards and terminology considered by the Working Group.
The table below focuses specifically on how an existing runtime library may be treated under those standards.
It is an orientation, not a substitute for the applicable standard.

| Standard | How an existing runtime library may be approached | What a project may need to show |
| --- | --- | --- |
| **IEC 61508-3** | The library may be treated as a software element incorporated into safety-related software. The necessary rigor depends on its role, the safety functions, the applicable Safety Integrity Level (SIL), how the software was developed, and the available evidence. | Defined requirements and assumptions, suitable architecture and design information, verification through reviews and tests, integration and safety-validation evidence, traceability, controlled versions and changes, and justification that the selected element is suitable for its use. |
| **EN 50716** | A library used in railway software needs to be addressed within the applicable railway software lifecycle, including the project's treatment of reused or pre-existing software. | A defined component and usage scope, requirements, design and implementation evidence, component and integration testing, verification and validation, configuration and change control, problem reporting, and management of assumptions and limitations. |
| **ISO 26262** | An off-the-shelf library may be considered for software-component qualification under ISO 26262-8, Clause 12, when its conditions apply. The project must also address its integration through the applicable software-development activities in ISO 26262-6. | Identification of the component, version, use cases, target environment, requirements, tests and coverage, known anomalies, configuration and changes, integration evidence, and the component's role in the automotive safety argument. |
| **IEC 62304** | A library may be treated as software of unknown provenance (**SOUP**) when adequate records of its development process are unavailable. This does not mean that the software is necessarily unsafe; it means the medical-device manufacturer must manage the resulting uncertainty through its lifecycle and risk-management activities. | Identification of the exact SOUP item, functional and performance expectations, architectural integration, risk controls, evaluation of known anomalies, integration and system tests, configuration management, maintenance, and problem resolution. |
| **DO-178C / DO-330** | A runtime library included in airborne software is part of the product software and is addressed through the applicable DO-178C objectives. DO-330 concerns supporting development and verification tools; it is not the basis for qualifying a runtime library merely because the library is software. | Requirements, design and code information as applicable, links among those artifacts, reviews and analysis, tests for expected, boundary, and abnormal conditions, structural coverage, configuration management, quality assurance, problem reporting, and integration evidence. A checker used in this methodology would be considered separately as a tool if a project relied on its output without an adequate independent check. |

Applying the [principles shared across safety lifecycles](../README.md#principles-shared-across-safety-lifecycles) to a runtime library raises several practical questions:

1. _**What exactly is being assessed?**_
   Identify the version, configuration, target, selected APIs, and excluded behavior.
2. _**What should it do?**_
   Record clear, reviewable descriptions of the expected behavior, assumptions, preconditions, and source references.
3. _**How do we know it was tested?**_
   Link each selected behavior to suitable tests and review whether their assertions actually check that behavior.
4. _**Which implementation paths were exercised?**_
   Gather the coverage required by the downstream context and examine code that was not exercised.
5. _**What limitations remain?**_
   Track anomalies, unsupported configurations, and any additional measures required from users.
6. _**How is the evidence kept current?**_
   Control versions and changes, and repeat relevant reviews, analyses, or tests when the library or its usage changes.

## Behavior-to-test traceability

Behavior-to-test traceability creates explicit links between a documented library behavior and the test code intended to verify it.
For example, a behavior might state that a function returns an iterator to the end of an output range, while an annotation identifies the particular assertion that checks the returned iterator.

Without these links, the relationship may exist only in test names, comments, reviewer knowledge, or private downstream documentation.
It becomes harder to answer questions such as:

- *Which test claims to verify this behavior?*
- *Is every documented behavior linked to at least one test?*
- *Did a change leave an invalid or outdated mapping?*
- *Can a downstream user reuse the mapping rather than reconstructing it?*

Traceability is useful, but limited.
A valid link does not prove that:

- the behavior description is correct or complete;
- the selected test adequately verifies it;
- the test builds or executes successfully on a particular target;
- the tests achieve the required structural coverage; or
- the library conforms to a standard or is qualified or certified.

Those conclusions require additional human review, test execution, analysis, and project-specific evidence.

### Proposed upstream methodology

An [initial concept](https://docs.google.com/presentation/d/1-JpF6kMbth1hL0ZkwRyHQ9A7edqd2vwM3U7Y9QcfQfI/edit?slide=id.g3acb06ff9f7_2_258#slide=id.g3acb06ff9f7_2_258) discussed by the Working Group in December 2025 explored how qualification evidence could be created incrementally at function level.
The concept considered behavioral requirements, design representations, traceability, tests, coverage, and supporting validation scripts.
Function-level scope was proposed because a library function can provide a relatively small unit for review and gradual expansion.

The subsequent [RFC](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468) and proofs of concept [for libc++](https://github.com/petbernt/llvm-project/blob/libcxx_qual_poc/libcxx/behavior/README.md) and [for libc](https://github.com/petbernt/llvm-project/blob/libc_qual_poc/libc/behavior/README.md) deliberately focus on one part of that larger problem: lightweight behavior-to-test traceability.
This narrower scope allows LLVM maintainers and contributors to evaluate its ordinary software-quality value and maintenance cost before considering wider qualification artifacts.

The current approach creates the following relationship:

> Authoritative source or documented LLVM choice -> behavior ID -> test source location or test case

It uses:

- short, original descriptions of observable behavior that help reviewers but do not replace an authoritative specification;
- stable behavior IDs and explicit source references;
- `// @verifies <behavior-id>` annotations close to relevant assertions or helper blocks in libc++, or immediately before recognized `TEST`-style declarations in libc; and
- a source-level checker that detects duplicate IDs, annotations that refer to unknown IDs, documented behaviors with no mapped test, an empty behavior inventory, and other inconsistencies supported by each proof of concept.

The libc PoC maps behaviors to named test cases provided by its unit-test framework.
libc++ conformance tests are generally identified by file in [lit](https://llvm.org/docs/CommandGuide/lit.html), so its PoC uses annotation locations to distinguish checks within a file.

The checker can run locally or through an optional CMake target in continuous integration (CI).
It checks the consistency of the source-level links without building the library or executing its tests.
Reviewers still assess the source interpretation, behavior description, and adequacy of the mapped assertions.

The checkers extract behavior IDs from YAML text; they do not validate YAML syntax or a metadata schema.
The metadata model and schema validation remain future work.

### Value upstream and downstream

| Value for LLVM contributors and maintainers | Value for downstream assurance |
| --- | --- |
| Makes the intent of selected tests explicit and reviewable. | Provides behavior-to-test mappings already reviewed with the upstream code. |
| Identifies documented behavior with no mapped test. | Reduces the need for each user to reconstruct the same mapping privately. |
| Detects invalid references as descriptions and tests change. | Provides an input to testing, coverage analysis, and a project-specific assurance argument. |
| Supports gradual adoption for selected APIs without requiring a whole-library backfill. | Makes changes in the upstream behavior and tests easier to identify and reassess. |
| Can expose unclear descriptions, weak assertions, and test gaps. | Leaves the user responsible for scope, target execution, coverage, integration, safety analysis, and compliance conclusions. |

The proposal can be useful beyond functional safety.
Clear descriptions and explicit test intent can also support general software quality, maintenance, onboarding, and security-related assurance activities.

## Materials and open questions

- [Initial function-based qualification concept (December 2025)](https://docs.google.com/presentation/d/1-JpF6kMbth1hL0ZkwRyHQ9A7edqd2vwM3U7Y9QcfQfI/edit?slide=id.g3acb06ff9f7_2_258#slide=id.g3acb06ff9f7_2_258)
- [RFC: Lightweight Conformance Test Traceability for libc++](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468)
- [libc++ proof of concept and instructions](https://github.com/petbernt/llvm-project/blob/libcxx_qual_poc/libcxx/behavior/README.md)
- [libc proof of concept and instructions](https://github.com/petbernt/llvm-project/blob/libc_qual_poc/libc/behavior/README.md)

The RFC is exploratory.
It asks whether the mechanism is useful, practical, and maintainable upstream, and what the smallest useful experiment should contain.
Open questions include:

- who creates and reviews the behavior descriptions;
- how descriptions evolve across language-standard versions;
- the appropriate metadata structure and location;
- the annotation style and checker behavior; and
- whether and how the check should eventually run in CI.

<!--
## Runtime Libraries Workshop discussion (2026 US LLVM Developers' Meeting)

** Lightweight Conformance Test Traceability for LLVM Runtime Libraries**

We would like to discuss a lightweight approach to making the intent of selected libc++ conformance tests explicit and machine-checkable.
Using a small proof of concept and an accompanying RFC, we will introduce atomic behavior descriptions with stable IDs, `@verifies` annotations linking behavior to tests, a checker for mapping consistency, and proposed metadata-schema validation.

The mechanism could provide reusable behavior-to-test traceability and software-quality infrastructure for LLVM runtime libraries, while potentially also supporting security and functional-safety use cases.
We seek feedback on whether the approach would be useful, practical, and maintainable upstream; what the smallest viable experiment should include; how it might apply to other runtimes; and whether optional AI-assisted workflows could reduce mechanical effort while retaining maintainer review.

The planned session uses a short demonstration followed by discussion.
The proof-of-concept documentation provides the walkthrough and commands for trying the mechanism.

The current instructions identify metadata-schema validation as future work.
The discussion should therefore distinguish the behavior-ID mapping checks already implemented from schema validation that is still proposed.
-->

## Scope and limitations

This work does not:

- qualify or certify libc, libc++, or another LLVM component;
- replace the applicable functional safety standard or project lifecycle;
- claim that a successful mapping check demonstrates semantic correctness, conformance to a language or safety standard, test execution, or adequate structural coverage;
- require all runtime-library behavior or tests to adopt the mechanism; or
- transfer responsibility for the downstream product, integration, safety argument, qualification, or certification to the LLVM community.

The initial work is intentionally optional and incremental.
Expansion should depend on feedback from library maintainers, contributors, downstream users, and reviewers from the relevant assurance domains.
