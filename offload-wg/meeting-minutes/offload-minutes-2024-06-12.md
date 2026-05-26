# Wednesday, June 12, 2024, 7:00 - 8:00 am PST

# Agenda

  273. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/76587](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/76587&sa=D&source=editors&ust=1779820787000233&usg=AOvVaw2Nnyx7VpyykB2TEwDWtiuO)
  2. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820787000458&usg=AOvVaw1epVN73IG05bKa-w2R7gUm)


  274. Unified Memory Framework (Intel)
  275. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820787000811&usg=AOvVaw1N6-z70NnMWuV2UOiwjaqy)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820787001049&usg=AOvVaw2ST3QqxokmeqXko0_vKB8O)


  276. Testing


  1. Keep a list of issues we discuss in the meetings
  2. Make 1-3 people the "bug keepers" (Joseph, Johannes)


  277. offload-tblgen


  1. [https://github.com/llvm/llvm-project/pull/88923](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/88923&sa=D&source=editors&ust=1779820787001596&usg=AOvVaw2GOKjMZ_hGC3qzLHQfpm8o) (Please review)
  2. [https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d](https://www.google.com/url?q=https://gist.github.com/jhuber6/2117cfd03b7c78d91f5481ac63da682d&sa=D&source=editors&ust=1779820787001862&usg=AOvVaw2V-Di1w28T1flBaFiApoYz)


  1. API draft Joseph typed up


  3. What are the next steps for introducing API changes?


  1. Design the entire new API before beginning to implement it? (By porting the existing plugins?)
  2. Move the existing plugins API to the tablegen framework and then introduce changes?
  3. Ignore the tablegen framework for now and change the existing plugin API directly?


  278. Parallel Thin LTO (WIP) [https://github.com/ggeorgakoudis/llvm-project/tree/hip-omp-parallel-thinlto-clean](https://www.google.com/url?q=https://github.com/ggeorgakoudis/llvm-project/tree/hip-omp-parallel-thinlto-clean&sa=D&source=editors&ust=1779820787002909&usg=AOvVaw3Xbj2xOrc2hc8nZGILikGX)
  279. Does the meeting invite ICS file need to be updated?


  1. Currently appearing at 8am PST


  280. Draft RFC on upstreaming the SYCL runtime with a short term dependency on UR


  1. [https://docs.google.com/document/d/1QI8opRuabWASxqe8Lu_dGLVO1dXlibzgBi_M-UEHxyw/edit?usp=sharing](https://www.google.com/url?q=https://docs.google.com/document/d/1QI8opRuabWASxqe8Lu_dGLVO1dXlibzgBi_M-UEHxyw/edit?usp%3Dsharing&sa=D&source=editors&ust=1779820787003585&usg=AOvVaw2dEZgbv_7Lu0PondhnVq7Q)
  2. Feedback welcome before the RFC is finished and shared



* * *

#
