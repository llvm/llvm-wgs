# Wednesday, July 9, 2025, 9-10am CDT

# Agenda

  123. PR Review LIST
  124. Liboffload API


  1. Unclear how best to implement "kernel handles"


  1. void * handles? Handles with public fields? A type like ol_program_t?
  2. How best to implement an equivalent to olGetKernelInfo (is a "stat" like function preferred? Should it accept the program as an argument)?


  1. Fields required for UR: Name, number of arguments, string of attributes.


  3. How best to implement olGetKernelMaxGroupSize. It's an info method that requires the amount of dynamic memory to also be specified.


  1. [https://github.com/llvm/llvm-project/pull/142950](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/142950&sa=D&source=editors&ust=1779820786912778&usg=AOvVaw36BKADmET-JTuBdpzma6qU)


  125. Auto-generated documentation for liboffload: [https://github.com/llvm/llvm-project/pull/147323](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/147323&sa=D&source=editors&ust=1779820786913151&usg=AOvVaw2PZj3ObgFkfsAim2Pt23tD)


  1. Can we get the documentation hosted somewhere? Equivalent to openmp.llvm.org?


  126. [https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/llvm_kernel_languages&sa=D&source=editors&ust=1779820786913575&usg=AOvVaw1jcWpa06F2q5eJs_sRsaFi) 
  127. Second PGO for GPU patches is ready, third under preparation


  1. [https://github.com/llvm/llvm-project/pull/93365](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/93365&sa=D&source=editors&ust=1779820786913920&usg=AOvVaw03lCxNXWCmXdAGYvFIgZIk)


  128. GPU ASAN (alternative) prototype ready


  1. Testing out "new-new" design to avoid memory allocations/accesses altogether
  2. Are there any PRs available for review?
  3. Is there a design discussion on discourse?


  129. Parallel Thin LTO (WIP) 


  1. Second try: [https://github.com/jdoerfert/llvm-project/tree/thin_lto](https://www.google.com/url?q=https://github.com/jdoerfert/llvm-project/tree/thin_lto&sa=D&source=editors&ust=1779820786914720&usg=AOvVaw1g9hrnv0Liy08KBnyoxNmo)
  2. Is this ready for review?  Are there public discussions on this?


  130. Performance monitoring


  1. [https://crpl.cis.udel.edu/lnt-sollve/](https://www.google.com/url?q=https://crpl.cis.udel.edu/lnt-sollve/&sa=D&source=editors&ust=1779820786915133&usg=AOvVaw1HDPtFOd9VINs6j5MeCiLT)
  2. [https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines](https://www.google.com/url?q=https://gitlab.e4s.io/uo-public/llvm-sollve/-/pipelines&sa=D&source=editors&ust=1779820786915363&usg=AOvVaw0fd-tIa73D9tVkxfV4ENlT)


  1. Caught: [https://github.com/llvm/llvm-project/pull/96909](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/96909&sa=D&source=editors&ust=1779820786915586&usg=AOvVaw2leACpJyArP4IS4Yw5XFsx)


  131. CUDA on LLVM/Offload


  1. [https://github.com/llvm/llvm-project/pull/94821](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/94821&sa=D&source=editors&ust=1779820786915874&usg=AOvVaw1MX_1fCFiUQJISCAibhkRH)
  2. [https://github.com/llvm/llvm-project/pull/95371](https://www.google.com/url?q=https://github.com/llvm/llvm-project/pull/95371&sa=D&source=editors&ust=1779820786916080&usg=AOvVaw1XHQw0hSnP2BGLsBp01u49)



#
