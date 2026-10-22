# Confidence in the use of software tools

## Introduction

Software tools support many activities in the development of safety-related systems, hardware, and software.
For example, compilers, code generators, build tools, analysis tools, test tools, requirements management tools, and configuration management tools can influence the artifacts produced by those activities or the conclusions drawn from them.
If such a tool malfunctions, it may introduce an error, fail to detect an existing error, or provide misleading information.
If the surrounding development process does not detect that problem, it can undermine confidence in the resulting system even when the system-development process itself is otherwise rigorous.

**Confidence in the use of a software tool** is a justified basis for relying on that tool for a defined usage in a safety-related context.
It is established by understanding how the tool will be used, what can go wrong, how an error could affect the supported activity or its outputs, which measures prevent or detect such errors, and what evidence and usage conditions are needed as a result.

Confidence is therefore not an abstract or universal property of a tool.
It is related to a defined tool version, intended or given usage, functions and features, inputs and outputs, configuration, execution environment, surrounding process, applicable safety or assurance requirements, and the extent to which relevant outputs are independently examined or verified.
The same tool may require different confidence measures when used in different ways.

The first question is not automatically *How should this tool be qualified?*
It is *Is further evidence of confidence needed for this usage?*
If relevant tool errors are prevented or reliably detected by the surrounding process, additional qualification may not be necessary.
When further confidence is needed, appropriate measures may include a combination of usage restrictions, output verification, tool validation, development-process evidence, service history, independent assessment, or other activities accepted by the applicable standard.
Tool qualification is one possible part of establishing confidence; it is not a synonym for the complete subject.

## Purpose and scope of this guidance

