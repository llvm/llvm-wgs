# Guide to LLVM-QUAL-TPL-004 — Tool Qualification Report

> [!NOTE]
> **Guidance provided by:** [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)  
> **Related template:** `LLVM-QUAL-TPL-004`  
> This guide set is informative.
> It does not replace the applicable safety or assurance standard, regulatory or certification guidance, a documented interpretation, or an organization's own processes.

## Purpose and boundary of TPL-004

LLVM-QUAL-TPL-004 records the execution and results of qualification activities defined in one Tool Usage Plan.
It integrates the resulting evidence, findings, limitations, and conditions into a bounded, standard-specific qualification conclusion.

TPL-004 is not another qualification plan.
It should not repeat:

- the intended or given tool usage and usage boundary;
- the selected qualification approaches and rationale;
- planned objectives, responsibilities, independence, or work products;
- planned procedures, coverage strategy, or acceptance criteria;
- the classification and malfunction analysis; or
- the planned change-management strategy.

Those items remain in TPL-002, TPL-003, and any plans or procedures referenced by them.
TPL-004 records what actually happened and whether the defined objectives and criteria were satisfied.

The report is not a substitute for the underlying evidence.
It summarizes, references, and integrates controlled requirements, tests, execution records, process assessments, service-history analyses, certificates, findings, reviews, and other evidence without copying every artifact into one document.

The report does not establish universal suitability, certify the tool, or demonstrate compliance with an entire standard.
It supports a conclusion only for the defined boundary.
Any additional review, assessment, approval, or certification process depends on the applicable standard and the needs of the organization or team using the template.

## Guide-set structure

TPL-004 guidance is divided into three files:

1. **This central guide** explains the workflow boundary, use of the Tool Usage Plan, completion of the streamlined template, evidence integration, findings, conclusions, reuse, maintenance, and review checklist.
2. The [qualification-approaches companion](LLVM-QUAL-TPL-004-qualification-approaches-guide.md) explains validation, service-history analysis, development-process evaluation, development under a safety or assurance standard, output verification and diversity, certification, and evidence reuse.
3. The [standards and test-coverage companion](LLVM-QUAL-TPL-004-standards-guide.md) explains what qualification or tool confidence means under IEC 61508, EN 50716, ISO 26262, IEC 62304, and DO-178C/DO-330; compares their approaches; and explains requirements/behavior and structural-coverage expectations.

Start with this guide.
Consult only the companion sections relevant to the applicable standard and selected qualification activities.

## Following the Tool Usage Plan and handling changes

### Default: follow the plan

One TPL-004 report is governed by one referenced TPL-002 revision.
That revision defines the tool version and usage boundary addressed by the report.
If another TPL-002 applies to a different tool version or usage boundary, prepare a separate TPL-004 report.
TPL-004 should also identify the corresponding TPL-003 revision.
Use references precise enough to identify the versions on which the report is based; a changing branch or undated web page may not be sufficient.

Hence, the streamlined template assumes that the qualification activities conform to the single referenced TPL-002 revision.
It therefore uses references instead of repeating planned content.

Before recording the results, check that the following remain consistent with that plan:

- tool usage and scope;
- qualification approaches and standard-specific basis;
- objectives and acceptance criteria;
- responsibilities and independence arrangements;
- procedures, coverage strategies, and evaluation criteria;
- assumptions, constraints, and required controls; and
- planned evidence and work products.

If all remain unchanged, proceed directly to recording the execution and results.

### When the plan needs to change

If the team decides that a planned element needs to change, update TPL-002 before continuing the affected qualification activity or establishing the qualification conclusion.
Review or approval of that update can follow the organization's or team's normal process.

- Update TPL-002 when the usage, approach, scope, objective, responsibility, procedure, evidence, or acceptance strategy changes.
- Update TPL-003 when the classification boundary or result, malfunction analysis, confidence in controls, required controls, or resulting qualification need changes.

TPL-004 then references the updated revision and, where available, the associated change record.
It does not restate the revised plan.

### When execution differs from the plan

An unexpected execution deviation is something that occurred while attempting to perform the planned activity, for example:

