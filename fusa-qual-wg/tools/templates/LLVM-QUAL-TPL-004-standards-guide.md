# Standards Companion to LLVM-QUAL-TPL-004 — Qualification Concepts and Test Coverage

> [!NOTE]
> **Guidance provided by:** [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)  
> **Related template:** `LLVM-QUAL-TPL-004`  
> **Central guide:** [`LLVM-QUAL-TPL-004-guide.md`](LLVM-QUAL-TPL-004-guide.md)  
> **Qualification-approaches companion:** [`LLVM-QUAL-TPL-004-qualification-approaches-guide.md`](LLVM-QUAL-TPL-004-qualification-approaches-guide.md)  
> This companion is informative.
> It compares concepts to support interpretation; it does not replace any standard, regulatory guidance, certification authority, or documented organizational interpretation.

## Purpose and limits of this comparison

The standards covered here do not all define software-tool qualification in the same way:

- IEC 61508 (E/E/PE systems) uses tool classes, conformance evidence, SIL-graded techniques and measures, and effective controls;
- EN 50716 (railways) uses tool classes and an evidence-and-control model focused on avoiding, detecting, or handling tool-induced failures;
- ISO 26262 (automotive) defines a tool-confidence classification and named software-tool qualification methods;
- IEC 62304 (medical) does not define a comparable tool-qualification scheme; and
- DO-178C and DO-330 (airborne) define qualification as the process used to obtain certification credit through a TQL-dependent, objective-based lifecycle.

Accordingly, this guide set uses **qualification approach** as an umbrella expression.
A selected approach whose execution or evidence is recorded in TPL-004 can be a:

- qualification method;
- standard-recognized technique or measure;
- conformance-evidence route;
- effective control or mitigation route;
- objective-based qualification lifecycle; or
- reuse and applicability assessment for existing evidence.

Retain the terminology of the applicable standard in the report.
Similar labels, such as "T3" or "validation", do not establish equivalence across standards.

## Meaning of tool qualification or confidence under each standard

### IEC 61508 (E/E/PE systems)

IEC 61508-3 does not organize tool confidence as a menu of qualification methods comparable to ISO 26262.
Its support-tool provisions are better understood as a structured argument about selection, reliance, conformance, and control.

For a bounded tool usage, the practical reasoning is:

1. justify selection of the tool;
2. classify the usage as T1, T2, or T3;
3. define or identify the specification, product documentation, instructions, and constraints needed for relevant T2 and T3 usages;
4. assess reliance on the tool and the failure mechanisms that could affect the safety-related software;
5. for relevant T3 usage, establish evidence that the tool conforms to its specification or documentation;
6. use an appropriate combination of tool validation and a history of successful use in similar applications and environments where applicable;
7. where adequate conformance evidence is unavailable, implement effective measures to control failures attributable to the tool; and
8. configuration-manage the tool, version, configuration, options, scripts, and qualification status.

IEC 61508-3 Annex A also identifies **certified tools and certified translators** and **tools and translators with increased confidence from use** as techniques or measures.
The certificate still needs to be interpreted together with its scope, supporting assessment, restrictions, and requirements.

From an IEC 61508 perspective, a TPL-004 conclusion should therefore explain why the conformance evidence and effective controls are adequate for the stated T class, SIL context, tool baseline, functions, environment, and reliance.

Relevant provisions include IEC 61508-3:2010, Clause 7.4.4 and Annex A, including Table A.3.
Consult the controlled copy used by the project.

### EN 50716 (railways)

EN 50716 uses an evidence-and-control model for support tools.
Its central concern is whether a tool can introduce an error or fail to detect an error in safety-related software activities, and whether that failure is prevented, detected, or otherwise adequately handled.

For a bounded tool usage, the practical reasoning includes:

1. justify the tool selection and T1, T2, or T3 classification;
2. identify potential erroneous outputs or failures to detect errors;
3. define the relevant tool specification, manual, usage instructions, and constraints;
4. establish output-conformance evidence, failure-detection evidence, or both;
5. select suitable evidence or controls for the applicable SIL and use;
6. validate the relevant tool functions and operating conditions where tool validation is selected;
7. consider history of successful use in sufficiently comparable applications and environments where applicable;
8. use independent output verification, manual-process equivalence, or tool diversity where these form part of the accepted approach;
9. justify applicable process-compliance evidence or another appropriate method where the standard permits it; and
10. configuration-manage the complete tool baseline and reassess changes.

