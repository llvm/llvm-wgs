> [!NOTE]
> **Template provided by:** [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)  
> **Document identifier:** `LLVM-QUAL-TPL-005`  
> **Usage guide:** [LLVM-QUAL-TPL-005-guide.md](LLVM-QUAL-TPL-005-guide.md)
>
> This template is provided for guidance and does not replace applicable safety or assurance standards.

# Safety Manual for `<Tool_Name>`

> [!TIP]
> Text between angle brackets, such as `<Tool_Name>`, is a placeholder to be replaced with tool-specific information.
>
> Remove the instructional notes and tips when publishing a completed document.

| Document information | Value |
|---|---|
| Organization / team name | `<Owner>` |
| Version | `<X.Y>` |
| Date | `<YYYY-MM-DD>` |

> [!TIP]
> List the roles involved in this document as applicable, for example authors, reviewers, or approvers.
> Add or remove rows as needed.

| Role | Name |
|---|---|
| `<Role>` | `<Name>` |

## Purpose

This safety manual communicates the information needed to use `<Tool_Name>` within the stated boundary for safety-related development.
It identifies supported and excluded usages, required setup and operating conditions, mandatory checks, complementary measures, known issues, and responsibilities.

## Scope

### Applicable standards

`<Standard and edition>`

### Related information

| Item | Applicable information |
| --- | --- |
| Tool name | `<Tool_Name>` |
| Version, revision, build, or commit | `<Exact identifier or supported range>` |
| Distribution or source | `<Package, repository, release location, supplier, and integrity or authenticity information>` |
| User manual | `<Reference>` |
| Installation manual/Other technical manuals | `<References>` |
| Release notes | `<References>` |
| Known-issue records | `<References>` |
| Support information | `<References>` |

### Supported and excluded usages

> [!IMPORTANT]
> Do not describe a use as supported merely because the tool can technically perform it.
> State only the usages for which the necessary behavior, conditions, controls, and evidence are established.

| Item | Applicable information |
| --- | --- |
| Supported use cases | `<Supported use cases and their boundaries>` |
| Disabled, excluded, prohibited, or unsupported use cases | `<Excluded use cases and reason or applicable alternatives>` |
| Supported platforms and execution environments | `<Host, target, operating system, runtime, container, or other environment>` |
| Required dependencies | `<Libraries, runtimes, services, hardware, licenses, or other tools, including versions>` |
| Required resources | `<Processor, memory, storage, connectivity, timing, or other resource assumptions>` |
| Applicable configuration set | `<Configuration baseline, options, profiles, scripts, or reference>` |

### Supported inputs and outputs

#### Accepted inputs

`<Description of inputs and preconditions (e.g., formats, ranges, validity, provenance, other preconditions)>`

#### Expected outputs

> [!TIP]
> If needed, summarize outputs or intermediate artifacts that must not be relied upon (e.g., diagnostic-only, temporary, or stale outputs), or reference the external document listing or describing those outputs or artifacts.

`<Description of outputs (e.g., artifacts, diagnostics, status, logs, other results), permitted reliance (e.g., who or what uses the output and how it may be relied upon), and required subsequent check or control (e.g., review, test, comparison, independent verification, other controls)>`

> [!IMPORTANT]
> The following sections usually present mandatory usage conditions that users must satisfy for the stated usage or confidence boundary to remain applicable.
>
> User actions affecting installation, configuration, execution, or result handling normally originate from the prevention, detection, or correction measures identified in LLVM-QUAL-TPL-003, or from limitations, restrictions, conditions, anomalies, and unresolved findings identified in LLVM-QUAL-TPL-004.
> If needed, explain the consequences if a mandatory condition is not satisfied.

## Installation and preparation for use

### Installation, integrity, and environment checks

| ID | Required action or check | Instruction or reference | Expected result and retained evidence | Action if not satisfied |
| --- | --- | --- | --- | --- |
| `SM-INST-<ID>` | `<Obtain, install, identify, authenticate, or verify the tool or dependency>` | `<Procedure or controlled reference>` | `<Expected version, checksum, signature, status, log, or record>` | `<Do not use / Correct and repeat / Escalate / Other>` |

> [!TIP]
> If applicable, identify test suites to be rerun (e.g., installation and environment verification tests) and expected-result baseline, re-execution triggers, and action on failure>

### User competence and procedural prerequisites

| Prerequisite | Required competence, information, or authorization | How it is established or checked |
| --- | --- | --- |
| `<Role or activity>` | `<Knowledge, training, experience, reference manual, project procedure, or authorization>` | `<Review, training record, access control, supervision, or other check>` |

## Configuration

| ID | Option, parameter, profile, or item | Permitted value or rule | Restriction and reason | How to verify and record it |
| --- | --- | --- | --- | --- |
| `SM-CFG-<ID>` | `<Configuration item>` | `<Required, permitted, or prohibited value>` | `<Boundary, interaction, limitation, or source>` | `<Command, report, review, log, manifest, or other evidence>` |

## Execution

### Execution procedure and checks

| ID | Stage | Required action or check | Expected result | Action on failure or unexpected result |
| --- | --- | --- | --- | --- |
| `SM-EXEC-<ID>` | `<Before / During / After execution>` | `<Invocation, input check, monitoring, status check, or other action>` | `<Observable result>` | `<Stop, reject output, correct, repeat, investigate, or report>` |

