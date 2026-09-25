# Guide to LLVM-QUAL-TPL-005 — Safety Manual

> [!NOTE]
> **Guidance provided by:** [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)  
> **Related template:** `LLVM-QUAL-TPL-005`  
> This guide is informative.
> It does not replace the applicable safety or assurance standard, regulatory or certification guidance, an approved interpretation, or an organization's safety processes.

## Purpose and boundary of TPL-005

LLVM-QUAL-TPL-005 communicates the information that tool users need in order to use a tool within a stated boundary and, where applicable, keep the usage within its confidence or qualification boundary.
It brings together the supported scope, instructions, mandatory conditions, complementary measures, known issues, and responsibility boundaries that must remain visible during real use of the tool for safety-related development.

The completed safety manual should answer practical questions such as:

- Which exact tool versions, functions, environments, inputs, outputs, and usages does this information cover?
- What must a user check before, during, and after execution?
- Which configurations or usages are required, restricted, or prohibited?
- Which reviews, tests, comparisons, or other measures remain outside the tool?
- What happens under invalid input, resource exhaustion, interruption, or partial failure?
- Which known anomalies affect the usage, and what must the user do about them?
- How are malfunctions, fixes, and changes reported and communicated?
- Which responsibilities belong to the developer or provider, user or integrator?

TPL-005 is user information.
It is not a second Tool Usage Plan, Tool Classification Report, or Tool Qualification Report.
It should communicate their user-relevant results without reproducing their complete planning, analysis, evidence, and approval records.

A project may publish the completed content under another clear title, such as *Safety-Related Usage Guide* or *Tool Usage in Safety-Critical Contexts*.

Keep the completed manual proportionate to the tool and usage.
If preferred, reference existing controlled installation, configuration, and user documentation rather than copying it.
Even a short manual should make the complete usage boundary, mandatory conditions, issues, and responsibility boundaries easy to find.

## Position in the LLVM tool-confidence workflow

TPL-005 may be useful whether or not qualification was required.
TPL-002 may plan user-facing documentation and complementary measures independently of the selected qualification strategy.
TPL-003 can identify restrictions and controls that must be communicated even when they reduce or remove a qualification need.
TPL-004 can add conditions, issues, and change triggers discovered while executing qualification activities.

Where these approved work products exist, derive the manual from their current controlled revisions.
If a proposed manual statement conflicts with the approved usage, classification, malfunction analysis, qualification scope, or conditions, update and approve the affected upstream work product first.
Do not silently repair an inconsistency only in TPL-005.

## Authors, users, and levels of reuse

### Tool developer, maintainer, or provider perspective

An upstream project, supplier, or tool maintainer can use TPL-005 to publish reusable information for intended usages of the tool.
This is particularly useful for a general-purpose tool, such as a compiler, analyzer, test tool, or traceability tool, whose provider cannot see each downstream system or project.

The provider can define:

- supported tool baselines, functions, environments, and use cases;
- installation, configuration, and execution instructions;
- known behavior and limits;
- mandatory conditions attached to supplied evidence;
- known anomalies and available corrections; and
- the evidence and support information that the provider actually maintains.

The provider normally cannot decide whether a downstream usage is suitable for a specific system, safety requirement, integrity level, jurisdiction, or approval process.
The manual should explain this boundary technically and factually; it should not use legal or defensive wording to transfer every responsibility to the user.

### Tool user or integrator perspective

A downstream project can use TPL-005 to turn developer information and its own tool-confidence work into project-specific instructions.
The resulting manual can identify the exact given usage, selected build, local configuration, project procedures, complementary measures, evidence-retention rules, and approval responsibilities.

The project-specific manual may reference the upstream manual rather than copy it, but it must preserve the exact upstream revision used and make any added or changed project conditions clear.

### Layered use

For an open-source tool, a practical structure is often:

1. an upstream manual describing a reusable intended-use boundary and known tool information;
2. a qualification or confidence package whose conditions are reflected in that manual; and
3. a downstream supplement describing the exact project usage and controls.

