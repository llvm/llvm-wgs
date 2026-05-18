### 2021, Oct 27

### Agenda 

  * Proposal for how to change to the new runtime
  * Snap (and reduced version) not working on nvptx trunk, different failure between new and old device rtl (Dan has further info


  * [https://bugs.llvm.org/show_bug.cgi?id=52169](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D52169&sa=D&source=editors&ust=1778600246465819&usg=AOvVaw2YhXmV14q11W08ss4rR4z0)   
[OpenMP] Wrong answers with nested 'omp parallel for'


  * New device runtime will become default soon


  * Partially tested on amdgpu, some patches in progress to bring that online


  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246466105&usg=AOvVaw0hViS0-0qh8KrJj4zyUoNS)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently offline (machine electrocuted itself)


  * Replacement exists, waiting for [PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246466414&usg=AOvVaw0Ny-0Qh0JyqUB7JF4l7T_W) fix and [D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246466474&usg=AOvVaw0JCzCYf07ahTL8V2cgyvol) approved
  * [https://reviews.llvm.org/D107193](https://www.google.com/url?q=https://reviews.llvm.org/D107193&sa=D&source=editors&ust=1778600246466574&usg=AOvVaw2iYZhcPERI1VjSURapZRRk) (don't clean source dir)


  * [llvm.org/PR50739](https://www.google.com/url?q=http://llvm.org/PR50739&sa=D&source=editors&ust=1778600246466711&usg=AOvVaw3z48-gOyj9dwWRsbWgW33T); [llvm.org/PR49940](https://www.google.com/url?q=http://llvm.org/PR49940&sa=D&source=editors&ust=1778600246466769&usg=AOvVaw3sPD5JQog-nx2ayt3dxoSO) [FLAKY] (miscompile)


  * FAIL: libomptarget :: nvptx64-nvidia-cuda::bug49334.cpp
  * [https://reviews.llvm.org/D104418](https://www.google.com/url?q=https://reviews.llvm.org/D104418&sa=D&source=editors&ust=1778600246466979&usg=AOvVaw2GY21AyE9B6dwyvUc6UoqO) (under review)



  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246467139&usg=AOvVaw1B3C9vICGYUuB9ZahrrRyo), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246467213&usg=AOvVaw1eneJ7GR3L6pBKt3cN8O7V))


  * Possibly revert the 2-3 patches and AMD will upstream JMC's implementation of the callback interface
  * Device tracing (or trace records) implementation will come separately
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246467530&usg=AOvVaw3bJtvGABWHkrkC31SdtEiL)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246467676&usg=AOvVaw2GcRQMKAL-m4T6WrhfmrOm) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246468014&usg=AOvVaw2YagtHGoRYtUPnz0BhPJ7l)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246468463&usg=AOvVaw3ttTjtBVlxIgELQyY8kqLt). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246468636&usg=AOvVaw2wpS5PRZtZGUV7sJYChrV0)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246468909&usg=AOvVaw0t8h-YGOK6sBUsSXaKLcef)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246469117&usg=AOvVaw1yf2KJ6EvBa103UzPTvRzB)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246469253&usg=AOvVaw2hRPuGjydBPg9wa__gc_6n)
  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246469734&usg=AOvVaw0AfRRA23KP6BDMfKuSH2a0)



### Patches to look at
