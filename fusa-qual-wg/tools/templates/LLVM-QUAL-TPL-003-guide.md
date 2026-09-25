# How to Use LLVM-QUAL-TPL-003
## Tool Classification Report

## Purpose

LLVM-QUAL-TPL-003 supports the classification of a software tool for one or more defined usages under an applicable functional safety standard.
The classification is supported by a structured analysis of:

- the defined tool use case;
- its inputs, processing, outputs, and intended reliance;
- credible tool malfunctions or erroneous behavior;
- the potential effects of those malfunctions;
- prevention and detection measures or controls; and
- the evidence and assumptions supporting confidence in those measures or controls.

The factual analysis is intentionally standard-neutral.
The final classification is expressed using the concepts and levels defined by each applicable standard.

The template records the classification that determines or informs subsequent confidence-building, qualification, usage-control, and user-information activities.

## Why the artifact is called a classification report

In this template, **evaluation by analysis** is the activity and **classification** is its documented result.

The term *tool classification* is used as a standard-neutral umbrella for determining the category or confidence level applicable to a defined tool usage:

- Under IEC 61508 and EN 50716, the analysis assigns the applicable software tool class, commonly expressed as T1, T2, or T3.
- Under ISO 26262, the analysis determines Tool Impact (TI), Tool Error Detection (TD), and the resulting Tool Confidence Level (TCL) as TCL1, TCL2, or TCL3.
- Under another standard, the result is expressed using that standard's own scheme.

These schemes overlap in purpose but are not directly equivalent.
Do not translate one standard's result into another standard's result without performing the analysis required by the second standard.

Always record the exact standard and edition used.
If an organization (e.g., downstream) has an approved interpretation, tailoring, or procedure for classification, reference it explicitly.

## Fundamental principle: classify the usage

A classification applies to a defined tool usage, not necessarily to the tool universally.

The same tool can:

- generate an artifact that contributes to executable software in one use case;
- support verification in another use case;
- produce informational output that is completely and independently checked in a third use case; and
- exercise different features, configurations, or processing paths in each case.

Those uses can have different malfunctions, effects, measures or controls, and classification results.
Therefore, classify each use case or each group of sufficiently similar use cases before deriving an overall result where the applicable standard or process requires one.

### Generic tool-developer classification

A tool developer may classify defined intended usages for a bounded set of versions, configurations, features, inputs, outputs, and assumed downstream controls.
Where the developer does not know the final project context, assumptions should be explicit and reasonably conservative.

A generic report should not claim that one result covers every possible use of the tool.
It should identify excluded uses and explain the limits of reuse.

### Project-specific user or integrator classification

A tool user or integrator may classify a given usage in a specific project.
A developer's existing classification can be used as an input, but the user should confirm that:

- the tool identity and configuration match;
- the project use case is within the developer's scope;
- the integrity level and safety context are compatible;
- the assumed prevention and detection controls are implemented; and
- the output is not relied upon more strongly than the developer assumed.

A narrower project use may support a more specific conclusion than a generic developer analysis, but the difference should be justified rather than assumed.

## What this analysis is — and is not

The recommended method is a qualitative, use-case-based malfunction-and-effect analysis.
It is **FMEA-like**, but it is not intended to be a complete product or process FMEA.

The useful analytical chain is:

> Defined use case → potential (credible) malfunction → potential effect → error propagation → measures or controls → standard-specific classification → follow-up action

TPL-003 should identify behavior relevant to the defined usage and the consequences of erroneous results.
Investigation of internal root causes, component-level verification coverage, development-process evidence, or qualification-test completeness normally belongs to the qualification strategy and TPL-004.

## Use TPL-002 as the classification basis

TPL-003 should not repeat an inventory of classification inputs.
Reference the applicable controlled revision of TPL-002, which should identify the tool and its usage-planning basis, including relevant supporting information and evidence sources.

Within TPL-003:

- cite a source only where it supports a specific malfunction, control, or classification rationale;
- record a classification-specific clarification or additional assumption in the affected use-case chapter;
- update TPL-002 when the clarification changes the intended or given usage, its assumptions, constraints, or configuration; and
- mark the corresponding classification result as undetermined when necessary information is unavailable rather than introducing an optimistic assumption.

