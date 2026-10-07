# LLVM functional safety model

> [!NOTE]
> **Draft for discussion.**
> This is an initial model prepared for review by the LLVM Qualification Working Group, LLVM component maintainers, and the wider community.
> The examples describe *possible* uses and failure effects; they are not findings about particular releases or claims that a component is suitable for a safety-related system.
> Component boundaries, terminology, examples, and proposed upstream activities need further review.

<!--
Before a PR, reconcile the component inventory and wording against the [working spreadsheet](https://docs.google.com/spreadsheets/d/1ShQjRBoAVWmIxdLpLZQWPAiwgOsxZTwg5gkBqidiau0/edit?gid=0#gid=0), the [SRG discussion notes](https://docs.google.com/document/d/1Iqu6LIcXTVM9QUJJtYG8-m3l01FAuDaQ3UHspWxRVjw/edit?tab=t.0), and the latest revision of the threat-model proposal.
-->

## Purpose

LLVM components can appear in a safety-related project in several ways.
Some become part of the software that runs in the final system.
Others are used to implement, build, examine, test, or debug that software.
A defect in either role can matter, but the path from a defect to a possible safety effect is different.

This model makes those paths easier to discuss.
For representative LLVM components and uses, it identifies:

- the activity or function supported by the component;
- the artifact or behavior on which a user might rely;
- a plausible incorrect behavior and how it could affect a safety-related system or the evidence used to assess it;
- information, tests, and quality improvements that might be reusable upstream; and
- decisions and checks that depend on a specific downstream system.

It is intended to help contributors choose useful, manageable quality work and to help users identify questions for their own assurance activities.
The model does not assign safety classifications to LLVM projects, perform a system hazard analysis, define universal tool qualification requirements, or certify LLVM.
The relevance and rigor of any activity depend on the exact component, version, configuration, target, use, applicable standard, and system safety requirements.

The [Qualification Working Group overview](../README.md#why-does-this-matter-for-llvm) introduces the central distinction between software included in a deployed product and software used to develop or verify that product.
This document applies that distinction to specific LLVM uses.

## How to read and extend the model

### Proposing an entry

The unit of analysis is a **component in a particular use**, not an entire repository or an LLVM project in the abstract.
The same code can take more than one role.
For example, a sanitizer runtime used only during testing is part of a verification method; a runtime library linked into the deployed binary is part of the product; and a JIT embedded in that product may be both a runtime dependency and a code-generation mechanism.

Contributors can extend this shared model with a representative use of an LLVM component.
Doing so makes plausible failure paths, reusable upstream quality work, and questions for users visible to the community.
A downstream project can then use a relevant entry as a starting point for analyzing its own selected component and workflow.
The entry itself does not establish whether that use is safety-relevant in a particular system.

When proposing an entry, describe what is known and indicate which details depend on the downstream use:

1. **Identity and boundary:**
   LLVM project or subsystem, executable or library, selected features, and relevant dependencies.
   Record a version, configuration, platform, or target when the example depends on it.
2. **Use and reliance:**
   a representative input, function, output or runtime behavior, and the activity or operational function it might support.
3. **Possible malfunction:**
   an incorrect result, omitted result, misleading diagnostic, failure to detect a defect, or unexpected runtime behavior.
4. **Possible effect:**
   how that malfunction could affect deployed behavior or weaken a verification result.
   Identifying a concrete hazard requires the downstream system context.
5. **Existing and potential measures:**
   documented behavior, regression and conformance tests, independent checks, reviews, anomaly records, and other ways to prevent or detect the malfunction.
   Distinguish measures already implemented from suggestions.
6. **Responsibility and evidence:**
   what maintainers could improve or publish upstream and what users must establish for their selected version, configuration, use, and applicable standard.

The component analyses below present this information in a compact form: **Use and possible effect** describes a plausible failure path; **Potential upstream work** suggests reusable improvements; and **Downstream questions** identify decisions that require a particular project's context.

The examples are starting hypotheses rather than completed assessments, and the proposed measures have not been shown to be sufficient for a particular safety case.
New entries should be supported by the component's documentation and, where possible, reviewed with its maintainers and users.

Defects or limitations found during this work should be reported through the appropriate LLVM project channels.

### Identifying the component and its use

In the inventories below, **LLVM area** identifies the LLVM projects or code-owning subsystems involved, while **Example artifact or feature** identifies what might actually be used.
The third column describes either a possible operational role for deployed code or a possible use or output of a tool.
When a technical stage such as parsing, IR transformation, code generation, or linking helps explain a failure path, describe it in the entry or the component analysis.
Shared infrastructure such as LLVM IR, the MC layer, or MLIR should be related to the concrete tool or runtime that uses it.
The host and target, enabled options, and actual dependencies determine the boundary of any later assessment.

## Relationship to the security threat model

The LLVM Security Response Group's [trust-based threat-model proposal](https://github.com/mrragava/llvm-project/blob/ragava/threat-model-proposal/llvm/docs/ThreatModel.md) provides a useful companion view of components, uses, trust assumptions, and responsibility boundaries.
This safety model seeks compatible component names and explicit assumptions, while asking a different question: *what if a component behaves incorrectly, and how could that affect a safety-related activity or system?*
An error can arise without an adversary.
Conversely, an intentional attack or an untrusted input can expose a defect that also has a safety effect.

The two analyses can share component boundaries, input and output descriptions, known limitations, tests, and defect reports.
Their scenarios and conclusions should remain distinguishable.
A security boundary does not establish that a component is safe for every use, and a safety-oriented test does not establish a security guarantee.
The Security Response Group develops its threat model; the Qualification Working Group develops this functional safety perspective.
Where the models disagree about a component or an assumption, the groups should discuss and record the difference rather than silently harmonizing it.

<!-- 
> [!NOTE]
> The [discussion notes for the Security Response Group](https://docs.google.com/document/d/1Iqu6LIcXTVM9QUJJtYG8-m3l01FAuDaQ3UHspWxRVjw/edit?tab=t.0) and the [initial safety-model spreadsheet](https://docs.google.com/spreadsheets/d/1ShQjRBoAVWmIxdLpLZQWPAiwgOsxZTwg5gkBqidiau0/edit?gid=0#gid=0) are working inputs for joint review. Neither companion draft should be interpreted here as an adopted LLVM policy.
--> 

## Possible uses in safety-related work

The first table gives a broad view of where LLVM components might be used in a project's work.
The two inventories that follow identify examples of deployed components and development or verification tools.
These are possible uses: no project is assumed to use every component, and inclusion in a table alone does not trigger *qualification*.

### Illustrative lifecycle activities

The activity families below help locate a possible use without prescribing the stages or terminology of a particular safety standard.
For an actual use, identify the project task, the output or behavior relied upon, and the applicable standard's expectations for that task.

| Illustrative activity family | Possible LLVM involvement |
| --- | --- |
| Requirements | No general mapping for the components currently listed. |
| Architecture design | No general mapping for the components currently listed. A defined MLIR pipeline might transform a design representation, but that use must be described specifically. |
| Software implementation and code generation | Clang, Flang, defined MLIR pipelines, LLVM IR transformations, and target code generation produce or transform implementation artifacts. |
| Build and software integration | The Clang driver, `llvm-ar`, LLD, `llvm-objcopy`, and BOLT may assemble, link, or modify artifacts at different points in the build. |
| Static examination of implementation | Clang Static Analyzer and selected `clang-tidy` checks may support code review or defect detection. |
| Test execution, defect discovery, and investigation | Sanitizers, libFuzzer, `lit`, `FileCheck`, and LLDB may support defined test or investigation workflows. |
| Assessment of test results | `llvm-profdata` and `llvm-cov` may support coverage assessment; `lit` and `FileCheck` may contribute test results when the project uses them for that purpose. |

A component may support more than one activity.
The operational role of code deployed in the product is shown in the next table, separately from development and verification activities.

### Libraries and other deployed components

These components may be linked into or loaded by the final software.
If their behavior contributes to a safety function, a defect can affect that function directly.
The user needs to consider the selected functionality in its actual configuration and operating environment.
This is the *product software* role described in the [WG overview](../README.md#why-does-this-matter-for-llvm).
The table identifies example deployable artifacts and the runtime functions they might provide; the actual role depends on what the delivered system includes and uses.

| LLVM area | Example artifact or feature | Possible operational role |
| --- | --- | --- |
| `compiler-rt` | Builtins and atomics | Low-level arithmetic or atomic operations emitted by a compiler and linked into the program. |
| `flang-rt` | Fortran runtime | Runtime support for a deployed application compiled with Flang. |
| `libc` | Selected C library functions | Memory, string, mathematical, I/O, or other C functionality used by the deployed program. |
| `libcxx` | Selected libc++ facilities | Containers, algorithms, strings, atomics, or other C++ functionality used by the deployed program. |
| `libcxxabi` and `libunwind` | ABI and unwinding facilities | Exception handling, runtime type information, and unwinding when enabled and used. |
| `llvm` and `orc-rt` | Embedded ORC JIT and runtime support | Generation, linking, and execution of code during operation, if a deployed product embeds a JIT. |
| `openmp` | Host and offload runtimes | Task scheduling, synchronization, and offload execution if the product uses OpenMP. |

> [!NOTE]
> Other LLVM runtimes, including device libraries, should be added when an actual use and owner are identified.
> Whether any library is present in the *deployed* system must be checked against the delivered binary or image; a source-level dependency name alone does not settle that question.

### Software used to develop or verify the product

These tools usually do not run in the delivered product.
Their outputs can nevertheless introduce a defect into it or fail to expose an existing one.
The relevant question is how a project relies on the tool for a particular activity and what other checks examine its output.
The WG's [tool-confidence guidance](../tools/README.md) explores that question in more detail.
The table identifies example tools and what they can do or produce; the earlier activity table shows where those functions might support project work.
Where a tool has several uses, analyze each reliance on its outputs separately.

| LLVM area | Example artifact or feature | Possible tool use or output |
| --- | --- | --- |
| `bolt` | `llvm-bolt` | Transform an already linked binary when post-link optimization is enabled. |
| `clang` | C-family front-end and driver | Parse and analyze supported C-family source code; produce diagnostics and LLVM IR. The driver coordinates code generation, assembly, and linking to produce object files or executables. |
| `clang`, `llvm`, `compiler-rt` | Sanitizer instrumentation and testing runtimes | Expose selected defects during instrumented tests. |
| `clang-tools-extra` and Clang analysis | `clang-tidy`, Static Analyzer | Detect selected coding errors or rule violations; support reviews. |
| `compiler-rt` | libFuzzer | Explore selected interfaces through coverage-guided fuzzing. |
| `flang` | Fortran compiler | Parse, lower, and compile Fortran source used by a safety-related application. |
| `lld` | Linker | Resolve symbols and relocations; combine objects and libraries into a loadable image. |
| `lldb` | Debugger | Examine program state while debugging or investigating a failure. |
| `llvm` | `lit`, `FileCheck` | Execute tests and check their expected results. |
| `llvm` | `llvm-objcopy`, `llvm-ar`, and related tools | Package, archive, or modify binary artifacts in a build or release flow. |
| `llvm` | `llvm-profdata`, `llvm-cov` | Process profile data and report test coverage. |
| `llvm` | Optimizer, code generator, assembler, and target backend | Transform IR and generate machine code for a specified target. |
| `mlir` | Dialects and passes used in a defined pipeline | Represent, transform, or lower a domain-specific design or program. |

`clangd` or an editor integration may help implementation, but its mere presence in a developer's IDE does not establish reliance on it for a required verification activity. Similarly, an internal LLVM framework becomes relevant through a concrete tool or runtime that uses it.

## Component-level analysis for libraries

The cases below deliberately distinguish an example failure from a known defect.
Suggested upstream work is an *opportunity*, not a claim that a given test or document already exists or that it would be sufficient downstream.

### `libc`

#### Use and possible effect

A deployed program may call a selected C library function.
Incorrect results, missed boundary conditions, or an unexpected implementation-dependent behavior could change application state or an output used by a safety function.

#### Potential upstream work

- Document behavior and supported configurations for selected functions;
- connect those behaviors to conformance and regression tests;
- examine boundary cases and target differences;
- record known anomalies.

#### Downstream questions

- *Which functions and build are present?*
- *What are the target and environment?*
- *Which assumptions and failure effects matter, and what integration tests or independent checks are required?*

### `libcxx`

#### Use and possible effect

A deployed C++ application may rely on a container, algorithm, string, atomic, or other selected facility.
A wrong result, synchronization error, or unexpected handling of a boundary case could propagate into application behavior.

#### Potential upstream work

- Make selected behavior descriptions and their links to tests more explicit;
- keep those links current as the implementation and supported C++ versions evolve;
- test relevant configurations and targets.

> [!TIP]
> The WG's [libc++ traceability RFC](https://discourse.llvm.org/t/rfc-lightweight-conformance-test-traceability-for-libc/91468) is one possible small experiment.

#### Downstream questions
- *Which APIs, language mode, ABI configuration, hardening settings, and target are selected?*
- *Are exceptions or threading facilities used, and how are the chosen behaviors checked in the final system?*

### `libcxxabi` and `libunwind`

#### Use and possible effect
Where exception handling or unwinding is enabled, ABI or unwind support can affect control flow, cleanup, and the state observed after a failure.
An incompatible or incorrect implementation could prevent expected recovery or cause a different program result.

#### Potential upstream work

- Describe supported ABI and unwinding combinations, add cross-component and cross-target tests, and make relevant limitations visible.
- Treat `libcxxabi` and `libunwind` as distinct artifacts when their functions or configurations call for distinct analyses.

#### Downstream questions

- *Are these libraries actually linked, and is unwinding permitted in the safety-related software?*
- *Which compiler, linker, ABI, target, and exception-handling configurations are used?*

### `compiler-rt` builtins and atomics

#### Use and possible effect

A compiler may emit calls to low-level builtins or atomic routines.
These functions can be present even when source code never calls them explicitly.
An incorrect implementation could affect arithmetic results or concurrency behavior at runtime.

#### Potential upstream work

- Document target-specific implementations and selection rules;
- test edge values and ABI conventions;
- exercise the path from code generation to the linked runtime on relevant targets.

#### Downstream questions

- *Which builtins are actually pulled into the image?*
- *Are the selected compiler runtime and target configuration compatible, and how are their observable effects verified?*

### OpenMP runtimes

#### Use and possible effect
An application using OpenMP may include its host runtime and, if offloading is used, target-side support.
A scheduling, synchronization, or offload error could affect deployed behavior.

#### Potential upstream work

- Keep host, target, and offload runtime boundaries explicit;
- test representative feature combinations and abnormal conditions;
- record supported targets and known limitations.

#### Downstream questions

- *Does the delivered system use these runtimes, and are parallel or offload facilities within the safety-related scope?*
- *Which timing, target, device, and failure-handling assumptions apply?*

### Flang runtime

#### Use and possible effect

A deployed Fortran application may rely on Flang runtime functions for operations such as array handling and I/O.
Incorrect results or an unexpected runtime failure could affect the application even if compilation of its source was correct.

#### Potential upstream work

- Describe selected runtime interfaces and supported configurations;
- test behavior across the Flang compiler/runtime boundary and on relevant targets.

#### Downstream questions

- *Which runtime functions are present, under which I/O and target environment, and how is the application's use verified?*

### ORC JIT and runtime support, when embedded

#### Use and possible effect

A deployed system that compiles or links code at runtime relies on the JIT path as part of its operational software.
A wrong translation or symbol resolution could affect the code it executes.
If ORC is used only in a development or test tool, analyze that separate use under the tools section instead.

#### Potential upstream work

- Document the supported execution boundary and assumptions;
- test compilation, linking, resource management, and target cases relevant to the selected configuration.

#### Downstream questions

- *What code is accepted?*
- *When and where does it run?*
- *Which inputs can change?*
- *How are generated code and its operational effects constrained and verified?*

## Component-level analysis for software tools

For each tool, the given use matters as much as the tool's name.
The possible failure paths below should be refined for a selected workflow before applying the WG's [tool-confidence templates](../tools/README.md).

### Clang front end and driver

#### Use and possible effect

Clang may preprocess, parse, diagnose, and lower source or drive compilation and linking.
Incorrect translation or a missed diagnostic may introduce a defect or let one remain.
A diagnostic matters to tool confidence only when the project relies on it for a defined activity.

#### Potential upstream work

- Add reproducible regression cases for language semantics, options, and diagnostics;
- connect critical behavior to tests or other verifications;
- make support limits and interactions among options clearer.

#### Downstream questions

- *Which language, version, flags, target, and build pipeline are used?*
- *What independently checks generated behavior or the specific diagnostics on which the project relies?*

### LLVM IR transformations, code generation, and target backend

#### Use and possible effect

Passes and backend code generate or transform code used in the product.
A wrong optimization, instruction selection, calling convention, or target-specific output can alter behavior while leaving the source unchanged.

#### Potential upstream work

- Preserve minimized regression tests for reported miscompilations, recording affected versions, targets, options, and fixes;
- run differential, end-to-end, and target-specific tests where practical, and identify gaps in their coverage;
- where applicable, use formal methods tools such as Alive2 to check proposed LLVM IR transformations and selected optimization passes, recording findings, timeouts, and unsupported cases;
- explore translation validation for selected backend code-generation paths as a separate, target-specific effort, documenting its assumptions and limitations.

#### Downstream questions

- *Which passes, optimization level, architecture, ABI, and generated artifacts are in scope?*
- *What tests exercise behavior on the intended target, including interactions with linked runtimes?*

### LLD

#### Use and possible effect

`lld` combines objects and libraries into a linked image.
An incorrect relocation, section layout, or symbol resolution could change the delivered program even if each input object was correct.

#### Potential upstream work

- Exercise target formats, relocations, linker scripts, and tool options with focused regression and end-to-end tests;
- preserve examples of failures and their affected configurations.

#### Downstream questions

- *Which linker, version, target format, scripts, and options are in the build?*
- *What checks cover the image's memory layout, symbols, startup behavior, and executable identity?*

### BOLT

#### Use and possible effect

`llvm-bolt` can transform a binary after linking.
An incorrect transformation could change control flow or target behavior in the delivered image.
This is a separate activity from linking.

#### Potential upstream work

- Test representative transformations, architectures, and profiles;
- preserve regression cases with affected configurations and a way to compare original and transformed behavior.

#### Downstream questions

- *Is BOLT used on the delivered binary?*
- *Which transformations and profiles are applied, and which verification runs on the final transformed image?*

### Binary utilities such as `llvm-objcopy` and `llvm-ar`

#### Use and possible effect

A utility may edit sections, package objects, or select archive members.
A wrong edit or missing object could affect a delivered artifact or the evidence about its identity.

#### Potential upstream work

- Test selected binary formats and options, including unexpected inputs and object combinations;
- document the exact transformations these commands perform.

#### Downstream questions

- *Which commands run at each stage of the build and release process?*
- *How is the resulting artifact inspected and identified?*

### Flang compiler

#### Use and possible effect

Flang lowers Fortran source through its own representations and LLVM infrastructure.
A wrong parse, lowering, or compiler/runtime interface can change a deployed program's behavior.

#### Potential upstream work

- Add source-to-result and compiler/runtime regression tests;
- document supported language features and targets.

#### Downstream questions

- *Which Fortran features, compiler options, runtime, and target are used?*
- *What checks verify the resulting program?*

### MLIR-based transformations

#### Use and possible effect

MLIR representations, dialects, and passes can be used in a specific compilation or model-lowering pipeline.
A wrong transformation can change the generated result.
'MLIR' alone is too broad to be a single user-facing tool assessment.

#### Potential upstream work

- Identify concrete dialects, passes, and pipeline boundaries;
- add tests that check transformations and interactions between representations.

#### Downstream questions

- *Which dialects, passes, and integration code are in the selected pipeline?*
- *What checks the behavior of the final generated artifact, including integration owned outside the LLVM project?*

### Clang analysis and `clang-tidy`

#### Use and possible effect

A project may use the Clang Static Analyzer or selected `clang-tidy` checks to find bugs or rule violations.
A false negative, disabled check, incorrect configuration, or a finding ignored by the process can leave a defect undetected.
These tools do not establish compliance with an entire coding standard merely by being run.

#### Potential upstream work

- Specify what individual checks detect;
- test known positive and negative cases;
- document language and configuration limits;
- keep regressions from reported misses.

#### Downstream questions

- *Which checks, source files, configurations, and versions are used?*
- *How are findings reviewed, and which other techniques address cases outside the checks' capabilities?*

### Sanitizer instrumentation and testing runtimes

#### Use and possible effect

Instrumentation and testing runtimes can expose selected runtime defects.
A missed instrumentation point, incorrect runtime report, or an untested target can create an unjustified belief that a property has been checked.
An instrumented binary usually has a different configuration from the delivered one.

#### Potential upstream work

- Test detection of representative known defects and expected failures;
- document supported configurations, incompatibilities, and blind spots;
- preserve reproducible cases for missed reports.

#### Downstream questions

- *What property is being tested, under which instrumented configuration and workload?*
- *Which tests and complementary methods address behavior that these techniques cannot observe?*

### libFuzzer

#### Use and possible effect

A project may use libFuzzer to search for failures in a selected interface.
A weak harness, restricted input space, or a misleading stopping criterion can leave important behavior untested; the absence of a finding is not proof that the target is defect free.

#### Potential upstream work

- Document harness assumptions and preserve reproducers for discovered defects;
- improve repeatability and coverage of the relevant interfaces.

#### Downstream questions

- *What is the fuzz target, input model, oracle, corpus, configuration, and duration?*
- *What other verification covers the remaining safety-related behavior?*

### `llvm-profdata` and `llvm-cov`

#### Use and possible effect

Projects may rely on profile processing and coverage reports when assessing tests.
Lost counters, mismatched binaries and profiles, or an incorrectly interpreted coverage metric can overstate what tests exercised.
Coverage is evidence about execution, not evidence by itself that a test checked the right behavior.

#### Potential upstream work

- Test report correctness on controlled programs, including mismatches and edge cases;
- make instrumentation and profile assumptions clear;
- retain regression tests for wrong or misleading reports.

#### Downstream questions

- *Do the binary, sources, and profile correspond to one controlled configuration?*
- *Which coverage criterion applies, how are uncovered regions assessed, and are test assertions adequate?*

### `lit` and `FileCheck`

#### Use and possible effect

`lit` runs tests and summarizes results; `FileCheck` checks specified text patterns.
A wrongly configured test or weak pattern can pass without checking the intended property.

#### Potential upstream work

- Test failure detection, test discovery, and result reporting;
- favor assertions that cover intended behavior rather than incidental output.

#### Downstream questions

- *What conclusion is drawn from each result?*
- *Have expected-failure, skipped, unsupported, and stale tests been handled?*
- *Are test assertions sufficient for the claim made from their results?*

### LLDB

#### Use and possible effect

A debugger can help investigate failures or observe state.
Incorrect or incomplete debug information, target support, or display behavior can mislead an investigation if the result is accepted without corroboration.

#### Potential upstream work

- Test representative target and debug-info combinations;
- document known limitations of inspected values.

#### Downstream questions

- *Is debugger output used to make a safety-relevant decision, or only to guide further testing?*
- *How are key observations checked against independent program behavior or other evidence?*

## From the model to practical upstream work

The model should lead to proposals with a clear benefit for LLVM users generally.
Candidate activities include:

- documenting selected, reviewable behaviors and supported configurations;
- keeping links from behavior or a known failure mode to the tests that exercise it, initially for a small selected scope;
- adding cross-component and target-aware regression tests for failures that unit tests alone can miss;
- making test limitations and diagnostic blind spots visible;
- reporting defects in the affected LLVM project, keeping minimal reproducers, and recording affected versions and resolutions; and
- preserving repeatable procedures and reviewable results that downstream users can reuse as inputs to their own work.

A maintainer may choose a small improvement because it helps correctness, diagnostics, or maintainability for everyone.
A downstream project decides whether that improvement supplies relevant evidence for its own safety argument.
Neither this model nor an upstream quality activity transfers the project's responsibility for system-level analysis, integration, testing, configuration control, and applicable compliance decisions.

## Questions for community review

1. *Do the LLVM area, example artifact or feature, and described use reflect the relevant LLVM components and workflows? Which boundaries or names need correction?*
2. *Which examples represent current "real" safety-related uses, and which should be narrowed or removed? Can users provide a concrete, shareable workflow?*
3. *Where should a component be split because a single project contains both deployable code and supporting tools, or because it has several distinct output uses?*
4. *Which prevention or detection measures already exist, and which are realistic proposals? What evidence can the community maintain over time?*
5. *Which assumptions and component boundaries should be shared with the Security Response Group's threat-model proposal? Where do the analyses need intentionally different conclusions?*
6. *What is the smallest component and use case suitable for a first, maintainer-reviewed worked example?*

## Working references

- [LLVM Qualification Working Group overview](../README.md)
- [Initial functional safety model spreadsheet](https://docs.google.com/spreadsheets/d/1ShQjRBoAVWmIxdLpLZQWPAiwgOsxZTwg5gkBqidiau0/edit?gid=0#gid=0)
- [Security Response Group threat-model proposal](https://github.com/mrragava/llvm-project/blob/ragava/threat-model-proposal/llvm/docs/ThreatModel.md)
- [LLVM component overview](https://llvm.org/), [Clang toolchain](https://clang.llvm.org/docs/Toolchain.html), [LLVM testing guide](https://llvm.org/docs/TestingGuide.html), and [OpenMP runtimes](https://openmp.llvm.org/design/Runtimes.html)
