> [!NOTE]
> **Template provided by:** [LLVM Qualification Working Group](https://llvm.org/docs/QualGroup.html)  
> **Document identifier:** `LLVM-QUAL-TPL-001`  
> **Usage guide:** [LLVM-QUAL-TPL-001-guide.md](LLVM-QUAL-TPL-001-guide.md)
>
> This template is provided for guidance and does not replace applicable
> safety standards.

# Determination of Need for Confidence in the Usage of `<Tool_Name>`

> [!TIP]
> Text between angle brackets, such as `<Tool_Name>`, is a placeholder to be
> replaced with tool-specific information.
>
> Remove the instructional notes and tips when publishing a completed document.

| Document information | Value |
|---|---|
| Organization / team name | `<Owner>` |
| Version | `<X.Y>` |
| Date | `<YYYY-MM-DD>` |

> [!TIP]
> List the roles involved in this document as applicable, for example authors,
> reviewers, or approvers. Add or remove rows as needed.

| Role | Name |
|---|---|
| `<Role>` | `<Name>` |

## Identification

| Item | Value |
|---|---|
| Tool name | `<Tool_Name>` |
| Tool version (optional) | `<Tool_Version>` |

## Introduction

This questionnaire is intended to determine whether it is necessary to provide
evidence of confidence in the use of `<Tool_Name>` with respect to the
`<Standard>` functional safety standard.

The outcome of this analysis is a Yes/No decision supported by documented
rationale and stated assumptions.

This template supports an initial determination step and does not replace tool
evaluation or qualification activities defined in functional safety standards.

## Questionnaire

> [!TIP]
> Before completing the questionnaire, document:
>
> 1. A description of the software tool and its intended or given usage.
> 2. Assumptions about the development process in which the software tool will
>    be used, including reviews, checks, or verification activities applied to
>    relevant tool outputs.
>
> The questions below are derived from functional safety standards such as
> IEC 61508:2010, Part 3, Annex H, and ISO 26262:2018, Part 8, 11.4.1.
>
> See [LLVM-QUAL-TPL-001-guide.md](LLVM-QUAL-TPL-001-guide.md) for detailed
> guidance.
>
> Remove this instruction when publishing a completed document.

| Question | Answer | Rationale |
|---|---|---|
| **Q1 - Is the software tool used to support a safety-related activity or task?**<br><br>Does the software tool play a role in executing any required activity or task defined by the reference functional safety standard, for example safety analysis, design, implementation, verification, testing, validation, requirements management, configuration management, change management, or safety management? | **A1 -** `<Yes / No>` | `<Rationale for A1>` |
| **Q2 - Does the activity or task rely on the correct functioning of the software tool?**<br><br>Does successful execution of the activity or task depend on the software tool performing its intended functions correctly?<br><br>If a malfunction or error of the software tool could adversely affect the outcome of the activity or task, the activity is considered to rely on the correct functioning of the tool. | **A2 -** `<Yes / No>` | `<Rationale for A2>` |
| **Q3 - Are the relevant outputs completely and sufficiently examined or verified for the applicable process step(s)?**<br><br>Are there, or do you assume there will be, defined reviews, checks, or verification activities that assess the completeness, correctness, and consistency of the relevant outputs produced by the software tool?<br><br>If some errors in the tool outputs could remain undetected by subsequent examination or verification, the outputs are not considered to be sufficiently examined. | **A3 -** `<Yes / No>` | `<Rationale for A3>` |

## Conclusion

### Decision logic

- If **A1 = Yes**, **A2 = Yes**, and **A3 = No**, evidence of confidence in the
  usage of the software tool is required.
- In all other cases, such evidence is not required.

This decision reflects whether a tool malfunction could directly and
undetectably affect a safety-related activity.

### Decision

**Further activities to establish confidence required:** `<Yes / No>`

> [!TIP]
> The summary rationale is optional. Remove this field if it is not needed.

**Summary rationale:**

`<Short summary of the main reasons for the decision>`

> [!NOTE]
> If evidence of confidence is required, this determination is expected to be
> followed by further activities such as tool specification, tool evaluation,
> and, where applicable, tool qualification.

## Validity and limitations

The conclusion is valid under the assumptions documented in this questionnaire.

Any significant change in tool usage, development process, or verification
activities may require this determination to be revisited and updated.