Each layer should state what it covers, what it assumes, and which responsibilities remain for the next layer.

## Write instructions that users can apply

### Separate mandatory, recommended, and explanatory content

Users need to know which statements are conditions of the stated boundary.
Use the following wording consistently:

| Wording | Meaning |
| --- | --- |
| **must** | Mandatory for the stated usage, confidence, qualification, or approval boundary |
| **must not** | Prohibited within that boundary |
| **should** | Recommended practice; a deviation does not automatically invalidate the stated boundary |
| **may** | Permitted option or possibility |

If an organization requires *shall* instead of *must*, use it consistently and define it.
Avoid ambiguous expressions such as *normally*, *where possible*, *as appropriate*, or *use with care* unless the manual also states who decides, using which criteria, and what evidence is retained.

### Make every mandatory condition verifiable

A usable condition identifies:

- what must be done or avoided;
- the tool version, function, option, input, output, environment, or use case to which it applies;
- when it applies;
- how the user confirms compliance; and
- why it is required and where it came from.

For example, *Use a supported configuration* is not sufficiently specific.
Identify the permitted option set or controlled configuration reference and the command, manifest, review, or log used to confirm it.

### Distinguish tool behavior from user action

For an anomalous condition, record separately:

1. established tool behavior;
2. how the user detects the condition;
3. the required response or recovery; and
4. the validity of outputs produced before, during, or after the condition.

Do not promise fail-safe, deterministic, complete, or diagnosable behavior unless evidence supports the statement.
If behavior is unknown or only partly characterized, say so and define a conservative user response, such as rejecting affected outputs and repeating the activity after the environment is restored.

### Use stable, version-specific references

The manual may link to source repositories, issue trackers, online manuals, release notes, test results, or qualification evidence.
Record enough identity to recover the applicable information later, such as a release, tag, commit, document revision, issue state and date, or archived evidence reference.

A link to a changing branch, an undated web page, a transient CI dashboard, or the current state of an issue tracker is not by itself a controlled baseline.

## Preparing the manual

### Collect the inputs

Before writing, identify the applicable:

- approved Tool Usage Plan and usage boundary;
- Tool Classification Report, malfunction concerns, and controls;
- Tool Qualification Report, conditions, findings, and conclusion;
- tool or operational requirements;
- installation, configuration, administration, and user documentation;
- supported platform and dependency information;
- release notes, issue records, advisories, and corrected versions;
- test, validation, service-history, or other supporting evidence;
- project procedures and complementary verification measures; and
- support, security-reporting, and change-notification channels.

Some of these inputs may not exist or may not be available to an upstream maintainer.
State that limitation instead of inventing or implying evidence.

### Extract user-relevant information

For each input, ask:

- Does this constrain the tool version, feature, input, output, configuration, environment, or use case?
- Does it require a user action before, during, or after execution?
- Does it require another review, test, comparison, or tool outside the tool?
- Does it affect the validity or permitted reliance on an output?
- Does it reveal an anomaly, workaround, prohibited use, or re-evaluation trigger?
- Does a downstream user need it to reproduce or audit the usage?

Transfer these items into the relevant detailed section.

### Resolve and trace the information

To make it easier to be referenced later, assign stable condition and anomaly identifiers.
If considered useful, trace a condition to the qualification finding, classification concern, requirement, test result, project decision, or other source that justifies it.
Trace project evidence back to the exact tool and manual baseline.

Do not turn every recommendation in a user manual into a safety-related condition.
Conversely, do not downgrade a qualification condition to optional advice because it is inconvenient for users.

## Completing the template

### Purpose and scope

State why the manual exists, who should use it, and which assurance contexts it supports.

Identify the exact tool version, build, revision, commit, or permitted range.
If a range is used, explain how users determine that a particular release is covered and how changes within the range are assessed.

Describe only the supported use cases or feature subset, and operating context.
Separate:

- what the tool can do;
- what the supplied information and evidence cover; and
- what the user is permitted to rely upon.