A TPL-004 conclusion under EN 50716 should state how the selected evidence and controls demonstrate that the relevant tool-induced failures are acceptably avoided, detected, or handled for the stated T class, SIL, usage, and conditions.

Relevant provisions include EN 50716:2023, Clause 6.7 and related SIL-dependent provisions.
Consult the controlled copy used by the project.

### ISO 26262 (automotive)

ISO 26262-8 defines a distinct "confidence in the use of software tools" process.
TPL-003 records the Tool Impact, Tool Error Detection, resulting Tool Confidence Level, and applicable ASIL boundary for each defined use case.
Where qualification is required, TPL-004 records the selected method or combination and its results.

ISO 26262:2018 identifies four software-tool qualification method families:

- increased confidence from use;
- evaluation of the tool development process;
- validation of the software tool; and
- development in accordance with a safety standard.

Method selection depends on the TCL and applicable ASIL.
Consult the exact recommendation tables and required method combinations in the applicable edition.

Qualification remains usage-specific.
The result applies to the defined tool functions, version, configuration, environment, inputs, outputs, assumptions, and complementary measures.
A provider package or previous qualification can support the result only after applicability has been demonstrated.

A TPL-004 conclusion under ISO 26262 should state which qualification method combination was applied, how it satisfies the TCL/ASIL-dependent expectation, what evidence supports it, and which usage conditions remain mandatory.

Relevant provisions include ISO 26262-8:2018, Clause 11.

### IEC 62304 (medical)

IEC 62304 is a lifecycle-process standard for medical-device software.
It does not define a peer software-tool qualification framework with:

- development-tool classes;
- a tool-confidence decision flow;
- tool qualification levels;
- a catalogue of acceptable tool qualification methods; or
- a prescribed tool qualification report.

Its software safety Classes A, B, and C apply to the medical-device software, not to the development or verification tools.

Confidence in tools used in medical-device work is normally established through the wider quality-management and regulatory framework.
Depending on the jurisdiction and tool purpose, this can require risk-based validation of software used in production or the quality management system, control of suppliers, configuration and change control, and objective evidence that the software performs as intended.

For example, current FDA Computer Software Assurance guidance addresses software used in medical-device production or the quality management system.
It supports a risk-based approach and a range of assurance activities, but it does not turn those activities into IEC 62304 qualification methods and does not apply as a complete tool-assurance framework for medical-device software development tools.

If TPL-004 is used in a medical-device context, the report should therefore identify the actual regulatory, QMS, or organizational requirement that creates the validation obligation.

### DO-178C / DO-330 (airborne)

DO-178C defines tool qualification in terms of obtaining "certification credit" for a software tool in the context of a specific airborne system.
Qualification becomes relevant when the project relies on a tool to eliminate, reduce, or automate lifecycle processes and the relevant errors are not independently detected by another process.

The tool usage is evaluated against three criteria:

- **Criterion 1:** the tool output is part of the airborne software and can introduce an error;
- **Criterion 2:** the tool automates verification and its result is used to eliminate or reduce other verification or development processes; and
- **Criterion 3:** the tool can fail to detect an error within the intended usage without meeting the stronger Criterion 2 conditions.

The tool criterion and airborne software level determine a Tool Qualification Level from TQL-1 through TQL-5.
Consult DO-178C and the applicable certification-authority guidance for the exact mapping.

DO-330 then supplies a complete, TQL-dependent set of qualification objectives, activities, independence expectations, and lifecycle data.
Qualification is therefore not performed by choosing one alternative method such as validation or prior use.
Operational requirements and verification are central, while progressively stronger development and verification objectives apply at higher TQLs.

Independent verification of the relevant tool output can change the need for qualification because it changes the certification credit claimed from the tool.
If the independent process fully performs the activity otherwise eliminated, reduced, or automated, qualification may be unnecessary.
This is a decision about reliance and credit, not merely a compensating test added after qualification.

A TPL-004 conclusion under DO-178C/DO-330 should state the intended use, criterion, airborne software level, TQL, applicable DO-330 objective set, lifecycle data, deviations, change-impact analysis, and certification-authority coordination.
Vendor qualification data is reusable only after the applicant establishes applicability to the certification project.

## Comparison of confidence approaches and concepts

The following table is an interpretive map.

