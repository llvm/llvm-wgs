# Wednesday, Oct 02, 2024, 7:00 - 8:00 am PST

# Agenda

  204. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786961222&usg=AOvVaw0QcwrTwZPasCjsou9xbRdk)


  205. GPU ASAN (alternative) prototype ready


  1. bad/double-free and kernel traces merged
  2. Testing out "new-new" design to avoid memory allocations/accesses all together



![](images/image4.png)

  206. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786962144&usg=AOvVaw2o8U5lr5awWhev1X2SrhIg)


  207. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786962439&usg=AOvVaw2yawJAaFYXYLeXT2QGBPhB)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786962723&usg=AOvVaw18hLEwnRhbjcVjIbUlBMjN)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786962976&usg=AOvVaw0EoQ39-U2ripRJCQzLfcje)


  208. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786963258&usg=AOvVaw0M8k_WeuvdUNuZmBQeQyED)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786963470&usg=AOvVaw0fAM5F6WP_Kk14gSPCFrUO)


  209. Testing


  1. Keep a list of issues we discuss in the meetings
  2. Make 1-3 people the "bug keepers" (Joseph, Johannes)


  210. Initial PR for new API and tablegen tooling is up: [https://github.com/llvm/llvm-project/pull/108413](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/108413&sa=D&source=editors&ust=1779820786964069&usg=AOvVaw060GXotFVzrYA4jo8Jw3r-) 


  1. New updates (Oct 2nd):


  1. Generated files are checked in
  2. Error handling is improved
  3. Unit tests added


  2. Open items:


  1. Decide on naming convention (offloadFoo is too verbose, camel case vs snake case)
  2. API versioning (tied to LLVM version?)


  211. New RFC for SYCL upstreaming - [https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323&sa=D&source=editors&ust=1779820786965070&usg=AOvVaw1xFGd4U8xP7VrracQHoom7)
