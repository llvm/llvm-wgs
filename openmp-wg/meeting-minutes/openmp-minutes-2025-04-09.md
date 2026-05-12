### 2025, Apr 9th

Agenda 

New 

  * Question:  
Does the OpenMP runtime guarantee binary backward compatibility? For example, is an application compiled with an older compiler version (e.g., v19.1) guaranteed to work correctly with a newer OpenMP runtime (e.g., v20.1)? Do we have a documented policy on this? The specific scenario in mind is when the OpenMP runtime is shipped with the operating system. If a new OS release includes the v21.1 OpenMP runtime, will existing applications (compiled with v19.1) need to be recompiled or relinked, or are they guaranteed to work correctly as-is?


  * [https://openmp.llvm.org/SupportAndFAQ.html#q-are-libomptarget-and-plugins-backward-compatible](https://www.google.com/url?q=https://openmp.llvm.org/SupportAndFAQ.html%23q-are-libomptarget-and-plugins-backward-compatible&sa=D&source=editors&ust=1778600245982372&usg=AOvVaw0rPPyW2izhAhuGFrxU7uzK)
  * 

  * Fat preprocessed file.


  * clang … \--save-temps -### &> reproducer.sh


  * [https://github.com/llvm/llvm-project/pull/126143](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/126143&sa=D&source=editors&ust=1778600245982617&usg=AOvVaw3mp6INMVHdX0PEzyKqQmkZ)


  * Waiting on AMD testing


  * Discuss 5.2 and 6.0 features


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245982856&usg=AOvVaw2t2CdkdNyPf_48c8DyI0eW)        
  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245983102&usg=AOvVaw0Y3o5iNnI0Fn6feNPu8dXR) 
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * GPU PGO:


  * [https://github.com/llvm/llvm-project/pull/94268](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94268&sa=D&source=editors&ust=1778600245983355&usg=AOvVaw0HyJu0fuJO4x40WUipF-fW) 


  * Sanitizer wish list:


  * out-of-bounds
  * Use-after-free
  * Use-after-scope
  * Alignment (which alignment?)
  * Address space
  * Double free()?


  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events). Currently avail in downstream: [https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245983900&usg=AOvVaw2yQL31maG0JHruBIMrasBy)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245984084&usg=AOvVaw0u7HzECkbc7D-JoZ7RnTZg) 
  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * ARB will vote to produce JSON files (for us to use)


  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Compound constructs in Flang (and Clang)


  * New [3/26]: Updated PR for compound root directive: [https://github.com/llvm/llvm-project/pull/118878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/118878&sa=D&source=editors&ust=1778600245984650&usg=AOvVaw2krTFJbJYvQh9kRTBTGisN)
  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600245984897&usg=AOvVaw2yjqBQK5RIVTR5SjSdRFug) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break
