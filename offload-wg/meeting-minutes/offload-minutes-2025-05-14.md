# Wednesday, May 14 2025, 7:00 - 8:00 am PST

# Agenda

  140. PR Review LIST
  141. Liboffload API


  1. Work on better error handling from the plugins is ongoing


  1. [https://github.com/llvm/llvm-project/pull/138258](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/138258&sa=D&source=editors&ust=1779820786921619&usg=AOvVaw3XuqdyG2xNmXttDRn2fJmD)
  2. [https://github.com/llvm/llvm-project/pull/139275](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/139275&sa=D&source=editors&ust=1779820786921854&usg=AOvVaw2FX97T6BWNNYtdLwkRRFXw)


  2. Currently investigating improvements to memory management


  1. Liboffload tracks all allocations in a DenseMap - this is a workaround we'd like to get rid of
  2. WIP changes allow plugins to free memory without knowing the allocation type
  3. The MemoryManager abstraction is awkward - the only way to check if an allocation belongs to it is either knowing the type or looking up the pointer.
  4. Would it be possible to decouple the generic MemoryManager from the plugin interface? I.e. make it an optional component that libomptarget can use. Individual plugins would still implement DeviceAllocatorTy.
  5. At the very least we need a way to disable it without relying on env vars


  142. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786923548&usg=AOvVaw2s2FK3mnpyC2ScjlEbx1GZ)


  143. GPU ASAN (alternative) prototype ready


  1. Testing out "new-new" design to avoid memory allocations/accesses all together
  2. Are there any PRs available for review?
  3. Is there a design discussion on discourse?


  144. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786924348&usg=AOvVaw3X1PRbNcrjNqsy2mEIeeT4)
  2. Is this ready for review?  Are there public discussions on this?


  145. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786924837&usg=AOvVaw3YKiCuS-3J4JGf5tFLQEMV)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786925119&usg=AOvVaw1GYN-s6QLigsQMNtwe828b)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786925430&usg=AOvVaw1OsTbSPU2yV5UwG7S9Oqko)


  146. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786925776&usg=AOvVaw0boO5_BZKG8oylk8L1jU_U)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786926050&usg=AOvVaw3tC2TJI4VLl65s_1QsgBux)



#
