### 2021, February 24

### Agenda

  * Device memory allocators


  * [https://reviews.llvm.org/D96669](https://www.google.com/url?q=https://reviews.llvm.org/D96669&sa=D&source=editors&ust=1778600246567703&usg=AOvVaw3KeupcmEInl8IYeEyhpQMk)
  * Change preomp_  to llvm_omp_
  * Ticket has been opened for OpenMP to provide a reserved name


  * [https://github.com/OpenMP/spec/issues/2689](https://www.google.com/url?q=https://github.com/OpenMP/spec/issues/2689&sa=D&source=editors&ust=1778600246567932&usg=AOvVaw2f0ZzEhfumOC_aCvuwv4ik)
  * 

  * A naming convention for OpenMP extensions to implement TR features [Oscar] 


  * We need to agree on potential namespaces: Add suggestions below 


  * omp_ext_
  * ompx
  * We want to avoid llvm or gnu specific keywords
  * Llvm_omp


  * Deprecation of enum entries: [https://github.com/llvm/llvm-project/blob/main/openmp/runtime/src/include/omp-tools.h.var#L208](https://www.google.com/url?q=https://github.com/llvm/llvm-project/blob/main/openmp/runtime/src/include/omp-tools.h.var%23L208&sa=D&source=editors&ust=1778600246568465&usg=AOvVaw1VoNFhzni5oNM8LbOQLpYG) 


  * Change runtime libraries to LLVM NamingStyle?
  * 3 patches short of running update_cc_checks on the OpenMP clang tests
  * [https://reviews.llvm.org/D96769](https://www.google.com/url?q=https://reviews.llvm.org/D96769&sa=D&source=editors&ust=1778600246568700&usg=AOvVaw1nHJwB0blPdhYt_KSpzEz-)  \- Skip backend and assemble phases for AMDGCN



### Open Bugs

  * 


### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * Ravi Narayanaswamy (Intel)
  * Johannes Doerfert (ANL)
  * Oscar Hernandez (ORNL)
  * George Rokos (Intel)
  * Andrey Churbanov (Intel)
  * Ron Lieberman, Saiyedul Islam, Sourabh, Ethan Stewart, Raghu Maddhipatla, Dhruva, Pushpinder (AMD)
  * Valentin Clement (ORNL)
  * Catherine Moore (Siemens)
  * Kelvin Li (IBM)
  * Joel Denny (ORNL)
  * Simon Garcia de Gonzalo (BSC)



###
