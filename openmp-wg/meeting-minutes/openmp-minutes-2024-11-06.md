### 2024, Nov 6th

Agenda 

New 

  * Three open issues about DWARF information generated for OpenMP regions by Joachim Jenke, RWTH:


  * [https://github.com/llvm/llvm-project/issues/110700](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/110700&sa=D&source=editors&ust=1778600246002523&usg=AOvVaw1H6XjZNTHVbYr6Ag6jLroC) (Iteration variable in OpenMP work-sharing loops is not printable)
  * [https://github.com/llvm/llvm-project/issues/110698](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/110698&sa=D&source=editors&ust=1778600246002745&usg=AOvVaw21IZVfsFwyJN63GCRnF02a) (Shared variables in OpenMP outlined regions have the wrong (reference) type)
  * [https://github.com/llvm/llvm-project/issues/107125](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/107125&sa=D&source=editors&ust=1778600246002944&usg=AOvVaw3WC-fenRsBVwr3U01EV2q6) (Application variables in OpenMP outlined regions are marked as artificial)


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
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600246003941&usg=AOvVaw1FRVOIsN9XWdOXKPsvT4Vc) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break


  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246004506&usg=AOvVaw2jdlyZyQ72pUj3QY5vipLZ) 
  * Where are we right now regarding documents, such as what features are supported and what are not?
