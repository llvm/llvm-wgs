### 2021, February 17

### Agenda

  * Omp_is_initial_device



#   if defined(_OPENMP) && defined(__clang__) && __clang_major__ > 11 && !defined(__APPLE__)

        #pragma omp begin declare variant match(device={kind(host)})

        static inline int omp_is_initial_device(void) { return 1; }

        #pragma omp end declare variant

        #pragma omp begin declare variant match(device={kind(nohost)})

        static inline int omp_is_initial_device(void) { return 0; }

        #pragma omp end declare variant

#   endif

  * Follow up on Metadata for embedded target code: [https://reviews.llvm.org/D95483](https://www.google.com/url?q=https://reviews.llvm.org/D95483&sa=D&source=editors&ust=1778600246570359&usg=AOvVaw2nIcdH1ui6lAIxaKAYEa6r)
  * Clang-format all files in OpenMP ([https://reviews.llvm.org/D95318](https://www.google.com/url?q=https://reviews.llvm.org/D95318&sa=D&source=editors&ust=1778600246570497&usg=AOvVaw1nQBZ_MRLAV32xv9eUwhq-))
  * Target is implemented as target teams


  * https://bugs.llvm.org/show_bug.cgi?id=47039


  * Clang codegen for SPMD vs Generic


  * https://bugs.llvm.org/show_bug.cgi?id=48851
  * Clang test autoupdate2


  * API/ABI stability (or lack thereof) in libomp, libomptarget between llvm releases
  * Libomptarget async rules
  * What to do for unknown cuda versions wrt the devicertl, currently errors
  * Build amdgcn runtime libs by default (add missing add_subdirectory(...) lines)
  * 


### Open Bugs

  * 


### Patches to look at

  * 


### Participants (voluntary/incomplete listing)

  * George Rokos (Intel)
  * Ravi Narayanaswamy (Intel)
  * Andrey Churbanov (Intel)
  * Joseph Huber (ORNL)
  * Raghu Maddhipatla, Ron Lieberman, Saiyedul Islam, Ethan Stewart(AMD)
  * Oscar Hernandez (ORNL)
  * Johannes Doerfert (ANL)
  * Joel Denny (ORNL)



#
