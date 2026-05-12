### 2024, Oct 9th

Agenda 

New 

  * Three open issues about DWARF information generated for OpenMP regions by Joachim Jenke, RWTH:


  * [https://github.com/llvm/llvm-project/issues/110700](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/110700&sa=D&source=editors&ust=1778600246004967&usg=AOvVaw2Eez61vmbOpsySyJ9AhQJG) (Iteration variable in OpenMP work-sharing loops is not printable)
  * [https://github.com/llvm/llvm-project/issues/110698](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/110698&sa=D&source=editors&ust=1778600246005184&usg=AOvVaw0pmS_EscX7Rs1gUyQV7XBS) (Shared variables in OpenMP outlined regions have the wrong (reference) type)
  * [https://github.com/llvm/llvm-project/issues/107125](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/107125&sa=D&source=editors&ust=1778600246005392&usg=AOvVaw1pvHaoqf25PkgqOVI4kQLk) (Application variables in OpenMP outlined regions are marked as artificial)


  * Offload workshop @ LLVM Dev still have open slots


  * Preliminary agenda will be posted on discourse today
  * Reach out if you want to present or have topics


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
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600246006633&usg=AOvVaw0DpkIWiNZ81cIMajDxxz_M) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break


  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246007217&usg=AOvVaw37Z1BrHntsAUNmTGe6Z1Sn) 
  * Where are we right now regarding documents, such as what features are supported and what are not?



###
