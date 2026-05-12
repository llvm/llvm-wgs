### 2025, Feb 12th

Agenda 

New 

  * [https://github.com/llvm/llvm-project/pull/126143](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/126143&sa=D&source=editors&ust=1778600245994307&usg=AOvVaw3XCNb1l7a3Rq1BvO3cOf-x)
  * Discuss 5.2 and 6.0 features


  * [https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/clang/docs/OpenMPSupport.rst&sa=D&source=editors&ust=1778600245994519&usg=AOvVaw2JYL4TzJHcCSXXrRfYI3pL)        


  * GPU PGO:


  * [https://github.com/llvm/llvm-project/pull/94268](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94268&sa=D&source=editors&ust=1778600245994660&usg=AOvVaw0OFuqwj7EaHoVkd4bSX7L5) 


  * OMPT upstreaming plans from AMD


  * First ompTest (unit test library for OMPT events). Currently avail in downstream: [https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest](https://www.google.com/url?q=https://github.com/ROCm/llvm-project/tree/amd-staging/offload/test/ompTest&sa=D&source=editors&ust=1778600245994928&usg=AOvVaw3qoLv7fElsG5z70_Kl2hLm)   
Example testsuite: [https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp](https://www.google.com/url?q=https://github.com/ROCm/aomp/blob/aomp-dev/test/smoke-limbo/omptest-device-emi/omptest-device-emi.cpp&sa=D&source=editors&ust=1778600245995104&usg=AOvVaw1ttWBfnSkYY5f2NcQGikIq) 
  * Second device tracing support. Likely have a little presentation to this group to collect feedback before opening PRs


  * Question: LLVM_ENABLE_RUNTIMES=openmp vs LLVM_ENABLE_PROJECT=openmp builds, which one is preferred?


  * For host openmp runtime
  * RUNTIME build is expected to work.
  * Preferred way is LLVM_ENABLE_RUNTIMES,  currently issue with flang


  * ARB will vote to produce JSON files (for us to use)


  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Compound constructs in Flang (and Clang)


  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600245996044&usg=AOvVaw2RUKRWlsTwCGkHqRhk60l9) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break


  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600245996604&usg=AOvVaw3dWNeAN-6oZO14Sm2hLhWq) 
  * Where are we right now regarding documents, such as what features are supported and what are not?
