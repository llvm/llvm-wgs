### 2024, Mar 13

Agenda 

New 

  * Offloading entries errors on invalid address with non-constexpr constructor


  * [https://github.com/llvm/llvm-project/issues/84942](https://www.google.com/url?q=https://github.com/llvm/llvm-project/issues/84942&sa=D&source=editors&ust=1778600246034486&usg=AOvVaw18sDwJAEE-vHY7t2Iglf18)


  * Pass libomptarget.so by name instead of `-lomptarget` and place it in the compiler's resource directory


  * Currently we will link against system `libomptarget`


  * OpenMP Examples : target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])     #pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);

  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * New PR: [https://github.com/llvm/llvm-project/pull/82459](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/82459&sa=D&source=editors&ust=1778600246035127&usg=AOvVaw1i5w6-WKfUfc0y8PwGN2J5)
  * AMD would  like to make sure it builds.
  * [https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246035365&usg=AOvVaw3GBvC07Q01Jy07OyGSzYe0) 
  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246035513&usg=AOvVaw0NfC3QXoSrj7tJZ2VoAlkn)


  * Hang started Feb 22/23:


  * [https://discourse.llvm.org/t/openmp-offloading-double-build-hanging/77256](https://www.google.com/url?q=https://discourse.llvm.org/t/openmp-offloading-double-build-hanging/77256&sa=D&source=editors&ust=1778600246035697&usg=AOvVaw1iLVueLXSY8mSGziS81yyg)


  * Schedule and dist schedule for GPUs, let's all make sure we are consistent:


  * [https://github.com/llvm/llvm-project/pull/83261/files](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/83261/files&sa=D&source=editors&ust=1778600246035897&usg=AOvVaw2ALmfIOMx6bwzDi-kTcg3v)


  * Compound/composite constructs in Flang (and Clang)
