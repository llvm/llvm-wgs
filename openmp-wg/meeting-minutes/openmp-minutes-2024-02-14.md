### 2024, Feb 14

Agenda 

New 

  * OpenMP Combined constructs.
  * Pass libomptarget.so by name instead of `-lomptarget` and place it in the compiler's resource directory


  * Currently we will link against system `libomptarget`


  * Meeting schedule


  * Starting Jan 17, meeting will alternate with the liboffload meeting
  * Next OpenMP meeting will be on Feb 14


  * OpenMP F2F meeting week of Jan 29- Feb 2


  * New invites will be sent out by MichaelKlemm and Johannes for OpenMp  and Offload meeting
  * Old invite by Ron L will have to be dropped and re-created (likely by Michael Klemm)


  * Getting rid of the plugin design and statically linking instead


  * Similar to LLVM's design for target backend


  * OpenMP Examples : target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

 #pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);

  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * [https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246039692&usg=AOvVaw3L00IBX0QsaTInsXq25mnB) 
  * Deep copy of libomptarget and (offload, libomptarget) co-exist till offload is stable enough to become default and libomptarget can be deleted?
  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246039982&usg=AOvVaw1Ur0ASd1sPyaquBAFmJCBM)


  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.3, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600246040222&usg=AOvVaw3kG6L9JrzbAoKgqn0JVy-W) (-DLLVM_ENABLE_PROJECTS=openmp): 


  * Link issue since https://github.com/llvm/llvm-project/pull/74520
  * Tries to use lld with gcc-compiled lto objects
  * RUNTIMES=openmp disables -flto because CMake test looks for LLVMgold.so


  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600246040565&usg=AOvVaw2pvyTVokzvVOsH6ikiGjsS) (-DLLVM_ENABLE_RUNTIMES=openmp): 21 failed tests



### 

### 024, Jan 17

Agenda 

New 

  * Meeting schedule


  * Starting Jan 17, meeting will alternate with the liboffload meeting
  * Next OpenMP meeting will be on Feb 14


  * OpenMP F2F meeting week of Jan 29- Feb 2


  * New invites will be sent out by MichaelK and Johannes for OpenMp  and Offload meeting
  * Old invite by Ron L will have to be dropped and re-created (likely by Michael K)


  * Getting rid of the plugin design and statically linking instead


  * Similar to LLVM's design for target backends


  * More a note than a discussion point: libomptarget -> offload: Buildbots should move accordingly


  * Buildbot updates


  * \- OpenMP AMDGPU Production bot currently offline and on transit to other data center
  * \- New OpenMP AMDGPU clang staging buildbot on gfx90a/rocm 6: [https://lab.llvm.org/staging/#/builders/185](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/185&sa=D&source=editors&ust=1778600246041767&usg=AOvVaw2zhTfHQ6139R9zIxNKe6Qu)
  * \- New OpenMP AMDGPU clang+flang staging buildbot on gfx90a/rocm 6: [https://lab.llvm.org/staging/#/builders/140](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/140&sa=D&source=editors&ust=1778600246041935&usg=AOvVaw0YK2hjrWf2kNpxKlN0lhZm)
  * \- OpenMP AMDGPU clang+libc staging buildbot on gfx906/rocm 5.6: [https://lab.llvm.org/staging/#/builders/11](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/11&sa=D&source=editors&ust=1778600246042093&usg=AOvVaw02Fwsodg1x0DVXX08FtiDR)


  *   * OpenMP Examples : target_struct_map.4.c (omp_5.1)



#pragma omp target data map(S2.p[:N])    

 #pragma omp target map(S2.p[:0], S2.a, S2.b) // implicit map of S2

       saxpyfun(&S2);

  * openmp/libomptarget -> llvm/offload _or_ llvm/offload as its own entity


  * [https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1PAeEshxHCv22JDBCPA9GXGggLp0t7rsnD_jL04MBbzw/edit?usp%3Dsharing&sa=D&source=editors&ust=1778600246042613&usg=AOvVaw0wYg6mSjdv6C_glCOcN6Rv) 
  * Deep copy of libomptarget and (offload, libomptarget) co-exist till offload is stable enough to become default and libomptarget can be deleted?
  * [https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-introducing-llvm-project-offload/74302/11&sa=D&source=editors&ust=1778600246042904&usg=AOvVaw2hNSjMo_qvpue0Ud9OoBJp)


  * Nvptx testing results from Michael Kruse. 


  * Nvidia Quadro P600, GP107, sm_61, Pascal generation, CUDA 12.3, WSL2
  * [openmp-offload-cuda-project](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/68&sa=D&source=editors&ust=1778600246043141&usg=AOvVaw0kT3vG46QM6M44UkgenMa-) (-DLLVM_ENABLE_PROJECTS=openmp): llvm-omp-device-info fail
  * [openmp-offload-cuda-runtime](https://www.google.com/url?q=https://lab.llvm.org/staging/%23/builders/7&sa=D&source=editors&ust=1778600246043278&usg=AOvVaw0m_EG2wrsjV6tNuvdLrhh5) (-DLLVM_ENABLE_RUNTIMES=openmp): 21 failed tests
