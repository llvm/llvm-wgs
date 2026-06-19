# LLVM Qualification Working Group - February 2026

- Sync-up meeting #8
- Focus: _WIP & Evolution of FuSa Standards_

## Non-technical topics

### FOSDEM 2026 🤓☝️

- Did any of our WG members attend?
- Any presentations, roundtables, etc, relevant for our WG?
- Example: https://fosdem.org/2026/schedule/event/VXTKQ3-safety-critical-oss-project-insights/

### Summary of docs updates

Merged:
- None

Open:
- None

Link to our docs: [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)

## Technical topics: WIP & Evolution of FuSa Standards

### From last sync-up… 🤔

- 👨‍💻 Start PoC for one function on [libraries qualification process](https://docs.google.com/presentation/d/1-JpF6kMbth1hL0ZkwRyHQ9A7edqd2vwM3U7Y9QcfQfI/edit?slide=id.g3acb06ff9f7_2_258#slide=id.g3acb06ff9f7_2_258) (Petter) ⇒ Git/GitHub access ongoing
- 🫱🏼‍🫲🏽 Security Group’s collab? (Petter) ⇒ Ongoing
- 📚 Report of defects in Alive2 (Carlos) ⇒ In progress, see [slide 7](https://docs.google.com/presentation/d/1hbXKpUSMP1PxCAEZGv8lqMS6EhGgDlOqcS_3PuGjp9k/edit?slide=id.g3c2c04e355e_0_646#slide=id.g3c2c04e355e_0_646)
- 📑 [Analysis of LLVM’s development process](https://www.researchgate.net/publication/398600910_What_ELISA's_Lighthouse_OSS_Best_Practices_Reveal_About_LLVM's_State_of_Practice) (Wendi) ⇒ No progress
- 📜 Continue [templates](https://drive.google.com/drive/u/1/folders/1u5CqCaRz1-RBrsEHfxSuHHp0WPwXt-Hj) (Wendi) ⇒ See [slide 8](https://docs.google.com/presentation/d/1hbXKpUSMP1PxCAEZGv8lqMS6EhGgDlOqcS_3PuGjp9k/edit?slide=id.g3bc8db37014_0_0#slide=id.g3bc8db37014_0_0)
- 🗫 Contact Clang C/C++ WG about libs subgroup (Wendi) ⇒ See Discord
- 🖼️ Drawing [libs qual workflow](https://docs.google.com/presentation/d/1aH-u3DOtiXqjkxzS8c6og4qCOemv_KyU3aFjktHgtqQ/edit?slide=id.g3bb64876fe1_0_9#slide=id.g3bb64876fe1_0_9) (Wendi+Carlos) ⇒ Ongoing, see [slide 8](https://docs.google.com/presentation/d/1hbXKpUSMP1PxCAEZGv8lqMS6EhGgDlOqcS_3PuGjp9k/edit?slide=id.g3bc8db37014_0_0#slide=id.g3bc8db37014_0_0) + Discord
- 🧐 Review YoungJun’s [Tutorial + Mapping projects/ISO 26262](https://docs.google.com/document/d/1rhPMoXHFeJjCsf39iNqjnRO6r8ERwNQmnYO0PGo410Y/edit?tab=t.0#heading=h.zc1so1lnbjsp) (all) ⇒ In progress, Carlos already added comments
- 🖼️ _**(NEW)**_ Drawing CUSWT’s [generic workflow from tool user’s perspective](https://docs.google.com/presentation/d/1aH-u3DOtiXqjkxzS8c6og4qCOemv_KyU3aFjktHgtqQ/edit?slide=id.g3bb64876fe1_0_46#slide=id.g3bb64876fe1_0_46) (Zaky) ⇒ In Review, see [slide 8](https://docs.google.com/presentation/d/1hbXKpUSMP1PxCAEZGv8lqMS6EhGgDlOqcS_3PuGjp9k/edit?slide=id.g3bc8db37014_0_0#slide=id.g3bc8db37014_0_0)

### Alive2 - Defect reports

**Links**

- Heap Buffer Overflow
  - https://github.com/AliveToolkit/alive2/issues/1282
- Null pointer dereference
  - https://github.com/AliveToolkit/alive2/issues/1283
- Many others (to be triaged/reported)

**Reminder - Why Alive2 is relevant for qualification**

- Verifies correctness of compiler optimizations against LLVM IR semantics
- Helps detect miscompilations, including subtle, optimization-induced errors
- Complements testing by providing exhaustive reasoning over classes of transformations
- Translation validation tools (e.g., _arm-tv_, based on Alive2), apply these formal checks to concrete compiler instances and configurations, strengthening confidence that generated code preserves semantics
- Primary purpose: Detect miscompilation bugs and ABI violations in compiled code
- Useful as supporting evidence, even when full formal verification is not feasible
- Tool error detectability measure (ISO 26262 / IEC 61508 concepts)
- **High-value confidence amplifier!!!**

### Updated workflows

Link: [here](https://docs.google.com/presentation/d/1aH-u3DOtiXqjkxzS8c6og4qCOemv_KyU3aFjktHgtqQ/edit?slide=id.g3bb64876fe1_0_5#slide=id.g3bb64876fe1_0_5)

**CUSWT’s generic workflow - Tool provider’s perspective**

1. Split of last step into two (disclaimer vs safety manual - upper boxes)
2. Addition of links to three templates
3. Update of second decision box

**CUSWT’s generic workflow - Tool user’s perspective**

1. Under review
2. Fixes under the radar

**Workflow of the methodology of upstream evidence generation for enabling libraries qualification**

1. Started drawing the steps
2. Connections still missing

Reference all the workflows, guidelines and templates in YoungJun’s [onboarding document](https://docs.google.com/document/d/1rhPMoXHFeJjCsf39iNqjnRO6r8ERwNQmnYO0PGo410Y/edit?tab=t.0#heading=h.zc1so1lnbjsp)

All these documents must live in the llvm-project’s GitHub repo in the near future

### Evolution of functional safety standards

Multiple foundational functional safety standards are being refreshed concurrently

Industry and safety committees are re-evaluating CUSWT and library qualification concepts

- IEC 61508
  - Current edition is Edition 2 (2010)
  - Edition 3’s _Committee Draft for Vote (CDV)_ is expected in early 2026
  - Final standard targeted for early 2027
- ISO 26262
  - Current edition is Edition 2 (2018)
  - Working draft / early committee discussions are underway
  - Final publication currently forecasted for around Oct 2027
- Other standards under revision?

### Clang conformance: Status check

Question for the WG: _**Should we revive our previous discussion on the current status of Clang conformance?**_

What we know, what’s missing, and how (or whether) the Qual WG should engage further on this topic

## Open Discussion

Let's discuss any doubts or concerns.  
If something comes up later, contact the Working Group on Discourse or Discord.
