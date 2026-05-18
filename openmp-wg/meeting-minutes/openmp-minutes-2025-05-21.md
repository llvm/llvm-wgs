### 2025, May 21th

Agenda 

New 

  * [https://discourse.llvm.org/t/rfc-removing-the-openmp-experimental-warning-for-llvm-21/86455](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-removing-the-openmp-experimental-warning-for-llvm-21/86455&sa=D&source=editors&ust=1778600245971853&usg=AOvVaw3ayJ9HIkkSc_Hk7L4pYBYf) 


  * RFC to remove "experimental" from OpenMP in flang


  * [https://github.com/llvm/llvm-project/pull/136729](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/136729&sa=D&source=editors&ust=1778600245972036&usg=AOvVaw3V-jzQeiw8lrT9hKbsYoHS)


  * Makes the DeviceRTL a separate runtime like libc


  * Discuss 5.2 and 6.0 features


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245972319&usg=AOvVaw1vL1D_Kwy50kD6r-rEytQX)        
  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245972596&usg=AOvVaw0zjufn0LNyD14K0oQZYdpU) 
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * WIP: 2 level reductions: [https://github.com/jdoerfert/llvm-project/tree/omp_multi_lvl_red](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/omp_multi_lvl_red&sa=D&source=editors&ust=1778600245972853&usg=AOvVaw0s2mvo_yS9Zb0IA6ggp6PA) 
  * Discuss [https://github.com/llvm/llvm-project/pull/137307](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/137307&sa=D&source=editors&ust=1778600245972987&usg=AOvVaw2diXN4_qMbwiKvBoiipL4s) ?


  * [https://github.com/jdoerfert/llvm-project/commit/56001404d76dde62982ef27ac2d4991d332b8392#diff-de101c82aff66b2bda2d1f53fde3dde7b0d370f14f1ff37b7919ce38531230df](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commit/56001404d76dde62982ef27ac2d4991d332b8392%23diff-de101c82aff66b2bda2d1f53fde3dde7b0d370f14f1ff37b7919ce38531230df&sa=D&source=editors&ust=1778600245973240&usg=AOvVaw2R6rf2pV6ejLpkEKmWNHDP) 


  * Bug(s) that needs looking into, see [https://github.com/llvm/llvm-project/pull/140786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/140786&sa=D&source=editors&ust=1778600245973400&usg=AOvVaw3jyyKZ1oGmFYZcSV_0dms3) 
  * Clang use of new GPU loop interface


  * [https://github.com/jdoerfert/llvm-project/tree/gpu_loop](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/gpu_loop&sa=D&source=editors&ust=1778600245973574&usg=AOvVaw3FT1uZjmGYxTMiMCUS-UZR) 



  * Sanitizer wish list:


  * out-of-bounds
  * Use-after-free
  * Use-after-scope
  * Alignment (which alignment?)
  * Address space
  * Double free()?


  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events). Currently avail in downstream: [https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245974155&usg=AOvVaw310ZVKeRVAZp60PvXhF1Qd)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245974341&usg=AOvVaw1mn_FhbyR2gfwe_nnn5dtW) 
  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * ARB will vote to produce JSON files (for us to use)


  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Compound constructs in Flang (and Clang)


  * New [3/26]: Updated PR for compound root directive: [https://github.com/llvm/llvm-project/pull/118878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/118878&sa=D&source=editors&ust=1778600245974928&usg=AOvVaw13SiHCVAn8NjZnGhUDS3N3)
  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600245975165&usg=AOvVaw0LKnhnfZHYq9ttRC5cjno6) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break



###