| Confidence approach or concept | IEC 61508 | EN 50716 | ISO 26262 | IEC 62304 | DO-178C / DO-330 |
| --- | --- | --- | --- | --- | --- |
| Core assurance model | Tool selection, T1/T2/T3 classification, conformance evidence, SIL-graded techniques/measures, and effective controls | T1/T2/T3 classification plus evidence or controls that avoid, detect, or handle tool-induced failures | TI/TD classification produces TCL; TCL and ASIL drive named qualification methods | No tool-qualification model; medical-device software lifecycle plus surrounding QMS/regulatory validation obligations | Certification-credit decision, tool criterion, software level, TQL, and TQL-dependent objectives/lifecycle data |
| Tool validation | Explicit route for relevant conformance evidence | Explicit evidence route with validation-report expectations | Explicit qualification method | Not defined as an IEC 62304 method; risk-based validation may be required by the surrounding framework | Operational and requirements-based verification is central within the DO-330 objective set |
| Prior successful use | History of successful use in similar applications and environments; increased confidence from use is also an Annex A technique/measure | History in comparable applications and environments can contribute | Explicit increased-confidence-from-use method | Not a named method; operational history and supplier evidence may contribute to a risk-based validation argument | Not a general replacement for applicable objectives; prior qualification data can be reused after applicability and change-impact analysis |
| Evaluation of the tool development process | Can contribute to confidence or certification evidence, but is not an identically named standalone route | Process and SIL-compliance evidence can contribute under the applicable route | Explicit qualification method | Not a named method; supplier or process assessment may support the wider QMS validation argument | Development, verification, configuration-management, quality-assurance, and related objectives are built into the applicable DO-330 lifecycle |
| Development in accordance with a safety or assurance standard | Can support certification or other conformance evidence | Applicable process-compliance evidence can contribute | Explicit qualification method | Not defined as a tool-confidence route | DO-330 is itself a dedicated assurance lifecycle for the tool, scaled by TQL |
| Certified tool or translator | Explicitly recognized technique/measure; scope and underlying assessment still require applicability review | Third-party evidence that must be mapped to the Clause 6.7 argument | Evidence that may support one or more of the four methods; not a fifth method | Not an IEC 62304 method; third-party assessment may be supporting evidence | Not a separate method; certification credit depends on project-specific DO-330 compliance and authority acceptance |
| Independent output verification or tool diversity | Can be an effective control and can affect reliance on the tool | Recognized evidence/control route for relevant usages | Usually affects tool-error detection/classification unless tied to an accepted qualification method | Possible risk control, but not an IEC 62304 qualification route | Can remove the need for qualification when it independently performs the activity for which tool credit would otherwise be claimed |
| Effective downstream controls | Explicit fallback where sufficient T3 conformance evidence is unavailable | Explicit failure-detection/control route | Can affect TD and TCL and remain a mandatory usage condition | Product and process controls can support risk-based assurance | Changes the certification credit relied upon and therefore the qualification need |
| Other justified approaches | Suitable combinations of evidence and controls are possible within the IEC requirements | Relatively open to other appropriately justified methods that avoid, detect, or handle failures | Constrained by the method-selection framework | No prescribed catalogue; follow the applicable QMS/regulatory obligation | Alternative means require substantiation and agreement through the certification process |
| Dedicated tool qualification objectives and lifecycle | No separate TQL-style lifecycle | No separate TQL-style lifecycle | No separate tool-development lifecycle; the selected methods are applied | None for tools | Yes; complete TQL-dependent objectives, activities, independence, and lifecycle data |
| Reuse of prior evidence | Reuse requires matching tool, use, environment, SIL context, restrictions, and current known-issue status | Reuse requires a documented applicability assessment | Qualification remains bounded to the intended use and current baseline | Supplier evidence may be reused, but the manufacturer retains responsibility | Reuse requires matching intended use, operational environment, criterion, software level, TQL, baseline, and change impact |

## Test-coverage expectations for software tools

### Distinguish three kinds of coverage

Tool-validation discussions often use the word *coverage* for different questions:

1. **Requirements or behavior coverage** asks which required or expected tool behaviors are addressed by tests and other evidence.
2. **Input and problem-space coverage** asks which use cases, feature interactions, input classes, boundaries, configurations, targets, invalid or unusual conditions, and known malfunction classes were exercised.
3. **Structural coverage of the tool implementation** measures which implementation elements were exercised, such as statements, decision outcomes, conditions, or functions.

These measures are complementary.
A complete requirements-to-test matrix can still be weak if the requirements are incomplete, the tests are superficial, or the oracle is wrong.
High structural coverage can still miss required behavior.
Neither metric alone establishes "adequate validation".

### Cross-standard comparison

