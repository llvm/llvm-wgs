### 2020, September 2

### Agenda

  * Support struct mapping : #pragma omp target map(alloc:S) map(S.p[:N]) map(to:S.a, S.b)  where S is  a struct with 3 fields p,a,b  
[https://reviews.llvm.org/D86119](https://www.google.com/url?q=https://reviews.llvm.org/D86119&sa=D&source=editors&ust=1778600246602343&usg=AOvVaw01Hf7iUxWL1o9Hf012IJvU) 
  * OpenMP device runtime build setup


  * 1) Remove the non .bc support, this is largely untested and unhelpful, also unneeded after we do step 2) and 3)
  * 2) Setup cmake to build the .bc device runtimes with the clang that was created in the build, if any. We have some precedence here I was told. (nb: LLVM_ENABLE_RUNTIMES didn't work for this out of the box)
  * 3) Setup cmake to build all supported .bc device runtimes and let the user opt-out of that. Building a device runtime is basically free compared to the rest of LLVM, having out-of-the-box support for all devices is worth it (IMHO).



Have a default clang which could be the one just built and then have an option to choose a different clang.

Please respond by next week so a decision can be made.

A related patch has been on the Phabricator in a blocked state: [https://reviews.llvm.org/D46842](https://www.google.com/url?q=https://reviews.llvm.org/D46842&sa=D&source=editors&ust=1778600246603274&usg=AOvVaw0TRISRDj1mLpIj9DMQ9sIp)

  * Unshackled task


  * All issues have been addressed in the review.


  * Target nowait is broken (Ye)


  * Mapper change introduced wrong arguments which results in seg fault.
  * George said there is a patch.[https://reviews.llvm.org/D84470](https://www.google.com/url?q=https://reviews.llvm.org/D84470&sa=D&source=editors&ust=1778600246603684&usg=AOvVaw10Ua9Qvcl7xvM9v0FGAiMN) which should  address the issue



  * Fat archive


  * Patch for offload bundler is waiting to be reviewed
  * Hope to get the  driver change to accept device archive


  * Runtime debug generation


  * Better support to print info to user
  * Ye: Errors common to all the plugins captured by libomptarget by number.
  * Ye: not sure all the plugins should be forced to use numbers instead of ad-hoc printing messages.



### Open Bugs

  * 


### Patches to look at

  * [https://reviews.llvm.org/D80816](https://www.google.com/url?q=https://reviews.llvm.org/D80816&sa=D&source=editors&ust=1778600246604400&usg=AOvVaw3lGb0Nt8eD-UpBom2OQoT5) \- offload-bundler archives patch



### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy, George Rokos(Intel)
  * Jan Sjodin (AMD)
  * Ye Luo (Argonne)
  * Johannes Doerfert (ANL)
  * Jon Chesterfield
  * Andrey Churbanov (Intel)
  * Kelvin Li (IBM)
