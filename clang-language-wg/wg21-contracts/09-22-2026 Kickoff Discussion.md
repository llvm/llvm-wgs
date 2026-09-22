LLVM Code of Conduct: [https://llvm.org/docs/CodeOfConduct.html](https://llvm.org/docs/CodeOfConduct.html)
Date: Sept 22, 2026

Attendees:
* Aaron Ballman (chair)
* Joshua Berne
* Chuanqi Xu
* Eric Fiselier
* ???(1)
* ???(2)

Minutes:
* Eric: I have a contracts branch that’s been stalled for 6-7 months, but is ready to get started on it again now that things are figured out. Work is dependent on employer being interested in the work. Joshua can help with that. Eric and Joshua looking for a high-quality implementation in Clang, open to whatever paths work to make that happen. Happy to cooperate.
* Joshua: if Eric is not being responsive, contact me and I’ll get it unstuck. I can help too, but I’ve mostly been touching GCC.
* ???(1): I’ve done a bunch of review on what Eric had worked on half a year ago. I think it was in pretty good shape. It should be smooth to upstream, but there’s work to be done still. Whoever has the most time should do the work, so if Eric doesn’t have time and Chuanqi does, maybe Chuanqi helps?
* Eric: I think there’s a bunch of work involved in taking either branch and breaking them up in a series of commits. If we’re breaking it up, it kind of feels like a third implementation. But we need to keep the tests from each branch, that’s really where the most value is. But I’m happy to go with either branch though. However, with my branch, I learned some hard lessons about things like when a DeclContext is required, etc and we should learn from that.
* Joshua: I’ve been addressing some bugs in Eric’s implementation, addressing some feedback we got from folks in Clang on it, etc. Breaking it up into multiple commits could be relatively mechanical. It’s more the cost of losing lessons that’s a concern. But it’s a question of how we divide the work.
* ???(2): Eric made good points that tests and design lessons are the most valuable here. Sometime last week, a handful of maintainers had a discussion where we wanted more of the design decisions in Clang to be reflected in the internals manual. So maybe a good start is Eric laying down the design he came up with as documentation, and Chuanqi reviews, and they get on the same page through that process?
* ???(1): Ambrose was working on expansion statements and he needed something like 10-15 PRs in a stack for that. It ended up being too many PRs and the updates were painful. We want to be careful how we split things. I think the way Chaunqi is doing things is a good granularity (one PR for parser, one PR for semantics, etc). If we make the PRs too small, it’s hard to review because you miss the bigger picture. I would be more confident starting with what Eric did because I don’t trust an LLM to do design and architecture, but I’m confident that an LLM is good at splitting things up and merging and the more mechanical bits.
* Eric: I agree with that
* Chuanqi: we should have a whole design in documentation, then aim for consensus on the high level of how the system for contracts should work. Then after that, it’s generally fine to do the review work in separate PRs. We have other reviewers who can do high quality reviews. And it seems fine for whoever to do that work, but what’s critical is that we get more reviewers and testers involved to improve quality. There will be a lot of edge cases. The ABI is something we have to get right up front though, so we need to nail that down early and likely have to live with what we decide. But the other changes are more flexible if we need to change things while going through the review process. And we need to share our tests. Land stuff incrementally so that we can get as much early testing as possible and can react to issues.
* ???(2): regarding expansion statement PRs: Ambrose did stacked pull requests and it was horrible when he was rebasing it. He was the only person who knew which PR did what and it was harder to review. Also, every time one PR would change, it would send 10+ PRs to everyone, which made it harder on him as a PR author.
* Eric: thank you to Chuanqi for all the work you’ve been doing on this. It sounds like we’re converging on fewer PRs being important. But getting to codegen is important; representational decisions really rely on codegen. Like how to interact with the standard library, for example. We have to agree with GCC on that sort of thing. One action item I think we can take is that we probably want a design rationale (from either implementation). AST representation needs an explanation, so the decisions you make in the parser are important much later like during codegen. The second thing I think we need is a design doc for the ABI
* ???(1): one of the things we should do is start to actually merge PR. I think contracts should be behind a cc1 flag (not driver flag). It doesn’t need to be complete, just complete enough to test. No need to wait six months to start merging things. I also think it might be politically smart to have things in Clang before the next C++ meeting, that may be helpful for the committee to understand.
* ???(2): good thing we are trying to restart the Itanium ABI group; they’re going to need to be involved. As for design and PRs, I expect design to be updated as we review the PRs. Ambrose had to redo a lot of things (multiple times) as we discussed the PRs, and I think that will happen here. We shouldn’t spend several months on design and then start the PRs, we can do this in parallel.
* Aaron: there is two ABI docs we need to think about: psABI — calling conventions, etc., then itanium ABI for mangling. We’re actively restarting the itanium ABI group. We’re not up an running yet, but we already had an inaugural meeting with previous maintainers. Jason is there. For Microsoft, we can use whatever ABI that makes sense, but we need to document it and mark it as unstable. Chuanqi, we can invite you to the group
* ???(1): yes, but it will be challenging timezone-wise.
* Aaron: the way ABI group is trending is that every community proposes something to the group, so you don’t need to be there to change it
* ???(1): I want to deal with the backlog of itaninum
* Eric: [https://contracts-abi.com/](https://contracts-abi.com/)
* Joshua: [https://github.com/notadragon/llvm-project/commits/contracts-p3850/](https://github.com/notadragon/llvm-project/commits/contracts-p3850/)
* Chuanqi: I also wanted to deal with modules in the itanium ABI. I think I’m the one who has the most time, so I can look at Joshua’s implementation. I can start the PR for the design docs. We don’t need a perfect implementation, but we need to make progress
* Eric: we used to have a wide consensus on the ABI between implementations 6-7 months ago, so proceeding with something else would reset our progress on that.
* ???(1): I’m sure it will need some tweaking on GCC side
* Eric: given that contracts are important for my employer, I should have a decent amount of time for this.
* Joshua: I think the only ABI we need to pin down is violation handler. Calling convention, etc. is not that sensitive to changes.
* Eric: violation handler and violation data
* Joshua: yes. We need to make sure libc++ violation handler, GCC violation code should be isolated from each other to work together.
* Chuanqi: I’m wondering if, can we allow the ABI to be unstable before we finalize it?
* Aaron: we can make ABI unstable, we’ve done that before. The important thing is that by the time we set the FTM, the ABI needs to be stable.
* Eric: there are also libc++ considerations
* ???(1): I don’t know if GCC is planning to be ABI stable any time soon either. The other design question we may have are driver flags. GCC already has some, so we can use that as precedent if we’re happy with the design. I think we should focus on having callee side contracts first, then caller side in terms of codegen. There’s also questions of exceptions, etc. The return variable in lambdas might be tricky, but we can figure that out.
* Joshua: definitely don’t need to stabilize the ABI, but we need to design towards the ABI we’re going to be targeting because the shape of the ABI matters to how we do codegen. e.g., we don’t want to allocate violation data in read-only memory, that won’t ever be ABI stable long-term. But neither compiler is going to set anything in stone until we are comfortable with the ABI.
* Aaron: we also need to think about C stack frames in-between C++ frames, and also how contracts work in the presence of dynamic libraries, especially if they are loaded at runtime. I’m hearing that we agree that we’re starting on documentation for the design, and start putting up PRs with implementation in parallel. Do we want a regular sync-up?
* Chuanqi: maybe we can review on GitHub async, then have meetings if people are confused. But if possible, better to do online
* ???(1): Aaron, what do we do for Windows?
* Aaron: we’ll have to do something for windows at some point, but I have zero issues not waiting for Microsoft to make contracts work there
* Chuanqi: I will be trying to send a Design Doc to the mail, or even if you're happy, I can send it as a PR on the github publicly. (Tell me if anyone don't want this to be public)
* Joshua: because contracts don’t touch psABI level calling conventions, it’s basically just a library. So we shouldn’t have major issues with supporting Windows. If Microsoft does something different someday, we can address it but hopefully they follow what we do.
* Chuanqi: my experience with modules is that it’s reasonable to ignore Windows; users will complain and then we address the concerns as they come up.
* Aaron: we can have an ABI flag for the old ABI if microsoft wakes up. Not the first time we do things before MSVC, always awkward like this.
* Eric: I’ll put up the design doc and tests.
* ???(1): describe the shape of AST nodes, should be enough
* Eric: lambdas are more complicated because of lambdas inside of contracts inside of lambdas inside of contracts
