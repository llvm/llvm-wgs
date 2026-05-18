### 2024, Aug 28

Agenda 

New 

  * Built libc++.a and libc++abi.a for the GPU


  * [https://discourse.llvm.org/t/rfc-building-libc-for-gpu-targets/80216](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-building-libc-for-gpu-targets/80216&sa=D&source=editors&ust=1778600246010472&usg=AOvVaw0mS9sp-Qg_IR4yDjbi-Jvk)


  * ARB will vote to produce JSON files (for us to use)


  * Proposed the generate to make it stable for outside consumer
  * Krzysztof and Johannes offer to be maintainer of the script


  * Thin-LTO for AMD GPU (modules without external calls):


  * [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1778600246010865&usg=AOvVaw1FdhYpxUsHNm3sp1oJAAOw)


  * Target data as a task generating construct


  * One of the changes for OpenMP 6.0
  * This includes support for "nogroup" (target data now has an implicit taskgroup, too)


  * Compound/composite constructs in Flang (and Clang)


  * OpenMP spec expose json files in some format that can be used by llvm (see above)
  * PR for exporting OpenMP definitions: [https://github.com/OpenMP/spec/pull/3943](https://www.google.com/url?q=https://github.com/OpenMP/spec/pull/3943&sa=D&source=editors&ust=1778600246011361&usg=AOvVaw2J2OZCZ4SaU9Nn35rQQmDM) 
  * Almost done with sema; now working on directive breakdown.
  * We might have to auto-gen tests to tame the combinatorial number of tests required.
  * Flang w/ MLIR should be less critical.  TBC.
  * Clang is more monolithic and thus could more easily break


  * Cooperative Kernel launch via HSA?


  * Posted as a question.
  * Asked around at AMD to no avail yet.


  * Kernel library shipped with Offload
  * GPUSan WIP


  * [https://github.com/jdoerfert/llvm-project/tree/gpu_san](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/gpu_san&sa=D&source=editors&ust=1778600246012000&usg=AOvVaw3MR853nyMsoZBxq52ROBDP)
  * -fsanitize=offload
  * Feedback welcome, very much WIP!



![](images/image3.png)

  * OpenMP version 5.2 as default


  * Could go straight to 6.0 and not bother with 5.2 at all
  * Older review that made a move from 5.0 to 5.1 [https://reviews.llvm.org/D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246012371&usg=AOvVaw2gbf7BAlWwNOfgjqjLLxFM) 
  * Where are we right now regarding documents, such as what features are supported and what are not?
