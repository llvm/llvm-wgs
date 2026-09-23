# Standards referenced by the LLVM Qualification Working Group

This page identifies standards referenced throughout the Working Group's documentation.

The applicable standards, editions, amendments, and associated regulatory or organizational guidance depend on the industry, system, jurisdiction, and defined use.
Inclusion in this list does not imply that every standard applies to every LLVM component or use case.

> [!NOTE]
> Standards may consist of several parts that are published separately, and their full text may require purchase or access through a standards subscription.
> Standards can also be amended, consolidated, superseded, or revised over time.
> The links below are provided as entry points to publisher information and may refer to a particular part or edition rather than the complete standard or series.
> Readers should verify with the relevant standards organization which parts, editions, amendments, and associated guidance apply to their project.

> [!TIP]
> For multipart standards, a reference such as `IEC 61508-3:2010` identifies the issuing organization (`IEC`), standard series (`61508`), part (`3`), and publication year of the cited edition (`2010`).
> Other references use different formats, as illustrated by `EN 50716:2023` and `DO-178C`.

| Reference | Title | Publisher information | Main application area | How it can relate to LLVM |
| --- | --- | --- | --- | --- |
| **DO-178C** | *Software Considerations in Airborne Systems and Equipment Certification* | [RTCA software standards](https://www.rtca.org/do-178/) | Airborne software | Defines objectives for software used in airborne systems. Runtime components included in airborne software need to be addressed as product software. |
| **DO-330** | *Software Tool Qualification Considerations* | [RTCA software standards](https://www.rtca.org/do-178/) | Software tools used in high-assurance development | Defines tool-qualification considerations. It applies to supporting tools under defined reliance conditions, not to runtime libraries merely because they are software. |
| **EN 50716** | *Railway applications - Requirements for software development* | [AFNOR — NF EN 50716 (2023)](https://www.boutique.afnor.org/en-gb/standard/nf-en-50716/railway-applications-requirements-for-software-development/fa201031/355192) | Railway applications | Defines requirements for railway software development, including the treatment of software components and supporting tools within the applicable railway lifecycle. |
| **IEC 61508** | *Functional safety of electrical/electronic/programmable electronic safety-related systems* | [IEC 61508-1:2010](https://webstore.iec.ch/en/publication/5515); [IEC 61508-3:2010](https://webstore.iec.ch/en/publication/5517) | General electrical, electronic, and programmable electronic safety-related systems | Provides a cross-industry functional safety framework. LLVM runtime components may form part of safety-related software, while LLVM development tools may require confidence or qualification measures depending on how they are used. |
| **IEC 62304** | *Medical device software - Software life cycle processes* | [IEC 62304:2006](https://webstore.iec.ch/en/publication/6792) | Medical-device software | Defines medical-device software lifecycle processes. Existing software for which adequate development records are unavailable may be treated as "software of unknown provenance", commonly abbreviated as **SOUP**. |
| **ISO 26262** | *Road vehicles - Functional safety* | [ISO 26262-1:2018](https://www.iso.org/standard/68383.html); [ISO 26262-8:2018](https://www.iso.org/standard/68390.html) | Road vehicles | Addresses automotive safety-related software, qualification of some pre-existing software components, and confidence in the use of software tools. |