This separation reduces conflicting copies of the same information and allows tool or usage-plan changes to be maintained in one place.

## Characterize each use case before analyzing malfunctions

Every use-case chapter begins by establishing a clear boundary:

> Inputs → processing → outputs → consumers and reliance → subsequent measures or controls

This is an analysis-focused characterization, not a second usage specification.
Reference the corresponding use case in TPL-002 and include only the details needed to understand the malfunctions, effects, controls, and classification rationale.

### Description and objective

Describe what the user is trying to accomplish, not merely the name of the tool command.
A useful description identifies the supported lifecycle activity, task, decision, or work product.

### Inputs

Identify the information supplied to the tool, including relevant:

- source artifacts and data;
- command-line options or API parameters;
- configuration files;
- environment variables or external state;
- target and host information;
- models, rules, plugins, libraries, databases, or other dependencies; and
- previous tool outputs used as new inputs.

Record assumptions concerning validity, completeness, format, provenance, allowed values, and permitted combinations.

### Processing

Describe the externally meaningful transformation, analysis, generation, verification, or decision.
The processing description should be detailed enough to identify different types of erroneous behavior, but it does not normally need to expose the tool's internal architecture.

### Outputs and intended reliance

Identify every relevant output, including:

- generated or modified artifacts;
- executable code or data;
- diagnostics and warnings;
- pass/fail, accept/reject, or gating results;
- reports and measurements;
- traceability information;
- logs, status codes, and metadata; and
- information used by another person or automated tool to make a decision.

For each output, identify its consumer and how strongly the consumer relies on it.
An informational output interpreted by a competent user may have a different effect path from an output that automatically releases, rejects, or transforms a safety-related artifact.

### Subsequent controls

Describe reviews, tests, comparisons, independent calculations, redundant tools, consistency checks, or other measures applied before the output is relied upon.
Avoid vague statements such as “the result is tested later”.
Identify what is checked, by what means, when, and against which acceptance criteria.

## Select the analysis granularity per use case

The template supports two granularities.
A single report may combine them.

| Granularity | Analysis unit | Use when |
| --- | --- | --- |
| Use-case level | The complete use case | The use case is fairly simple; its complexity is sufficiently low, so potential effects, controls, and expected classification per subfunction are sufficiently homogeneous |
| Function or feature level | Relevant functions or features within the use case | Different functions can malfunction differently, produce different outputs, use different processing paths, or be covered by different controls |

### Use-case-level analysis

Use-case-level analysis is appropriate when treating the use as one unit does not hide a materially different malfunction, effect, reliance path, control, or classification result.

Use-case level does not mean that only one malfunction is considered.
Identify and analyze as many credible malfunctions as are needed to support the classification of the complete use case.

This is not a shortcut that requires less rigor.
The report should state why the use case is an adequate analysis boundary.

### Function or feature-level analysis

Decompose a use case when one or more of the following apply:

- the use case exercises materially different functions;
- it produces several outputs used for different purposes;
- it includes both generation and verification behavior;
- different configurations or processing paths lead to different effects;
- some outputs are independently verified while others are trusted;
- a particular feature has different known limitations or controls;
- the high-level analysis produces a classification that is difficult to justify; or
- separate classifications could be meaningful because the functions and outputs remain separable in actual usage.

The functions should be relevant to the classification and meaningful in the context of the tool usage, such as parsing, code generation, optimization, diagnostic checking, report generation, requirements import, test execution, result evaluation, or coverage calculation.
Do not decompose into internal implementation functions merely because they exist in the source code.

### A practical sufficiency test

A use case can normally remain at the high level if all credible malfunctions would lead to substantially the same:

- type of adverse effect;
- error-propagation or reliance path;
- prevention and detection measures or controls; and
- standard-specific classification result.

If any of these differ materially, decompose the relevant portion of the use case.

### Mixed and partially refined analyses

It is acceptable to decompose only the functions that need finer treatment.
For example, a compiler use case might analyze code generation and diagnostic enforcement separately while treating several reporting-only functions as one group.

Record whether the function results remain separate or are consolidated into one use-case classification.
Do not leave the aggregation rule implicit.

