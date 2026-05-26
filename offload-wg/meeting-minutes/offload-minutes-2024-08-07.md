# Wednesday, Aug 07, 2024, 7:00 - 8:00 am PST

# Agenda

  239. LLVM Dev deadline approaching
  240. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/76587](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/76587&sa=D&source=editors&ust=1779820786978750&usg=AOvVaw0KzQxIAM_Rqwf0emgeg74a)
  2. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786979060&usg=AOvVaw2oIaxf_3NY3vUNBA5XwfNU)


  241. GPU ASAN (alternative) prototype ready


  1. bad/double-free and kernel traces merged
  2. Testing out "new-new" design to avoid memory allocations/accesses all together



![](images/image4.png)

  242. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786979954&usg=AOvVaw3Q7AgF7xIzx_YVRJaSjD8G)


  243. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786980280&usg=AOvVaw1M7O3mmI1USrI2ke1ROsTS)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786980536&usg=AOvVaw2smHnc75PB-88sQ2QNCJok)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786980812&usg=AOvVaw3AEWYDtC9iGyotP1CgA0a0)


  244. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786981156&usg=AOvVaw0FJapr2RVLLYwzgBq5Ev-4)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786981406&usg=AOvVaw31eNEH2Mo_p7N1TBNw9ojI)


  245. Testing


  1. Keep a list of issues we discuss in the meetings
  2. Make 1-3 people the "bug keepers" (Joseph, Johannes)


  246. offload-tblgen


  1. [https://github.com/llvm/llvm-project/pull/88923](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/88923&sa=D&source=editors&ust=1779820786982052&usg=AOvVaw1vMlV1Wf2pa-AEdISp7VAp) (Please review)
  2. [https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d](https://www.google.com/url?q=https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d&sa=D&source=editors&ust=1779820786982366&usg=AOvVaw07YzHzw-x4bkTFz7tzeT8k)


  1. API draft Joseph typed up


  3. What are the next steps for introducing API changes?


  1. Design the entire new API before beginning to implement it? (By porting the existing plugins?)
  2. Move the existing plugins API to the tablegen framework and then introduce changes?
  3. Ignore the tablegen framework for now and change the existing plugin API directly?


  247. New RFC for SYCL upstreaming - [https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323&sa=D&source=editors&ust=1779820786983618&usg=AOvVaw0E6NWlM5MUCPzd-4NgTpTZ)
