> [!NOTE]
> **Template provided by:** [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)  
> **Document identifier:** `LLVM-QUAL-TPL-003`  
> **Usage guide:** [LLVM-QUAL-TPL-003-guide.md](LLVM-QUAL-TPL-003-guide.md)
>
> This template is provided for guidance and does not replace applicable
> safety standards.

# Tool Classification Report for `<Tool_Name>`

> [!TIP]
> Replace text shown as `<placeholder>` with the applicable information. Remove unused alternatives and instructional callouts when completing the report.

| Document information | Value |
| --- | --- |
| Organization / team name | `<Owner>` |
| Version | `<X.Y>` |
| Date | `<YYYY-MM-DD>` |

## Identification

| Item | Value |
|---|---|
| Tool name | `<Tool_Name>` |
| Tool version (optional) | `<Tool_Version>` |
| Related Tool Usage Plan | `<Reference to LLVM-QUAL-TPL-002>`

> [!TIP]
> The referenced Tool Usage Plan is the authoritative source for the tool identity, version, configuration, environment, intended or given usages, assumptions, constraints, and other usage-planning information. Do not duplicate that information here.

## Classification scope and basis

### Scope

**Purpose of this classification:**  
`<State why the tool usage is being classified and what decision or subsequent activity the report supports>`

