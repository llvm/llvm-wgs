### 2022, June 15

Agenda

  * What does static / hidden mean on the device
  * LLVM-objdump for offloading images


  * [https://reviews.llvm.org/D126904](https://www.google.com/url?q=https://reviews.llvm.org/D126904&sa=D&source=editors&ust=1778600246306295&usg=AOvVaw0KO0ta3bhcowKNex-m-IOw)
  * https://clang.llvm.org/docs/ClangOffloadPackager.html


  * Multi-arch compilation support


  * Introduced clang-offload-packager
  * Basically fatbinary for LLVM offloading
  * https://reviews.llvm.org/D127304
  * [D127246](https://www.google.com/url?q=https://reviews.llvm.org/D127246&sa=D&source=editors&ust=1778600246306641&usg=AOvVaw02-0pdDztqeQkJPSf9tUni): [LinkerWrapper] Rework the linker wrapper and use owning binaries
  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246306765&usg=AOvVaw235AQZlJxStwGuRyrwrLGc): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * First patch in the series posted for review:


  * Going to use [D126836](https://www.google.com/url?q=https://reviews.llvm.org/D126836&sa=D&source=editors&ust=1778600246306986&usg=AOvVaw24V6KHdzfKo3qhcytLi8ET) to move the compatibility testing to plugin
  * [D124525](https://www.google.com/url?q=https://reviews.llvm.org/D124525&sa=D&source=editors&ust=1778600246307098&usg=AOvVaw0CIFcLUZIDegSWKoyI5bD4): [OpenMP][ClangLinkerWrapper] Extending linker wrapper to embed metadata for multi-arch fat binaries


  * Changed the __tgt_device_image to include ImageInfo.


  * [Pending patch] OffloadArch tool/library to query system arch
  * [Pending patch] Driver changes to generate image files for different architectures and pass to clang-offload-packager.


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246307584&usg=AOvVaw0MSy9hsQr3E3ZH5iaVtB5d)
  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246307678&usg=AOvVaw1JBttEwJJ5wXW_2w6u3FdM)
  * 

  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246307942&usg=AOvVaw0mtDd33k3pnZoxhdf8G6kg) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246308103&usg=AOvVaw0nQz11l4XgueCLPkO1-130) only adds the plugin runtime support


  * Add another argument to __tgt entry functions for interoperability?


  * Add dynamic memory and stream like with <<< >>> in cuda
  * `omp target …. ompx_global_shared(N)`


  * Device atomics
  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246308563&usg=AOvVaw1VvK_Op_AV61hjWdJj9Dlv)


  * 


### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246308745&usg=AOvVaw3bnjctQBWR2f8mxfmVjWN5) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246308858&usg=AOvVaw3457YKBOsmo3hRcFPojvQJ)
  * https://github.com/llvm/llvm-project/issues/55943



###
