# Wednesday, Sep 4, 2024, 7:00 - 8:00 am PST

# Agenda

  221. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/76587](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/76587&sa=D&source=editors&ust=1779820786970035&usg=AOvVaw1RepF9trMJkhmSyDXjfhXX)
  2. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786970254&usg=AOvVaw0zP9USKdnQZ9XmkaE8W_Z4)


  222. GPU ASAN (alternative) prototype ready


  1. bad/double-free and kernel traces merged
  2. Testing out "new-new" design to avoid memory allocations/accesses all together



![](images/image4.png)

  223. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786971094&usg=AOvVaw0-oS24wTVoCZPb2ZhttqJp)


  224. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786971377&usg=AOvVaw2_1cgoCgCPa3L5CMlqn6it)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786971633&usg=AOvVaw3rLKrvjEegrhIhxa-lnmjy)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786971901&usg=AOvVaw0peh9S4Ns3KgZLAG29ug4Z)


  225. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786972186&usg=AOvVaw1jN7jmnwC2hIche5NumFwE)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786972388&usg=AOvVaw0RBGAt_hlwykEtIVVaC0pS)


  226. Testing


  1. Keep a list of issues we discuss in the meetings
  2. Make 1-3 people the "bug keepers" (Joseph, Johannes)


  227. offload-tblgen


  1. Current ongoing work to create a first PR that:


  1. Introduces offload-tblgen
  2. Implements auto-generated validation and tracing
  3. Implements minimal new API functions needed to run sycl-ls / urinfo via Unified Runtime (basically just device discovery and device property querying)


  2. Not quite finished yet but intend to present at the next meeting


  228. New RFC for SYCL upstreaming - [https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323](https://www.google.com/url?q=https://discourse.llvm.org/t/rfc-sycl-runtime-upstreaming-questions/80323&sa=D&source=editors&ust=1779820786973731&usg=AOvVaw3rGPJgRLWt_2vQgy6I5ilo)
