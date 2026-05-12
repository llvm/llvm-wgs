### 2023, Sept 06

Agenda

New 

  * Due to OpenMP F2F and IWOMP  next 2 meetings cancelled.  Resume on Sept 27
  * OpenMP, GPUs and large FP types (long double, __float128, and possibly double double).   
GPUs do not support those types. HIP/CUDA silently demote them to double, breaking host/GPU in-memory representation compatibility. OpenMP currently insists on matching in-memory representation but does not always generate correct code ([https://reviews.llvm.org/D158778#4626181](https://www.google.com/url?q=https://reviews.llvm.org/D158778%234626181&sa=D&source=editors&ust=1778600246056288&usg=AOvVaw3N_Ks3F1tTKAubwWOfdHJb)). The problem is that the demotion is currently done in the back-end, and OpenMP forces host-matching FP format on the AST level, which makes it hard to provide consistent results as the back-end just does not have support for the FP types the openmp front-end may ask it to compile.  
Q: What does OpenMP expect to happen when compiled code uses FP type not supported by the back-end (or back-end uses a different in-memory representation for the type)?  
\- error out?   
\- deal with mismatched GPU-side implementation the way CUDA does (the code is valid, but we can't exchange those types across host/GPU by just copying)? 
  * OpenMP label(s) granularity on Github: [https://github.com/llvm/llvm-project/pull/65331](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/65331&sa=D&source=editors&ust=1778600246056941&usg=AOvVaw0BVxTfjqZoMuzTbjMj0mcp) 
  * omp_get_num_procs() on the device not supported anymore? ([https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c#inline-9277](https://www.google.com/url?q=https://reviews.llvm.org/rG1f3a28d4e54649d1453eb951f570a8c1958d4a5c%23inline-9277&sa=D&source=editors&ust=1778600246057170&usg=AOvVaw09ehLgojYhW6vDMrPth2j-))


  * OMP Places [https://www.openmp.org/spec-html/5.1/openmpse62.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.1/openmpse62.html&sa=D&source=editors&ust=1778600246057312&usg=AOvVaw0nxNYXVY0st2ufvTVfFqcQ)
  * omp_get_place_num_procs(): [https://www.openmp.org/spec-html/5.0/openmpsu134.html](https://www.google.com/url?q=https://www.openmp.org/spec-html/5.0/openmpsu134.html&sa=D&source=editors&ust=1778600246057456&usg=AOvVaw2_JqRSIsfdiPqmVsqkhdcf)


  * Update our clang support page


  * [https://clang.llvm.org/docs/OpenMPSupport.html](https://www.google.com/url?q=https://clang.llvm.org/docs/OpenMPSupport.html&sa=D&source=editors&ust=1778600246057620&usg=AOvVaw3iG4SSQh-plDhP5hK1p5MN)
  * To be cherry-picked on the stable branch ?


  * [D156894](https://www.google.com/url?q=https://reviews.llvm.org/D156894&sa=D&source=editors&ust=1778600246057754&usg=AOvVaw08GxJTrY7EkuvrMw-jkQ2B): [NFC] Update OpenMP Support page for Clang/LLVM 17
  * [D156901](https://www.google.com/url?q=https://reviews.llvm.org/D156901&sa=D&source=editors&ust=1778600246057864&usg=AOvVaw13xbPeJW3x7HYmuCEbf7jA): [OpenMP] Change OpenMP default version in documentation and help text for -fopenmp-version