For each use case, identify accepted inputs, expected outputs, intended output consumers, permitted reliance, and subsequent controls.
Inputs may need format, range, provenance, integrity, completeness, language-subset, or project-approval checks.
Outputs may include generated artifacts, modified files, reports, diagnostics, logs, metadata, and status values.
If preferred, reference the document and section that includes the information (e.g., Tool Usage Plan).

### Installation and preparation

Provide or reference reproducible instructions to obtain and install the exact tool and dependencies.
Address, as applicable:

- authentic source and package identity;
- checksums, signatures, or other integrity checks;
- supported hosts, targets, runtimes, containers, and services;
- dependency and license versions;
- required processor, memory, storage, connectivity, permissions, and timing;
- installation self-tests or smoke tests; and
- evidence that the correct installation was selected for the activity.

Competence requirements should name the knowledge or procedure needed for the assigned task.
*Use by qualified personnel* is not useful unless the manual explains what competence is relevant and how the project establishes it.

### Configuration, execution, and result handling

Identify mandatory and prohibited options, permitted ranges, interactions, and defaults.
Defaults can change between releases or depend on the target and environment; require users to resolve and record them when they affect the stated boundary.

Execution instructions should include observable checks, not only example commands.
Consider:

- input and environment validation;
- configuration confirmation;
- invocation and sequencing;
- monitoring, exit status, diagnostics, warnings, logs, and timeouts;
- concurrent or incremental operation;
- cleanup and repeated execution;
- output identity, completeness, integrity, and traceability; and
- evidence to retain for reproduction or audit.

Explain which outputs require review, tests, comparisons, independent verification, or other acceptance measures before use.
An independent check must be sufficiently independent of the tool and failure being controlled; a second invocation using the same input, configuration, and implementation may only repeat the same error.

### Mandatory conditions and complementary measures

A complementary measure is performed outside the tool to prevent, detect, correct, or limit the effect of tool malfunction.
Examples include:

- independent review of generated or modified artifacts;
- requirements-based testing of the resulting software;
- comparison with another implementation or method;
- validation of inputs and independent checking of configuration;
- review of diagnostics and investigation of warnings;
- output-integrity and reproducibility checks; and
- restriction to a verified language, feature, target, or option subset.

Do not list a measure without explaining which usage or concern it addresses, when it is performed, and how completion is confirmed.
Ensure it remains consistent with TPL-003: a control credited when classifying the tool must be implemented with the independence, coverage, timing, and evidence assumed by that analysis.

### Anomalous operating conditions

Consider conditions such as:

- malformed, incomplete, inconsistent, unsupported, or unexpectedly large inputs;
- invalid, conflicting, or unavailable configuration;
- insufficient memory, storage, processor time, permissions, or connectivity;
- interruption, timeout, crash, restart, or partial execution;
- unavailable or incompatible dependency or external service;
- corrupted cache, state, database, intermediate artifact, or output;
- concurrency, nondeterminism, race, or ordering effects;
- truncated, suppressed, duplicated, or misleading diagnostics; and
- failure during cleanup, recovery, or incremental processing.

State whether pre-existing outputs, partial outputs, and outputs from a repeated execution remain valid.
Identify required cleanup, restoration, and checks before the tool returns to service.

### Known issues, limitations, and workarounds

Include relevant adverse information rather than reporting only favorable behavior.
For each issue, identify the affected versions and scope, symptom, potential effect, detectability, required restriction or workaround, and fix or status.

A workaround should be verified for the stated boundary.
Record its own limitations and configuration.
If no verified workaround exists, state that the affected usage is excluded or that output validity is undetermined.

The issue tracker can support current investigation and collaboration, but the manual should retain enough information to remain understandable after the issue is edited, closed, moved, or deleted.

### Support and reporting

Identify the applicable service channel if any, supported versions, response arrangements, and correction process.
For an open-source tool, state what the community actually provides: for example an issue tracker, mailing list, release notes, security policy, and maintained release branches.
Do not imply a response time, long-term-support period, or service-level commitment that does not exist.