The scope of this report consists of the use cases listed in Section [Classification summary](#classification-summary) and defined in the referenced Tool Usage Plan.

**Classification-specific scope adjustment, if any:**  
`<Record only an adjustment needed for this classification. Otherwise state "None". Update TPL-002 if the intended or given usage itself changes.>`

### Applicable standards and classification schemes

> [!TIP]
> Record the exact standard edition used. If several standards apply, derive and document each result separately.

| Standard and edition | Applicable clause or scheme | Expected result (optional) |
| --- | --- | --- |
| `<Standard and edition>` | `<Clause or organization-specific interpretation>` | `<For example, T1/T2/T3 or TCL1/TCL2/TCL3>` |

### Method and analysis boundaries

This report classifies defined tool usages by analyzing credible tool malfunctions or erroneous behavior, their potential effects, and the control measures applicable to the tool outputs.

The analysis is performed at the use-case level unless decomposition into relevant functions or features is needed.

**Additional method assumptions or tailoring:**  
`<Describe any project-specific interpretation, analysis exclusions, or aggregation rule>`

## Classification summary

> [!TIP]
> Keep this table concise. Detailed rationale belongs in the corresponding use-case chapter. Add one row per use case or independently classified function group.

| ID and use case | Analysis granularity | Standard-specific result | Further action | Status |
| --- | --- | --- | --- | --- |
| `<UC-ID - Use-case name>` | `<Use-case / Function or feature>` | `<Classification result>` | `<None / TPL-004 / Added control / Usage constraint / Investigation>` | `<Complete / Open>` |

**Report-level aggregation rule:**  
`<Explain how use-case or function-level results are consolidated, where an overall classification is required>`

**Overall classification result, if applicable:**  
`<Result and short rationale, or state that classifications remain use-case-specific>`

## Use-case classification analyses

> [!IMPORTANT]
> Copy the complete use-case chapter below for every use case. Select either use-case-level analysis or function/feature-level analysis within each chapter, and remove the unused option. A single report may use different granularities for different use cases.

### `<UC-ID>` - `<Use-case name>`

#### Use-case characterization

**Description and objective:**  
`<Describe what the user intends to accomplish with the tool>`

**Supported activity, decision, or work product:**  
`<Identify the safety-related lifecycle activity, task, decision, or artifact supported by this use>`

**Inputs:**  
`<Identify source artifacts, data, commands, options, configuration, environmental inputs, or other information supplied to the tool>`

**Input assumptions and constraints:**  
`<State assumptions about validity, completeness, format, provenance, allowed ranges, or permitted usage>`

**High-level processing:**  
`<Describe the transformation, generation, analysis, verification, or decision performed>`

**Outputs:**  
`<Identify generated or modified artifacts, results, diagnostics, reports, status values, or decision inputs>`

**Functions or features used:**  
`<List the relevant functionality exercised by this use case>`

**Output consumers and intended reliance:**  
`<Identify who or what consumes each relevant output, how it is used, and whether it is trusted without further examination>`

**Existing subsequent verification or controls:**  
`<Describe reviews, tests, comparisons, independent verification, or other controls applied before the output is relied upon>`

**Excluded functionality or output:**  
`<Identify features, processing paths, outputs, or configurations outside this use-case classification>`

#### Selected analysis granularity

**Selected granularity:** `<Complete use case / Function or feature level>`

**Rationale:**  
`<Explain why the selected level is sufficient to identify materially different malfunctions, effects, controls, and classification results>`

#### Malfunction analysis

> [!TIP]
> Analyze one or more credible potential malfunctions at either granularity. Select the analysis boundary independently from the record presentation: detailed malfunction subsections and a compact table are both acceptable. Adapt the structure consistently to the complexity and preferences of the author, and remove unused guidance.

**Option A — Use-case-level analysis**

> [!TIP]
> Apply the malfunction records directly to the complete use case when its relevant functions, effects, outputs, controls, and classification results can be analyzed together.

**Option B — Function or feature-level analysis**

> [!TIP]
> Add and repeat the following subsection when decomposition into relevant functions or features is useful. Place the malfunction records within the corresponding function or feature subsection.

##### `<Function ID>` - `<Function or feature name>`

**Function or feature objective:**  
`<Describe the behavior within the parent use case>`

**Relevant inputs and assumptions:**  
`<Identify the subset of inputs and assumptions relevant to this function or feature>`

**Processing and contribution to the use-case output:**  
`<Describe the processing performed and the resulting output or contribution>`

**Malfunction record presentation (applicable to either option)**

> [!TIP]
> Choose either Format 1 or Format 2. For Option A, place the records directly under the complete use case. For Option B, place them within each relevant function or feature subsection. A report may use the detailed format where explanation is needed and the compact format for simpler analyses.

**Format 1 — Structured malfunction subsections**

> [!TIP]
> Copy the following subsection for each credible malfunction. Adjust the heading level when the record is nested under a function or feature subsection.

##### Malfunction record `<M-ID>` - `<Short malfunction name>`

**Potential malfunction or erroneous behavior:**  
`<Describe an incorrect, incomplete, missing, spurious, stale, inconsistent, misleading, or otherwise erroneous behavior>`

**Relevant inputs, conditions, or processing:**  
`<Identify the inputs, configuration, processing stage, or operating condition associated with the malfunction>`

**Potential effect and propagation or reliance path:**  
`<Describe the effect and explain how the erroneous result could reach or influence a safety-related artifact, activity, or decision>`

**Prevention measures:**  
`<Describe measures intended to prevent the malfunction, invalid input, invalid configuration, or prohibited use>`

**Detection measures:**  
`<Describe measures intended to detect the erroneous result before it is relied upon>`

**Confidence in the measures:**  
`<Explain the relevance, coverage, independence, timing, repeatability, supporting evidence, and limitations of the measures or controls>`

**Remaining concern:** `<None identified / Controlled under stated assumptions / Additional evidence or control needed / Undetermined>`

**Required action or usage constraint:**  
`<State any added control, investigation, qualification activity, restriction, or documentation action>`

**Format 2 — Compact malfunction table**

> [!TIP]
> Use this format when each entry can remain concise. Add one row per malfunction. If the cells become paragraph-heavy or obscure the reasoning, it is recommended to use Format 1 instead.

| ID, malfunction, and relevant conditions | Potential effect and propagation | Prevention measures | Detection measures | Confidence | Remaining concern and action |
| --- | --- | --- | --- | --- | --- |
| **`<M-ID>`** - `<Malfunction, inputs, conditions, or processing>` | `<Effect and reliance path>` | `<Measures>` | `<Measures>` | `<Rationale and limitations>` | `<Status, action, or constraint>` |

#### Classification conclusion

| Standard and edition | Classification |
| --- | --- |
| `<Standard and edition>` | `<For example, TCL or tool class>` |

**Further confidence-building or qualification action:**  
`<None identified / Required through LLVM-QUAL-TPL-004 / Undetermined, with rationale>`

**Mandatory usage constraints:**  
`<List constraints necessary for the classification to remain valid>`

**Information to communicate to users:**  
`<List limitations, required checks, known anomalies, or safety-manual content to address through LLVM-QUAL-TPL-005 or other documentation>`

**Open questions or actions:**  
`<List unresolved items, owners, and target dates>`

## Overall conclusion and follow-up

**Conclusion:**  
`<Summarize the classifications established for the included use cases and the principal rationale>`

**Usages for which no additional qualification action is identified:**  
`<List the use cases and the conditions supporting this conclusion>`

**Usages requiring further confidence-building or qualification:**  
`<List the use cases and reference the corresponding LLVM-QUAL-TPL-004 activities>`

**Required usage constraints and user information:**  
`<List items to carry into LLVM-QUAL-TPL-005, user documentation, or project procedures>`

**Unresolved classification items:**  
`<List items that remain undetermined and how they will be resolved>`

## Validity, limitations, and re-evaluation

This classification is valid only for the tool versions, configurations, use cases, environments, assumptions, output reliance, and control measures defined in the referenced Tool Usage Plan and the applicable use-case analyses in this report.

**Known limitations:**  
`<State limitations of the analysis, evidence, or classification>`

**Conditions requiring review or re-evaluation:**

- a change to the tool version, revision, configuration, enabled feature set, or dependencies;
- a change to the intended or given use, inputs, processing, outputs, output consumers, or reliance on the outputs;
- a change to prevention, detection, correction, review, test, or independent verification measures;
- a new or changed limitation or known tool issue relevant to the classified use;
- a change to the operating environment, target, development process, applicable integrity level, standard, or standard edition;
- `<Additional project-specific trigger>`.

**Planned review point or validity period, if applicable:**  
`<Date, release, milestone, or condition>`
