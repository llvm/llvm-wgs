# How to Use LLVM-QUAL-TPL-002
## Tool Usage Plan

## Purpose

LLVM-QUAL-TPL-002 supports planning the activities, work products, and evidence
needed to establish confidence in the usage of a software tool in a
safety-related development context.

The template is intended to be completed when the determination performed using
LLVM-QUAL-TPL-001 concludes that further activities to establish confidence are
required.

The resulting tool usage plan may include:

- planning of the tool classification and associated risk analysis;
- planning of qualification activities and methods, where applicable;
- planning of the documentation needed to define the intended usage, operating
  conditions, constraints, and known limitations of the tool; and
- planning of a safety manual and other information needed by tool users.

The template plans these work products and activities. It does not replace them
or require their detailed content to be included in the plan itself.

## Relationship with LLVM-QUAL-TPL-001

LLVM-QUAL-TPL-001 determines whether further evidence of confidence in the
usage of a software tool is required.

Use LLVM-QUAL-TPL-002 when that determination concludes that further
confidence-building activities are required. The scope and assumptions recorded
in LLVM-QUAL-TPL-001 should be carried into the tool usage plan and refined as
needed.

Before completing this plan, the following information should normally be
available:

- a completed LLVM-QUAL-TPL-001 determination;
- a high-level description of the software tool and its intended or given
  usage; and
- information about the development process and safety lifecycle context in
  which the tool will be used or is assumed to be used.

## What the plan should establish

The completed plan should establish:

- the scope of tool usage for which confidence will be addressed;
- the maximum pre-determined safety criticality covered by the plan;
- the documentation and evidence that will be produced;
- the tool classification activities that will be performed;
- the qualification methods that may be applied, depending on the classification
  results;
- the constraints and guidance that will be communicated to tool users;
- review and independence expectations; and
- the conditions under which the plan and resulting evidence must be revisited.

## Planning the context of usage

The context-of-usage section is not intended to contain every detailed
specification or manual. Its purpose is to ensure that relevant information is
planned, assigned to an appropriate work product, and not unintentionally
omitted.

### Maximum pre-determined safety criticality

Define the maximum safety criticality covered by the plan, such as an ASIL, SIL,
or equivalent integrity level. Record assumptions concerning the allocation of
safety requirements and any limitations resulting from the selected maximum
criticality.

This value defines the planning envelope. It does not by itself demonstrate
that the tool is suitable or qualified for that integrity level.

### User-facing documentation

Identify the manuals and guides required to support correct use of the tool. 
Depending on the tool, these may include:

- user manuals;
- installation or setup instructions;
- configuration or administration guides;
- release notes; and
- other usage guidance.

For each planned document, indicate its scope, owner or source, target audience,
and expected availability where useful.

Existing upstream or supplier documentation may be referenced rather than
reproduced, provided that its applicability and sufficiency for the planned
usage are assessed.

### Intended usage and use cases

Plan how the intended or given usage will be defined. Distinguish, where
relevant, between:

- generic usage assumptions defined by a tool developer; and
- project-specific usage conditions defined by a tool user or integrator.

Include supported use cases and explicitly excluded or unsupported use cases.

### Inputs, outputs, configuration, and environment

Plan how tool inputs, expected outputs, configuration options, execution
environment, dependencies, and technical constraints will be specified.

The level of detail should be sufficient to identify the usage envelope covered
by the classification and qualification evidence. A change outside that envelope
may require the evidence to be reviewed or extended.

### Features and technical properties

Identify the functions and feature subsets included in the planned usage.
Consider technical properties that may influence confidence, such as:

- determinism;
- traceability;
- diagnostic behavior;
- reproducibility;
- handling of invalid input; and
- dependency on external components or services.

### Anomalous conditions and known malfunctions

Plan how expected behavior under anomalous operating conditions, known
malfunctions, limitations, workarounds, and countermeasures will be documented
and communicated.

The plan should identify where this information will be maintained and how users
will be informed when it changes.

### Validation work products

When software-tool validation is selected as a qualification method, plan the
necessary work products. These may include:

- software tool requirements;
- a software tool architecture description;
- a validation or test strategy;
- test plans and test cases; and
- test results.

The detailed content belongs in the corresponding specifications, plans, and
reports rather than in LLVM-QUAL-TPL-002.

## Planning the confidence strategy

The planning summary should state the overall approach clearly.

