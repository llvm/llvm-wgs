# How to Use LLVM-QUAL-TPL-006

## Safety Considerations

## Purpose

LLVM-QUAL-TPL-006 helps a software tool provider or tool user/integrator document why evidence of confidence in the usage of a software tool is not considered necessary under the assumptions documented using LLVM-QUAL-TPL-001.

The resulting safety considerations provide a clear and reasoned description of:

- the role of the tool in safety-related activities;
- how its outputs are intended to be used;
- relevant assumptions and usage constraints;
- how tool outputs are expected to be handled or verified; and
- the responsibilities associated with the tool's use.

For a tool provider, the safety considerations may be communicated to downstream users as part of the tool documentation.
For a tool user/integrator, they may be retained as project-specific documentation of the rationale and assumptions associated with the given tool usage.

The goal is transparency and informed usage, not justification by omission.

## Relationship with LLVM-QUAL-TPL-001

LLVM-QUAL-TPL-006 does not redefine the determination logic for confidence in the usage of a software tool.

First use LLVM-QUAL-TPL-001 to determine whether evidence of confidence in the usage of the software tool is required.
Use LLVM-QUAL-TPL-006 when that determination concludes that such evidence is not required and the tool provider or tool user/integrator wishes to document the supporting rationale and assumptions.

The safety considerations should be based on the documented answers and rationales for A1, A2, and A3 in LLVM-QUAL-TPL-001.

## When to use the template

Use LLVM-QUAL-TPL-006 when:

- LLVM-QUAL-TPL-001 concludes that evidence of confidence in the usage of the software tool is not required under the stated assumptions;
- the tool may reasonably be used in safety-critical or high-assurance development contexts; and
- the tool provider wants to communicate the basis, assumptions, and limitations of that conclusion to downstream users, or the tool user/integrator wants to document the corresponding project-specific rationale.

The template may be used by tool providers and tool users/integrators, for open-source or proprietary tools.

### Tool provider perspective

When completed by a tool provider, the safety considerations are generally based on the intended usage of the tool and assumptions about the development process in which downstream users may use it.

This is particularly useful for generic tools, tools intended for broad use, and tools that may be reused across multiple projects.
In these cases, the tool provider may have limited knowledge or visibility of the final system context, including the specific system, applicable safety requirements, or development process in which the tool will be used.

### Tool user/integrator perspective

When completed by a tool user/integrator, the safety considerations are generally based on the given usage of the tool in a particular project and the actual or planned development process surrounding that usage.

The documented rationale should therefore reflect the relevant project-specific usage constraints, reviews, checks, verification activities, and other assumptions used in the LLVM-QUAL-TPL-001 determination.

## Writing the safety considerations

The safety considerations should be understandable on their own, without requiring the reader to examine the complete determination performed using LLVM-QUAL-TPL-001.

The text should cover the following topics as applicable.

### 1. Role of the tool

Describe what the tool does and which safety-related activities it may support.

Do not overstate the importance of the tool or imply that it performs activities that remain outside the tool itself.

### 2. Dependency and decision-making

Explain whether and how the tool outputs are relied upon in the assumed or given development process.

Clarify whether the tool performs direct safety-relevant decisions, such as acceptance, rejection, or gating decisions, in the assumed or given development process.

### 3. Output handling and safeguards

Describe how relevant tool outputs are assumed to be reviewed, interpreted, checked, verified, or otherwise constrained.

Explain why incorrect tool behavior is not expected to directly affect safety or remain undetected before affecting a safety-related activity.

The described safeguards should be consistent with the assumptions documented for A1, A2, and A3 in LLVM-QUAL-TPL-001.

### 4. Assumptions and usage constraints

State the assumptions under which the conclusion remains valid.

Examples may include:

- use of the tool in accordance with its documented purpose;
- use by competent users;
- independent review or interpretation of relevant outputs;
- complementary verification activities;
- use of specified configurations or feature subsets; and
- restrictions on how tool outputs may be consumed or trusted.

Clearly stating assumptions and limitations is particularly relevant when the tool is generic, intended for broad use, reusable across multiple projects, or distributed without the tool provider having knowledge or visibility of the final system context.

### 5. Responsibilities

When the document is prepared by a tool provider, clarify that downstream users remain responsible for:

- assessing whether the tool is suitable for their specific safety context;
- determining whether the documented assumptions hold in their development process;
- deciding whether additional confidence, evaluation, or qualification activities are required; and
- complying with applicable safety standards and project requirements.

When the document is prepared by a tool user/integrator, document the corresponding project-specific responsibilities, checks, and constraints that support the conclusion.

## Writing style

Keep the language factual, specific, and neutral.

Avoid:

- legal, marketing, or defensive wording;
- unsupported claims about tool quality or reliability;
- claims of compliance with a functional safety standard;
- claims that the tool is suitable for a particular safety integrity level; and
- statements that transfer all responsibility to the user without explaining the technical assumptions and rationale.

## Example statements

The following statements illustrate the type of information that may be included.
They should be adapted to the tool and the rationale documented in LLVM-QUAL-TPL-001.

> This tool is intended to support development activities but is not intended to replace safety analyses, reviews, or verification activities.

> The outputs of this tool are informational and require interpretation by competent users.

> Users operating in safety-critical contexts are expected to assess whether additional measures are required for their specific application.

These examples are not a complete safety-considerations section and should not be copied without checking that they accurately describe the tool and its assumed usage.

## Use in documentation

When prepared by a tool provider, the completed document may be included, in whole or in part, as a dedicated chapter in the software tool's user manual or official documentation.

Possible chapter titles include:

- **Safety Considerations**; or
- **Tool Usage in Safety-Critical Contexts**.

Providing this information directly to users is strongly recommended when the tool may reasonably be used in safety-critical or high-assurance development contexts.

Including the safety considerations in user documentation:

- improves transparency about the intended use and limitations of the tool;
- helps users understand whether additional confidence or qualification activities may be required in their specific context;
- reduces the risk of implicit or unintended reliance on the tool in safety-related decisions;
- supports informed decision-making by tool users, integrators, and auditors; and
- supports good practice for communicating safety-related assumptions in open-source and proprietary tools.

When prepared by a tool user/integrator, the completed document may instead be maintained as part of the project's safety, tool-confidence, qualification, or other relevant engineering documentation.
In this case, its purpose is to preserve the project-specific rationale and assumptions supporting the determination that further confidence evidence is not required.

This is guidance rather than a documentation mandate.
The level of detail may be adapted to the size, maturity, and expected usage of the tool.

## What this template does not do

LLVM-QUAL-TPL-006 does not:

- determine whether evidence of confidence in the usage of the tool is required;
- evaluate or qualify the tool;
- certify the tool or establish compliance with a functional safety standard;
- demonstrate suitability for a particular safety integrity level; or
- replace the applicable safety standards or a project-specific assessment.

## Validity and maintenance

The safety considerations remain valid only while the assumptions and usage conditions on which they are based remain valid.

A significant change in tool functionality, intended usage, development process, output-verification activities, or usage constraints may require the LLVM-QUAL-TPL-001 determination and the associated safety considerations to be reviewed and updated.
