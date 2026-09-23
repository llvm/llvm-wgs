# How to Use LLVM-QUAL-TPL-007

## Software Tool List

## Purpose

LLVM-QUAL-TPL-007 provides a simple way to catalog the software tools used in the development of a safety-related system, hardware item, or software item.
It also provides one place from which users can find relevant tool documentation and tool-confidence information.

Although the template is primarily intended to support functional safety activities, the resulting overview may also be useful for security purposes.
For example, it makes the tools, versions, providers, and available documentation visible in one place.

The list is intended to help a project answer practical questions such as:

- Which software tools are being used?
- Which versions are in scope?
- Who provides or develops each tool?
- Where can users find the applicable documentation?
- Has the need for confidence been considered?
- Which planning, evaluation, qualification, or usage information is available?

The list records outcomes and links to information produced through the different activities performed, when applicable.

## Status of this template

Functional safety standards do not prescribe this particular software tool list or require the fields used in LLVM-QUAL-TPL-007.
The template is an optional organizational aid.

Depending on the applicable standard and project context, some of the underlying decisions or work products referenced by the list may still be needed.
Always consult the applicable requirements.

The information may be managed in any form that works for the project.
For example, a project may use Markdown, a spreadsheet, a database, an application lifecycle management system, or a configuration management system.
The fields may be renamed, separated, combined, or extended.

## When to use the template

Use LLVM-QUAL-TPL-007 when a project would benefit from a shared overview of its software tools and the available confidence information for each one.

The list can be useful for:

- making the tools used by a project visible;
- finding tool documentation and confidence artifacts;
- identifying missing or unfinished information;
- checking whether a tool or version change may require existing information to be revisited; and
- supporting communication among developers, safety engineers, assessors, and other interested parties.

## Define the scope

State what the list covers before adding tools.
The scope may be a complete project, one product or component, a lifecycle phase, a team, or another clearly defined boundary.

For functional safety purposes, include at least the software tools that support activities or tasks in the applicable safety lifecycle.
The relevant activities depend on the industry and applicable functional safety standard.
Consult the applicable standard when defining the scope.

Examples may include:

- compilers, assemblers, linkers, and build tools;
- code generators;
- requirements, design, and configuration management tools;
- static analysis and verification tools;
- test tools and test environments; and
- continuous integration and automation tools.

Additional tools may be included when useful for security or other project needs.
The list does not have to include every general-purpose utility used by every project member.
Define and apply criteria that are appropriate for the project.

## Complete the tool list

Add one row for each tool within the defined scope.
The following guidance explains the suggested fields.

| Field | What to record |
|---|---|
| **Tool name** | The name used to identify the software tool. |
| **Version(s)** | The exact version, approved set of versions, revision, or other identifier used by the project. If different versions have different documentation or confidence information, consider using separate rows. |
| **Provider / Developer** | The organization responsible for providing or developing the tool, such as an in-house team, commercial vendor, or open-source project. |
| **Documentation** | Links to documentation that applies to the listed version or versions. Include the user manual and release notes when available. Other useful links may include installation instructions, configuration guidance, known issues, or change logs. |
| **Confidence decision** | The outcome of the determination of need for confidence and a link to the supporting record, such as a completed LLVM-QUAL-TPL-001. When further confidence evidence is not needed, this field may also link to the corresponding justification or disclaimer, such as information based on LLVM-QUAL-TPL-006. |
| **Usage plan** | A link to the tool usage plan or equivalent planning information, such as a completed LLVM-QUAL-TPL-002. |
| **Classification** | A link to the classification record, such as a completed LLVM-QUAL-TPL-003. |
| **Qualification** | Whether tool qualification is needed for the defined usage (use **To be determined** while the decision is still open), and link to the qualification report (such as a completed LLVM-QUAL-TPL-004) when qualification is needed. |
| **Safety manual** | A link to the safety manual or equivalent guidance for appropriate use, such as information based on LLVM-QUAL-TPL-005, when available. |
| **License and notes** | Optionally record the license type or a link to the applicable license. This field may also contain other project-relevant information that does not fit elsewhere. |

The linked information does not have to use the LLVM Qualification Working Group templates or have the same document names.
Link to the records actually used by the project.

License information may be relevant to project governance, distribution, or reuse, but it does not by itself establish confidence in the usage of a tool.

## Record unavailable or non-applicable information

Do not leave a field blank when its status matters.
Use a short, clear value, for example:

- **Not started** - the activity or document is planned but has not begun;
- **In progress** - work has begun but is not complete;
- **Not available** - the information is not currently available; or
- **Not applicable** - the information is not needed for the defined usage.

For example, if the confidence decision concludes that further confidence activities are not needed, the usage plan, evaluation report, qualification report, and safety manual fields may be marked **Not applicable**, as appropriate.

## Keep the list useful

Update the list when relevant information changes, for example when:

- a tool is added or removed;
- the project adopts a different tool version;
- the intended or given usage changes;
- linked documentation or confidence information is added or updated; or
- an open decision is completed.

The project may choose any practical way to maintain the list.
For example, ordering the list alphabetically can be useful.