| Standard and route | Requirements or behavior coverage | Structural coverage of the tool's own code |
| --- | --- | --- |
| IEC 61508 — tool validation or T3 conformance evidence | Evidence should address the relevant specification or product documentation, used functions, identified failure mechanisms, operating conditions, test cases, results, and discrepancies. Traceability should make the claimed conformance reviewable. | No universal statement, branch, function, or MC/DC target is imposed merely because support-tool validation is used. Structural coverage can become applicable through a selected development or certification basis, or can be added as justified supplementary evidence. |
| EN 50716 — support-tool validation or conformance evidence | Evidence should address the functions, outputs, conditions, and failure possibilities relevant to the classified usage, including the basis for deciding that output conforms or failures are detected. | No universal structural-coverage target is imposed merely by the support-tool validation route. It can apply through a development/process-compliance basis or as selected additional evidence. |
| ISO 26262 — qualification by validation of the software tool | Validation should be based on the tool requirements and qualified usage and should address the relevant functions, malfunctions and consequences, operating environment, and reaction to invalid, unusual, boundary, or other error-related conditions (called anomalous operating conditions in the standard). Requirements-to-test traceability is normally a key adequacy measure. | ISO 26262 does not apply the Part 6 product-software structural-coverage ladder universally to tool validation. Structural coverage can be supplementary or can enter through a development-process or development-in-accordance method whose selected basis requires it. |
| IEC 62304 | IEC 62304 itself specifies no development-tool qualification or coverage scheme. Requirements/behavior evidence for a tool depends on the applicable QMS, regulatory guidance, intended use, and risk. | Not specified for tools by IEC 62304. The surrounding validation framework may justify implementation evidence, but there is no IEC 62304 structural-coverage ladder for tools. |
| DO-178C / DO-330 | Tool Operational Requirements validation and requirements-based verification are central. The required evidence and independence depend on the TQL, intended use, and certification credit. | DO-330 applies TQL-dependent structural coverage to the tool software at the higher TQLs: statement coverage at TQL-3, decision coverage at TQL-2, and MC/DC at TQL-1. The corresponding structural-coverage objective is not generally applicable at TQL-4 or TQL-5. Consult the exact DO-330 Annex A tables and applicable authority guidance. |

### What to record when structural coverage is not required

Absence of a structural-coverage mandate does not reduce tool validation to one row per written requirement.
Record how the validation addresses:

- the completeness and testability of the qualification requirements;
- every function and output within the qualified boundary;
- feature and option interactions relevant to the usage;
- input classes, boundaries, invalid inputs, and unusual or error-related conditions;
- host, target, dependencies, configuration, and operational environment;
- TPL-003 malfunctions and error-propagation paths;
- known issues and defect-regression scenarios;
- the trustworthiness and independence of expected results or test oracles;
- supporting tools, harnesses, comparators, and result processing;
- passed, failed, skipped, blocked, flaky, and not-run tests; and
- remaining gaps, uncertainty, and downstream controls.

If a percentage is reported, define its denominator and exclusions.
“100% requirements coverage” is not meaningful when requirements were omitted, grouped too coarsely, or mapped to tests that do not contain effective checks.

### Structural-coverage terminology

Use structural-coverage terms precisely:

- **statement coverage** measures executed statements and is not necessarily identical to source-line coverage;
- **decision or branch coverage** measures decision outcomes and does not mean that every possible execution path was tested;
- **MC/DC** demonstrates the independent effect of each condition on a decision outcome under the applicable definition; and
- **function or method coverage** shows that functions were invoked but says little about internal decisions or behavior adequacy.

Structural coverage should be recorded when it is:

- required by the applicable standard and qualification level;
- inherited from the selected development or certification basis;
- used to assess the completeness of requirements-based testing; or
- deliberately selected as supplementary evidence.

When it is not applicable, state that explicitly and identify the standard-specific basis rather than reporting an unexplained zero or omitting the topic.

## Using the same evidence under several standards

Shared factual evidence can reduce duplicated work.
For example, one controlled validation execution may provide useful evidence under IEC 61508, EN 50716, and ISO 26262.
Reuse does not make the standards interchangeable.

For each applicable standard:

1. retain its own classification and integrity-level basis;
2. identify the exact method, technique, evidence route, control route, or objective set;
3. map the shared evidence to that basis;
4. identify additional activities or work products needed only by that standard;
5. assess evidence adequacy separately; and
6. state a separate conclusion.

Do not create a combined “highest tool qualification level”.
SIL, ASIL, TCL, T1/T2/T3, software levels, and TQL express different concepts.
