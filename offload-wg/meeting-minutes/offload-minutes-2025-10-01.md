# Wednesday, October 1 2025, 9:00 - 10:00 am CDT

# Agenda

  83. PR Review list


  1. 

  84. Location for scripts / Infrastructure for testing (JP)


  1. Consolidate scripts that the buildbots run into llvm-project. Makes reproducibility better as it ties the scripts to the LLVM version. Also enables developers to easier recreate what the buildbots do locally. 
  2. We already have the container recipes  public, CMake cache files are in-tree that are used for the build. What's left is the actual scripts that are run when testing.
  3. Immediate ideas where to put these:


  1. llvm-project/offload/ci 


  4. No concerns


  85. Liboffload API


  1. Further discussion on device/memory allocation link - in regards to [https://github.com/llvm/llvm-project/pull/154733](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/154733&sa=D&source=editors&ust=1779820786869315&usg=AOvVaw0ZZcDzlKlGEdEeJdLAtGDn)  (closed), new PR: [https://github.com/llvm/llvm-project/pull/157478](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/157478&sa=D&source=editors&ust=1779820786869579&usg=AOvVaw0Kh1PEhSjSaw7SVP5qMosX) 


  1. Joseph: why can't we re-allocate if we got a duplicate address from allocation?  Keeping track of platforms adds too much burden on the user.


  1. Ross: We'd like to get the "owner" of each valid address.
  2. Joseph: In case of USM, the linux kernel should manage the address space.
  3. Sergey: Different drivers do not communicate with one another.
  4. Joseph: It's very unlikely to get a conflict, re-allocation would be rare
  5. Piotr: Multiple devices are common with integrated GPUs.


  2. Concern with memcpy having to do pointer lookup: may not be worth the effort.


  1. If memcpy took device ids the lookup wouldn't be needed
  2. Ross: there is a use-case with bare pointers
  3. Unified RT needs to know if the pointer is on host or on an actual device
  4. Further discussion to be continued in the PR


  2. Callum and Ross will stop working on the liboffload at the end of the month.  Intel will pick up the work.


  86. [https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages&sa=D&source=editors&ust=1779820786871968&usg=AOvVaw1M1ldjLTD_HYszkr_G-Slo) 


  1. Jonas is implementing basic interface, expect more PRs in the next week or so.


  1. [https://github.com/llvm/llvm-project/pull/156259](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/156259&sa=D&source=editors&ust=1779820786872424&usg=AOvVaw3Vzx3vxTUW162AsvJElBQN)


  1. Joseph added comments to the PR, waiting for response
  2. Jonas's internship has ended, but he will continue working on this (at a slower pace, perhaps).


  2. More PRs coming soon


  87. Parallel Thin LTO (WIP) 


  1. Some parts are already in upstream. Shilei (?) has been working on that
  2. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786873409&usg=AOvVaw0UQwVpchQJl-EvDqiZDJ5F)


  88. Level zero plugin


  1. Review in progress


  89. Offload commit/PR github notifications (Alex/Nick)


  1. Should we have a subscriber group like clang?
  2. What if people only care about a subset of files



* * *

#
