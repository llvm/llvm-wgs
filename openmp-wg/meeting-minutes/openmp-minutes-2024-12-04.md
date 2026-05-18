### 2024, Dec 4th

Agenda 

New 

  * Discuss 5.2 and 6.0 features
  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events). Currently avail in downstream: [https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245999522&usg=AOvVaw3WolMadwv9TCpHJL3orlKg)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245999711&usg=AOvVaw1gNdnbYgTGPUq4COQMXgeE) 
  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * Three open issues about DWARF information generated for OpenMP regions by Joachim Jenke, RWTH:


  * [https://github.com/llvm/llvm-project/issues/110700](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/110700&sa=D&source=editors&ust=1778600246000042&usg=AOvVaw1s3Ge2rC6Onnb29TfrB0ts) (Iteration variable in OpenMP work-sharing loops is not printable)
  * [https://github.com/llvm/llvm-project/issues/110698](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/110698&sa=D&source=editors&ust=1778600246000260&usg=AOvVaw0Lv8-KH-vmsZ14P9_ZWagP) (Shared variables in OpenMP outlined regions have the wrong (reference) type)
  * [https://github.com/llvm/llvm-project/issues/107125](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/107125&sa=D&source=editors&ust=1778600246000464&usg=AOvVaw1URmM-gmFdXYd9_8fRAqbp) (Application variables in OpenMP outlined regions are marked as artificial)


  * Question: LLVM_ENABLE_RUNTIMES=openmp vs LLVM_ENABLE_PROJECT=openmp builds, which one is preferred?


  * For host openmp runtime
  * RUNTIME build is expected to work.


  * ARB will vote to produce JSON files (for us to use)


  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Target data as a task generating construct


  * One of the changes for OpenMP 6.0
  * This includes support for "nogroup" (target data now has an implicit taskgroup, too)


  * Compound/composite constructs in Flang (and Clang)


  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600246001462&usg=AOvVaw1CcupvVftM7lIAeUEv3ftZ) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break


  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246002020&usg=AOvVaw0rG4zkytcb5sykjDr0ZaaI) 
  * Where are we right now regarding documents, such as what features are supported and what are not?
