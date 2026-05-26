# Wednesday, July 24, 2024, 7:00 - 8:00 am PST

# Agenda

  248. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/76587](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/76587&sa=D&source=editors&ust=1779820786984291&usg=AOvVaw0vz16IIfgWa6F5KTYF58DP)
  2. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786984539&usg=AOvVaw0BJgjp2BSBJpS0_tduvJH6)


  249. GPU ASAN (alternative) prototype ready



![](images/image4.png)

  250. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786985007&usg=AOvVaw1a7W1Us4CCP0RE2LdPM9b1)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786985232&usg=AOvVaw28dEb44kpn3g38BDG2tYM_)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786985455&usg=AOvVaw2_W85KxCuEovXV1iiYRaj0)


  251. CUDA on LLVM/Offload


  1.   2. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786985769&usg=AOvVaw2sbDuoGObOpj9NutZfKCND)
  3. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786986005&usg=AOvVaw0JZ9FnljvvB-5yuersQNC3)


  252. Testing


  1. Keep a list of issues we discuss in the meetings
  2. Make 1-3 people the "bug keepers" (Joseph, Johannes)


  253. offload-tblgen


  1. [https://github.com/llvm/llvm-project/pull/88923](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/88923&sa=D&source=editors&ust=1779820786986650&usg=AOvVaw0Z7q6dG5q6ITnuB6wGNuFG) (Please review)
  2. [https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d](https://www.google.com/url?q=https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d&sa=D&source=editors&ust=1779820786987014&usg=AOvVaw0VGqMTbpAtz7M6BtFtiA_x)


  1. API draft Joseph typed up


  3. What are the next steps for introducing API changes?


  1. Design the entire new API before beginning to implement it? (By porting the existing plugins?)
  2. Move the existing plugins API to the tablegen framework and then introduce changes?
  3. Ignore the tablegen framework for now and change the existing plugin API directly?


  254. Parallel Thin LTO (WIP) [https://github.com/ggeorgakoudis/llvm-project/tree/hip-omp-parallel-thinlto-clean](https://www.google.com/url?q=https://github.com/ggeorgakoudis/llvm-project/tree/hip-omp-parallel-thinlto-clean&sa=D&source=editors&ust=1779820786988157&usg=AOvVaw3rp85A2WNkC-e_z0HWGpHQ)
  255. New RFC for SYCL upstreaming - [https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323&sa=D&source=editors&ust=1779820786988565&usg=AOvVaw0qI3ZgZIcqwy9S8YUwukc1)



#