### Select the malfunction-record presentation

The analysis boundary and the record presentation are separate choices.
At either use-case or function/feature level, the author may use:

- **Structured malfunction subsections**, which are preferable when the effect path, controls, confidence rationale, or evidence needs explanation; or
- **A compact malfunction table**, which is convenient when several records can be expressed accurately in short entries and compared using the same fields.

The compact table should not recreate the unreadable wide table that the chapter-based structure is intended to avoid.
If cells become paragraph-heavy, controls need separate explanation, or evidence and assumptions are difficult to trace, use structured subsections instead.

The template may be adapted to the user's working style.
A report may use different presentations for different use cases, but the presentation should be consistent within a classification unit, and each malfunction should be recorded only once.

## Identify potential (credible) malfunctions or erroneous behavior

A use case or function may have one or more malfunction records.
Each record describes a relevant departure from the expected behavior of the defined use.
Consider, where relevant:

- an incorrect output;
- an incomplete or truncated output;
- a missing output or failure to perform an action;
- a spurious output, diagnostic, or action;
- a stale, inconsistent, or non-reproducible result;
- use of the wrong input, configuration, dependency, target, or processing path;
- incorrect handling of a valid input;
- failure to reject, constrain, or diagnose an invalid input when rejection or diagnosis is an intended function;
- an incorrect status, pass/fail result, measurement, or decision;
- corruption or unintended modification of an input or another artifact; and
- behavior outside documented limits that is not made apparent to the user.

Distinguish between:

1. a tool malfunction under valid usage conditions;
2. the tool's failure to detect invalid usage when detection is part of its intended behavior; and
3. user misuse that violates an explicit and adequately communicated constraint.

Misuse should not automatically be recorded as a tool malfunction.
It can nevertheless expose a need for stronger prevention, documentation, or user-interface controls.

Do not attempt to enumerate every theoretically possible internal fault.
Select credible malfunction descriptions that are sufficiently complete to support the effect and classification analysis.

## Analyze the effect and propagation path

### Potential effect

Describe what the malfunction could do to the supported activity, work product, verification result, or decision.
Examples include:

- introducing an error into an artifact;
- corrupting or omitting information;
- failing to reveal an existing defect;
- producing misleading evidence;
- causing an incorrect acceptance, rejection, prioritization, or release decision;
- breaking traceability or configuration consistency; or
- causing a required activity to be skipped or performed on the wrong item.

Keep the effect distinct from the internal root cause.
“An optimizer pass contains a defect” is a cause statement; “the generated object code does not preserve the specified program behavior” is an externally meaningful malfunction and effect statement.

### Error propagation or reliance path

Explain how the erroneous result could reach something safety-related.
Identify:

- the output carrying the error;
- the downstream consumer;
- any transformation or decision between the output and the safety-related work product;
- the checks encountered before reliance; and
- the point at which the error could become embedded, accepted, or no longer readily detectable.

If the effect cannot propagate under the stated conditions, document why and identify the assumptions that prevent propagation.

## Describe control measures

The guide uses **control measures** as an umbrella term.
Divide them into the categories below so their role remains clear.

### Prevention measures

Prevention measures or controls reduce the opportunity for an erroneous result or invalid usage to occur.
Examples include:

- restricting tool versions, targets, options, features, or input subsets;
- schema, type, range, or configuration validation;
- controlled wrappers or approved command lines;
- avoiding a known problematic feature;
- controlled installation and configuration;
- competent-user requirements and documented procedures; and
- interface constraints that prevent prohibited combinations.

### Detection (and correction) measures

Detection and correction measures or controls reveal and address an erroneous result before it is relied upon.
Examples include:

- independent review against defined criteria;
- comparison with an independently implemented tool or calculation;
- requirements-based testing of the generated artifact;
- round-trip, consistency, or plausibility checks;
- redundant generation and comparison;
- independent static or dynamic analysis;
- test-result review and anomaly resolution; and
- downstream verification that demonstrably covers the relevant erroneous behavior.

### Usage constraints and containment

Usage constraints and containment measures can limit where or how the output is used.
They should not be presented as prevention or detection unless they actually prevent the behavior or reveal its result.

