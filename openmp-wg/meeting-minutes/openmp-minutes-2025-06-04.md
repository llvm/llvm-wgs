### 2025, Jun 4th

Agenda 

New 

  * Makes the DeviceRTL a separate runtime like libc


  * [https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143&sa=D&source=editors&ust=1778600245967801&usg=AOvVaw0y0y-VTYc0afmuUxZrA0HD) 
  * Everybody provide feedback before it is finalized.
  * [https://github.com/llvm/llvm-project/pull/136729](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/136729&sa=D&source=editors&ust=1778600245968003&usg=AOvVaw2vJPxagivPD_uYktwwNSUf)


  * Discuss 5.2 and 6.0 features


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245968207&usg=AOvVaw1dRuiPj3rU1ZTZOv7YAQ91)        
  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245968498&usg=AOvVaw2tF_x7MLklcz8FGJ71HwOn) 
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * WIP: 2 level reductions: [https://github.com/jdoerfert/llvm-project/tree/omp_multi_lvl_red](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/omp_multi_lvl_red&sa=D&source=editors&ust=1778600245968764&usg=AOvVaw0WX1m4uYCYOp_Fq3cGrMcI) 
  * Discuss [https://github.com/llvm/llvm-project/pull/137307](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/137307&sa=D&source=editors&ust=1778600245968905&usg=AOvVaw0YEqzpT8j7g8cG_zZyJrI-) ?


  * [https://github.com/jdoerfert/llvm-project/commit/56001404d76dde62982ef27ac2d4991d332b8392#diff-de101c82aff66b2bda2d1f53fde3dde7b0d370f14f1ff37b7919ce38531230df](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commit/56001404d76dde62982ef27ac2d4991d332b8392%23diff-de101c82aff66b2bda2d1f53fde3dde7b0d370f14f1ff37b7919ce38531230df&sa=D&source=editors&ust=1778600245969156&usg=AOvVaw2vJtdHecZu31im39bJwCIs) 


  * Bug(s) that needs looking into, see [https://github.com/llvm/llvm-project/pull/140786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/140786&sa=D&source=editors&ust=1778600245969318&usg=AOvVaw1_LkUadMwpajtZ4uwnJRSK) 
  * Clang use of new GPU loop interface


  * [https://github.com/jdoerfert/llvm-project/tree/gpu_loop](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/gpu_loop&sa=D&source=editors&ust=1778600245969490&usg=AOvVaw1QCK3t5rB8I1B81YA3K4V7) 



  * Sanitizer wish list:


  * out-of-bounds
  * Use-after-free
  * Use-after-scope
  * Alignment (which alignment?)
  * Address space
  * Double free()?


  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events). Currently avail in downstream: [https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245970084&usg=AOvVaw1xtc69aAwZHZF18yWrUInh)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245970274&usg=AOvVaw0wMtYPe4omKihY81UyssNs) 
  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * ARB will vote to produce JSON files (for us to use)


  * Update : ARB has approved for LLVM to use.  OpenMP Lang committee needs to approve each release
  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Compound constructs in Flang (and Clang)


  * New [3/26]: Updated PR for compound root directive: [https://github.com/llvm/llvm-project/pull/118878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/118878&sa=D&source=editors&ust=1778600245970947&usg=AOvVaw395sNvLzEHzIYS14imVUdo)
  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600245971221&usg=AOvVaw0O1gIuhiaYbtTzRhEqdEOS) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break
