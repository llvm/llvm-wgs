> [!NOTE]
> **Template provided by:** [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)  
> **Document identifier:** `LLVM-QUAL-TPL-004`  
> **Usage guide:** [LLVM-QUAL-TPL-004-guide.md](LLVM-QUAL-TPL-004-guide.md)
>
> This template is provided for guidance and does not replace applicable safety standards.

# Tool Qualification Report for `<Tool_Name>`

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

## Identification and inputs

| Item | Value |
|---|---|
| Tool name | `<Tool_Name>` |
| Tool version (optional) | `<Tool_Version>` |
| Related Tool Usage Plan | `<Reference to LLVM-QUAL-TPL-002>` |
| Related Tool Classification Report | `<Reference to LLVM-QUAL-TPL-003>` |
| Qualification perspective | `<Upstream project / Tool provider / Downstream distributor / Integrator / Project-specific user / Other>` |

> [!NOTE]
> The referenced Tool Usage Plan is the source for the tool identity, version, configuration, environment, intended or given usages, assumptions, constraints, planned approaches, independence arrangements, and acceptance criteria.
>
> The Tool Classification Report is the source for the use-case classifications, malfunction analyses, control assumptions, and identified qualification needs.
>
> Reference those sources instead of duplicating them here.

> [!IMPORTANT]
> This template assumes that the qualification activities are performed in accordance with the Tool Usage Plan referenced above.
>
> One TPL-004 report is governed by one TPL-002 revision.
> If a different Tool Usage Plan applies to another tool version or usage boundary, prepare a separate TPL-004 report for that plan.
>
> If a change to any of these planned elements is required, TPL-002 should be updated before the affected qualification activity continues or the qualification conclusion is established.
> Changes affecting the classification basis, malfunction analysis, or required controls shall also be reflected in TPL-003.
>
> Unexpected deviations encountered during execution are expected to be recorded in this report, then either be resolved by performing the activity in accordance with the plan or addressed through a plan update before the qualification conclusion is established.

## Qualification activity summary

> [!TIP]
> Summarize each qualification activity and its current status here.
> Use the standard-specific activity name from the plan.
> Record the detailed execution and results in the corresponding activity record.

| Activity ID and name | Reference | Status or result |
| --- | --- | --- |
| `QMA-<ID>` — `<Qualification activity>` | `<Applicable TPL-002 section or activity identifier>` | `<Planned / In progress / Complete — Pass / Complete — Conditional / Complete — Fail / Complete — Inconclusive>` |

## Evidence inventory and applicability

> [!NOTE]
> List the controlled evidence actually used by this report.
> A link to changing content, an unbounded branch, a transient dashboard, or an unsupported assertion is not a controlled evidence baseline.

| Evidence ID | Evidence item and exact baseline | Source or owner | Activity, objective, or concern supported | Applicability and limitations | Controlled location |
| --- | --- | --- | --- | --- | --- |
| `QE-<ID>` | `<Item, version, revision, commit, date, or execution identifier>` | `<Source>` | `<QMA, TPL-002 objective, or TPL-003 reference>` | `<Applicable scope, matches, gaps, restrictions, provenance, and review status>` | `<Reference>` |

**Evidence unavailable to downstream users or assessors:**  
`<None / Identify restricted, proprietary, transient, or otherwise unavailable evidence and explain how reviewability is preserved>`

## Coverage and findings

### Coverage

> [!NOTE]
> An individual activity can pass while an overall qualification need remains only partially covered.
> Integrate the results against the objectives and the concerns established by TPL-003.

| Objective or concern | Qualification activities | Evidence | Coverage conclusion and residual action |
| --- | --- | --- | --- |
| `<TPL-002 or TPL-003 reference>` | `<QMA references>` | `<QE references>` | `<Covered / Partially covered / Not covered / Not applicable, with rationale and required action>` |

**Coverage gaps and cross-activity dependencies:**  
`<None / Identify gaps, shared assumptions or evidence, common-cause concerns, impact, and resolution>`

### Issues and findings

> [!TIP]
> Include adverse evidence.
> Do not report only favorable results.

