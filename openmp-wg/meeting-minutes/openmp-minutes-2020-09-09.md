### 2020, September 9

### Agenda

  * FE optimization :  if (omp_is_initial_device())



                                        d

 Results in d passed as arg on host compilation and not for device compilation

Proposed solution:

        #omp begin declare variant match(device={kind(host)})

        Int omp_is_initial_device() { return 1; }

        #omp end declare variant

#omp begin declare variant match(device={kind(nohost)})

        Int omp_is_initial_device() { return 0; }

        #omp end declare variant

[https://clang.godbolt.org/z/cnhe6G](https://www.google.com/url?q=https://clang.godbolt.org/z/cnhe6G&sa=D&source=editors&ust=1778600246599430&usg=AOvVaw0w1CBtf20asnO5Us0iz6hd)

[https://clang.godbolt.org/z/Wqo9hM](https://www.google.com/url?q=https://clang.godbolt.org/z/Wqo9hM&sa=D&source=editors&ust=1778600246599553&usg=AOvVaw3zDES4ZhDCHHwMS0L3ZtEm)

  * Using Clang to compile openmp device code
  * Change the default linkage for OpenMP kernels (and such) to `weak_odr`  (from `weak`)
  * Target nowait is broken.  Has the mapper fixed uploaded?


  * Have patch which fixes the problem.
  * Need LIT test.  George or Alexey will add it
  * Declare mapper is unstable. Should  we disable it?


  * Clean revert is problematic
  * Seems like disabling in 11 is the right choice


  * Support struct mapping : #pragma omp target map(alloc:S) map(S.p[:N]) map(to:S.a, S.b)  where S is  a struct with 3 fields p,a,b  
[https://reviews.llvm.org/D86119](https://www.google.com/url?q=https://reviews.llvm.org/D86119&sa=D&source=editors&ust=1778600246600271&usg=AOvVaw1kO1VvRAyMsF_Pxz-yjYXu) 
  * OpenMP device runtime build setup [from last week]
  * Runtime debug generation


  * https://reviews.llvm.org/D87165



### 

### Open Bugs

  * 


### Patches to look at

  * [https://reviews.llvm.org/D80816](https://www.google.com/url?q=https://reviews.llvm.org/D80816&sa=D&source=editors&ust=1778600246600671&usg=AOvVaw1GuYyfokOyfXq5JyttSflB) \- offload-bundler archives patch
  * [https://reviews.llvm.org/D84470](https://www.google.com/url?q=https://reviews.llvm.org/D84470&sa=D&source=editors&ust=1778600246600792&usg=AOvVaw0PfqioPZPai8a2ybIRtFku)  Mapper bug fix
  * [https://reviews.llvm.org/D86558](https://www.google.com/url?q=https://reviews.llvm.org/D86558&sa=D&source=editors&ust=1778600246600893&usg=AOvVaw0EN2QvbxNjyGGfIv86LIcC) \- Support for allocated locals in untied tasks.
  * [https://reviews.llvm.org/D86119](https://www.google.com/url?q=https://reviews.llvm.org/D86119&sa=D&source=editors&ust=1778600246601018&usg=AOvVaw2NFcPgPV0s7LBuOEBQJu7w) \- support for overlapped mappings
  * [https://reviews.llvm.org/D85762](https://www.google.com/url?q=https://reviews.llvm.org/D85762&sa=D&source=editors&ust=1778600246601166&usg=AOvVaw2k1M0_QXBZwKQVOjQZzuQR) \- [Do not allow threadprivates as base for array-like reduction.](https://www.google.com/url?q=https://reviews.llvm.org/D85762&sa=D&source=editors&ust=1778600246601272&usg=AOvVaw3PDXPf5R0WUSHIhoYWIQXo)
  * [https://reviews.llvm.org/D84887](https://www.google.com/url?q=https://reviews.llvm.org/D84887&sa=D&source=editors&ust=1778600246601363&usg=AOvVaw3TzZGQ8jijVVS9UnzPxkeX) \- [Fix codegen for is_device_ptr component, captured by reference.](https://www.google.com/url?q=https://reviews.llvm.org/D84887&sa=D&source=editors&ust=1778600246601509&usg=AOvVaw1O36gck2EL9fj39lmr_Uwo) 



### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Valentin Clement (ORNL)
  * Shilei Tian (SBU)
  * Joel Denny (ORNL)
  * George Rokos (Intel)
  * Saiyedul Islam (AMD)
  * Johannes Doerfert, Ye Luo (ANL)
  * Andrey Churbanov (Intel)
  * Kelvin Li (IBM)
