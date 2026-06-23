# Notes - January 2026

## Participants - Tuesday 2026/01/06, 13:00 UTC, 1h

- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
- [@petbernt](https://discourse.llvm.org/u/petbernt)
- [@uwendi](https://discourse.llvm.org/u/uwendi)
- [@ZakyHermawan](https://discourse.llvm.org/u/zakyhermawan)

## Agenda

[LLVM Qualification WG sync-ups meeting minutes](https://discourse.llvm.org/t/llvm-qualification-wg-sync-ups-meeting-minutes/87148/19) [Community](https://discourse.llvm.org/c/community/20)

## Links

[docs.google.com](https://docs.google.com/presentation/d/1jthEfQcBt_1t7pOpkEzs4Wdt7WcpLr7rzqd0Q61mHlA/edit?slide=id.p1#slide=id.p1)

[202601\_llvm\_qual\_wg](https://docs.google.com/presentation/d/1jthEfQcBt_1t7pOpkEzs4Wdt7WcpLr7rzqd0Q61mHlA/edit?slide=id.p1#slide=id.p1)

[Google Drive](https://drive.google.com/drive/folders/1u5CqCaRz1-RBrsEHfxSuHHp0WPwXt-Hj)

[Templates - Google Drive](https://drive.google.com/drive/folders/1u5CqCaRz1-RBrsEHfxSuHHp0WPwXt-Hj)

## Highlights

- **Libraries Qualification Process:**

  - Seeking feedback from a relevant group in the community might be beneficial (e.g. subgroup in the Clang C/C++ WG?), especially if they have prior experience with improving testing.
  - Move forward with creating a small example as part of a PR to communicate the objective of the process more clearly. Start the work on a PoC using the existing example, potentially refining it.
  - The discussion around the PoC included refining an example function and planning follow-up functions. We will include proposed folder modifications in the PoC to elicit feedback from maintainers through the PR process, especially regarding naming conventions.
  - Other suggestions:
    - Create a commit on a cloned repository for internal review before making a PR.
    - Draft the process as a workflow, with steps and I/Os.
- **Note on Standards and Templates:**
  - Keep the process documentation free of excessive standards jargon to avoid deterring potential contributors.
  - Regarding ongoing work on templates, [only one template](https://docs.google.com/document/d/1rT1ozdPkSGi63PJUhTdjVAqZxjrmECQSdlevF6-_JOY/edit?tab=t.0) has been started but five others remain to be written, with a goal of keeping them simple by adding guidelines and examples directly within the Markdown comments.
  - An initial template confusion was resolved by changing the wording to reflect that it was meant to determine the need for evaluation and qualification, not the evaluation report itself.
- **LLVM Development Process and External Checklists:**
  - Presented [findings](https://www.researchgate.net/publication/398600910_What_ELISA's_Lighthouse_OSS_Best_Practices_Reveal_About_LLVM's_State_of_Practice) on the LLVM development process concerning an ELISA checklist, noting areas like governance and community were strong, but quality assurance and engineering discipline were only “so so” due to inconsistent pre-merge peer review.
  - [LLVM has already been self-assessed](https://www.bestpractices.dev/en/projects/8273/passing) against the [Open Source Security Foundation (OpenSSF) checklist](https://www.bestpractices.dev/en) by Tom Stellard in 2024, achieving green status on the passing badge but showing non-completion in areas for the silver and gold badges.
  - Next step is to compare the evaluation using the ELISA checklist with Tom Stellard’s detailed assessment and potentially contact Tom for clarification, as evaluating the development process is a key complementary method to testing and validation for qualification.
- **External Interest and Templates:** two companies (one of them is [Quadric](https://quadric.io/)) have expressed interest in using the templates. Real project usage of our outputs could help improve our proposals.
- **Reporting Defects in Alive2:** long-pending action of reporting defects found in Alive2 - we have the list of findings and they need to be formally reported, with the goal of completing this task this month before the next meeting.
- **Engagement with LLVM Security Group:**
  - Last two MoMs from the LLVM Security Group mention functional safety and a “testability problem”.
  - Take the initiative to contact them to explore potential collaboration, particularly regarding test traceability.
- **Need for High-Level Guidance for Onboarding:**
  - Need for higher-level guidance, such as a visual flow or simple framework, to help potential users self-assess their needs and navigate the templates.
  - This guidance, including a possible questionnaire, could be integrated into the existing tutorial on mapping projects and ISO 26262 clauses.

## Actions / Next steps

- [@petbernt](https://discourse.llvm.org/u/petbernt) :
  - Start a small proof of concept for one function using the same example from the slides, including proposed folder modifications, and refine it internally before creating a pull request.
  - Contact Peter Smith to discuss the security group’s minutes mentioning functional safety and test traceability, and inform our group on Discord about how to proceed.
- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez) :
  - Report the list of findings of defects in Alive2 before the next meeting this month.
- [@uwendi](https://discourse.llvm.org/u/uwendi) :
  - Review Tom Stellard’s LLVM self-assessment against the OpenSSF checklist, compare it with her notes, and potentially contact Tom.
  - Continue writing the templates, making them as simple as possible with comments, guidelines, and examples.
  - Contact Aaron to find out if there is a subgroup about C/C++ libraries, then inform [@petbernt](https://discourse.llvm.org/u/petbernt)
  - Draw the workflow for the libraries qualification process, then share with [@petbernt](https://discourse.llvm.org/u/petbernt)
- All:
  - Review [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)‘s tutorial + mapping with the projects and ISO 26262 clauses. Add comments and suggestions directly in the document.
