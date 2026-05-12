### 2024, Feb 28

New 

  * Pass libomptarget.so by name instead of `-lomptarget` and place it in the compiler's resource directory


  * Currently we will link against system `libomptarget`


  * OpenMP Examples : target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

 #pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);

  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * New PR: [https://github.com/llvm/llvm-project/pull/82459](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/82459&sa=D&source=editors&ust=1778600246036738&usg=AOvVaw17H3sT-B68N1MG6UZWShcp)
  * AMD would  like to make sure it builds.
  * [https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246036967&usg=AOvVaw0flt6_qy2aLOGXDsQhjEHy) 
  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246037128&usg=AOvVaw2kZ38zDjCbqjPeDwUHcXZI)


  * Hang started Feb 22/23:


  * [https://discourse.llvm.org/t/openmp-offloading-double-build-hanging/77256](https://www.google.com/url?q=https://discourse.llvm.org/t/openmp-offloading-double-build-hanging/77256&sa=D&source=editors&ust=1778600246037344&usg=AOvVaw2672iGO1xUvxaZoUBg0xmw)


  * Schedule and dist schedule for GPUs, let's all make sure we are consistent:


  * [https://github.com/llvm/llvm-project/pull/83261/files](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/83261/files&sa=D&source=editors&ust=1778600246037559&usg=AOvVaw3xyUU-sOvzCQGMHo7C8b6p)


  * Compound/composite constructs in Flang (and Clang)
  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.3, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600246037850&usg=AOvVaw2wJc5FJNOyBgcyqrXkCw7d) (-DLLVM_ENABLE_PROJECTS=openmp): 


  * Link issue since https://github.com/llvm/llvm-project/pull/74520
  * Tries to use lld with gcc-compiled lto objects
  * RUNTIMES=openmp disables -flto because CMake test looks for LLVMgold.so


  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600246038196&usg=AOvVaw23Ges45nJUBR44J_SgO26o) (-DLLVM_ENABLE_RUNTIMES=openmp): 21 failed tests
