### 2022, May 25

Agenda

  * Introduced clang-offload-packager


  * Basically fatbinary for LLVM offloading


  * What does static / hidden mean on the device
  * Multi-arch compilation support


  * First patch in the series posted for review:


  * [D124525](https://www.google.com/url?q=https://reviews.llvm.org/D124525&sa=D&source=editors&ust=1778600246314473&usg=AOvVaw0zw0LdH3tOlLJ6p2rAEYOU): [OpenMP][ClangLinkerWrapper] Extending linker wrapper to embed metadata for multi-arch fat binaries


  * Changed the __tgt_device_image to include ImageInfo.
  * Image metadata stays with the image, gets populated with creation of bin_desc struct.
  * At the time of env compatibility testing if ImageInfo is found to be null, we consider that image was built with an older compiler.
  * Compatibility issues?


  * [Pending patch] OffloadArch tool/library to query system arch
  * [Pending patch] Driver changes to generate image files for different architectures and pass to clang-offload-packager.


  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246315331&usg=AOvVaw2XOFYTgBq9kQp4cixPaIAw) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246315503&usg=AOvVaw05ROpohr986k1mEzqbdbGr) only adds the plugin runtime support


  * Add another argument to __tgt entry functions for interoperability?


  * Add dynamic memory and stream like with <<< >>> in cuda
  * `omp target …. ompx_global_shared(N)`


  * Lambda captures
  * Device atomics



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246316019&usg=AOvVaw093OuKkRl_SPJAzB7OGdDL) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246316156&usg=AOvVaw1QcNQ3PUMhBR75fk-xRlzd)
