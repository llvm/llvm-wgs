### 2022, June 29

Agenda

  * Reformat Libomptarget to use consistent variable case style (e.g. device_num -> DeviceNum).
  * Remove i386 from the clang tests
  * LLVM-objdump for offloading images


  * [https://reviews.llvm.org/D126904](https://www.google.com/url?q=https://reviews.llvm.org/D126904&sa=D&source=editors&ust=1778600246303653&usg=AOvVaw2f3Az-3m-nMUi4edn89ysp)
  * https://clang.llvm.org/docs/ClangOffloadPackager.html


  * Multi-arch compilation support


  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246303844&usg=AOvVaw28Gj_qNKhDhyoB8MrDZQC5): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D127432](https://www.google.com/url?q=https://reviews.llvm.org/D127432&sa=D&source=editors&ust=1778600246303968&usg=AOvVaw22vcQpEEiK7jS4uvHUYwZu): [Libomptarget] Add support for offloading binaries in libomptarget
  * [D127505](https://www.google.com/url?q=https://reviews.llvm.org/D127505&sa=D&source=editors&ust=1778600246304090&usg=AOvVaw1Z4XNl1ELjFWJGBUFsJ9aU): [Libomptarget] Add checks for CUDA subarchitecture using new info
  * [D127769](https://www.google.com/url?q=https://reviews.llvm.org/D127769&sa=D&source=editors&ust=1778600246304225&usg=AOvVaw12y7_F7XE13hA6H_ZyJqU6): [Libomptarget] Add checks for AMDGPU TargetID using new image info
  * [D127304](https://www.google.com/url?q=https://reviews.llvm.org/D127304&sa=D&source=editors&ust=1778600246304348&usg=AOvVaw3rKuts3D9MMzGEJSUhTAaH): [LinkerWrapper] Embed OffloadBinaries for OpenMP offloading images
  * [D128090](https://www.google.com/url?q=https://reviews.llvm.org/D128090&sa=D&source=editors&ust=1778600246304479&usg=AOvVaw2404mifvrTTwg2EjJhHmi2): [Clang][OpenMP] Process multi-arch compilation options given via -march


  * OMPD (Vignesh)


  * [https://reviews.llvm.org/D100185](https://www.google.com/url?q=https://reviews.llvm.org/D100185&sa=D&source=editors&ust=1778600246304680&usg=AOvVaw2Cu1vH_biXMhs5M6kaBH9Z)
  * [https://reviews.llvm.org/D100186](https://www.google.com/url?q=https://reviews.llvm.org/D100186&sa=D&source=editors&ust=1778600246304779&usg=AOvVaw1a9l4RefusB1OIPm5FTAou)
  * 

  * Allocators - shared, managed, gpu, other
  * Dynamic shared memory


  * [https://openmp.llvm.org//design/Runtimes.html#libomptarget-dynamic-shared](https://www.google.com/url?q=https://openmp.llvm.org//design/Runtimes.html%23libomptarget-dynamic-shared&sa=D&source=editors&ust=1778600246305034&usg=AOvVaw2vppQq7ya0gFNReo5-pj15) 
  * Add dynamic memory and stream like with <<< >>> in cuda
  * [https://reviews.llvm.org/D125252](https://www.google.com/url?q=https://reviews.llvm.org/D125252&sa=D&source=editors&ust=1778600246305195&usg=AOvVaw2NUZrtCpbwdYMRUgDaQbGK) only adds the plugin runtime support


  * Add another argument to __tgt entry functions for interoperability?


  * [https://reviews.llvm.org/D128549](https://www.google.com/url?q=https://reviews.llvm.org/D128549&sa=D&source=editors&ust=1778600246305410&usg=AOvVaw0Jv99M6uHgcyeU3MREb8FC)
  * Add dynamic memory and stream like with <<< >>> in cuda
  * `omp target …. ompx_global_shared(N)`


  * Device atomics
  * Meta directive 


  * [https://reviews.llvm.org/D122255](https://www.google.com/url?q=https://reviews.llvm.org/D122255&sa=D&source=editors&ust=1778600246305766&usg=AOvVaw2xFioMoL4mVmuA7sBimoyt)


  * OMPT target patches needing review. Top of stack [⚙ D127372 [OpenMP] [OMPT] [8/8] Added lit tests for OMPT target callbacks (llvm.org)](https://www.google.com/url?q=https://reviews.llvm.org/D127372&sa=D&source=editors&ust=1778600246305957&usg=AOvVaw0TUb6zCe_vyHD4fXVQNYQ7)



###
