# Wednesday, June 26, 2024, 7:00 - 8:00 am PST

# Agenda

  264. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/76587](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/76587&sa=D&source=editors&ust=1779820786995294&usg=AOvVaw3G6wx2Gi_qulkkTLf8pd2Z)
  2. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786995595&usg=AOvVaw2QJFwvywbveg3WUUlIQDww)


  265. Unified Memory Framework (Intel)
  266. GPU ASAN (alternative) prototype ready



![](images/image4.png)

  267. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786996147&usg=AOvVaw2lX-cHBpis7Jsd7hfmEJU4)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786996412&usg=AOvVaw0IQlQUMOJRU-iZQAPo0tG6)


  268. Testing


  1. Keep a list of issues we discuss in the meetings
  2. Make 1-3 people the "bug keepers" (Joseph, Johannes)


  269. offload-tblgen


  1. [https://github.com/llvm/llvm-project/pull/88923](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/88923&sa=D&source=editors&ust=1779820786997140&usg=AOvVaw0DGno1k5HE22xkvy3i8YXO) (Please review)
  2. [https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d](https://www.google.com/url?q=https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d&sa=D&source=editors&ust=1779820786997437&usg=AOvVaw1q5b_2mNly7YvbCyaOgMTa)


  1. API draft Joseph typed up


  3. What are the next steps for introducing API changes?


  1. Design the entire new API before beginning to implement it? (By porting the existing plugins?)
  2. Move the existing plugins API to the tablegen framework and then introduce changes?
  3. Ignore the tablegen framework for now and change the existing plugin API directly?


  270. Parallel Thin LTO (WIP) [https://github.com/ggeorgakoudis/llvm-project/tree/hip-omp-parallel-thinlto-clean](https://www.google.com/url?q=https://github.com/ggeorgakoudis/llvm-project/tree/hip-omp-parallel-thinlto-clean&sa=D&source=editors&ust=1779820786998574&usg=AOvVaw0h6tih1leWtvKas0U0bRVU)
  271. Does the meeting invite ICS file need to be updated?


  1. Currently appearing at 8am PST


  272. Draft RFC on upstreaming the SYCL runtime with a short term dependency on UR


  1. [https://docs.google.com/document/d/1QI8opRuabWASxqe8Lu_dGLVO1dXlibzgBi_M-UEHxyw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1QI8opRuabWASxqe8Lu_dGLVO1dXlibzgBi_M-UEHxyw/edit?usp%3Dsharing&sa=D&source=editors&ust=1779820786999315&usg=AOvVaw0V8sp1qSLxRJ04Xt43r_JV)



# Feedback welcome before the RFC is finished and shared

* * *

#
