### 2025, July 2nd

Agenda 

New 

  * Interop presentation by Intel (Alex)
  * OpenMP Paris F2F review
  * Makes the DeviceRTL a separate runtime like libc


  * [https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-llvm-policy-for-top-level-directories-and-language-runtimes/86143&sa=D&source=editors&ust=1778600245963780&usg=AOvVaw0Q_wSuddlVELsVCWYNWljD) 
  * Everybody provide feedback before it is finalized.
  * [https://github.com/llvm/llvm-project/pull/136729](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/136729&sa=D&source=editors&ust=1778600245963961&usg=AOvVaw1HfdVdw6RHHgU9iHzqichf)


  * Discuss 5.2 and 6.0 features


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245964197&usg=AOvVaw1mZQqaFR-vr3RfZ5x_KZ-t)        
  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245964458&usg=AOvVaw131q1rgpF5ZiVFU7LwirZQ) 
  * Where are we right now regarding documents, such as what features are supported and what are not?


  * WIP: 2 level reductions: [https://github.com/jdoerfert/llvm-project/tree/omp_multi_lvl_red](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/omp_multi_lvl_red&sa=D&source=editors&ust=1778600245964730&usg=AOvVaw0HB-fdVAJ5y3uYN-MQDWql) 
  * Discuss [https://github.com/llvm/llvm-project/pull/137307](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/137307&sa=D&source=editors&ust=1778600245964865&usg=AOvVaw1j4rQN34TcTSBixaULhv9B) ?


  * [https://github.com/jdoerfert/llvm-project/commit/56001404d76dde62982ef27ac2d4991d332b8392#diff-de101c82aff66b2bda2d1f53fde3dde7b0d370f14f1ff37b7919ce38531230df](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/commit/56001404d76dde62982ef27ac2d4991d332b8392%23diff-de101c82aff66b2bda2d1f53fde3dde7b0d370f14f1ff37b7919ce38531230df&sa=D&source=editors&ust=1778600245965118&usg=AOvVaw1YdD9Kbj999jBJc8KudYWG) 


  * Bug(s) that needs looking into, see [https://github.com/llvm/llvm-project/pull/140786](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/140786&sa=D&source=editors&ust=1778600245965267&usg=AOvVaw139uI7BwEccdQRZJd5GFQs) 
  * Clang use of new GPU loop interface


  * [https://github.com/jdoerfert/llvm-project/tree/gpu_loop](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/gpu_loop&sa=D&source=editors&ust=1778600245965447&usg=AOvVaw234t--RgnBtm4CW52QSlL4) 


  * Sanitizer wish list:


  * out-of-bounds
  * Use-after-free
  * Use-after-scope
  * Alignment (which alignment?)
  * Address space
  * Double free()?


  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events). Currently avail in downstream: [https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245965973&usg=AOvVaw3_7u9YEPuCuUIlt0aZjcaZ)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245966174&usg=AOvVaw3atZGF7e-4qMIfOX72jJvI) 
  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * ARB will vote to produce JSON files (for us to use)


  * Update : ARB has approved for LLVM to use.  OpenMP Lang committee needs to approve each release
  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Compound constructs in Flang (and Clang)


  * New [3/26]: Updated PR for compound root directive: [https://github.com/llvm/llvm-project/pull/118878](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/118878&sa=D&source=editors&ust=1778600245966858&usg=AOvVaw1JCKykmvUdBRwtRoBc7EGz)
  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600245967086&usg=AOvVaw258Kn2pt-gmdkBWTaQ_Fpv) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break
