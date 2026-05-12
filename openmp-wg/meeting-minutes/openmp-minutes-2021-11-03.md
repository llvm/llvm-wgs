### 2021, Nov 03

### Agenda 

  * Proposal for how to change to the new runtime 


  * Agreed to switch to new runtime and keep old runtime and decide later when to delete it


  * Snap (and reduced version) not working on nvptx trunk, different failure between new and old device rtl (Dan has further info


  * [https://bugs.llvm.org/show_bug.cgi?id=52169](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D52169&sa=D&source=editors&ust=1778600246461621&usg=AOvVaw0XMD5QzDouVME7hrn9SArI)   
[OpenMP] Wrong answers with nested 'omp parallel for'


  * FOTV generic device offload runtime proposal


  * See [https://doi.org/10.1007/978-3-030-85262-7_12](https://www.google.com/url?q=https://doi.org/10.1007/978-3-030-85262-7_12&sa=D&source=editors&ust=1778600246461847&usg=AOvVaw11AHqFvFerKo0rOZs6IJ5L)


  * OvO (-O3, new RT) passes 100% C/C++ tests now on A100 (sm_80) :) 


  * Ye: still fails in A40 and RTX3060 Ti. sm_86 cards but works as sm_80.


  * Non-standard ompx OpenMP library 
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246462226&usg=AOvVaw15D95deHgaFSA4Z30KwzXp) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246462330&usg=AOvVaw0wmBpEfEcwI4XsBRwuDZUz) (irbuilder)
  * 

  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246462451&usg=AOvVaw19vIcWGL_hCb0q7hJdLRgG)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently offline (machine electrocuted itself)


  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246462779&usg=AOvVaw2Ie_5KuLOUSIk0fPXaeR_H), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246462856&usg=AOvVaw2hOxMfv2KCmnmnmalzvB_L))


  * Possibly revert the 2-3 patches and AMD will upstream JMC's implementation of the callback interface
  * Device tracing (or trace records) implementation will come separately
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246463200&usg=AOvVaw0lQ6qj8ibnAC9Bf2OK8a2t)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246463357&usg=AOvVaw2cdxEGangEaTAYzfOYqcbi) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246463697&usg=AOvVaw3D3AbbYpKPSCnAeznjJej9)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246464105&usg=AOvVaw2Sgl1rtCe4m5CxvJ_Cx8u1). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246464286&usg=AOvVaw00dw8iHbNlMRTzZUZrd0Sq)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246464563&usg=AOvVaw2p72YnDYOA4krxY7DPG6ra)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246464769&usg=AOvVaw1sF9dh8pYX7nNo1HES9qs6)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246464891&usg=AOvVaw0IkJRpniqPO-TGtMTCA4BM)
  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246465401&usg=AOvVaw20mILz6BRqblgbq-E-1UAF)