| Finding ID and type | Description and affected scope | Qualification impact and disposition | Required control or follow-up | Status and evidence |
| --- | --- | --- | --- | --- |
| `QF-<ID>` — `<Unexpected tool behavior or incorrect output / Test failure or discrepancy / Process or review finding / Evidence gap / Evidence reuse mismatch / Execution deviation / Other>` | `<Affected use cases, functions, activities, or objectives>` | `<Impact and corrected, accepted, mitigated, deferred, or rejected disposition with rationale>` | `<Constraint, workaround, countermeasure, or corrective action>` | `<Open / Closed and QE references>` |

## Qualification conclusions

> [!IMPORTANT]
> Complete a separate conclusion for each applicable standard.
> Do not infer compliance with one standard from qualification under another.
> Use "qualified" only when the applicable criteria have been satisfied for the stated boundary.

### `<Standard and edition>`

> [!TIP]
> Repeat this section for each applicable standard.

**Qualification activities and principal evidence:**  
`<QMA and QE references>`

**Requirements or interpretation mapping:**  
`<Reference the mapping used to determine completeness and adequacy>`

**Conclusion:** `<Qualified for the stated usage / Qualified with stated conditions / Qualification incomplete / Qualification not established / Other standard-specific result>`

**Rationale:**  
`<Explain why the integrated evidence and acceptance-criteria assessments support this result, including treatment of adverse findings>`

**Mandatory conditions, limitations, and unresolved items:**  
`<None / Conditions, controls, exclusions, open findings, unmet requirements, and resolution plan>`

### Consolidated statement

`<Summarize the standard-specific conclusions>`

## Detailed qualification activity results

> [!IMPORTANT]
> Copy the complete activity chapter below for each qualification activity.
> The Tool Usage Plan remains authoritative for the selected approach and intended activity.
> This report records what was actually executed, the evidence obtained, and the resulting conclusion.

### `QMA-<ID>` — `<Qualification activity name>`

#### Execution identification

**Activity and qualification-basis reference:** `<Applicable TPL-002 section or activity identifier, including its objective and standard-specific qualification basis>`

**Performed by:** `<Name(s), organization(s), and role(s)>`

**Reviewed by:** `<Name(s), role(s), and how the independence arrangement was achieved>`

**Execution period or evidence date:** `<Date or range>`

**Execution or assessment environment:** `<Host, target, platform, infrastructure, harness, external services, tools, and equipment, as applicable>`

**Execution deviations:** `<None / Describe the deviations identified>`

#### Results and evidence

**Results summary:** `<State the outcome of what was performed>`

**Coverage achieved and gaps:** `<Summarize applicable requirements or behavior coverage, input and problem-space coverage, functions, use cases, configurations, conditions, process areas, objective sets, changes, structural coverage where required, exclusions, and gaps>`

**Applicability of reused evidence or third-party assessment, if applicable:** `<Explain how the evidence baseline, scope, environment, use case, integrity or software level, TQL where applicable, assumptions, and assessment or certification scope match the current qualification boundary. Identify mismatches, limitations, and additional activities. Otherwise state "Not applicable".>`

**Issues and findings:**  
`<None / Reference the applicable QF records and briefly summarize any incorrect, unexpected, or otherwise significant results>`

**Detailed evidence references:** `<QE references to test results, traceability, logs, audit records, process artifacts, history analyses, comparisons, certificates, assessment reports, reviews, or other evidence>`

#### Activity conclusion

**Activity result:** `<Pass / Conditional / Fail / Inconclusive>`

**Assessment against the acceptance criteria:**  
`<Explain how the referenced criteria were satisfied or identify each unmet criterion>`

**Residual limitations, dependent controls, and required follow-up:**  
`<None / Limitations, mandatory user or downstream activities, additional evidence, corrective action, re-execution, or usage restriction>`

## Validity and user information

This qualification conclusion is valid only for the defined usage and classification boundaries, the executed tool and evidence baselines, and the mandatory conditions identified by the referenced work products and this report.

**Report-specific limitations or additional conditions requiring review or re-qualification:**  
`<None / Identify limitations or triggers arising from the qualification results>`

**Planned review point or validity period, if applicable:**  
`<Date, release, milestone, or condition>`

**Information to communicate through safety manual or other user documentation:**

- `<supported versions, configurations, environments, and use cases>`;
- `<mandatory installation, configuration, invocation, or integrity checks>`;
- `<required independent reviews, tests, comparisons, or output-verification activities>`;
- `<known issues, limitations, workarounds, and unsupported uses>`;
- `<conditions that invalidate the evidence or require re-evaluation>`;
- `<additional item>`.
