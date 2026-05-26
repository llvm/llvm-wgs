# Wednesday, Jan 22 2025, 7:00 - 8:00 am PST

# Agenda

  180. Port DeviceRTL to C++ [https://github.com/llvm/llvm-project/pull/123673](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/123673&sa=D&source=editors&ust=1779820786945336&usg=AOvVaw2eed0bpCrakiUN2cCKBufc)
  181. PR Review LIST
  182. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786945766&usg=AOvVaw3FfwSmgRFW5YxLLSN7z1ai)


  183. GPU ASAN (alternative) prototype ready


  1. bad/double-free and kernel traces merged
  2. Testing out "new-new" design to avoid memory allocations/accesses all together



![](images/image1.png)![](images/image3.png)![](images/image2.png)

  184. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786946569&usg=AOvVaw19jjCe0R5hijj1l3XnCNlu)


  185. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786946843&usg=AOvVaw2BgetwJWoEHZZGlqAVvkwI)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786947074&usg=AOvVaw2lqTaSWzVtJcoxadtS8LZS)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786947310&usg=AOvVaw1G0KKZ7fakSODUEGQ9vUPB)


  186. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786947589&usg=AOvVaw1TqYsZL8Kt8Dax3fvB4ldr)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786947811&usg=AOvVaw3ofGQiDTUVqtQBuf0642wG)


  187. Initial PR for new API and tablegen tooling has finally merged


  1. Thanks to everyone for the help with the various reviews, reverts and getting it properly landed eventually
  2. Draft follow-up PR to demonstrate the new tooling: [https://github.com/llvm/llvm-project/pull/119549](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/119549&sa=D&source=editors&ust=1779820786948528&usg=AOvVaw0yTJZDPhq9vHpQdC3RzfaF)


  1. Shows the minimal changes required to add to the API, and the resulting auto-generated files (in the include/generated folder)


  3. Second follow up that implements the remaining initial API:  
[https://github.com/llvm/llvm-project/pull/122106](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/122106&sa=D&source=editors&ust=1779820786949091&usg=AOvVaw33L19vTA7t6SJHfhgauiu4)


  1. Still WIP but enough to run a basic SYCL program!
  2. Intend to finish this soon. Want to confirm - are we ok with (many,  ongoing) breaking changes until we reach some kind of stability? Above PRs are based on the existing plugin design; don't want to be stuck if we decide to change things.



* * *

#