The initial overview presented at the [2025 AsiaLLVM Developers' Meeting](https://llvm.org/devmtg/2025-06/) focused mainly on automotive software and ISO 26262.
It introduced a progression from tool definition, through evaluation and possible qualification, to the information needed by users for appropriate use.
The [presentation](https://llvm.org/devmtg/2025-06/slides/technical-talk/urribarri-automotive.pdf) and [recording](https://youtu.be/wAQ1XBjXfog) provide background on that work.

The present workflows and supporting artifacts broaden that starting point into cross-industry guidance.
They are organized around two complementary perspectives:

- a **tool developer, maintainer, or provider**, considering one tool and preparing reusable information or evidence for one or more intended usages; and
- a **tool user or integrator**, considering several tools used by a project and determining what is needed for each given usage.

The LLVM Qualification Working Group includes experienced safety engineers with knowledge of software-tool confidence in several industries.
The group has used that experience to develop workflows, templates, and guides that can be adapted and reused in different contexts.
It has also tried to explain the concepts in language that is accessible to LLVM developers and maintainers who have limited or no previous experience of functional safety.

These are **suggested workflows, templates, and guides**.
They are informative, not normative, and do not claim to represent the only valid approach.
They do not replace the applicable functional-safety or assurance standards, regulatory or certification guidance, approved interpretations of those sources, or an organization's own processes.
Users remain responsible for consulting the applicable requirements and adapting the material to their industry, project, and approval context.

The LLVM Qualification Working Group welcomes comments, observations, and suggestions from readers, reviewers, and users, and will consider them as these artifacts continue to evolve.

## Value within and beyond safety-critical development

People working in safety-critical industries may be able to reuse these artifacts directly as starting points for their own tool-confidence activities.
The broader intention is also to reuse useful concepts, methods, and lessons from safety standards to improve the general quality of tools across the LLVM infrastructure.

For example, clearly defining tool behavior and supported usage, analyzing credible malfunctions, making assumptions and limitations visible, linking requirements with tests and evidence, tracking versions and changes, and communicating known issues and usage conditions can improve reliability, transparency, and trust for all users.
Applying these practices does not by itself qualify LLVM or demonstrate compliance with a safety standard, but it can strengthen the upstream information and quality evidence on which both ordinary and safety-related users depend.

## How to use this overview

This overview connects the LLVM Qualification Working Group's generic software tool-confidence workflows with the corresponding templates and guidance.
It first maps the complete artifact family, then explains each workflow step from the provider and user perspectives.
The final sections explain the common decision workflow, maintenance expectations, and points to align in the workflow diagrams.

The workflow can be applied from two complementary perspectives:

- a **tool developer, maintainer, or provider** preparing reusable information and evidence for one or more intended usages; and
- a **tool user or integrator** assessing a given tool usage in a specific project.

The same organization may perform both roles for an in-house tool.
The artifacts may also be layered: an upstream provider can supply reusable information, while a downstream project confirms its applicability and adds project-specific information and controls.

## Templates and guides

| ID | Work product | Role in the workflows | Template and guidance |
|---|---|---|---|
| LLVM-QUAL-TPL-001 | Determination of Need for Confidence in the Usage of a Software Tool | Determines whether further confidence evidence is needed for a defined intended or given usage. | [Template](templates/LLVM-QUAL-TPL-001.md) · [Guide](templates/LLVM-QUAL-TPL-001-guide.md) |
| LLVM-QUAL-TPL-002 | Tool Usage Plan | Plans the usage boundary, classification, possible qualification activities, evidence, user information, reviews, and maintenance. | [Template](templates/LLVM-QUAL-TPL-002.md) · [Guide](templates/LLVM-QUAL-TPL-002-guide.md) |
| LLVM-QUAL-TPL-003 | Tool Classification Report | Analyzes defined use cases, credible malfunctions, effects, and prevention or detection controls, then records the applicable standard-specific classification. | [Template](templates/LLVM-QUAL-TPL-003.md) · [Guide](templates/LLVM-QUAL-TPL-003-guide.md) |
| LLVM-QUAL-TPL-004 | Tool Qualification Report | Records the execution, evidence, results, findings, and conclusions of qualification activities for a defined usage boundary. | [Template](templates/LLVM-QUAL-TPL-004.md) · [Central guide](templates/LLVM-QUAL-TPL-004-guide.md) · [Qualification approaches](templates/LLVM-QUAL-TPL-004-qualification-approaches-guide.md) · [Standards and test coverage](templates/LLVM-QUAL-TPL-004-standards-guide.md) |
| LLVM-QUAL-TPL-005 | Safety Manual | Communicates the information needed to use the tool within the stated confidence or qualification boundary, including mandatory conditions, complementary measures, known anomalies, and responsibilities. | [Template](templates/LLVM-QUAL-TPL-005.md) · [Guide](templates/LLVM-QUAL-TPL-005-guide.md) |
| LLVM-QUAL-TPL-006 | Safety Considerations | Documents and communicates the rationale, assumptions, constraints, safeguards, and responsibilities when TPL-001 concludes that further confidence evidence is not needed. | [Template](templates/LLVM-QUAL-TPL-006.md) · [Guide](templates/LLVM-QUAL-TPL-006-guide.md) |
| LLVM-QUAL-TPL-007 | Software Tool List | Provides an optional project-level catalog of tools, versions, documentation, confidence decisions, and related artifacts. | [Template](templates/LLVM-QUAL-TPL-007.md) · [Guide](templates/LLVM-QUAL-TPL-007-guide.md) |

The templates are generic.
A project may use equivalent work products with different names and formats and may link to those actual records from its software tool list.

## Tool developer maintainer or provider workflow

This workflow supports the preparation of reusable information and evidence for an intended tool usage.
A provider normally cannot determine whether the tool is suitable for every downstream system or project; downstream users must confirm the applicability of the provider's assumptions, scope, evidence, and usage conditions.

### 1. Describe the tool and its intended usage

Begin with a high-level description of the tool and its intended usage.
Identify the relevant functions, use cases, outputs, assumed development activities, usage constraints, and maximum predetermined safety criticality covered by the analysis.
Also state assumptions about the process in which the tool will be used, especially how relevant outputs are reviewed or verified.

These inputs establish the initial boundary for the determination in [LLVM-QUAL-TPL-001](templates/LLVM-QUAL-TPL-001.md).

### 2. Determine whether further confidence evidence is needed

Use [LLVM-QUAL-TPL-001](templates/LLVM-QUAL-TPL-001.md) and its [guide](templates/LLVM-QUAL-TPL-001-guide.md) to answer three questions for the defined usage:

1. Does the tool support a safety-related activity or task?
2. Does that activity or task rely on the correct functioning of the tool?
3. Are the relevant outputs completely and sufficiently examined or verified for the applicable process steps?

Further confidence evidence is needed only when the answers are **Yes**, **Yes**, and **No**, respectively.

### 3. If further confidence evidence is not needed, document the safety considerations

Use [LLVM-QUAL-TPL-006](templates/LLVM-QUAL-TPL-006.md) and its [guide](templates/LLVM-QUAL-TPL-006-guide.md) to communicate the reasoned basis for the conclusion.
Carry forward the TPL-001 rationale and assumptions, and make the tool's role, output handling, safeguards, usage constraints, and responsibility boundaries understandable without requiring users to reconstruct the complete determination.

Revisit the determination and safety considerations if the intended usage, assumptions, tool behavior, or surrounding process changes.

### 4. If further confidence evidence is needed, prepare the Tool Usage Plan

Use [LLVM-QUAL-TPL-002](templates/LLVM-QUAL-TPL-002.md) and its [guide](templates/LLVM-QUAL-TPL-002-guide.md) to refine the usage boundary and plan the activities and work products needed to establish confidence.
The plan should address the intended usages and use cases, environment and configuration, classification, possible qualification approaches, evidence, user-facing documentation, responsibilities, reviews, and change management.

TPL-002 plans the work; it does not replace the classification, qualification results, safety manual, or their supporting evidence.

### 5. Classify the defined tool usage

Use [LLVM-QUAL-TPL-003](templates/LLVM-QUAL-TPL-003.md) and its [guide](templates/LLVM-QUAL-TPL-003-guide.md) to analyze each defined use case, or group of sufficiently similar use cases.
Identify credible malfunctions or erroneous behavior, their potential effects and propagation paths, and the available prevention and detection controls.
Then derive and record the classification using the concepts of each applicable standard.

The activity is an **evaluation by analysis**; the documented work product is a **Tool Classification Report**.
The classification applies to the defined usage, not necessarily to the tool universally.

### 6. Decide whether qualification is required

Use the classification result, the applicable standard, the Tool Usage Plan, and any required controls to decide whether qualification activities are needed.
Classification schemes and qualification expectations differ across standards; do not translate a result from one standard directly into another.

If qualification is not required, continue by communicating the applicable conditions and controls to users.
If qualification is required, perform the planned activities before establishing the qualification conclusion.

### 7. Perform and report qualification activities when required

Execute the activities planned in TPL-002 and record them using [LLVM-QUAL-TPL-004](templates/LLVM-QUAL-TPL-004.md).
Start with the [central guide](templates/LLVM-QUAL-TPL-004-guide.md), and consult the [qualification-approaches companion](templates/LLVM-QUAL-TPL-004-qualification-approaches-guide.md) and [standards and test-coverage companion](templates/LLVM-QUAL-TPL-004-standards-guide.md) as applicable.

The report should identify the exact usage and evidence boundary, summarize the activities performed, link to controlled evidence, record coverage and findings, and state bounded standard-specific conclusions.
If the plan or classification basis changes, update TPL-002 and, where relevant, TPL-003 before completing the qualification report.

### 8. Provide the information needed for appropriate usage

Use [LLVM-QUAL-TPL-005](templates/LLVM-QUAL-TPL-005.md) and its [guide](templates/LLVM-QUAL-TPL-005-guide.md) to communicate the information users need to remain within the stated usage, confidence, or qualification boundary.
This includes installation, configuration and execution instructions, mandatory conditions, complementary measures, known anomalies and workarounds, support information, and responsibility boundaries.

TPL-005 can be useful whether or not qualification was required.
Derive its user-relevant content from the current TPL-002, TPL-003, and TPL-004 revisions, where those work products exist.
Do not reproduce their complete planning, analysis, or evidence in the manual.

## Tool user or integrator workflow

This workflow supports the selection, assessment, and controlled integration of tools for a specific project.
Provider artifacts may be reused, but the project must verify that their tool version, usage boundary, environment, assumptions, controls, and applicable standard match the given usage.

### 1. Establish and maintain the project software tool list

Use [LLVM-QUAL-TPL-007](templates/LLVM-QUAL-TPL-007.md) and its [guide](templates/LLVM-QUAL-TPL-007-guide.md) when a shared tool overview is useful.
Define the scope and inclusion criteria, then record each relevant tool, its version, provider, documentation, and the status or location of related confidence artifacts.

For functional safety, include at least the tools that support activities or tasks in the applicable safety lifecycle.
The list need not include every general-purpose utility used by every project member.
The list is an optional organizational aid and should be maintained throughout the workflow rather than treated as a one-time input.

### 2. Define the given tool usage and project assumptions

For each tool in scope, define how the project will use it, including the selected version and functions, inputs and outputs, configuration, execution environment, intended reliance, surrounding process, and relevant output checks.
Identify the applicable standard and project safety criticality.

Provider documentation can inform this definition, but provider assumptions are not automatically project facts.

### 3. Determine whether further confidence evidence is needed

Perform a project-specific determination using [LLVM-QUAL-TPL-001](templates/LLVM-QUAL-TPL-001.md) and its [guide](templates/LLVM-QUAL-TPL-001-guide.md).
This may still be necessary when the provider has already performed a generic determination, classification, or qualification because the project's given usage and controls may differ.

### 4. If further confidence evidence is not needed, document and apply the safety considerations

Use [LLVM-QUAL-TPL-006](templates/LLVM-QUAL-TPL-006.md) and its [guide](templates/LLVM-QUAL-TPL-006-guide.md) to retain the project-specific rationale, assumptions, checks, and constraints.
Update the software tool list with the TPL-001 conclusion and the corresponding safety considerations, then integrate the tool in accordance with those assumptions and constraints.

### 5. If further confidence evidence is needed, plan the given usage and confidence activities

Use [LLVM-QUAL-TPL-002](templates/LLVM-QUAL-TPL-002.md) and its [guide](templates/LLVM-QUAL-TPL-002-guide.md) to document or reference the exact project usage and plan classification, possible qualification activities, evidence reuse, user information, responsibilities, and maintenance.
Existing provider plans and artifacts may be referenced after their applicability has been assessed.

### 6. Classify the project-specific usage

Use [LLVM-QUAL-TPL-003](templates/LLVM-QUAL-TPL-003.md) and its [guide](templates/LLVM-QUAL-TPL-003-guide.md) to analyze the given use cases and controls and record the standard-specific classification.
A provider's generic classification may be reused only to the extent that its boundary and assumptions match the project usage.

### 7. Determine whether qualification is needed

Use the project-specific classification and applicable standard to determine whether qualification is required for the given usage.
If it is not required, continue by extracting and applying the relevant restrictions, controls, and conditions of use.

### 8. Assess available qualification evidence and close any gaps

If qualification is required, identify any provider, upstream, supplier, or prior-project evidence and assess whether it applies to the project's exact tool version, functions, usage, environment, integrity level, and required qualification approach.
Evidence may be reusable without being sufficient by itself.

When gaps remain, plan and perform the additional qualification activities needed for the project.
Record the resulting evidence, findings, and bounded conclusion in [LLVM-QUAL-TPL-004](templates/LLVM-QUAL-TPL-004.md), following its [central guide](templates/LLVM-QUAL-TPL-004-guide.md) and the relevant companion guides.

### 9. Extract and implement usage conditions

Extract the applicable restrictions, constraints, complementary measures, known anomalies, and change triggers from provider documentation and the classification and qualification results.
Use the provider's [Safety Manual](templates/LLVM-QUAL-TPL-005.md) where available, and prepare a project-specific manual or supplement when needed to record the exact local configuration, procedures, checks, evidence-retention rules, and responsibilities.

### 10. Update the software tool list and integrate the tool

Update [LLVM-QUAL-TPL-007](templates/LLVM-QUAL-TPL-007.md), or the project's equivalent tool register, with the completed decisions, artifact links, and current status.
Integrate and use the tool only within the defined project boundary and associated conditions.

Revisit the affected steps when a tool version, usage, environment, assumption, control, evidence source, known anomaly, or applicable requirement changes.

## TPL-001 decision workflow

The TPL-001 decision workflow is the common decision sub-workflow used by both providers and users.
It takes two inputs:

- a description of the tool and its intended or given usage; and
- assumptions about the development process in which the tool will be used.

The decision sequence is:

1. If the tool does not support a safety-related activity or task, further confidence evidence is not needed for the defined usage.
2. If the activity or task does not rely on correct functioning of the tool, further confidence evidence is not needed.
3. If the relevant outputs are completely and sufficiently examined or verified for the applicable process steps, further confidence evidence is not needed.
4. Otherwise, further confidence evidence is needed.

For every answer, record the rationale and assumptions in [LLVM-QUAL-TPL-001](templates/LLVM-QUAL-TPL-001.md).
On the **No further evidence needed** branch, document the resulting communication or project record using [LLVM-QUAL-TPL-006](templates/LLVM-QUAL-TPL-006.md).
On the **Further evidence needed** branch, continue with the [Tool Usage Plan](templates/LLVM-QUAL-TPL-002.md).

## Maintenance and change impact

The workflow does not end permanently when the initial artifacts are completed.
Maintain links between the current tool version, usage definition, assumptions, classification, qualification evidence, user information, and project tool list.
When one of these changes, evaluate the impact on downstream artifacts and repeat or update the affected workflow steps.

Where provider and project-specific artifacts are layered, identify their exact revisions and make clear which assumptions and responsibilities belong to each layer.
