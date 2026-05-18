### 2022, Aug 03

Agenda

  * Updating default version to 5.1 [ready, waiting for more features]


  * [D129635](https://www.google.com/url?q=https://reviews.llvm.org/D129635&sa=D&source=editors&ust=1778600246279666&usg=AOvVaw3Tu3rmJUtv5Zhj4WpKKJG1): [OpenMP] Update the default version of OpenMP to 5.1 [Accepted]
  * [https://clang.llvm.org/docs/OpenMPSupport.html#openmp-5-1-implementation-details](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html%23openmp-5-1-implementation-details&sa=D&source=editors&ust=1778600246279873&usg=AOvVaw35VnqgcVPKgP97zHLtfWBz) 


  * How to handle destructors in libomptarget


  * Remove libomptarget's destructors, instead destroy the state when the user code calls deinit_library for the last time
  * The implicit destruction order will destroy the plugins first and leave some libraries in uncertain states
  * Should accessing the plugins at destruction be impossible?


  * How to handle device destructors in this case


  * Should -mlink-builtin-bitcode import all symbols for OpenMP


  * Device runtime defines many functions that are only included if used by the user module
  * OpenMPOpt then tries to emt a call to these functions that weren't previously included
  * Should we get rid of the "LinkOnlyNeeded" flag and import everything so this doesn't happen


  * Downside is a slight increase in compile time, DCE should strip the unused definitions later.


  * Deprecating the old driver completely for OpenMP


  * [https://reviews.llvm.org/D130020](https://www.google.com/url?q=https://reviews.llvm.org/D130020&sa=D&source=editors&ust=1778600246280938&usg=AOvVaw0kYfofJgyUWWXLfHtJeqnO)


  * Link order can cause Clang to find the system's libomptarget first


  * Pass libomptarget.so to clang directly?


  * Number of arguments to parallel on device


  * [https://github.com/llvm/llvm-project/issues/56389](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56389&sa=D&source=editors&ust=1778600246281251&usg=AOvVaw36joj8PXgApL_GetN3Dqo0)
  * -> [https://reviews.llvm.org/D102107](https://www.google.com/url?q=https://reviews.llvm.org/D102107&sa=D&source=editors&ust=1778600246281357&usg=AOvVaw22k-zrEeXoOLotGq_Zy5ts) 


  * Multi-arch compilation support


  * [D128090](https://www.google.com/url?q=https://reviews.llvm.org/D128090&sa=D&source=editors&ust=1778600246281490&usg=AOvVaw1p7803cqoFL_41a-PH1GPO): [Clang][OpenMP] Process multi-arch compilation options given via -march


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246281692&usg=AOvVaw11mYWbdHU12Tg1dUygGHxG) (gdb plugin) - landed!


  * Breaks many builds by adding dependencies no required by LLVM


  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246281883&usg=AOvVaw1yNdpug8QH6_ajpXtNePyp) (ompd tests based on gdb plugin)
  * (Joachim) Can we enable OMPD_SUPPORT by default, if OMPT_SUPPORT is enabled?


  * _OPENMP (Joachim)


  * Currently 201611 (= TR4 date - aka 5.0 Preview 1)


  * Allocators - shared, managed, gpu, other


  * Does AMD have support?


  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246282381&usg=AOvVaw0g5bV2QZ-bPGldRN4zfNbe) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246282548&usg=AOvVaw3jf76Z5uI-mCM0rDomp3ON) only adds the plugin runtime support


  * Change the target interface to __tgt_target_kernel and use a struct for the arguments.


  * [D128549](https://www.google.com/url?q=https://reviews.llvm.org/D128549&sa=D&source=editors&ust=1778600246282747&usg=AOvVaw0kV0ue7ZqWKiJ1tcU55o99) [Libomptarget] Implement a unified kernel entry function
  * [D128817](https://www.google.com/url?q=https://reviews.llvm.org/D128817&sa=D&source=editors&ust=1778600246282867&usg=AOvVaw0Q4YPL02_JpVudXR-J7Vis) [Libomptarget] Use new tripcount argument instead of the push function


  * Device atomics


  * What atomic works and unit tests for what works.


  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246283194&usg=AOvVaw2sB4cOgjhOYLo9aYCyKrwF)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246283385&usg=AOvVaw1vBoYOyxUZelHmZ68XgRRy)



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246283571&usg=AOvVaw2Zg_-VDn6uADfbbsA7dKC6) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246283687&usg=AOvVaw3KlXw5pqZGS7IYdugungeB)
  * [https://github.com/llvm/llvm-project/issues/55943](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/55943&sa=D&source=editors&ust=1778600246283805&usg=AOvVaw2J2i-AnFNBPgUIhTnwwdzT)
  * [https://github.com/llvm/llvm-project/issues/56406](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/56406&sa=D&source=editors&ust=1778600246283924&usg=AOvVaw2yNBJ7cHyIUjs2cuPBi8_s)



###
