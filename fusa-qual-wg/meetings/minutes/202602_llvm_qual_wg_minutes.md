# Notes - February 2026

## Participants - Tuesday 2026/02/03, 13:00 UTC, 1h

- [@evodius96](https://discourse.llvm.org/u/evodius96)
- [@capitan-davide](https://discourse.llvm.org/u/capitan-davide)
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
- [@kwk](https://discourse.llvm.org/u/kwk)
- [@petbernt](https://discourse.llvm.org/u/petbernt)
- [@uwendi](https://discourse.llvm.org/u/uwendi)
- [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)

## Agenda

![](https://sea1.discourse-cdn.com/flex021/user_avatar/discourse.llvm.org/uwendi/48/25075_2.png)

[LLVM Qualification WG sync-ups meeting minutes](https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148/21) [Community](https://discourse.llvm.org/c/community/20)

> LLVM Qualification Group’s February 2026 Sync-Up Agenda
> Here’s the proposed agenda for our next sync-up meeting:
> Ongoing Actions – Follow-up
> Quick check-in on current actions: what’s progressing, what’s stuck, and what (if anything) needs help or re-prioritization.
> Tool Qualification & Safety Standards – What’s Changing
> Open discussion on recent and ongoing evolutions in safety standards related to tool qualification, and what they may imply for LLVM users and our group’s work.
> Clang …

## Links

[docs.google.com](https://docs.google.com/presentation/d/1hbXKpUSMP1PxCAEZGv8lqMS6EhGgDlOqcS_3PuGjp9k/edit?slide=id.p1#slide=id.p1)

### [202602\_llvm\_qual\_wg](https://docs.google.com/presentation/d/1hbXKpUSMP1PxCAEZGv8lqMS6EhGgDlOqcS_3PuGjp9k/edit?slide=id.p1#slide=id.p1)

LLVM Qualification WG Sync-up meeting #8 February 2026 Focus: WIP & Evolution of FuSa Standards


![](https://us1.discourse-cdn.com/flex021/uploads/llvm/original/3X/0/b/0bccd9ec69dfe94c5e936d7dbff8edc6fa432189.png)
[Google Drive](https://drive.google.com/drive/folders/1u5CqCaRz1-RBrsEHfxSuHHp0WPwXt-Hj)

### [Templates - Google Drive](https://drive.google.com/drive/folders/1u5CqCaRz1-RBrsEHfxSuHHp0WPwXt-Hj)

## Highlights

- Ongoing work on defects detection in Alive2. Found approximately 20 to 30 defects, which [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) is in the process of documenting and reporting.
- Clarification that Alive2 is currently intended to be presented as a confidence-building element and proposed for a test strategy, not for immediate operational use.
- Work started on a workflow for [@petbernt](https://discourse.llvm.org/u/petbernt)’s libraries qualification methodology, but noted the need for clarification on connecting steps and placement of the traceability step. Suggestion: traceability should ideally be iterative and span all artifacts.
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) started a draft generic workflow for the tool user’s perspective, starting from the tool catalog / Software Bill of Materials (SBOM) and detailing steps for commercial, in-house, and open-source tools, including the need to argue why evidence is or is not necessary
- Current direction is to use [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)’s onboarding/tutorial document as the “master guideline“ connecting the different workflows, templates, and standards
- IEC 61508 and ISO 26262 are both expected to be re-edited around 2027. The railways standard was updated recently and not due for another revision yet.
- Tool qualification chapter in ISO 26262 is being revised. It will propose two sub-chapters differentiating qualification activities for the tool developer and the tool user. Good idea provided the definitions are clear. Software component qualification chapter is also being revised. It is expected that the PAS 8926 (pre-existent elements) will be integrated into this chapter.
- Question: Should we restart discussions on Clang conformance? given interest from outside observers
  - One major problem is copyright issues regarding having the specifications openly and replicating the official wording of C or C++ language specifications.
  - Solid Sands acquired Plum Hall, another provider of test kits.
  - Complex subject. It might be discussed with Aaron/Vlad again (value of a full conformance test kit for the broader community, required effort, etc.).

## Actions / Next steps

[@petbernt](https://discourse.llvm.org/u/petbernt) :

- Continue company process to submit upstream contributions to open source projects
- Start a small proof of concept for one library function, before creating a PR
- Contact Peter/Kristof about collaboration with the Security WG
- Communicate with Michael (`libc`) and Louis (`libc++`) - with [@uwendi](https://discourse.llvm.org/u/uwendi) ‘s support

[@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) :

- Continue reporting findings of defects in Alive2
- Continue work with [@uwendi](https://discourse.llvm.org/u/uwendi) to support [@petbernt](https://discourse.llvm.org/u/petbernt) on workflow for the libraries qualification methodology

[@uwendi](https://discourse.llvm.org/u/uwendi) :

- Continue writing the templates TPL-003, TPL-004, TPL-005, and TPL-007
- Revive the discussion: [Where should WG meeting materials live?](https://discourse.llvm.org/t/where-should-wg-meeting-materials-live/88913)
- Call with Aaron about Clang conformance (status check)
- Set up dedicated call with [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) about the tool qualification workflow from the tool user’s perspective
- Set up dedicated call with [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee) about the tutorial / master guideline for onboarding
- *(Delayed)* Review Tom’s LLVM self-assessment against the OpenSSF checklist versus assessment against the checklist from ELISA Lighthouse OSS SIG

[@YoungJunLee](https://discourse.llvm.org/u/youngjunlee) : dedicated call with [@uwendi](https://discourse.llvm.org/u/uwendi) to review the tutorial and mapping document

[@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan) : dedicated call next week with [@uwendi](https://discourse.llvm.org/u/uwendi) to discuss and rework the generic workflow from the tool user’s perspective