Ask for the information needed to reproduce and assess a malfunction while respecting security, confidentiality, privacy, and disclosure restrictions.
Provide a private route for suspected security vulnerabilities when one exists.

### Responsibilities

Responsibility should follow control and knowledge.
A developer can maintain the upstream baseline and communicate supported use, evidence, issues, and changes.
A user or integrator controls the selected release, given use, inputs, configuration, project environment, complementary measures, and output reliance.
A project or approval authority determines the applicable standards, integrity level, evidence obligations, deviations, and acceptance decision.

Do not hard-code all planning, evaluation, and qualification responsibility onto the tool developer.
An upstream developer may prepare reusable inputs, but the downstream organization normally remains responsible for showing that they apply to its given usage and approval context.

### Validity and maintenance

Map each manual revision to the covered tool baseline.
Review the manual when the tool, usage, configuration, environment, dependencies, controls, anomaly state, support status, or approval basis changes.

Change impact should consider more than edited text.
Determine whether an existing instruction or condition remains correct, needs a new verification, invalidates previous outputs, or requires the usage, classification, or qualification work products to be revisited.

## Illustrative compiler-oriented conditions

The following examples show the desired form.
They are not claims about any particular LLVM component and must not be copied without supporting evidence.

| Weak statement | More usable statement pattern |
| --- | --- |
| Use the correct compiler. | Before each controlled build, the user must record the compiler version and build identifier and compare them with the baseline in the manual. A mismatch places the build outside this manual's boundary. |
| Use supported options. | The user must invoke the compiler through configuration profile `<ID>`. Any option not resolved by that profile must be reviewed against the permitted-option list before the output is accepted. |
| Check compiler warnings. | The user must retain all diagnostics and disposition each diagnostic in classes `<classes>` according to procedure `<reference>` before accepting the build output. |
| Verify the output. | The generated output must undergo `<named review, test, or comparison>` with acceptance criteria `<reference>` before it is used by `<consumer>`. |
| Do not use output after failure. | If execution returns `<status or symptom>`, all output and intermediate artifacts from that invocation must be treated as invalid, the workspace must be restored using `<procedure>`, and the activity must be repeated. |

Useful compiler-specific topics can include the language and extension subset, preprocessor behavior, optimization level, target triple, code-generation options, linker and library baseline, diagnostics policy, generated-code verification, build reproducibility, and known miscompilations.
Include only the topics applicable to the defined use case and available evidence.

## Review and completeness checklist

Before publication or approval, confirm that:

- [ ] the manual's purpose is clear;
- [ ] exact tool and manual baselines are identified and mapped to one another;
- [ ] supported use cases/features, environments, configurations, inputs, outputs, and reliance are bounded;
- [ ] excluded and prohibited usages are explicit;
- [ ] installation, integrity, dependency, resource, and competence prerequisites are actionable;
- [ ] configuration defaults, restrictions, and interactions are addressed;
- [ ] execution, diagnostics, warning, failure, and output-validity checks are defined;
- [ ] required output acceptance and complementary measures are specific and evidenced;
- [ ] every mandatory condition is visible, verifiable, and traced to its source;
- [ ] anomalous operating conditions distinguish established tool behavior, detection, required response, recovery, and output validity;
- [ ] open issues and adverse evidence remain visible;
- [ ] workarounds are verified for the stated boundary and their limitations are recorded;
- [ ] support, malfunction reporting, security reporting, correction, and change-notification information reflects what is actually available;
- [ ] developer or maintainer, user or integrator, and approval responsibilities are technically and fairly allocated;
- [ ] statements do not overclaim qualification, certification, reliability, or whole-standard compliance;
- [ ] online references are versioned or accompanied by enough controlled identity to remain reviewable;
- [ ] the manual is consistent with approved TPL-002, TPL-003, and TPL-004 revisions, where applicable; and
- [ ] validity, review, migration, and change-impact conditions are identified.
