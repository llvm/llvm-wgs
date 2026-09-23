Problem: Libomptarget and liboffload initialization process are not currently compatible.
- Liboffload olInit initializes the library and a list of backends and all their device (by default all).
- Libomptarget currently
   a) Loads the plugins (but doesn't initialize them)
   b) Registers a new image
   c) Process new images
- Init plugins "compatible" with the Image
- Init all devices "compatible" with the Image

Notes: 
(a) & (b) can happen in any order.  If (b) happens after (a), (c) happens immediately. If (b) happens before (a), (a) gets delayed until (a) happens.
(b) can happen multiple times and even after some offload work has been done (e.g., if dlopen is used)
Here "compatible" means our current implementation but it might insufficient going forward (but that's mostly an orthogonal discussion)
Currently another ordering issue related to OMPT exists (but will be gone when [offload] Extract OMPT out of PluginInterface by ivanradanov · https://github.com/llvm/llvm-project/pull/221726 is merged).

Gaps:
- Liboffload requires to know which backends will be used when initialized
- There's no support to check if an image is compatible with a platform
- After olInit no new backends can be initialized

Goal: In order to call liboffload APIs from libomptarget we need to get to a state where libomptarget obtains the ol_device_handles from liboffload.
 
Possible solutions:
- Liboffload lazy initialization of platforms and devices (https://github.com/llvm/llvm-project/pull/221731).
- This keeps the normal liboffload flow but plugins and devices are initialized when absolutely necessary. This allows to load the plugins only, and initialize them as they are needed by the different images.
- Split olInit behavior (https://github.com/llvm/llvm-project/pull/225725) allowing to load the plugins and initialize them on-demand with a new olInitPlatform.  Add a new olIterateCompatiblePlatforms ([Offload] Add olIterateCompatiblePlatforms API by adurang · Pull Request #225135 · llvm/llvm-project, https://github.com/llvm/llvm-project/pull/225135) to only initialize the "compatible" ones.
- Add a temporary ad-hoc solution for libomptarget ([offload][omp] Add temporary helpers to initialize libomptarget through liboffload by adurang · Pull Request #225690, https://github.com/llvm/llvm-project/pull/225690).
- Not ideal but this recognizes that this balances that we might want to think more how to change liboffload initialization btut provides a temporary scaffolding that allows other parts of libomptarget to start using liboffload while we resolve it.

