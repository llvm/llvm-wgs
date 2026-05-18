### 2022, July 27

Agenda

  * Linking llvm libs into libomptarget (instead of copy/pasting from llvm for D127432 etc)


  * Previously thwarted by license differences, since been resolved
  * Every time this is proposed people come out of the woodwork to complain about the library they use from llvm using other parts of llvm
  * Let's tell those people to just build llvm if they want to use parts of llvm
  * https://reviews.llvm.org/D129875


  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246284679&usg=AOvVaw1aPjrg1YrljmvtujLZg4mf): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  *   * [https://clang.llvm.org/docs/OpenMPSupport.html#openmp-5-1-implementation-details](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246284946&usg=AOvVaw2wZZ0ujULjoPP5qrKD07CO) 


  * How to handle destructors in libomptarget


  * The implicit destruction order will destroy the plugins first and leave some libraries in uncertain states
  * Should accessing the plugins at destruction be impossible?


  * How to handle device destructors in this case


  * Should -mlink-builtin-bitcode import all symbols for OpenMP


  * Device runtime defines many functions that are only included if used by the user module
  * OpenMPOpt then tries to emt a call to these functions that weren't previously included
  * Should we get rid of the "LinkOnlyNeeded" flag and import everything so this doesn't happen


  * Downside is a slight increase in compile time, DCE should strip the unused definitions later.


  * Deprecating the old driver completely for OpenMP0-


  * [https://reviews.llvm.org/D130020](https://www.google.com/url?q=https://reviews.llvm.org/D130020&sa=D&source=editors&ust=1778600246285924&usg=AOvVaw1egsVe2lgJXXs-XS6CjAL7)


  * Link order can cause Clang to find the system's libomptarget first


  * Pass libomptarget.so to clang directly?


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246286247&usg=AOvVaw29PtLGyFtjJK0yuHWqz6o8)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246286356&usg=AOvVaw3cxtHUc_6nCqa30IPhd2pj) 


  * Multi-arch compilation support


  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246286476&usg=AOvVaw0bDLHMNpYpZHBDlrkrDWI_): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D127432](https://www.google.com/url?q=https://reviews.llvm.org/D127432&sa=D&source=editors&ust=1778600246286597&usg=AOvVaw0FBA9WrEqrVSJjWzqcFXo3): [Libomptarget] Add support for offloading binaries in libomptarget
  * [D127505](https://www.google.com/url?q=https://reviews.llvm.org/D127505&sa=D&source=editors&ust=1778600246286724&usg=AOvVaw0-5LVyNANi-d16jnPN8p35): [Libomptarget] Add checks for CUDA subarchitecture using new info
  * [D127769](https://www.google.com/url?q=https://reviews.llvm.org/D127769&sa=D&source=editors&ust=1778600246286856&usg=AOvVaw0jaWMSCRAs6cA-w4ZesQLC): [Libomptarget] Add checks for AMDGPU TargetID using new image info
  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246286978&usg=AOvVaw2LekGvXsTyTcOi8bACZ8eR): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D128090](https://www.google.com/url?q=https://reviews.llvm.org/D128090&sa=D&source=editors&ust=1778600246287098&usg=AOvVaw3Ij7YmBXdMrxqf-DhkMHY5): [Clang][OpenMP] Process multi-arch compilation options given via -march


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246287333&usg=AOvVaw3SMWgDi7vZfCXa6uUAlgq1) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246287532&usg=AOvVaw1yqMuXXMye836gzvWfQKnp) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * _OPENMP (Joachim)


  * Currently 201611 (= TR4 date - aka 5.0 Preview 1)


  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246287976&usg=AOvVaw2_wk346SJHlY_2NHERtTJH) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246288146&usg=AOvVaw2rYDJV3CdRB869lHP_Egc3) only adds the plugin runtime support


  * Change the target interface to __tgt_target_kernel and use a struct for the arguments.


  * [D128549](https://www.google.com/url?q=https://reviews.llvm.org/D128549&sa=D&source=editors&ust=1778600246288349&usg=AOvVaw2XcQ7Q7ZU08x69bE54lbOm) [Libomptarget] Implement a unified kernel entry function
  * [D128817](https://www.google.com/url?q=https://reviews.llvm.org/D128817&sa=D&source=editors&ust=1778600246288469&usg=AOvVaw1uz12XpR5ncvRrW8bKGGew) [Libomptarget] Use new tripcount argument instead of the push function


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246288786&usg=AOvVaw3ymN9Zz4rhGhOjbgvYcRRp)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246288973&usg=AOvVaw3Uqqj0cnrMD40U9jmCz_zG)
  * -O3 optimization for new Device RTL


  * [https://reviews.llvm.org/D129344](https://www.google.com/url?q=https://reviews.llvm.org/D129344&sa=D&source=editors&ust=1778600246289132&usg=AOvVaw0wQvK79mJDoMZ2cwWy7Hg9) 



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246289355&usg=AOvVaw0G3so5gNBh7qm1bqf1SENa) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246289480&usg=AOvVaw1HW9TDnTaNBIWAzTvLe6Bb)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600246289600&usg=AOvVaw2L5pb_ujHFqcbOj2E782yI)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600246289724&usg=AOvVaw3aEgK-PmWeqtiOc6DDfGoX)



###
