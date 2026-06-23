# Notes - March 2026

## Participants - Tuesday 2026/03/03, 13:00 UTC, 1h

- [@CarlosAndresRamirez](https://discourse.llvm.org/u/carlosandresramirez)
- [@kbeyls](https://discourse.llvm.org/u/kbeyls)
- [@petbernt](https://discourse.llvm.org/u/petbernt)
- [@slotosch](https://discourse.llvm.org/u/slotosch)
- [@smithp35](https://discourse.llvm.org/u/smithp35)
- [@YoungJunLee](https://discourse.llvm.org/u/youngjunlee)
- [@whuhn](https://discourse.llvm.org/u/whuhn)
- [@uwendi](https://discourse.llvm.org/u/uwendi)

## Links

[threat-model-proposal/llvm/docs/ThreatModel.md](https://github.com/mrragava/llvm-project/blob/ragava/threat-model-proposal/llvm/docs/ThreatModel.md)

## Highlights

- Some overlapping subjects between Security and Safety/Qualification are toolchain shipping, ensuring security/safety tests are run correctly (enabled and fully tested), establishing test traceability for security/safety-related features. Potential solutions for traceability could be a key area for collaboration between the groups.
- What is a security issue? What is a functional safety issue? Includes determining impact/severity and probability of occurring. The community needs a pragmatic approach, with clearly defined assumptions.
- Cyber Resilience Act (CRA) requests to establish a reporting mechanism for incidents. Classification requires reporting if an incident is actively exploited or if there is a high danger that it could be exploited or “fail to protect” the user. Caution: a literal interpretation of the CRA’s reporting requirements could overwhelm us with bugs, necessitating a pragmatic interpretation for the regulation to be practical.
- The security group has not yet agreed on a final threat model, which is currently being written up for presentation to the community. The current position is that the upstream LLVM project should aim for a threat model that represents the common subset developers can subscribe to, with derivatives handling additional guarantees. Those on the extremes needing stricter security will have to fix that gap themselves. Therefore, the current focus is on the security of the output programs, reflecting a similarity to functional safety concerns.
- One point of view: The compiler itself is often less important than the security of the compiled program’s output, except in niche cases like a GPU compiler running on the device. Another point of view: citing the Stuxnet story where an exchanged library impacted the centrifuges, emphasizing the risk of supply chain attacks. Compared to the XZ library incident. Such attacks are very difficult to prevent in an open-source project, primarily relying on good review practices and diverse user bases.
- AI agents are an emerging risk. The landscape is changing rapidly due to code commits made by AI agents and agents attacking other agents, potentially leading to increased supply chain attacks via malicious code agents. Increasing need for real-time processing in pipelines or the cloud for AI-related components. Though, the LLVM policy currently ensures a human is always in the loop. Special attention to be paid to possibility of AI-generated security reports, which can also overwhelm the security response group and the community if the issue arises.
- Suggestion of a framework for collaboration centered on defining a “safety model” that the LLVM community can accept. Propose separating libraries from tools in a safety model, as libraries embedded in executables may need to be safe, while tools don’t. The Qual WG could perform a generic risk analysis for key tools that could be used in development of safety-related software.
- The community could potentially label upstream issues as “potentially safety related,” which could aid in collaboration. However, inconsistent labels and the difficulty in getting people to consistently apply them are significant challenges. Example: past issue that was considered security-relevant but was classified as undefined behavior
- Traceability and annotation challenges: annotations could be added to lit tests to cover specific security features or C standards. The primary difficulty identified for implementing traceability through annotations is the long-term maintenance burden and the risk that annotations become outdated when code changes. There is no automated way to detect when an annotation becomes stale or incorrect, which raises concerns about verification costs.
- Any progress on traceability requires starting with a small prototype, running it, and sharing experiences before developing a broader plan. Focusing on the simplest, smallest possible thing the community will accept is essential, with library qualification being a more promising area due to potential maintainer interest.
- Focus on features like stack protector that are not covered by commercial offerings. This would require a strategy with a complete number of test cases and a reasoning argument for their sufficiency.
- Next step from the security group will likely be the release of a threat model, potentially as an RFC.
- Written contributions and review will be enabled by discussions on Discourse and the [#fusa-qual-wg](https://discord.com/channels/636084430946959380/1389362444169773117) channel on Discord.

## Actions

[@uwendi](https://discourse.llvm.org/u/uwendi) :

- Contact authors of the threat model to provide feedback
- Write first draft of ideas for a safety model with the Qual WG, and share with the Security Response WG.