Examples include prohibiting automatic acceptance, requiring human confirmation, restricting the output to informational use, or preventing the output from directly modifying a controlled artifact.

## Assess confidence in the controls

Do not list a control without analyzing why it addresses the specific malfunction.
Consider:

- **Relevance:** Does the control address this malfunction and its effect path?
- **Coverage:** Does it cover the relevant inputs, functions, configurations, and outputs?
- **Independence:** Is it sufficiently independent from the tool, its implementation, inputs, and assumptions?
- **Timing:** Is it applied before the output is relied upon or the error becomes embedded?
- **Acceptance criteria:** Is correct versus erroneous behavior defined clearly enough to support the control?
- **Repeatability:** Is the control performed consistently rather than informally or occasionally?
- **Evidence:** Are execution records, results, reviews, or other objective evidence retained?
- **Competence:** Are users or reviewers able to recognize the relevant error?
- **Limitations:** Which malfunction variants or conditions are not covered?
- **Common cause:** Could the same incorrect requirement, model, input, library, rule set, or implementation assumption defeat both the tool and the control?

The conclusion can use the following neutral follow-up statuses:

- **None identified:** no further confidence-building action is identified for the analyzed use under the applicable standard and assumptions;
- **Controlled under stated assumptions:** existing controls address the concern, but the assumptions and controls are mandatory;
- **Additional evidence or control needed:** TPL-004 or a process change is required;
- **Undetermined:** important information is missing or the analysis is inconclusive.

These statuses do not replace the classification levels defined by the applicable standard.

## Derive the standard-specific classification

Perform the neutral analysis first, then apply the selected standard's criteria.
This keeps the reasoning reusable while preserving the differences between standards.

### IEC 61508

For the exact edition selected by the project, determine the tool class using the standard's criteria and terminology.
The analysis should make visible whether the tool usage:

- has no direct or indirect influence on executable software or data;
- supports testing or verification and could fail to reveal a defect; or
- generates or transforms an output that contributes directly or indirectly to executable software or data and could introduce a defect.

These relationships support reasoning about T1, T2, or T3.
Apply the standard's exact definitions and requirements rather than treating the bullets above as a substitute for the standard.

Control measures can determine the confidence-building strategy and evidence required for the classified use.
Do not assume that a downstream control changes the tool class unless the applicable standard and approved interpretation support that conclusion.

### EN 50716

For the exact edition selected by the project, determine the applicable tool class using its criteria and terminology.
As with IEC 61508, the use-case characterization should identify the relationship between the tool output and executable software or data, and whether a verification tool could fail to reveal a defect.

Record the EN 50716 result separately even where its class names resemble those used by IEC 61508.
Similar labels do not by themselves establish equivalence of definitions, obligations, or required evidence.

### ISO 26262

For the exact edition selected by the project, record the required intermediate determinations and the resulting classification, normally including:

- **Tool Impact (TI):** whether a malfunction of the tool can introduce or fail to detect an error in a safety-related item or element;
- **Tool Error Detection (TD):** the degree of confidence in measures that prevent or detect errors in the tool output; and
- **Tool Confidence Level (TCL):** the result derived from TI and TD using the standard's rules.

The template's *potential effect* analysis supports TI reasoning.
The prevention, detection, correction, and confidence analysis supports TD reasoning.

Do not assume that a listed downstream verification or test automatically establishes a particular TD result.
The rationale should address the specific malfunction, coverage, independence, timing, and evidence.

### Other standards or organizational schemes

Add the required classification elements and results to the same use-case conclusion.
If the scheme introduces additional concepts, define them in the report and explain how the neutral malfunction-and-effect analysis supports them.

### Multiple applicable standards

When several standards apply:

1. perform the neutral use-case and malfunction analysis once where the factual basis is genuinely shared;
2. derive each standard-specific classification separately;
3. identify any additional analysis required by a particular standard; and
4. avoid collapsing the results into a single invented cross-standard level.

## Consolidate function and use-case results

Every use-case chapter should end with a clear classification boundary and conclusion.

If functions were analyzed separately, choose and justify one of these approaches:

