# Wednesday, May 28 2025, 7:00 - 8:00 am PST

# Agenda

  132. PR Review LIST
  133. Liboffload API


  1. PRs related to improving error handling have all been merged
  2. Currently investigating improvements to memory management


  1. PR up for removing the need to pass the allocation type when freeing memory
  2. Investigating how to implement SYCL/UR contexts on top of liboffload without adding the concept of a memory context to the plugins (no real equivalent in CUDA and HSA)


  3. We now have a [UR adapter for Offload](https://www.google.com/url?q=https://github.com/intel/llvm/tree/sycl/unified-runtime/source/adapters/offload&sa=D&source=editors&ust=1779820786917454&usg=AOvVaw2Ha42tgiB4tejXJPlsTvz2) \- planning on addressing low-hanging fruit in terms of missing functionality


  134. [https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages&sa=D&source=editors&ust=1779820786917906&usg=AOvVaw0pvKU8dS5PR-jyWCPaaE9E) 
  135. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786918317&usg=AOvVaw1acnz2IzVE5TbewgIvYwR9)


  136. GPU ASAN (alternative) prototype ready


  1. Testing out "new-new" design to avoid memory allocations/accesses altogether
  2. Are there any PRs available for review?
  3. Is there a design discussion on discourse?


  137. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786919210&usg=AOvVaw0R5-5TWbo7LOXp9gFane1U)
  2. Is this ready for review?  Are there public discussions on this?


  138. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786919682&usg=AOvVaw33j4tT_BHglJYnF9X5pVjI)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786919927&usg=AOvVaw3stuBct0SpY40giPC10hkd)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786920221&usg=AOvVaw2i4rouTjOTtoawdJzurCPD)


  139. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786920521&usg=AOvVaw0UG64o6Njj71ruNT-SqM81)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786920727&usg=AOvVaw2LUNvislc2Js0JInxkikrq)



#
