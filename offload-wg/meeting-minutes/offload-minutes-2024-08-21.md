# Wednesday, Aug 21, 2024, 7:00 - 8:00 am PST

# Agenda

  229. LLVM Dev deadline approaching
  230. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/76587](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/76587&sa=D&source=editors&ust=1779820786974397&usg=AOvVaw0GFgQ4rGrWpsz-iBkbZR0M)
  2. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786974607&usg=AOvVaw3pC4k_2730dfYKRzWBSG7Q)


  231. GPU ASAN (alternative) prototype ready


  1. bad/double-free and kernel traces merged
  2. Testing out "new-new" design to avoid memory allocations/accesses all together



![](images/image4.png)

  232. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786975376&usg=AOvVaw34LDWCaLpcTxIJ11b_sdOz)


  233. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786975642&usg=AOvVaw0KV7LJaJySmK6mEdrVx2WV)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786975867&usg=AOvVaw3hUObEjM8wBY9uZcyA4eQr)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786976087&usg=AOvVaw3FV1ZetEqcpEk__med5MVG)


  234. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786976356&usg=AOvVaw3JsnJKOtcapWBlO21Dnmcy)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786976554&usg=AOvVaw3aejX6CBk1_AknRySx82Ny)


  235. Testing


  1. Keep a list of issues we discuss in the meetings
  2. Make 1-3 people the "bug keepers" (Joseph, Johannes)


  236. offload-tblgen


  1. Current ongoing work to create a first PR that:


  1. Introduces offload-tblgen
  2. Implements auto-generated validation and tracing
  3. Implements minimal new API functions needed to run sycl-ls / urinfo via Unified Runtime (basically just device discovery and device property querying)


  2. Not quite finished yet but intend to present at the next meeting


  237. New RFC for SYCL upstreaming - [https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323&sa=D&source=editors&ust=1779820786977886&usg=AOvVaw0eZ13td7FCGWZe7ezFrS5z)
  238.