### Diagnostics, errors, warnings, and logs

| Diagnostic, status, or event | Meaning and possible impact | Required user response | Output validity | Information to retain |
| --- | --- | --- | --- | --- |
| `<Exit status, warning class, error, timeout, crash, truncated log, or other event>` | `<Meaning, limitations, and affected processing>` | `<Required investigation, correction, repetition, or escalation>` | `<Valid / Invalid / Valid only under stated conditions / Undetermined>` | `<Log, command line, input identity, output identity, environment, or other evidence>` |

### Output acceptance, verification, and retention

| Output or result | Required acceptance or verification activity | Acceptance criteria | Required record | Conditions invalidating the result |
| --- | --- | --- | --- | --- |
| `<Output>` | `<Review, test, comparison, independent verification, or integrity check>` | `<Observable criteria or controlled reference>` | `<Evidence and retention location>` | `<Input, configuration, environment, diagnostic, tool, or process condition>` |

### Anomalous operating conditions

> [!NOTE]
> Record established behavior only.
> If behavior has not been established, say so and define a conservative user response.

> [!TIP]
> Recovery and return-to-service instructions can be procedures, required cleanups or state restoration, re-execution conditions, and checks before results may again be accepted.

| Condition | Expected or observed tool behavior | How the user can detect it | Required user response or recovery | Validity of existing and new outputs |
| --- | --- | --- | --- | --- |
| `<Invalid or unexpected input, resource exhaustion, interruption, dependency failure, unavailable service, partial failure, concurrency issue, corrupted state, or other condition>` | `<Behavior, degraded mode, safe termination, partial result, or "Not established">` | `<Diagnostic, monitoring, comparison, or symptom>` | `<Stop, reject, restore, clean, repeat, verify, or report>` | `<Validity decision and required assessment>` |

## Known issues, limitations, and workarounds

> [!TIP]
> Include adverse information relevant to the stated usage, including open issues.
> Link to the upstream issue where useful, but preserve enough version-specific information for the manual to remain understandable if that issue later changes or becomes unavailable.

| Anomaly ID | Affected baseline and scope | Behavior and possible impact | Required restriction or verified workaround | Status, fix, and controlled reference |
| --- | --- | --- | --- | --- |
| `AN-<ID>` | `<Versions, configurations, platforms, inputs, functions, or use cases>` | `<Symptom, incorrect or missing behavior, detectability, and impact>` | `<Do not use / Additional check / Workaround and its limitations>` | `<Open / Fixed in version / Accepted limitation, with issue, advisory, test, or release-note reference>` |

> [!NOTE]
> Instead of the previous table, another practice could be to reference a dedicated issue tracker or database where the tool user can consult the necessary information.

## Support and reporting

| Topic | Information |
| --- | --- |
| Requesting help or reporting an issue | `<Issue tracker, service request, mailing list, or support channel; required report contents>` |
| Reporting a security concern | `<Private reporting channel or security policy>` |
| Obtaining corrections or workarounds | `<How fixes, patched versions, and verified workarounds are communicated>` |

> [!TIP]
> Information to include in an issue report can be:
> tool version, revision, build, and source;
> platform, environment, dependencies, and resource conditions;
> complete configuration and invocation;
> input identity and a minimized reproducer where disclosure permits;
> expected and observed behavior;
> diagnostics, logs, status, and relevant outputs; and
> safety or assurance impact, urgency, and workaround already applied.

## Responsibilities and limits of responsibility

> [!IMPORTANT]
> Allocate responsibilities explicitly.
> A tool developer or provider can supply reusable information and evidence, but normally cannot determine whether every downstream usage satisfies a project's standards, safety requirements, or acceptance obligations.

| Role | Responsibilities within this manual's boundary |
| --- | --- |
| Tool developer or maintainer | `<Define and maintain the supported usage and tool baseline; provide accurate instructions and user-relevant limitations; provide any applicable installation or environment verification test suite, procedure, expected results, and covered baseline; communicate known anomalies, changes, and available corrections; maintain or reference applicable evidence>` |
| Tool user or integrator | `<Select and check the applicable version; establish project-specific suitability; comply with the stated usage and mandatory conditions; verify inputs, configuration, environment, diagnostics, and outputs; execute and retain the results of any required provider-supplied installation or environment verification tests; apply complementary measures; preserve required evidence; report relevant anomalies>` |
| Project, qualification, assurance, or approval authority | `<Determine the applicable standards and integrity level; approve the given usage, confidence or qualification strategy, deviations, and residual risk; decide whether additional evidence or controls are required>` |
| `<Additional role>` | `<Responsibilities>` |

## Validity, change management, and approval

This manual is valid only for the tool, usage, configuration, environment, assumptions, and controls identified above.

Review the manual and the underlying usage or confidence argument when any of the following changes:

- the tool version, revision, build, source, enabled feature set, or dependency;
- the intended or given use, input, processing, output, output consumer, or reliance on the output;
- the configuration, platform, execution environment, infrastructure, or resource assumption;
- an installation, execution, verification, complementary, or recovery measure;
- a known anomaly, limitation, security issue, workaround, correction, or support status relevant to the stated usage;
- the applicable standard, edition, integrity level, project process, or approval basis; or
- `<Additional project-specific trigger>`.
