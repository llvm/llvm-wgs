# Wednesday, Jan 08 2025, 7:00 - 8:00 am PST

# Agenda

  188. PR Review LIST
  189. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786950476&usg=AOvVaw1NeEN1xpb0_hFpASOKDsF8)


  190. GPU ASAN (alternative) prototype ready


  1. bad/double-free and kernel traces merged
  2. Testing out "new-new" design to avoid memory allocations/accesses all together



![](images/image1.png)![](images/image3.png)![](images/image2.png)

  191. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786951343&usg=AOvVaw27jsuv0_t0vcc5uWdnCs-2)


  192. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786951624&usg=AOvVaw2Qv9vSX7m3mQ2T-d8xotkR)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786951846&usg=AOvVaw3jsWMZV5IFKuevrlXquG6y)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786952076&usg=AOvVaw29_6Ai0TWyltyYgRzCzvTa)


  193. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786952412&usg=AOvVaw2jF4ffEc5jRDPBeb3fiaGy)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786952681&usg=AOvVaw2NSkcV3ThXD8MaxYOvZzN4)


  194. Testing


  1. Keep a list of issues we discuss in the meetings
  2. Make 1-3 people the "bug keepers" (Joseph, Johannes)


  195. Initial PR for new API and tablegen tooling has finally merged


  1. Thanks to everyone for the help with the various reviews, reverts and getting it properly landed eventually
  2. Draft follow-up PR to demonstrate the new tooling: [https://github.com/llvm/llvm-project/pull/119549](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/119549&sa=D&source=editors&ust=1779820786953671&usg=AOvVaw2i2HutyM2JdIUz0K-D8iS2)


  1. Shows the minimal changes required to add to the API, and the resulting auto-generated files (in the include/generated folder)


  3. Second follow up that implements the remaining initial API:  
[https://github.com/llvm/llvm-project/pull/122106](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/122106&sa=D&source=editors&ust=1779820786954293&usg=AOvVaw3u86Wr6S4gA9SiUtGCf8hv)


  1. Still WIP but enough to run a basic SYCL program!



# Intend to finish this soon. Want to confirm - are we ok with (many,  ongoing) breaking changes until we reach some kind of stability? Above PRs are based on the existing plugin design; don't want to be stuck if we decide to change things.

* * *

#