1. **Separate classification:** retain separate results when functions, outputs, configurations, and uses remain meaningfully separable and the separation can be enforced.
2. **Function-group classification:** combine functions that share substantially the same effect paths, controls, and classification result.
3. **Use-case classification:** consolidate the findings for the complete use case according to the applicable standard, normally accounting for the result-driving malfunction and the least effective relevant control.

At report level, an overall tool result should be stated only if required or useful.
Preserve the use-case results and the assumptions behind them even when an overall result is reported.

## Determine follow-up actions

TPL-003 should make the consequence of the classification explicit.
Possible follow-up includes:

- no additional action beyond maintaining the documented assumptions and controls;
- strengthening a prevention or detection control;
- narrowing or prohibiting a feature, configuration, input, output, or use;
- collecting missing evidence about an existing control;
- defining qualification activities through TPL-004;
- documenting required usage checks, constraints, and known limitations through TPL-005;
- resolving an open anomaly or uncertainty before the output is relied upon; or
- repeating part or all of the classification at project level.

An undetermined result should lead to investigation or a conservative interim restriction.
It should not be silently treated as a favorable classification.

## Illustrative example of choosing the granularity

Consider the use case:

> **UC-01 — Compile C++ source files into target object files.**  
> Inputs include source files, headers, compiler options, target description, and linked assumptions about the language subset.
> The primary output is object code consumed by a linker.
> Diagnostics may also be relied upon to reject prohibited constructs.

A use-case-level analysis may be sufficient if all exercised functions are treated as one object-code generation activity, share the same downstream controls, and lead to the same classification.

A function-level analysis may be preferable if the organization relies differently on:

- parsing and semantic processing;
- optimization;
- target code generation;
- diagnostic enforcement; and
- dependency-file generation.

For example, incorrect target code generation can introduce erroneous executable behavior, whereas a missing diagnostic can fail to prevent use of a prohibited construct.
Dependency information may influence build completeness rather than instruction semantics.
These behaviors can have different outputs, propagation paths, controls, and classification implications.

The analysis does not need to enumerate individual compiler passes.
It should decompose only to the level needed to support a credible, reviewable classification argument.

## Review and completeness checklist

Before completing the report, confirm that:

- [ ] the report references the applicable controlled revision of TPL-002;
- [ ] the tool version, configuration, environment, classification perspective, and usage assumptions are unambiguous in TPL-002 rather than duplicated in TPL-003;
- [ ] the applicable standard and edition are recorded;
- [ ] every included use case is traceable to TPL-002;
- [ ] inputs, processing, outputs, consumers, and intended reliance are described;
- [ ] exclusions and usage constraints are explicit;
- [ ] the selected granularity is justified for each use case;
- [ ] one or more credible potential malfunctions are analyzed for each classification unit, as needed;
- [ ] the selected malfunction-record presentation remains readable and traceable;
- [ ] credible erroneous output and failure-to-detect behaviors are considered;
- [ ] effects are distinguished from internal causes;
- [ ] propagation paths identify how safety-related work could be influenced;
- [ ] prevention controls and detection/correction controls are distinguished;
- [ ] confidence claims address coverage, independence, timing, evidence, limitations, and common cause;
- [ ] standard-specific elements and results are recorded separately;
- [ ] function-level results are aggregated or retained separately using an explicit rule;
- [ ] required qualification activities, added controls, restrictions, and user information are identified;
- [ ] undetermined items have owners and resolution actions; and
- [ ] validity conditions and re-evaluation triggers are stated.

## Reuse, maintenance, and re-evaluation

A classification can be reused only while the scope and assumptions defined in the referenced TPL-002 and the applicable use-case analyses remain valid.
Review or repeat the analysis when there is a relevant change to:

- the tool version, revision, build, dependencies, configuration, or enabled functions;
- the host, target, execution environment, or integration interface;
- the intended or given use, input set, processing path, output, consumer, or reliance;
- the safety context or applicable integrity level;
- the prevention, detection, correction, review, test, or independent verification measures;
- known anomalies, limitations, security issues, or operational experience;
- the applicable standard, edition, or organizational interpretation; or
- the evidence supporting the classification or control-confidence rationale.

Where only one use case or function is affected, update and re-review the localized chapter and the classification summary.
Also check whether the change affects the report-level aggregation or another use case that shares the same control or assumption.
