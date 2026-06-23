# LLVM Qualification Working Group - March 2026

- Sync-up meeting #9
- Focus: _Meeting with members of the Security Response Group_

## Non-technical topics

### Summary

- Discussion continues about where to store our artifacts → See [Discourse](https://discourse.llvm.org/t/where-should-wg-meeting-materials-live/88913)
- Biannual membership review done → See [Discord](https://discord.com/channels/636084430946959380/1389362444169773117/1478209895357612254)

### Summary of docs updates

Merged:
- None

Open:
- None

Link to our docs: [LLVM Qualification Group](https://llvm.org/docs/QualGroup.html)

## Technical topics: Discussion with Security Response Group’s members

### Expectations

Concrete expectations from the Security Response Group around

- Test traceability for security mitigations
- Making tests visible to integrators
- Interaction between the threat model and safety/security standards*
- Clarifying how the Functional Safety/Qualification group can review or complement their work

*The Security WG would naturally own the threat model.

Maybe the Qual WG’s contribution could be around structuring evidence derivation mechanisms, if that’s helpful.

### Inputs

Not exhaustive

- Security Response WG’s [trust-based threat model](https://github.com/mrragava/llvm-project/blob/ragava/threat-model-proposal/llvm/docs/ThreatModel.md) proposal
- Petter’s [Function-based Qualification of C/C++ Standard Library Functions](https://docs.google.com/presentation/d/1-JpF6kMbth1hL0ZkwRyHQ9A7edqd2vwM3U7Y9QcfQfI/edit?slide=id.g3acb06ff9f7_2_258#slide=id.g3acb06ff9f7_2_258) proposal
- [Ferrocene test annotations](https://www.youtube.com/watch?v=_ITnWoPvMKA) (example for Rust)
- Paper on [integrated safety & security co-analysis under ISO 26262 and ISO/SAE 21434](https://www.mdpi.com/1424-8220/24/6/1848)

### What tangible outcome expected?

- Agreement on a pilot?
- Agreement on terminology?
- Agreement that the problem exists?

### Test traceability

Test traceability problem

- Help articulate the problem structure
- Explain how safety frameworks approach traceability
- Possibly suggest mechanisms (without imposing standards)

In safety contexts, traceability is about making assumptions explicit and test coverage visible.

We might be facing a structurally similar issue here.

3-layer explanation:

- Requirement / mitigation / assumption
- Linked test(s)
- Evidence extraction mechanism

Only for the parts that are currently considered as security-sensitive?

### Test annotations

Questions

- Could LLVM tests be annotated?
- What taxonomy would make sense?
- Who owns it?
- How to avoid burdening maintainers?

If we look at this from an integrator’s point of view, the question is not only “Are there tests?” but “Can I systematically know which mitigations were exercised?”

### Threat model and safety/security standards

Threat model interaction

- Clarity on whether acknowledging those standards adds value
- Especially for integrators

Repeated theme

- Vendors / packagers / integrators
- How will the threat model provide value?
- How do integrators know what was tested?

Perhaps the threat model doesn’t need to implement ISO 26262 or ISO 21434, but it might be useful to make its assumptions explicit in a way that integrators operating under those standards can map.

## Open Discussion

Let's discuss any doubts or concerns.  
If something comes up later, contact the Working Group on Discourse or Discord.
