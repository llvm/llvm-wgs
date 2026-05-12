### 2022, June 8

Agenda

  *   * What does static / hidden mean on the device
  * LLVM-objdump for offloading images


  * [https://reviews.llvm.org/D126904](https://www.google.com/url?q=https://reviews.llvm.org/D126904&sa=D&source=editors&ust=1778600246309307&usg=AOvVaw3TGHvkTsti1qZKQ9hgGTbC)
  * https://clang.llvm.org/docs/ClangOffloadPackager.html


  * Multi-arch compilation support


  * Introduced clang-offload-packager
  * Basically fatbinary for LLVM offloading
  * https://reviews.llvm.org/D127304
  * [D127246](https://www.google.com/url?q=https://reviews.llvm.org/D127246&sa=D&source=editors&ust=1778600246309668&usg=AOvVaw0MKT_KM__ecwxnVq4S_ifE): [LinkerWrapper] Rework the linker wrapper and use owning binaries
  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246309804&usg=AOvVaw0jEgu1MPChNMtEv2E3zySU): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * First patch in the series posted for review:


  * Going to use [D126836](https://www.google.com/url?q=https://reviews.llvm.org/D126836&sa=D&source=editors&ust=1778600246310013&usg=AOvVaw0Bqn7wmWTwJI5x4KNvQJ6F) to move the compatibility testing to plugin
  * [D124525](https://www.google.com/url?q=https://reviews.llvm.org/D124525&sa=D&source=editors&ust=1778600246310139&usg=AOvVaw0mCvV39V5QwCylC_Zrb59l): [OpenMP][ClangLinkerWrapper] Extending linker wrapper to embed metadata for multi-arch fat binaries


  * Changed the __tgt_device_image to include ImageInfo.


  * [Pending patch] OffloadArch tool/library to query system arch
  * [Pending patch] Driver changes to generate image files for different architectures and pass to clang-offload-packager.


  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246310736&usg=AOvVaw2gXI4HLYrqep-TJuMku7Vw) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246310911&usg=AOvVaw3h59BS6Btdr6oDaG3Z_0ea) only adds the plugin runtime support


  * Add another argument to __tgt entry functions for interoperability?


  * Add dynamic memory and stream like with <<< >>> in cuda
  * `omp target …. ompx_global_shared(N)`


  * Device atomics
  * Meta directive 



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246311455&usg=AOvVaw1aHWxkFOSdZD4FD91QDO0R) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246311583&usg=AOvVaw1XY3IsguGAUpHJ4KElAAmr)
  * https://github.com/llvm/llvm-project/issues/55943



###
