> [!NOTE]
> **Template provided by:** [LLVM Qualification Working Group](https://llvm.org/docs/QualGroup.html)  
> **Document identifier:** `LLVM-QUAL-TPL-002`  
> **Usage guide:** [LLVM-QUAL-TPL-002-guide.md](LLVM-QUAL-TPL-002-guide.md)
>
> This template is provided for guidance and does not replace applicable safety standards.

# Tool Usage Plan for `<Tool_Name>`

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

## Identification

| Item | Value |
|---|---|
| Tool name | `<Tool_Name>` |
| Tool version (optional) | `<Tool_Version>` |

## Introduction

This document defines the tool usage plan for `<Tool_Name>`.
It specifies which activities, work products, and evidence are planned in order to ensure an appropriate level of confidence in the use of the software tool, consistent with the applicable functional safety standard(s): `<References to standards>`.

This document does not contain the detailed content of tool documentation, specifications, validation results, or qualification evidence.
Instead, it defines what will be produced, at which level, and for which usage context.

## Context of usage

> [!TIP]
> The objective of this section is to ensure that all aspects relevant to confidence in the usage of the software tool are consciously planned, even if they are documented elsewhere or produced later.
>
> The elements listed below are not required to be fully specified in this document.
> Identify which aspects are applicable, which work products are planned, and where they will be documented.

This section defines the scope of usage for which confidence in the use of `<Tool_Name>` is planned to be established.

### Maximum pre-determined safety criticality

> [!TIP]
> State how the maximum pre-determined criticality supported by this plan will be defined.
> Consider, as applicable:
>
> - the maximum ASIL, SIL, or equivalent safety integrity level;
> - assumptions on the allocation of safety requirements to the item or element under development; and
> - limitations resulting from this criticality assumption.

`<To be completed by the author>`

### User-facing documentation

> [!TIP]
> Identify the user-facing documents planned to support correct and controlled usage of the tool, such as:
>
> - user manuals;
> - installation, setup, and administration guides;
> - configuration guides;
> - release notes; and
> - other usage-related documentation.
>
> For each document, briefly indicate whether it is planned, its intended scope, and its target audience, for example tool users, integrators, or administrators.

`<To be completed by the author>`

### Intended usage and use cases

> [!TIP]
> Define how the intended usage of the software tool will be documented, including:
>
> - intended or given usage, whether generic or project-specific;
> - intended use cases; and
> - explicitly excluded or unsupported use cases, if applicable.

`<To be completed by the author>`

### Inputs and expected outputs

> [!TIP]
> Identify how the following will be specified:
>
> - tool inputs, for example source code, models, configuration files, queries, or libraries;
> - tool outputs, for example processed data, binaries, reports, logs, or diagnostics; and
> - assumptions on input correctness and output usage.

`<To be completed by the author>`

### Configuration options

> [!TIP]
> Describe how configuration aspects will be addressed, including:
>
> - supported configuration options;
> - default configurations;
> - configuration constraints or restrictions relevant to safety; and
> - handling of configuration changes.

`<To be completed by the author>`

### Execution environment

> [!TIP]
> Define how the execution environment will be documented, including:
>
> - supported platforms, such as hardware, operating systems, or runtime environments;
> - external dependencies;
> - toolchain or infrastructure assumptions, such as minimum required versions; and
> - environmental constraints relevant to correct operation.

`<To be completed by the author>`

### Features, functions, and technical properties

> [!TIP]
> Identify how the following will be specified or referenced:
>
> - relevant tool features and functions;
> - technical properties that influence confidence, for example determinism, traceability, or diagnostics; and
> - feature subsets that are in scope or out of scope for safety-related usage.

`<To be completed by the author>`

### Expected behavior under anomalous operating conditions

> [!TIP]
> Indicate how the expected behavior of the tool under anomalous conditions will be addressed, such as:
>
> - invalid or unexpected inputs;
> - resource exhaustion;
> - partial failures; and
> - degraded modes of operation.

`<To be completed by the author>`

### Known malfunctions and countermeasures

> [!TIP]
> Identify how known issues will be handled, including:
>
> - known malfunctions or limitations;
> - existing workarounds or countermeasures; and
> - communication of this information to tool users.

`<To be completed by the author>`

### Validation activities, if applicable

> [!TIP]
> If software-tool validation is expected or selected as a qualification method, identify which of the following work products are planned, without detailing their content:
>
> - software tool requirements;
> - software tool architecture description;
> - validation or test strategy;
> - test plans;
> - test cases; and
> - test results.

`<To be completed by the author>`

## Planning summary

> [!TIP]
> The purpose of this section is to ensure that all necessary confidence-building activities are planned explicitly, even if their execution or level of rigor varies depending on the tool, usage, and safety context.

This section provides a consolidated overview of the planned approach to ensure confidence in the usage of the software tool for the context defined above.

The objective is to define the planned activities and work products that will be produced in order to:

- address the risks identified for the software tool usage;
- provide justified confidence in the reliability and suitability of the tool; and
- support its use within the defined usage context and safety criticality.

### Strategy

The following overall strategy is selected:

- Tool classification will be performed.
- Tool qualification will follow, depending on the results of tool classification.

> [!TIP]
> An alternative strategy may be described above.
>
> The selected strategy should be consistent with:
>
> - the role of the tool in the development lifecycle;
> - its contribution to safety-relevant decisions or transformations;
> - the feasibility of qualification methods; and
> - the assumed safety integrity level.

### Planned work products overview

The table below summarizes the planned work products and their purpose.

| Work product | Template | Purpose |
|---|---|---|
| Tool usage plan | `LLVM-QUAL-TPL-002` | Defines scope, assumptions, and planned activities. |
| Tool classification report | `LLVM-QUAL-TPL-003` | Documents the classification and supporting risk analysis of the tool usage. |
| Tool qualification report | `LLVM-QUAL-TPL-004` | Documents the results of applying selected qualification methods, if applicable. |
| Safety manual | `LLVM-QUAL-TPL-005` | Defines constraints, assumptions, and guidance for correct tool usage. |

> [!TIP]
> Additional work products, for example configuration-management or change-management plans, may be referenced as applicable.

### Completion and acceptance criteria

This plan is considered complete when:

- all planned activities have been performed or explicitly justified as not applicable;
- the planned work products have been produced and reviewed; and
- the conclusions are consistent with the assumptions and scope defined in this plan.

## Planned activities

This section describes the activities planned to ensure confidence in the usage of `<Tool_Name>`.

### Tool classification (risk analysis)

> [!TIP]
> Plan the analysis supporting classification of the software tool usage, including the risks associated with that usage.
>
> The activity is expected to result in a tool classification report documenting, in particular:
>
> - potential tool failure modes and their effects;
> - detectability and preventability of tool malfunctions; and
> - justification of the selected confidence level.
>
> The results may be documented using `LLVM-QUAL-TPL-003 - Tool Classification Report`.

`<To be completed by the author>`

### Tool qualification activities, if applicable

> [!TIP]
> If the tool classification concludes that qualification activities are required and feasible, define:
>
> - the planned qualification method(s);
> - the scope and objectives of each method;
> - the planned work products and evidence to be produced; and
> - the rationale for the planned qualification strategy.
>
> Depending on the applicable functional safety standard, the software tool, and its intended or given usage, qualification may be based on one or more complementary methods.
> These may include, for example:
>
> - validation of the software tool against its specified requirements;
> - evaluation of the software tool development process;
> - analysis of test results and coverage;
> - operational experience or previously established confidence;
> - usage constraints and complementary verification measures; or
> - a justified combination of technical and process measures.
>
> Qualification is a strategy, not a single technique.
>
> The results may be documented using `LLVM-QUAL-TPL-004 - Tool Qualification Report`.

`<To be completed by the author>`

### Usage constraints and guidance (safety manual)

> [!TIP]
> Independently of whether qualification activities are performed, define how constraints and guidance for correct tool usage in safety-related development contexts will be captured and communicated to users.
>
> Include planning for the documentation of required complementary measures outside the tool.
>
> These elements may be documented using `LLVM-QUAL-TPL-005 - Safety Manual`.

`<To be completed by the author>`

### Reviews and independence

> [!TIP]
> Identify:
>
> - review activities for the planned work products;
> - roles and responsibilities for reviews; and
> - expectations regarding independence, where applicable.

`<To be completed by the author>`

### Updates and change management

> [!TIP]
> Define the conditions under which the planned activities or produced evidence must be revisited, such as:
>
> - changes to the tool or its configuration;
> - changes to the usage context or execution environment; and
> - changes to safety requirements or criticality assumptions.

`<To be completed by the author>`

> [!NOTE]
> This template aims to be minimal.
> Other sections may be added depending on the needs of the author, for example terms and definitions, abbreviations and acronyms, intended audience, resources, or schedule.
> References to related templates and work products may be provided where applicable.
