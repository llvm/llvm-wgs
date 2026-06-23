# LLVM Qualification Group’s December Sync-Up Agenda

Hello all,

Our next sync-up meeting will be dedicated to a special topic: Function-Level Qualification Methodology for libc/libc++ ([@petbernt](https://discourse.llvm.org/u/petbernt) ’s proposal)

Slides (open for comments): [llvm\_qual\_grp\_lib\_qual](https://docs.google.com/presentation/d/1YX_MBtN77px0wRwn9Iz1eySgoIQ0Ad1uyIoToZiI2Vc/edit?slide=id.p1#slide=id.p1)

[@petbernt](https://discourse.llvm.org/u/petbernt) will tell us more about why standard libraries matter for qualification, giving us a walkthrough illustrated with examples from the slide deck:

- Overview of the proposed proof-of-concept:
  - Unique challenges: vast API surface, varied implementations, historical behavior, testability
  - Why “function-level qualification” might offer a scalable entry point
  - Relationship to previous WG discussions on requirements traceability, upstream-friendly artefacts, and modular qualification pilots
- Structure of the approach
- Requirements decomposition (per function)
- Test strategy (functional, boundary, behavioral)
- Traceability approach across libc/libc++
- Criteria for function selection in the PoC

Let’s take time also for any clarifying questions and discussion about strengths & gaps. Some guiding questions:

- Does the function-level approach scale?
- Is the requirements/test breakdown consistent with typical qualification workflows?
- What do we consider “minimum viable artefacts” for a PoC?
- How should the WG ensure upstream-friendliness?
- What is the interaction with existing test suites (libc/test, libc++/test, other conformance suites)?
- How might other methods & tools (static analyzers, fuzzing, translation validation) play a complementary role?
- Any foreseeable blockers?

See you next week!
