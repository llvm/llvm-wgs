# Wednesday, August 20 2025, 9:00 - 10:00 am CDT

# Agenda

  102. PR Review LIST


  1. Michael: OMPT PR147389  is approved and ready to merge.


  103. Liboffload API


  1. How to handle ambiguities in pointers with olMemFree / olGetMemInfo


  1. For example, a system has both AMD and Nvidia cards, olMemAlloc is called on both to create device pointers. Both devices happen to select 0x1000 as the memory address, how should olMemFree free that memory?


  1. The current logic doesn't work for devices that have their own allocators
  2. In unified runtime you have to pass device id to free/getmeminfo.
  3. This is specifically for device_type allocators, so the memory won't be visible on host.
  4. Solution: pass device id to olMemFree / olGetMemInfo. Make it optional for managed allocations if possible.
  5. Callum: it would be useful to have an example of where this issue happens.
  6. Ross: will create a PR


  2. Liboffload does not support multiple active plugins in a single process image. Do other low-level APIs support this and is it planned to add this capability to liboffload?


  1. Joseph: this should work
  2. Plugin = vendor-specific portion of the library
  3. For example, SYCL would want to use that functionality.


  104. Can we get offload documentation hosted somewhere? Equivalent to [openmp.llvm.org](https://www.google.com/url?q=http://openmp.llvm.org&sa=D&source=editors&ust=1779820786895330&usg=AOvVaw3DPbjpZHgjIf5ZDjL1tEnA)?


  1. Email Tanya Lattner (Someone from Codeplay)


  1. Callum will follow-up, (can also email Brittany Watson [bwatson@llvm.org](mailto:bwatson@llvm.org), Tanya's backup)


  105. [https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages&sa=D&source=editors&ust=1779820786896034&usg=AOvVaw2WJJ74-_s1ixV9GyFt8aOF) 


  1. Intern at LLNL implementing basic interface, expect PRs in the next week or so.


  1. Jonas: still need some cleanup
  2. There were some problems, but were resolved.  PR expected to be ready this or next week.


  106. GPU ASAN (alternative) prototype ready


  1. Testing out "new-new" design to avoid memory allocations/accesses altogether
  2. Are there any PRs available for review?
  3. Is there a design discussion on discourse?


  1. Kevin working on this, but no update yet.


  107. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786897835&usg=AOvVaw2H_f98v5ziMhoYxcfM5qHv)
  2. Is this ready for review?  Are there public discussions on this?


  1. Kevin will ask about the progress about this.

* * *