- a required test could not be executed;
- the actual environment differed from the planned environment;
- an assessment sample or observation period was incomplete;
- an expected independent reviewer was unavailable;
- a procedure step was omitted or performed differently; or
- an evidence source was unavailable or had changed.

Do not rewrite the plan retroactively to make the execution appear conformant.
Record the deviation and its impact in the activity record.
Then either:

1. correct the condition and re-execute the affected work according to the plan; or
2. update the plan and determine which work needs to be repeated or extended.

A qualification conclusion should not rely on an unresolved contradiction between the plan and the recorded execution.

## Meaning and limits of qualification

Software-tool qualification is the structured application of the approaches and evidence required by the applicable standard to justify confidence or obtain credit for a defined tool usage and assurance context.

“Tool X is qualified” is normally too broad.
A defensible conclusion is bounded by the defined usage, tool and evidence baseline, functions and outputs, environment, integrity or software level, assumptions, restrictions, and mandatory controls.

The standards do not all use the same qualification concept.
In particular, IEC 62304 (medical device software) does not define a comparable development-tool qualification framework, while DO-178C/DO-330 (airborne systems) focuses on project-specific certification credit and a TQL-dependent objective set.
Consult the [standard-by-standard explanations](LLVM-QUAL-TPL-004-standards-guide.md#meaning-of-tool-qualification-or-confidence-under-each-standard) before choosing report terminology.

### Qualification is not certification (and vice-versa)

Certification is third-party attestation under a defined conformity-assessment scheme.
Its underlying assessment can include process audit, product validation, lifecycle-compliance review, service history, or a combination.

The certificate's qualification value depends on what was assessed, what the attestation claims, and whether its scope matches the current use.
IEC 61508 (E/E/PE systems) gives certified tools and translators an explicit technique/measure role, but this does not make every certificate sufficient for every use.

See the detailed chapter on [certification and its relationship with qualification](LLVM-QUAL-TPL-004-qualification-approaches-guide.md#certification-and-its-relationship-with-qualification).

### Qualification is not ordinary product testing

Regression or conformance testing can contribute important evidence, but a qualification report also asks whether:

- expected behaviors relevant to the qualified use were defined;
- test scope is traceable to the defined objectives and TPL-003 concerns;
- expected results and test oracles are trustworthy;
- the actual environment is representative of the planned environment;
- invalid, unusual, boundary, and other error-related conditions are addressed;
- failures, skipped tests, discrepancies, and limitations are retained and dispositioned; and
- the execution and evidence baseline can be reproduced and reviewed.

Structural coverage of the tool's code is not a universal tool-validation requirement.
Requirements or behavior coverage also does not by itself demonstrate adequate validation.
See the [test-coverage chapter](LLVM-QUAL-TPL-004-standards-guide.md#test-coverage-expectations-for-software-tools).

### Standards terminology in plain language

Safety and assurance standards sometimes use **anomaly** as a broad term for a condition, behavior, result, or documentation item that differs from what is expected.
Software developers and maintainers may describe the same thing more specifically as a bug, regression, crash, incorrect output, missing diagnostic, test failure, known issue, or limitation.

An anomaly can be an observation that still needs investigation.
It does not automatically mean that a defect or its root cause has already been confirmed.

This guide uses the most specific familiar term available.
It retains **anomaly** when explaining a standard or when the nature of an observed issue has not yet been determined.
In particular:

- a **known anomaly** can usually be read as a known issue, defect, unexpected behavior, or documented limitation; and
- **anomaly handling** normally means recording, investigating, tracking, and resolving or otherwise addressing such issues.

**Anomalous operating conditions** has a different meaning.
It refers to conditions outside the ordinary successful-use path, not necessarily to a bug in the tool.
Examples include malformed or invalid input, boundary values, unsupported options, missing or corrupted files, unavailable dependencies, resource exhaustion, interrupted external services, and unexpected environmental conditions.

The standards companion may retain _anomaly_ or _anomalous operating conditions_ where that wording helps preserve the connection to a particular standard.

## Completing the template

### Identification and inputs

Identify the single TPL-002 revision governing the report and the corresponding TPL-003 revision.
Use a revision, commit, release, date, or other reference that lets a reader find the intended document rather than only naming a changing branch.

The tool version is optional in TPL-004 because TPL-002 is the main source for the tool identity and baseline.
Repeating it in TPL-004 can still be convenient for readers, provided the information remains consistent with TPL-002.

Use **Qualification perspective** to explain who is preparing the report, such as an upstream project, tool provider, distributor, integrator, or project-specific user.
This helps readers understand which evidence and conclusions are within that contributor's knowledge and control.

The role table is intentionally flexible.
List authors, reviewers, approvers, or other roles only where they are useful.
TPL-004 does not require document status, approval, or sign-off fields; an organization or team can add those fields according to its own process and the applicable standard.

### Qualification activity summary

For each activity:

- use the activity name from the plan;
- reference the planned activity or applicable TPL-002 section; and
- state its current status or final result.

If TPL-002 assigns unique identifiers to qualification activities, preserve them.
Otherwise assign a report identifier such as `QMA-01` and reference the corresponding TPL-002 section unambiguously.

### Evidence inventory and applicability

Assign a stable `QE` identifier to every evidence item used by the report.
Identify an immutable version, revision, commit, report date, execution ID, or equivalent controlled baseline.

The applicability field is a documented gap analysis.
Compare the evidence context with the current qualification boundary, including:

- exact tool or component identity;
- covered functions, outputs, objectives, and malfunction concerns;
- host, target, dependencies, configuration, and execution environment;
- use cases, inputs, options, output reliance, and downstream controls;
- applicable integrity or software level and TQL where relevant;
- assumptions, restrictions, known issues, and validity conditions; and
- evidence provenance, review, maintenance, and availability.

Classify reused evidence as fully applicable, partially applicable with stated gaps, or not applicable.
A partial match can support a bounded portion of the argument, but it requires additional activity, restriction, or delta qualification for the uncovered part.

### Coverage and findings

Trace the objectives and TPL-003 concerns to the activities and evidence that address them.
Record whether each is covered, partially covered, not covered, or not applicable, with a rationale and residual action.

Review cross-activity dependencies and common-cause weaknesses.
Several activities can appear independent while relying on the same incomplete requirement, incorrect oracle, shared parser, generated harness, infrastructure, data source, or reviewer assumption.

Record adverse evidence, including:

- unexpected tool behavior and incorrect outputs;
- test or expected-result discrepancies;
- process or review findings;
- service-history data gaps;
- certificate or evidence-reuse mismatches;
- execution deviations; and
- unresolved qualification questions.

Use a `QF` identifier when it is useful to link the same issue or finding from an activity, the coverage summary, and the qualification conclusion.
`QF` means **Qualification Finding** and is an identifier provided by this template, not terminology required by the standards.

For an open finding, record enough information to understand its impact, rationale, planned follow-up or compensating measure, current status, and supporting evidence.
Add an owner or decision authority where the team's process needs one.

### Standard-specific qualification conclusions

Complete a separate conclusion for each applicable standard.
Shared evidence does not make different standards or qualification levels equivalent.

Each conclusion should identify or reference:

- completed activities and principal evidence;
- the requirements or interpretation mapping used for completeness;
- the conclusion and its rationale;
- mandatory conditions, limitations, exclusions, and unresolved items.

The conclusion remains bounded by the TPL-002 and TPL-003 references and by the validity statement in the report.
If the applicable standard, certification context, organization, or team requires confirmation, independent assessment, approval, or authority coordination, record that information in the evidence inventory or in additional fields chosen by the template user.

For DO-178C/DO-330, distinguish the certification credit claimed from the applicable DO-330 qualification objectives.
A vendor certificate or existing qualification package does not by itself grant project certification credit.

### Detailed qualification activity results

Copy one complete result chapter for each qualification activity.
Reference the TPL-002 content and record only execution-specific information:

- actual performers, reviewers, independence, and dates;
- the execution or assessment environment;
- execution deviations and their disposition;
- results, achieved coverage, gaps, discrepancies, and findings;
- applicability of reused evidence or third-party assessment;
- detailed evidence references;
- assessment against the acceptance criteria; and
- limitations, dependent controls, and follow-up.

The activity result is not automatically the overall qualification conclusion.
An activity can pass while another required activity fails, an objective remains uncovered, or an assumption is not satisfied.

The [qualification-approaches companion](LLVM-QUAL-TPL-004-qualification-approaches-guide.md) provides activity-specific interpretation and review questions.

### Validity and user information

Reference the change and re-evaluation conditions defined in the plan.
Record only additional triggers or limitations discovered through the qualification results.

Transfer user-relevant conditions into a safety manual such as TPL-005, or into other suitable user documentation.
This can include supported baselines, mandatory configuration checks, required downstream verification, known issues, workarounds, unsupported uses, and conditions invalidating the evidence.

## Qualification perspectives and evidence layering

An upstream project can provide reusable source identity, documentation, behavior descriptions, regression tests, CI definitions and retained results, contribution and release practices, issue records, and bounded generic analyses.
It often cannot know the final target, options, integrity level, output reliance, integration environment, or downstream controls.

A tool provider or distributor can stabilize source and binary baselines, add controlled builds and documentation, execute validation on defined platforms, assess processes, and maintain a qualification support package.
Patches, backports, configuration, packaging, and rebuilding can create differences from upstream evidence that require analysis.

An integrator or project-specific user normally confirms the actual installation, use cases, target, dependencies, integrity level, output reliance, downstream verification, and any organizational review or sign-off needs.

A qualification service or certification body can perform validation, process assessment, or certification.
Where relevant, record its role, independence, scheme or criteria, scope, evidence access, result, and limitations.

A scalable pattern is a generic upstream or provider evidence package plus a downstream applicability addendum.
The addendum preserves every assumption and restriction of the reusable package and closes the project-specific gaps.

## Change impact and delta qualification

Qualification evidence is configuration-dependent.
When a tool, usage, environment, control, standard, or evidence package changes, perform a change impact analysis before reusing the previous conclusion.

Classify evidence and activities as:

- unaffected and reusable with rationale;
- affected but reusable after confirmation;
- requiring partial repetition or extension;
- invalid for the changed boundary; or
- requiring investigation before disposition.

Delta qualification is not merely rerunning the most convenient tests.
It is a reasoned selection of affected requirements, functions, configurations, malfunction concerns, evidence sources, activities, and user conditions.

## Illustrative compiler qualification structure

For a bounded compiler usage, the plan might select validation and independent output verification.
TPL-004 would then record, by reference rather than restating the strategy:

1. the defined tool usage, such as language subset, compiler options, target, environment, and output reliance;
2. the corresponding TPL-003 code-generation and diagnostic concerns;
3. the exact compiler build, validation suite, harness, target, and execution campaign actually used;
4. validation results, requirements/behavior and problem-space coverage, skipped or failed cases, and observed issues;
5. execution and results of the independent output-verification activity;
6. applicability of upstream tests, certificates, prior reports, or other reused evidence;
7. integrated coverage of the defined objectives and TPL-003 concerns; and
8. a bounded conclusion with required options, checks, restrictions, known issues, and change triggers.

## Review and completeness checklist

Before considering the report complete, check that:

- [ ] the single TPL-002 revision and corresponding TPL-003 revision are identified;
- [ ] the recorded activities and results are consistent with TPL-002;
- [ ] plan changes were made before the affected activity continued or the conclusion was established, and were reviewed or approved if the team's process requires it;
- [ ] unexpected execution deviations remain visible and are resolved or dispositioned;
- [ ] every qualification activity has an execution and result record;
- [ ] the evidence and execution context are identifiable and reviewable;
- [ ] reused evidence has a documented applicability assessment;
- [ ] acceptance criteria were defined before interpreting results;
- [ ] achieved coverage, gaps, skipped work, and adverse evidence are visible;
- [ ] findings and common-cause dependencies are assessed;
- [ ] objectives and TPL-003 concerns are traced to activities, evidence, and conclusions;
- [ ] conclusions are stated separately for each applicable standard;
- [ ] the conclusion does not exceed the boundary defined by TPL-002 and TPL-003;
- [ ] mandatory conditions and known issues are passed to a safety manual or other suitable user documentation;
- [ ] any review, assessment, approval, sign-off, or authority coordination required by the applicable context is complete; and
- [ ] report-specific validity limitations and additional re-evaluation triggers are identified.
