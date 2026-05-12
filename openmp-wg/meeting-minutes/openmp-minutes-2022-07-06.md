### 2022, July 6

Agenda

  * Reformat Libomptarget to use consistent variable case style (e.g. device_num -> DeviceNum).


  * [https://reviews.llvm.org/rGd27d0a673c64068c5f3a1981c428e0ef5cff8062](https://www.google.com/url?q=https://reviews.llvm.org/rGd27d0a673c64068c5f3a1981c428e0ef5cff8062&sa=D&source=editors&ust=1778600246299303&usg=AOvVaw3XZtKNxHeoqXZRW6teBaHf)


  * Remove i386 from the clang tests
  * LLVM-objdump for offloading images


  * [https://reviews.llvm.org/D126904](https://www.google.com/url?q=https://reviews.llvm.org/D126904&sa=D&source=editors&ust=1778600246299509&usg=AOvVaw16ivQ9Mz1weRAp3lwbC-rs)
  * [https://clang.llvm.org/docs/ClangOffloadPackager.html](https://www.google.com/url?q=https://clang.llvm.org/docs/ClangOffloadPackager.html&sa=D&source=editors&ust=1778600246299623&usg=AOvVaw0pLGa6EzLSPUOK5U-txqu8)


  * LLVM objcopy for offloading images


  * Should allow us to treat them like the old offload-bundler


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246299957&usg=AOvVaw1UOOF8uS-8XzMnb9txULJD)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246300058&usg=AOvVaw3EqKcAU4SgVwRxd_0DOZcq) 


  * Multi-arch compilation support


  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246300216&usg=AOvVaw19WJ2SYIMVulMSFk4jR4J6): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D127432](https://www.google.com/url?q=https://reviews.llvm.org/D127432&sa=D&source=editors&ust=1778600246300351&usg=AOvVaw0LULjjZ43EZ_ujC72sJq1r): [Libomptarget] Add support for offloading binaries in libomptarget
  * [D127505](https://www.google.com/url?q=https://reviews.llvm.org/D127505&sa=D&source=editors&ust=1778600246300474&usg=AOvVaw23iMgSLBBw2HfSjVrFOmr2): [Libomptarget] Add checks for CUDA subarchitecture using new info
  * [D127769](https://www.google.com/url?q=https://reviews.llvm.org/D127769&sa=D&source=editors&ust=1778600246300609&usg=AOvVaw0G44T_0NyxH_XmIlfOiVJN): [Libomptarget] Add checks for AMDGPU TargetID using new image info
  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246300740&usg=AOvVaw1kab2LW-m5z_-y83Du5zSg): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D128090](https://www.google.com/url?q=https://reviews.llvm.org/D128090&sa=D&source=editors&ust=1778600246300863&usg=AOvVaw03NRIYuPPNm8MS_q3nyR6A): [Clang][OpenMP] Process multi-arch compilation options given via -march


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246301060&usg=AOvVaw3EdI26BQPPrAyIsPasHUcK) (gdb plugin)
  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246301169&usg=AOvVaw3qBFjJhlLVbLpzP3P7iCE0) (ompd tests based on gdb plugin)


  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246301433&usg=AOvVaw3QRjY3IDMctM6Sb9yU23B5) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246301601&usg=AOvVaw0R__Rh-SLjhTik9atVZ482) only adds the plugin runtime support


  * Change the target interface to __tgt_target_kernel and use a struct for the arguments.


  * [D128549](https://www.google.com/url?q=https://reviews.llvm.org/D128549&sa=D&source=editors&ust=1778600246301803&usg=AOvVaw0l4y6RnKRmPKzEXtsOc5s_) [Libomptarget] Implement a unified kernel entry function
  * [D128817](https://www.google.com/url?q=https://reviews.llvm.org/D128817&sa=D&source=editors&ust=1778600246301917&usg=AOvVaw0SDxYjCNHHTlPEx0RsROsE) [Libomptarget] Use new tripcount argument instead of the push function


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246302238&usg=AOvVaw1eJH-IK97L5stTi5d0v47L)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246302431&usg=AOvVaw34rQPVrzMRBxr4fRHy608k)
  * Updating default version to 5.1


  * Do we want to do it?
  * When? Before llvm-15 branching?
  * [https://clang.llvm.org/docs/OpenMPSupport.html#openmp-5-1-implementation-details](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246302713&usg=AOvVaw0MWKePp0EOaUHgt2vGCo3s) 



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246302882&usg=AOvVaw2yNyy98ht03Hkpm99-TCxy) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246302997&usg=AOvVaw3B-_p7DeP_VVcMNVZ7xkHp)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600246303108&usg=AOvVaw2iNOj8aQw8i8jRehWZ9yH9)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600246303233&usg=AOvVaw3IgXr2Mw9ohvBCpGlz1-XV)



###
