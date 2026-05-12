### 2024, July 17

Agenda 

New 

  * ARB will vote to produce JSON files (for us to use)


  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Reworking linker wrapper to pass all files to the device link step


  * [https://github.com/llvm/llvm-project/pull/97573/](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/97573/&sa=D&source=editors&ust=1778600246018209&usg=AOvVaw0GW0dY5Df6N4b0JwJ2F8Mp)


  * OpenMP transparent tasks:


  * What is the community's feeling on the transparent tasks discussion in the language committee and potential implementation in the LLVM libomp runtime?
  * Is there some interest to try to get an implementation going to get some better idea of the feature impact before the TR of OpenMP 6.0 or something?


  * Taskgraph


  * Has been voted into the spec on Jul 16
  * Runtime implementation available
  * Compiler support in Clang seems to be missing still
  * Need to ping BSC folks about their plans
  * Finally, Flang?


  * Target data as a task generating construct


  * One of the changes for OpenMP 6.0
  * This includes support for "nogroup" (target data now has an implicit taskgroup, too)


  * Compound/composite constructs in Flang (and Clang)


  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600246019412&usg=AOvVaw3EgIm5oHDRJ4wV2rJyt8AK) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break


  * Cooperative Kernel launch via HSA?


  * Posted as a question.
  * Asked around at AMD to no avail yet.


  * Kernel library shipped with Offload
  * GPUSan WIP


  * [https://github.com/jdoerfert/llvm-project/tree/gpu_san](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/gpu_san&sa=D&source=editors&ust=1778600246020063&usg=AOvVaw3fAIsMFNCnNjgzHPtGKYms)
  * -fsanitize=offload
  * Feedback welcome, very much WIP!



![](images/image3.png)

  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246020448&usg=AOvVaw2_2FxJeo7NfHrtAokI9jiC) 
  * Where are we right now regarding documents, such as what features are supported and what are not?
