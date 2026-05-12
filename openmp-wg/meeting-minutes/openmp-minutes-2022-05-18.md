### 2022, May 18

Agenda

  * Compiling CUDA with the new driver is up for review [https://reviews.llvm.org/D123812](https://www.google.com/url?q=https://reviews.llvm.org/D123812&sa=D&source=editors&ust=1778600246316377&usg=AOvVaw3yQ5D4_mG_ub6pBVHZ1CdS). Allows OpenMP Offloading to be compiled with and call CUDA.
  * Patch that allows OpenMP to use -offload-arch= [https://reviews.llvm.org/D124721](https://www.google.com/url?q=https://reviews.llvm.org/D124721&sa=D&source=editors&ust=1778600246316570&usg=AOvVaw0O36ZGyMXbb9zU8ZoPiXwN)
  * Introduced clang-offload-packager


  * Basically fatbinary for LLVM offloading


  * Should we embed the -cuda-install path into the device binary at compile time and use that?


  * Every PTX file is expected to be made with a valid CUDA install
  * It's possible that the install could've changed between compilation and building


  * Could default to $PATH if not found


  * What does static / hidden mean on the device
  * Multi-arch compilation support


  * First patch in the series posted for review:


  * [D124525](https://www.google.com/url?q=https://reviews.llvm.org/D124525&sa=D&source=editors&ust=1778600246317233&usg=AOvVaw0xd6i4DMLD83p3g0iZoAU-): [OpenMP][ClangLinkerWrapper] Extending linker wrapper to embed metadata for multi-arch fat binaries


  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246317568&usg=AOvVaw2p1EDTjhUKQar9-hAhCK6k) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246317729&usg=AOvVaw3XRxSklBYNma2Rg8rYar8s) only adds the plugin runtime support


  * Add another argument to __tgt entry functions for interoperability?


  * Add dynamic memory and stream like with <<< >>> in cuda
  * `omp target …. ompx_global_shared(N)`
  * 

  * Lambda captures
  * "Post processing" for lookups w/o reference count updates
  * Device atomics



### Open Bugs

  * [https://github.com/llvm/llvm-project/issues/50602](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/50602&sa=D&source=editors&ust=1778600246318288&usg=AOvVaw1YpznIPmXo5tyIYlEjmPxf) 
  * [https://github.com/llvm/llvm-project/issues/53081](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/53081&sa=D&source=editors&ust=1778600246318411&usg=AOvVaw0tCYWkr2YJO1oKBSohHBbD)
