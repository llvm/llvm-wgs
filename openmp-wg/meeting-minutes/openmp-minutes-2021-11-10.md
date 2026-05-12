### 2021, Nov 10

### Agenda 

  * FOTV generic device offload runtime proposal


  * See [https://doi.org/10.1007/978-3-030-85262-7_12](https://www.google.com/url?q=https://doi.org/10.1007/978-3-030-85262-7_12&sa=D&source=editors&ust=1778600246455897&usg=AOvVaw3ifiYSkrGAP08iivX3eah7)


  * JIT support


  * Prototype: [https://github.com/tianshilei1992/llvm-project/tree/jit-lto](https://www.google.com/url?q=https://github.com/tianshilei1992/llvm-project/tree/jit-lto&sa=D&source=editors&ust=1778600246456072&usg=AOvVaw1Jx8y2IlZbyFmm6s0euRrg)
  * Optimization: kernel argument specialization, pointer alignment, # teams and # threads folding, # registers, readonly global specialization
  * Image caching
  * Portability: e.g. image of sm_35 but run on sm_75
  * Kernel time improvement: SU3 ~6.5%, XSBench ~8.27%, 503.postencil ~300%


  * OvO (-O3, new RT) passes 100% C/C++ tests now on A100 (sm_80) :) 


  * Ye: still fails in A40 and RTX3060 Ti. 100% pass as well. sm_86 cards but works as sm_80.


  * LLVM change committed before the weekend (11/5) caused tests to hang when dispatching to the GPU:


  * [https://reviews.llvm.org/D105169](https://www.google.com/url?q=https://reviews.llvm.org/D105169&sa=D&source=editors&ust=1778600246456773&usg=AOvVaw12JYVZuD90bn-vzyjoBIwK)



[Clang/Test]: Rename enable_noundef_analysis to disable-noundef-analysis and turn it off by default

  * hang went away if the test was compiled with: -mllvm -openmp-opt-disable-internalization=1
  * change was later (11/8) reverted here: fd9b099906c61e46574d1ea2d99b973321fe1d21
  * required also rebuilding the OpenMP runtime libraries (just rebuilding clang was not sufficient)
  * presentation on this change: [https://llvm.org/devmtg/2020-09/slides/Lee-UndefPoison.pdf](https://www.google.com/url?q=https://llvm.org/devmtg/2020-09/slides/Lee-UndefPoison.pdf&sa=D&source=editors&ust=1778600246457321&usg=AOvVaw0Byl-4yXFZmFqTHXh595dv)
  * likely still some optimization in llvm not correctly handing poison/freeze that was affecting OpenMP


  * Snap (and reduced version) not working on nvptx trunk, different failure between new and old device rtl (Dan has further info


  * [https://bugs.llvm.org/show_bug.cgi?id=52169](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D52169&sa=D&source=editors&ust=1778600246457680&usg=AOvVaw0A0367Ftn-rAVSWh4o2vzs)   
[OpenMP] Wrong answers with nested 'omp parallel for'


  * Non-standard ompx OpenMP library 
  * Interop directive


  * [https://reviews.llvm.org/D106674](https://www.google.com/url?q=https://reviews.llvm.org/D106674&sa=D&source=editors&ust=1778600246457912&usg=AOvVaw19aGmEAEeossxAYlMIRwBJ) (runtime)
  * [https://reviews.llvm.org/D105876](https://www.google.com/url?q=https://reviews.llvm.org/D105876&sa=D&source=editors&ust=1778600246458012&usg=AOvVaw2Or5B3FATVtQTWXf9BJMpj) (irbuilder)
  * 

  * [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246458193&usg=AOvVaw0ELh2WDg2kbVwbd9_gLUhZ)  (Revisit)


  * [WIP][RFC] Sample code for containerizing offload images into one ELF


  * NVPTX buildbots


  * Currently offline (machine electrocuted itself)


  * OMPT for omptarget ([https://reviews.llvm.org/D106975](https://www.google.com/url?q=https://reviews.llvm.org/D106975&sa=D&source=editors&ust=1778600246458540&usg=AOvVaw2rf3GWvbCNjqoMOWDo3yP0), [https://reviews.llvm.org/D106976](https://www.google.com/url?q=https://reviews.llvm.org/D106976&sa=D&source=editors&ust=1778600246458617&usg=AOvVaw3PF7cJr87tlfbUuCsGAfd4))


  * Possibly revert the 2-3 patches and AMD will upstream JMC's implementation of the callback interface
  * Device tracing (or trace records) implementation will come separately
  * Related: [https://dl.acm.org/doi/abs/10.1145/3458744.3473358](https://www.google.com/url?q=https://dl.acm.org/doi/abs/10.1145/3458744.3473358&sa=D&source=editors&ust=1778600246458932&usg=AOvVaw2s-50kCpRYYhKXdhx1mR7-)​​​​​​​


  * Libarcher in Ubuntu/Debian packages ([https://bugs.llvm.org/show_bug.cgi?id=45945](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D45945&sa=D&source=editors&ust=1778600246459085&usg=AOvVaw27-wUWP9dWmYSF8vb39R20) issue with -Wl,-Bsymbolic-functions flag) - tried to ping [pkg-llvm-team@lists.alioth.debian.org](mailto:pkg-llvm-team@lists.alioth.debian.org), but no reply  comment from Sylvestre, but no solution yet
  * [https://bugs.llvm.org/show_bug.cgi?id=51117 ](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51117&sa=D&source=editors&ust=1778600246459445&usg=AOvVaw2qj7XrJM8y-Z7HUteXF2jL)


  * Report contains an extensive list of runtime/libarcher tests, that fail when building llvm-13 with gcc-11 on certain machines (could not reproduce)


  * Any update on CUDA issues with ELF notes?


  * Not yet, still waiting
  * Uploaded sample code for containerizing several images into one ELF: [https://reviews.llvm.org/D112103](https://www.google.com/url?q=https://reviews.llvm.org/D112103&sa=D&source=editors&ust=1778600246459841&usg=AOvVaw3a8d-kk3PMdHixNv6IQl9C). It is based on [https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp](https://www.google.com/url?q=https://github.com/intel/llvm/blob/sycl/clang/tools/clang-offload-wrapper/ClangOffloadWrapper.cpp&sa=D&source=editors&ust=1778600246460012&usg=AOvVaw1-vHtn8FGIBQW6e_-WYssK)


  * Multiple architecture offload compilation


  * Generation of multi-image binary by clang and runtime's ability to load appropriate image: [[OpenMP] Multi architecture compilation support] [https://reviews.llvm.org/D106870](https://www.google.com/url?q=https://reviews.llvm.org/D106870&sa=D&source=editors&ust=1778600246460290&usg=AOvVaw1C7TbkE207VnMMwdtv2ns7)
  * Query current offload architecture to find "appropriate image": [OffloadArch] Library to query properties of current offload architecture [https://reviews.llvm.org/D106960](https://www.google.com/url?q=https://reviews.llvm.org/D106960&sa=D&source=editors&ust=1778600246460505&usg=AOvVaw3CKQgGpfbOY1AdRaE6egQ9)


  * [RFC] "declare target indirect" doc: [https://reviews.llvm.org/D110193](https://www.google.com/url?q=https://reviews.llvm.org/D110193&sa=D&source=editors&ust=1778600246460632&usg=AOvVaw1koNzB-IF8DIV0bmOO9gC4)
  * User experience (was Rpath, runpath, env vars and fragility of toolchains)


  * Still need to work out how to make the user executable find libomp and libomptarget - currently it needs to use LD_LIBRARY_PATH, but we could set up a runpath for applications under a clang flag
  * Why llvm/lib is after system lib locations?



### Open Bugs

  * [https://bugs.llvm.org/show_bug.cgi?id=51737](https://www.google.com/url?q=https://bugs.llvm.org/show_bug.cgi?id%3D51737&sa=D&source=editors&ust=1778600246461117&usg=AOvVaw3hU2ntjyM8g_cTte4pwBXr)



###
