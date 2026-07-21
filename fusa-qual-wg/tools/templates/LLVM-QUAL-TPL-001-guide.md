# How to Use LLVM-QUAL-TPL-001

## Determination of Need for Confidence in the Usage of a Software Tool

## Purpose

LLVM-QUAL-TPL-001 helps determine whether evidence of confidence in the usage
of a software tool is needed when the tool is used in safety-related
development activities.

The determination may be:

1. **Generic**, performed by a tool provider while considering a worst-case
   usage scenario and the resulting tool evaluation or qualification needs; or
2. **Project-specific**, performed by a tool user or integrator while
   considering a specific usage of the software tool for a given project, or
   when no evidence is available from the tool provider.

Functional safety standards do not mandate that this determination be performed
only by the tool provider.

The template supports an early, structured Yes/No decision based on:

- how the tool is used;
- what activities it supports; and
- what assumptions exist about verification of its outputs.

It does not evaluate use cases, qualify or certify a tool, or assess its
technical quality. It answers only the following question:

> Is evidence needed so that users can place justified confidence in this tool
> for a given usage?

## When to use the template

Use LLVM-QUAL-TPL-001 when:

- you provide a software tool that may be used in safety-related contexts; or
- you are a tool user or integrator who needs to perform a tool-confidence
  determination as part of a safety-related project; and
- you want to clarify whether evidence of confidence in the usage of the tool
  is needed.

A tool user or integrator may need to perform this determination even when the
tool provider has already classified or qualified the software tool.

Typical examples include:

- compilers, build tools, or linkers;
- test, verification, or analysis tools;
- requirements or configuration management tools; and
- continuous integration or automation tools supporting safety-related
  activities.

The template applies to open-source and proprietary tools, including tools
developed either out of context or for a specific project.

## Information needed before starting

Before completing the questionnaire, prepare the following information.

### 1. Description of the tool and its usage

Describe:

- what the tool does;
- how it is intended, or given, to be used;
- any usage constraints, such as restricted configurations or feature subsets;
  and
- which development activities it supports.

**Intended usage** typically applies to tools developed out of context, where
the tool provider defines or assumes usage conditions.

**Given usage** typically applies to tools used in a defined project context,
where the usage conditions are already known.

### 2. Assumptions about the development process

Document relevant assumptions, for example:

- whether tool outputs are reviewed;
- which checks or verification activities are applied; and
- whether any outputs are trusted without further examination.

These assumptions are important because the conclusion remains valid only while
they hold.

## How to answer the questionnaire

The questionnaire contains three questions. Answer each one with **Yes** or
**No**, and always document the rationale.

### Q1 - Safety-related activity

Determine whether the tool supports an activity that is safety-related under
the applicable functional safety standard.

Examples include design, implementation, verification, testing, requirements
management, configuration management, change management, and safety
management.

### Q2 - Dependency on correct functioning

Determine whether correct execution of the activity depends on the tool
functioning correctly.

If a tool malfunction could adversely affect the outcome of the activity, the
activity relies on the correct functioning of the tool.

### Q3 - Sufficiency of output verification

Determine whether the relevant tool outputs are completely and sufficiently
examined or verified for the applicable process steps.

Consider the reviews, checks, or verification activities that are performed or
assumed. If some tool-output errors could remain undetected after those
activities, answer **No**.

## How the decision is made

The answers are referred to as A1, A2, and A3.

- If **A1 = Yes**, **A2 = Yes**, and **A3 = No**, evidence of confidence in the
  usage of the software tool is required.
- In all other cases, such evidence is not required.

This logic reflects whether a tool malfunction could directly and undetectably
affect a safety-related activity.

## What happens after the determination

If the answer is **No**, the documented rationale explains why confidence
evidence is not required under the stated assumptions. If those assumptions do
not hold in practice, the determination may need to be revisited.

If the answer is **Yes**, the determination normally serves as an entry point
to further activities such as:

- tool specification;
- tool evaluation; and
- where applicable, tool qualification.

Those activities are outside the scope of LLVM-QUAL-TPL-001.

## What this template does not do

LLVM-QUAL-TPL-001 does not:

- certify or qualify a tool;
- replace applicable functional safety standards;
- mandate a specific development process; or
- impose industry-specific practices on open-source projects.

It is guidance intended to support transparent and reasoned decisions.

## Reuse and maintenance

The determination may be reused across projects while the documented
assumptions remain valid.

Any significant change in tool usage, development process, or verification
activities may require the determination to be revisited and updated.

## References

The questionnaire is derived from concepts in functional safety standards,
including:

- IEC 61508:2010, Part 3, Annex H; and
- ISO 26262:2018, Part 8, 11.4.1.