Tool classification is based on an analysis of the risks associated with
the tool usage and determines the necessary confidence level or qualification
needs. Depending on the outcome, one or more qualification methods may then be
selected and performed.

An alternative strategy may be used where justified. The strategy should be
consistent with:

- the role of the tool in the safety lifecycle;
- how tool malfunctions could affect safety-related activities;
- the likelihood that malfunctions will be prevented or detected;
- the maximum safety criticality covered by the plan; and
- the availability and feasibility of suitable qualification methods.

## Related work products

The LLVM Qualification Working Group template set uses the following mapping:

| Work product | Template | Role |
|---|---|---|
| Tool usage plan | `LLVM-QUAL-TPL-002` | Plans the scope, activities, responsibilities, and evidence. |
| Tool classification report | `LLVM-QUAL-TPL-003` | Documents the classification and supporting risk analysis of the tool usage. |
| Tool qualification report | `LLVM-QUAL-TPL-004` | Documents the selected qualification methods and the results of applying them. |
| Safety manual | `LLVM-QUAL-TPL-005` | Communicates the usage envelope, assumptions, restrictions, limitations, and complementary measures. |

Additional plans, specifications, manuals, test evidence, or
configuration-management records may be referenced as appropriate.

## Planning tool classification

The analysis supporting tool classification should examine potential tool
failure modes and their effects in the intended or given usage context.

The plan should identify how this analysis will address, as applicable:

- potential tool malfunctions;
- effects on safety-related development activities and work products;
- prevention and detection measures;
- assumptions concerning downstream reviews or verification;
- the resulting tool confidence or classification; and
- the need for qualification activities.

The results may be documented using LLVM-QUAL-TPL-003.

## Planning tool qualification

Where qualification is required and feasible, identify the selected methods,
their objectives, scope, responsibilities, input evidence, and expected output
evidence.

Qualification methods may include, 
**depending on the applicable standard and usage context**:

- validation of the software tool;
- increased confidence from the development process;
- evaluation of the tool development process;
- "proven-in-use" or service-history evidence;
- independent output verification; or
- other justified combinations of technical and process measures.

The plan should not claim qualification before the selected activities have
been completed and their results assessed. The results may be documented using
LLVM-QUAL-TPL-004.

## Planning the safety manual

Plan how usage constraints and guidance will be communicated to users,
regardless of whether qualification activities are performed.

The safety manual should consolidate information users need to apply the tool
within the evaluated or qualified usage envelope, including:

- intended usage and supported configurations;
- assumptions and dependencies;
- known limitations and malfunctions;
- required workarounds or complementary measures;
- output-verification expectations; and
- conditions that invalidate or limit the available confidence evidence.

These elements may be documented using LLVM-QUAL-TPL-005.

## Reviews, independence, and responsibilities

Identify who is responsible for producing, reviewing, approving, and
maintaining each planned work product.

Where an applicable safety standard or organizational process expects
independence, document the required degree of independence and how it will be
achieved.

For open-source tools, responsibilities may be distributed among upstream tool
developers, downstream integrators, tool providers, qualification service
providers, and project teams. The plan should distinguish evidence supplied by
others from activities performed for the specific usage context.

## Completion and acceptance

Define objective criteria for considering the plan and its resulting work
products complete. At minimum, confirm that:

- planned activities have been performed or justified as not applicable;
- planned work products exist and have been reviewed;
- open findings and limitations are recorded;
- conclusions remain consistent with the defined scope and assumptions; and
- the resulting constraints and responsibilities are communicated to users.

## Updates and change management

Define the events that require the plan, classification report, qualification
evidence, or safety manual to be reviewed. Examples include:

- a new tool version or significant tool change;
- a change in configuration or feature subset;
- a change in the execution environment or dependencies;
- a new use case or project context;
- a change in the maximum safety criticality;
- new known malfunctions or corrected defects; or
- changes to output-verification or other complementary measures.

Not every change requires complete repetition of all activities. Perform and
document an impact analysis to determine which evidence remains valid and which
activities must be repeated or extended.

## What this template does not do

LLVM-QUAL-TPL-002 does not:

- determine whether confidence evidence is required;
- classify the software tool usage;
- qualify or certify the software tool;
- demonstrate compliance with a functional safety standard;
- demonstrate suitability for a particular safety integrity level; or
- replace project-specific planning or applicable safety standards.

It is a planning template intended to support a transparent, proportionate, and
traceable approach to confidence in the usage of software tools.
