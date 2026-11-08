# How to Use LLVM-QUAL-TPL-001

## Determination of Need for Confidence in the Usage of a Software Tool

## Purpose

LLVM-QUAL-TPL-001 helps determine whether evidence of confidence in the usage of a software tool is needed when the tool is used in safety-related development activities.

The determination may be:

1. **Generic**, performed by a tool developer while considering a worst-case usage scenario and the resulting tool evaluation or qualification needs; or
2. **Project-specific**, performed by a tool user or integrator while considering a specific usage of the software tool for a given project, or when no evidence is available from the tool developer.

Functional safety standards do not mandate that this determination be performed only by the tool user.

The template supports an early, structured Yes/No decision based on:

- how the tool is used;
- what activities it supports; and
- what assumptions exist about verification of its outputs.

It does not evaluate use cases, qualify or certify a tool, or assess its technical quality.
It answers only the following question:

> Is evidence needed so that users can place justified confidence in this tool for a given usage?

## When to use the template

Use LLVM-QUAL-TPL-001 when:

- you provide a software tool that may be used in safety-related contexts; or
- you are a tool user or integrator who needs to perform a tool-confidence determination as part of a safety-related project; and
- you want to clarify whether evidence of confidence in the usage of the tool is needed.

A tool user or integrator may need to perform this determination even when the tool developer has already classified or qualified the software tool.

Typical examples include:

- compilers, build tools, or linkers;
- test, verification, or analysis tools;
- requirements or configuration management tools; and
- continuous integration or automation tools supporting safety-related activities.

The template applies to open-source and proprietary tools, including tools developed either out of context or for a specific project.

## Information needed before starting

Before completing the questionnaire, prepare the following information.

### 1. Description of the tool and its usage

A description of:

- what the tool does;
- how it is intended, or given, to be used;
- any usage constraints, such as restricted configurations or feature subsets; and
- which development activities it supports

is useful information to properly determine the tool-confidence need.

**Intended usage** typically applies to tools developed out of context, where the tool developer defines or assumes usage conditions.

**Given usage** typically applies to tools used in a defined project context, where the usage conditions are already known.

### 2. Assumptions about the development process

Relevant assumptions such as:

- whether tool outputs are reviewed;
- which checks or verification activities are applied; and
- whether any outputs are trusted without further examination.

are also important inputs to the tool-confidence determination, because the conclusion remains valid only while they hold.

## How to answer the questionnaire

The questionnaire contains three questions.
Answer each one with **Yes** or **No**, and always document the rationale.

### Q1 - Safety-related activity

Determine whether the tool supports an activity that is safety-related under the applicable functional safety standard.

Examples include design, implementation, verification, testing, requirements management, configuration management, change management, and safety management.

### Q2 - Dependency on correct functioning

Determine whether correct execution of the activity depends on the tool functioning correctly.

If a tool malfunction could adversely affect the outcome of the activity, the activity relies on the correct functioning of the tool.

### Q3 - Sufficiency of output verification

Determine whether the relevant tool outputs are completely and sufficiently examined or verified for the applicable process steps.

Consider the reviews, checks, or verification activities that are performed or assumed.
If some tool-output errors could remain undetected after those activities, answer **No**.

For example, source review can detect defects in the input to a compiler.
Tests run on the generated executable can reveal compilation errors that affect the behavior exercised by those tests.
Explain what the checks cover for the usage being assessed.

## How the decision is made

The answers are referred to as A1, A2, and A3.

- If **A1 = Yes**, **A2 = Yes**, and **A3 = No**, evidence of confidence in the usage of the software tool is required.
- In all other cases, such evidence is not required.

This logic reflects whether a tool malfunction could directly and undetectably affect a safety-related activity.

## What happens after the determination

If the answer is **No**, the documented rationale explains why confidence evidence is not required under the stated assumptions.
If those assumptions do not hold in practice, the determination may need to be revisited.

If the answer is **Yes**, the determination normally serves as an entry point to further activities such as:

- planning the usage of the tool;
- tool classification; and
- where applicable, tool qualification.

Those activities are outside the scope of LLVM-QUAL-TPL-001.

## Reuse and maintenance

The determination may be reused across projects while the documented assumptions remain valid.

Any significant change in tool usage, development process, or verification activities may require the determination to be revisited and updated.

For example, for a determination tied to a specific configuration, it could be useful to record or reference the assessed baseline, as applicable.
The baseline description could include not only the tool version, but also effective options, execution environment and target, and the revision and configuration of the source or other inputs.
When reusing the results of the determination, it would then be possible to analyze whether any differences affect its applicability to the intended tool use.

## References

The questionnaire is derived from concepts in functional safety standards, including IEC 61508:2010 for E/E/PE systems, and ISO 26262:2018 (particularly in Part 8, 11.4.1) for automotive systems.

In the case of airborne projects, DO-178C (§12.2.1) requires confidence in a software tool when the project uses the tool to eliminate, reduce, or automate a DO-178C process without verifying the tool’s output as specified in its §6.
For example, in the case of a compiler generating a binary to be embedded in the final system, verifying the output would include requirements-based testing and structural coverage analysis as applicable.
The decision applies to the intended use on the project.

The A3 rationale identifies which outputs are checked, how they are checked, and what the checks cover.
An airborne project can use that rationale as input when assessing whether its verification satisfies §6 for that use.
If confidence is needed, DO-178C §12.2.2 and Table 12-1 use the applicable tool criterion and airborne software level to determine a Tool Qualification Level (TQL).
DO-330 provides the objectives, activities, and life cycle data for that level.
